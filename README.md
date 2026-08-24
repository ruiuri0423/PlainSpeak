# PlainSpeak

PlainSpeak is a Codex skill for producing explanations that align with the user's intent, establish a shared conceptual frame, and make relationships explicit before introducing detail.

## What it does

- Identifies the user's underlying objective and intended use.
- Establishes the minimum shared knowledge plane needed for understanding.
- Separates architecture, behavior, implementation, and user-visible effects.
- Uses factual explanations by default and bounded analogies when they improve understanding.
- Preserves logical and causal relationships instead of optimizing only for brevity.

## Repository structure

```text
.codex/skills/knowledge-plane-communication/
├── SKILL.md
└── agents/
    └── openai.yaml
Knowledge_Plane_Communication_Skill.docx
```

The Word document is the original source specification. The `.codex/skills` directory contains the packaged, executable Codex skill.

## Use in Codex

Open this repository as a Codex workspace and invoke:

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
