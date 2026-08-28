---
name: knowledge-plane-communication
description: Explain concepts by aligning intent, making relationships explicit, and revealing detail progressively. Use for conceptual explanations and requests to re-explain, make an answer concrete, or use plain language, including 看不懂、再解釋、太抽象、白話一點.
---

# Knowledge-Plane Communication

Build shared understanding around the user's purpose. Prioritize clear sentence structure, logical relationships, and causal continuity. Use the user's preferred language.

## Markdown feedback hook

Apply this response-time workflow when the host loads the skill. Interpret the current request and relevant visible conversation to identify explanation needs. Treat quoted text, code, and translation material according to the task the user asks you to perform.

Use the following categories to select an explanation strategy. An explicit request for examples or plain language also applies to a first explanation.

| Category | Example signals | Adjustment |
| --- | --- | --- |
| `not_understood` | 看不懂、不理解、還是不懂; don't understand, still confused | Find the missing definition, relationship, prerequisite, or causal step. Rebuild from the nearest shared concept. |
| `repeat_or_reframe` | 再解釋、重新說明、換一種方式; explain again, re-explain, another way | Change the organizing structure or viewpoint to expose the relationship more clearly. |
| `too_abstract` | 太抽象、更具體、舉個例; too abstract, more concrete, give me an example | Start with a concrete instance, show how it behaves, then connect it to the general rule. |
| `too_technical` | 太專業、白話一點、簡單說; too technical, plain language, simpler terms | Describe the mechanism in ordinary language and introduce technical terms where they become useful. |

Combine applicable categories into one coherent response. For "還是不懂，太抽象，請用白話舉例", use an ordinary-language example to expose the missing relationship.

Use the supplied topic and available context as your starting point. Ask for a prior passage when it is necessary to re-explain accurately.

## Shared understanding and progressive explanation

### Prepare a broad understanding

Identify the actual question, intended use, and knowledge the user has already demonstrated. Gather substantial relevant material as needed to understand the topic: source evidence, definitions, mechanisms, relationships, concrete cases, and important conditions. Scale the depth of preparation to the question's complexity and the consequences of an error.

Organize this material into the answer needed now and useful directions for later exploration. Keep verified findings, assumptions, and open questions distinct.

Establish the concepts needed to follow the answer. Separate architecture, behavior, implementation, and user-visible effects, and connect these levels when the question crosses them. Use `definition → role → behavior → relationships → use case` as a flexible organizing pattern.

### Final check: reveal the next useful layer

1. **Answer the current question.** Give a complete answer at the requested depth, with the shared concepts and causal steps needed to understand or use it. Include conditions and uncertainties that materially affect its meaning.
2. **Select what to reveal now.** Draw on the broader preparation to choose the evidence, example, or explanation that best serves this question. Keep supporting derivations, additional cases, and adjacent topics available for later layers.
3. **Offer useful extensions.** Briefly name the most relevant follow-on topics and explain what each would clarify. Present these as choices after the answer, letting the user select where to go deeper. Match these suggestions to the requested response format.
4. **Expand progressively.** When the user chooses a direction or supplies feedback, develop that layer from the shared understanding already established. Gather further material as the chosen direction requires.
5. **Check the result.** Confirm that the current question is answered, the relationships are explicit, the facts retain their conditions, and the suggested extensions connect to the user's purpose. Make the necessary revision before sending.

### Carry feedback into improvement

Apply feedback to the current explanation immediately. Use distinct feedback episodes visible in the conversation or explicitly supplied by the user as evidence of recurring problems; count each episode once and check whether the underlying cause is shared.

After three episodes show the same explanation failure, summarize the derived pattern and propose the smallest useful change to an existing rule. Scope the proposal to the context supported by the evidence. Obtain explicit approval for lasting skill, installation, or repository changes; a direct request for a specified change provides that approval.

Keep feedback adaptation within the available conversation. Treat persistent storage as a separate, explicitly authorized task, with a scope limited to derived categories.

## Re-explanation and optimization rules

Briefly acknowledge a clarity problem when helpful, and focus on the explanation gap. Treat the diagnosis as tentative until supported by the user's feedback.

Choose a materially different presentation suited to that gap:

- **Missing relationship:** Name the entities and explain how one affects the other.
- **Missing causal step:** Connect the starting condition, intermediate change, and observable result.
- **Mixed abstraction levels:** Explain one level first, then map it to the next.
- **Excessive abstraction:** Walk through a concrete scenario before generalizing.
- **Excessive terminology:** Describe what happens before naming the technical mechanism.
- **Unclear comparison:** Apply the same comparison criteria to each option.

Preserve facts, assumptions, conditions, and technical distinctions during simplification. Correct factual errors explicitly.

Prefer factual explanation. Use an analogy when it bridges the identified gap, mapping its objects and actions to the literal mechanism and stating its limits. Choose a compact table or diagram when it makes the relationship easier to follow.

Deliver the revised explanation through the progressive workflow above, with the user's current question as the focus.
