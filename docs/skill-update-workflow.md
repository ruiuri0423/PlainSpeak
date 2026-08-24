# Knowledge-Plane Skill Update Workflow

This repository is the source of truth for the `knowledge-plane-communication` skill.

## Paths

- Editable skill source: `.codex/skills/knowledge-plane-communication/`
- Local observation log: `.feedback/knowledge-plane-communication.jsonl`
- Global installed copy: `%CODEX_HOME%/skills/knowledge-plane-communication/`

The observation log is intentionally ignored by Git. It may contain anonymized contextual summaries from local conversations and must not contain raw user messages, secrets, personal data, or proprietary content.

## Feedback signal

Record an observation only when the user clearly indicates that an explanation must be repeated or reframed, for example because it was unclear, answered at the wrong abstraction level, omitted a needed relationship, or used an unhelpful analogy.

Each JSONL record should contain only:

- `timestamp`
- `intent_type`
- `failed_pattern`
- `requested_change`
- `successful_adjustment`, when known

## Update gate

Do not change the skill from a single observation. When at least three observations show the same underlying failure pattern:

1. Summarize the pattern without quoting private conversation content.
2. Propose the smallest instruction change that would correct it.
3. Ask the user to approve the change.
4. Update the repository skill and validate it.
5. Commit and push only when requested or already authorized.
6. Reinstall or synchronize the global copy after the source change is accepted.

Treat the repository version as authoritative. The globally installed copy is a runtime artifact, not the editing source.
