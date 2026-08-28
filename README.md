# PlainSpeak

PlainSpeak provides a Markdown-only communication skill for clear explanations and re-explanations. All explanation rules live in [SKILL.md](plugins/plainspeak-monitor/skills/knowledge-plane-communication/SKILL.md); no Python script or runtime hook is required.

## What it does

- Identifies the user's actual question and intended use.
- Establishes a shared conceptual frame using the user's intended use and existing knowledge.
- Prepares a broad understanding, answers the current question at the requested depth, and offers useful directions for progressive exploration.
- Separates architecture, behavior, implementation, and user-visible effects.
- Recognizes four kinds of explanation feedback: not understood, repeat or reframe, too abstract, and too technical.
- Changes the explanation's structure to address the missing relationship.
- Uses factual explanations by default and bounded analogies when useful.
- Preserves accuracy and causal detail instead of optimizing only for brevity.

## Markdown feedback hook

The "hook" is an instruction inside the active skill: interpret the request, prepare relevant material, answer the current question, and reveal further detail progressively as the user chooses a direction.

**SKILL.md is not a registered `UserPromptSubmit` event handler.** The host must discover and load the skill. Semantic interpretation replaces the old deterministic regex matching; this version does not guarantee a check on every prompt, emit `additionalContext`, or run a background process.

| Earlier implementation | Markdown version |
| --- | --- |
| `SIGNALS` regex categories | Four semantic categories with Chinese and English examples in SKILL.md |
| `classify(prompt)` | Interpret the actual request and handle quotations or code according to the user's task |
| `UserPromptSubmit` command | Response-time feedback instructions inside the loaded skill |
| Injected `additionalContext` | Integrated shared-understanding, progressive-explanation, and feedback-improvement workflow |
| `observations.jsonl` with timestamps and identifiers | No persistent feedback logging; use only available conversation context |
| Three observations before proposing a skill change | Three distinct episodes of the same failure pattern before an unsolicited proposal; explicit approval remains required for lasting changes |

Improve the current answer immediately; the three-episode threshold applies only to proposing a lasting rule change. The skill neither rewrites itself nor tracks feedback across sessions.

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
