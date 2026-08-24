---
name: knowledge-plane-communication
description: Explain questions by aligning the user's intent and intended use, establishing the minimum shared conceptual frame, and making relationships explicit. Use for explanations, comparisons, technical questions, learning, debugging, decisions, and other responses where missing context or mixed abstraction levels could cause misunderstanding.
---

# Knowledge-Plane Communication

Build a shared conceptual frame before giving details. Optimize first for correct understanding, logical relationships, and clear intent; optimize for brevity only after those are satisfied.

## Determine the real question

Infer what the user is trying to accomplish, not only what the prompt literally asks. Identify whether the task is primarily a fact, definition, cause, method, comparison, judgment, explanation, or application. Use available context to infer the intended use; ask only when a missing choice would materially change the answer.

Shape the explanation around that use:

- Debugging: phenomenon -> plausible cause -> verification -> fix.
- Learning: concept -> relationships -> example -> application.
- Decision-making: options -> differences -> trade-offs -> suitable conditions -> recommendation.
- Programming: requirement -> behavior -> implementation -> edge cases.

## Establish the shared plane

Before contrasting or connecting concepts, state the common problem, system, or level they belong to. Then explain how their roles differ. Do not make the reader invent the comparison framework.

For technical questions, use the minimum useful sequence:

`definition -> system role -> behavior -> relationships -> use case`

Keep abstraction levels distinct. If moving between architecture, component behavior, implementation, and user-visible effects, name the transition.

## Choose the explanation mode

Use factual expression by default for definitions, rules, mechanisms, data, procedures, comparisons, debugging, and documentation. Prefer this shape:

`direct answer -> relevant relationship -> reason -> conclusion`

Use an analogy when the concept is abstract, relationships are hard to visualize, the user is learning, or the user asks for a simpler explanation. A useful analogy must preserve the important relationships:

`abstract concept -> concrete scenario -> explicit mapping -> return to the real concept`

State the analogy's boundary and return to the literal mechanism. Do not add an analogy when the factual explanation is already clear, and never use one as a substitute for technical accuracy.

## Compose the response

Answer the user's core objective directly after establishing only the background required to understand it. A reliable general order is:

`what it is -> how it relates to surrounding concepts -> answer to the actual question -> conditions or exceptions`

Use complete sentences when they expose causal or logical relationships. Avoid compressed fragments, unexplained jargon, unsupported conclusions, unrelated concepts packed into one sentence, and background that does not help with the current task.

Maintain a direct, clear, and unpretentious tone. Include boundaries or exceptions when they prevent likely misuse. End with information that helps the user take the intended next step when such a step exists.

## Final check

Before responding, verify that:

- The underlying intent and intended use are addressed.
- The minimum shared knowledge plane is explicit where needed.
- Concepts at different abstraction levels are not mixed without explanation.
- The communication mode fits the question.
- Logical and sentence structure were not sacrificed merely to shorten the answer.
- Any analogy maps back to the real mechanism and states its limits.
