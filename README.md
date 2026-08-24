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

## Installation

Prerequisites: Git and a Codex CLI release with `codex plugin` support (verified with Codex CLI 0.149.1).

### Option 1: Git marketplace (recommended)

```sh
codex plugin marketplace add ruiuri0423/PlainSpeak
codex plugin add plainspeak-monitor@ruiuri0423
```

### Option 2: Clone and install from a local marketplace

```sh
git clone https://github.com/ruiuri0423/PlainSpeak.git
codex plugin marketplace add ./PlainSpeak
codex plugin add plainspeak-monitor@ruiuri0423
```

### Option 3: Update an existing Git marketplace installation

```sh
codex plugin marketplace upgrade ruiuri0423
codex plugin add plainspeak-monitor@ruiuri0423
```

Published updates should use a new plugin version or Codex cachebuster before reinstalling.

After installation, start a new Codex task so the skill is discovered. Run `/hooks`, inspect the `UserPromptSubmit` command from `plainspeak-monitor`, and trust it only if it matches the repository source. Then invoke `$knowledge-plane-communication`, or ask Codex to use `plainspeak-monitor:knowledge-plane-communication`.

To uninstall:

```sh
codex plugin remove plainspeak-monitor@ruiuri0423
```

## Use in Codex

After installation and hook review, open a new Codex task and invoke:

```text
$knowledge-plane-communication
```

Example:

```text
Use $knowledge-plane-communication to explain the difference between an arbiter and a data path.
```

## Skill workflow

The skill guides responses through four decisions:

1. Determine the user's actual question and intended use.
2. Establish a shared conceptual plane.
3. Choose factual or analogy-based explanation.
4. Answer directly, including only boundaries and context that prevent misunderstanding.

## License

Copyright © 2026. All rights reserved. No permission is granted to copy, modify, distribute, or sublicense this repository without the copyright holder's written permission.
