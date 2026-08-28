# PlainSpeak

PlainSpeak provides a Markdown-only communication skill for clear explanations and re-explanations. All explanation rules live in [SKILL.md](plugins/plainspeak-monitor/skills/knowledge-plane-communication/SKILL.md); no Python script or runtime hook is required.

## What it does

- Identifies the user's actual question and intended use.
- Establishes what the user and the available explanation already share, then develops the remaining conceptual connection.
- Prepares a broad understanding, answers the current question at the requested depth, and offers useful directions for progressive exploration.
- Separates architecture, behavior, implementation, and user-visible effects.
- Recognizes four kinds of explanation feedback: not understood, repeat or reframe, too abstract, and too technical.
- Routes feedback and re-explanation through the same assessment of common ground and divergence in the available conversation.
- Turns supported divergence into a practical, reusable improvement method with a clear scope of application.
- Uses factual explanations by default and bounded analogies when useful.
- Preserves accuracy and causal detail instead of optimizing only for brevity.

## Markdown feedback hook

The "hook" is an instruction inside the active skill: establish the shared conceptual starting point, prepare material for the remaining question, and reveal the next useful layer. Feedback returns to that same alignment assessment.

**SKILL.md is not a registered `UserPromptSubmit` event handler.** The host must discover and load the skill. Semantic interpretation replaces the old deterministic regex matching; this version does not guarantee a check on every prompt, emit `additionalContext`, or run a background process.

| Earlier implementation | Markdown version |
| --- | --- |
| `SIGNALS` regex categories | Four semantic categories with Chinese and English examples in SKILL.md |
| `classify(prompt)` | Interpret the actual request and handle quotations or code according to the user's task |
| `UserPromptSubmit` command | Response-time feedback instructions inside the loaded skill |
| Injected `additionalContext` | One shared-knowledge workflow for initial explanations, feedback, and re-explanations |
| `observations.jsonl` with timestamps and identifiers | No persistent feedback logging; use only available conversation context |
| Three observations before proposing a skill change | Supported divergence guides a reusable improvement method for the user; saving a lasting rule change is an optional step requiring explicit approval |

Trace the relevant available conversation to establish common ground and the point of divergence. Ground the assessment in the user's confirmations, restatements, or corrections, and ask a focused question when a material uncertainty remains. Resolve the current question and offer a reusable method for similar problems, stating what to do and when it applies. Saving the method as a lasting skill rule is an optional step requiring explicit approval.

## Use the standalone Markdown file

Copy [SKILL.md](plugins/plainspeak-monitor/skills/knowledge-plane-communication/SKILL.md) into a `knowledge-plane-communication` skill folder recognized by your agent. The file is self-contained: its YAML frontmatter supplies skill metadata and its Markdown body supplies all behavior. No other repository file is needed for the explanation rules.

Invoke it using the mechanism your host supports. In Codex, the existing invocation name is retained:

```text
Use $knowledge-plane-communication to explain the difference between an arbiter and a data path.
```

Example feedback:

```text
還是不懂，太抽象，請用白話舉一個兩個 master 同時要用 SRAM 的例子。
```

If your host does not discover skills, provide the Markdown contents as instructions using a mechanism supported by that host. Merely naming a file SKILL.md does not register an event hook.

## Optional Codex plugin packaging

The repository retains its existing plugin and marketplace identifiers for compatibility. These JSON files are packaging metadata; the communication behavior is entirely in Markdown.

```text
.agents/plugins/marketplace.json
plugins/plainspeak-monitor/
├── .codex-plugin/plugin.json
└── skills/knowledge-plane-communication/SKILL.md
```

The plugin name remains `plainspeak-monitor`, but version 0.2.0 no longer installs a monitoring command or advertises a hooks capability.

The repository's existing installation commands require Git and a Codex CLI release with `codex plugin` support:

```sh
codex plugin marketplace add ruiuri0423/PlainSpeak
codex plugin add plainspeak-monitor@ruiuri0423
```

To update an existing marketplace installation after this change is merged:

```sh
codex plugin marketplace upgrade ruiuri0423
codex plugin add plainspeak-monitor@ruiuri0423
```

The version was bumped for this change. Verify that your host has loaded the updated skill and removed the old PlainSpeak command hook. If an old command remains registered, remove that old registration through your host's hook settings. Do not configure a command that tries to execute SKILL.md.

Existing feedback logs from the earlier version are not read, migrated, or deleted by this version. No installation or CLI runtime compatibility test is implied by the Markdown conversion.

To uninstall the plugin:

```sh
codex plugin remove plainspeak-monitor@ruiuri0423
```

## License

Copyright © 2026. All rights reserved. No permission is granted to copy, modify, distribute, or sublicense this repository without the copyright holder's written permission.
