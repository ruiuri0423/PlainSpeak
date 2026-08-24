#!/usr/bin/env python3
"""Deterministic, privacy-minimized UserPromptSubmit hook for PlainSpeak."""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# This file is UTF-8. Keep the phrases readable so maintainers can review them.
SIGNALS = {
    "not_understood": (
        r"看不懂|聽不懂|不明白|不理解|還是不懂|不太懂",
        r"don.t understand|still confused|not clear",
    ),
    "repeat_or_reframe": (
        r"再(?:說明|解釋|講)|重新(?:說明|解釋)|換(?:個|一種)方式",
        r"explain (?:it )?again|re-?explain|another way",
    ),
    "too_abstract": (
        r"太抽象|更具體|舉(?:個|一個)例|實際例子",
        r"too abstract|more concrete|give (?:me )?an example",
    ),
    "too_technical": (
        r"太技術|太專業|白話(?:一點)?|簡單(?:一點)?說",
        r"too technical|plain language|simpler terms",
    ),
}


def classify(prompt: str) -> list[str]:
    return [
        label
        for label, patterns in SIGNALS.items()
        if any(re.search(pattern, prompt, re.IGNORECASE) for pattern in patterns)
    ]


def feedback_path(event: dict) -> Path:
    override = os.environ.get("PLAINSPEAK_FEEDBACK_DIR")
    root = (
        Path(override).expanduser()
        if override
        else Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
        / "plainspeak-feedback"
    )
    try:
        root.mkdir(parents=True, exist_ok=True)
    except OSError:
        root = Path(event.get("cwd") or Path.cwd()) / ".plainspeak-feedback"
        root.mkdir(parents=True, exist_ok=True)
    return root / "observations.jsonl"


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0

    labels = classify(str(event.get("prompt", "")))
    if not labels:
        return 0

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "signal_types": labels,
        "session_id": event.get("session_id"),
        "turn_id": event.get("turn_id"),
    }
    try:
        with feedback_path(event).open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass

    context = (
        "PlainSpeak detected an explicit re-explanation signal: "
        + ", ".join(labels)
        + ". Identify the missing conceptual relationship or mismatched "
        "abstraction level, then answer with a materially different structure. "
        "Do not merely repeat the prior wording and do not update any skill "
        "automatically."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": context,
                }
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
