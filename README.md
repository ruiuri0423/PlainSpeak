# PlainSpeak

PlainSpeak is a Codex plugin that monitors explicit requests for re-explanation and provides a communication skill for producing clearer answers.

## What it does

- Identifies the user's underlying objective and intended use.
- Establishes the minimum shared knowledge plane needed for understanding.
- Separates architecture, behavior, implementation, and user-visible effects.
- Uses factual explanations by default and bounded analogies when they improve understanding.
- Preserves logical and causal relationships instead of optimizing only for brevity.

## Repository structure

```text
.agents/plugins/marketplace.json
plugins/plainspeak-monitor/
├── .codex-plugin/plugin.json
├── hooks/hooks.json
├── scripts/record-feedback.py
└── skills/knowledge-plane-communication/SKILL.md
```

The marketplace index makes this repository installable by Codex. The plugin directory contains the manifest, hook, script, and packaged skill.

## Install from the public repository

Prerequisites: Git and the Codex CLI must be installed and available on `PATH`.

Run this single command in Windows Command Prompt or PowerShell. It downloads the repository to a stable user-level directory, registers the marketplace, and installs the plugin:

```powershell
powershell -NoProfile -Command "$dst=Join-Path $env:USERPROFILE '.codex\marketplaces\plainspeak'; if (Test-Path $dst) { git -C $dst pull --ff-only } else { git clone https://github.com/ruiuri0423/PlainSpeak.git $dst }; codex plugin marketplace add $dst; codex plugin add plainspeak-monitor@ruiuri0423"
```

Review the command before running it. After installation:

1. Start a new Codex task so the plugin skill is discovered.
2. Run `/hooks`, inspect the `UserPromptSubmit` command from `plainspeak-monitor`, and trust it only if the displayed command matches the repository source.
3. Invoke `$knowledge-plane-communication`, or ask Codex to use the `plainspeak-monitor:knowledge-plane-communication` skill.

To update, run the same command again. It fast-forwards the local checkout before reinstalling the plugin. Plugin releases should use a new version or Codex cachebuster so the updated package is not confused with an older cache entry.

## Use in Codex

After installation and hook review, open a new Codex task and invoke:

```text
$knowledge-plane-communication
```

Example:

```text
Use $knowledge-plane-communication to explain the difference between an arbiter and a data path.
```

See `INSTALL_PROMPT.md` for portable installation and rollback instructions.

## Skill workflow

The skill guides responses through four decisions:

1. Determine the user's actual question and intended use.
2. Establish a shared conceptual plane.
3. Choose factual or analogy-based explanation.
4. Answer directly, including only boundaries and context that prevent misunderstanding.

## License

Copyright © 2026. All rights reserved. No permission is granted to copy, modify, distribute, or sublicense this repository without the copyright holder's written permission.
