---
name: knowledge-plane-communication
description: Explain questions by aligning intent, establishing a shared conceptual frame, and making relationships explicit. Use for explanations and whenever the user says an earlier explanation was unclear or asks for another explanation.
---

# Knowledge-Plane Communication

Establish the minimum shared conceptual frame before details. Separate architecture, behavior, implementation, and user-visible effects.

For a first explanation, use `definition -> role -> behavior -> relationships -> use case`. Match the user's intended use.

When the hook reports a re-explanation signal:

1. Acknowledge what failed without blaming the user.
2. Infer the missing relationship or mismatched abstraction level.
3. Reframe with a materially different structure, example, diagram, or analogy.
4. Map an analogy back to the literal mechanism and state its boundary.
5. Answer the current question without discussing monitoring unless asked.

After three observations show the same failure pattern, summarize only derived categories, propose the smallest skill change, and request explicit approval before editing, installing, committing, or pushing. Never store raw prompts, responses, secrets, personal data, or proprietary content.
