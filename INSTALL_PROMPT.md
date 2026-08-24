# PlainSpeak Monitor installation prompt

Paste this into Codex after cloning or opening this repository:

```text
Install the PlainSpeak Monitor plugin from this repository.

Before changing anything, show this impact notice and ask for explicit confirmation:
- The plugin adds a UserPromptSubmit command hook. A local Python script examines each submitted prompt for a small fixed list of phrases that explicitly request re-explanation.
- The script is deterministic; it is not a background model or reviewer agent.
- It never stores raw prompt text. On a match it stores only timestamp, derived labels, session id, and turn id.
- Global installation affects future Codex sessions for this user. Codex separately requires hook review and trust with /hooks.
- Skill changes are never automatic. Three similar observations only trigger a proposal that still requires my approval.

If I approve global installation, install plainspeak-monitor from this repository's local marketplace into my user environment. Do not edit global AGENTS.md unless I separately approve the exact diff.

If global installation is unavailable or fails, do not silently fall back. Explain the failure and ask whether I approve project-local installation under the current repository's .codex configuration. State that project-local hooks run only in trusted projects.

After installation, report exact scope and paths, observation-log path, /hooks trust and disable steps, new-task requirement, and complete rollback steps.
```

## Portable path conventions

Resolve these placeholders at installation time:

- `<repo-root>`: absolute root of the currently opened or cloned PlainSpeak repository.
- `<plugin-root>`: `<repo-root>/plugins/plainspeak-monitor`.
- `$CODEX_HOME`: current user's Codex configuration directory; when unset, use the platform's normal Codex user directory.
- `<project-hooks>`: `<repo-root>/.codex/hooks.json`.

Do not assume a drive letter, operating-system username, home-directory spelling, or checkout location.

## Expected global commands

Resolve `<repo-root>` from the current workspace first:

```text
codex plugin marketplace add <repo-root>
codex plugin add plainspeak-monitor@ruiuri0423
```

For local fallback, merge the hook into `<project-hooks>`, preserve existing hooks, and ask before writing. Never replace an existing hooks file wholesale. Resolve the script from `<plugin-root>/scripts/record-feedback.py`; do not embed the original developer's absolute path.
