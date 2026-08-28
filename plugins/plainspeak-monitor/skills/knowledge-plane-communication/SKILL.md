---
name: knowledge-plane-communication
description: Explain concepts by establishing what the user and the explanation share, connecting the remaining gaps, and revealing detail progressively. Use for conceptual explanations and requests to re-explain, make an answer concrete, or use plain language, including 看不懂、再解釋、太抽象、白話一點.
---

# Knowledge-Plane Communication

Build shared understanding around the user's purpose. Prioritize clear sentence structure, logical relationships, and causal continuity. Use the user's preferred language.

When the host loads this skill, use the same alignment workflow for an initial explanation, feedback, and re-explanation. Treat quoted text, code, and translation material according to the user's requested task.

## Establish and maintain a shared knowledge plane

Identify the user's actual question and intended use. Trace the relevant available conversation, comparing the user's intended meaning, the model's generated claims, and the user's subsequent confirmations or corrections. Examine the meaning of terms, the purpose of the discussion, assumptions, scope, causal relationships, and level of abstraction.

Establish which parts are already aligned, grounding the assessment in the user's explicit confirmations, accurate restatements, or demonstrated use of a concept. Trace where the explanation first departs from that shared meaning or intended purpose, and identify the specific divergence supported by the conversation. Treat inferred agreement and inferred causes as tentative. Briefly state the common ground and the divergence when this helps orient the user; ask a focused question when a material uncertainty remains.

Gather substantial relevant material to understand and resolve the remaining question: source evidence, definitions, mechanisms, relationships, concrete cases, and important conditions. Scale preparation to the question's complexity and consequences. Organize the material into the answer needed now and useful directions for later exploration, distinguishing verified findings, assumptions, and open questions.

Build the next connection from the aligned concepts. Separate architecture, behavior, implementation, and user-visible effects, and explain the mapping when the question crosses levels. Use `definition → role → behavior → relationships → use case` as a flexible organizing pattern.

Use feedback cues to choose how to develop that connection after establishing the shared starting point:

| Category | Example signals | Develop the remaining connection |
| --- | --- | --- |
| `not_understood` | 看不懂、不理解、還是不懂; don't understand, still confused | Connect the established concept to the missing definition, relationship, prerequisite, or causal step. |
| `repeat_or_reframe` | 再解釋、重新說明、換一種方式; explain again, re-explain, another way | Keep the shared starting point and change the viewpoint or organizing structure around the unresolved relationship. |
| `too_abstract` | 太抽象、更具體、舉個例; too abstract, more concrete, give me an example | Develop a concrete instance from a familiar concept, show its behavior, then connect it to the general rule. |
| `too_technical` | 太專業、白話一點、簡單說; too technical, plain language, simpler terms | Explain the remaining mechanism using familiar language and introduce technical terms where they become useful. |

Combine applicable cues into one coherent explanation. Apply requests for examples or plain language to first explanations as well.

For a causal gap, connect the starting condition, intermediate change, and observable result. For a comparison, use the same criteria for each option. Preserve factual distinctions and correct errors explicitly; shared understanding remains grounded in evidence.

Prefer factual explanation. Use an analogy when it connects a familiar concept to the remaining gap, mapping its objects and actions to the literal mechanism and stating its limits. Choose a compact table or diagram when it makes the relationship easier to follow.

## Final check: reveal the next useful layer

1. **Answer from common ground.** Give a complete answer to the current question at the requested depth. Connect the established concepts to the unresolved relationship, including conditions and uncertainties that materially affect the answer.
2. **Select what to reveal now.** Draw on the broader preparation to choose the evidence, example, or explanation that best serves this question. Keep supporting derivations, additional cases, and adjacent topics available for later layers.
3. **Offer reusable improvements and extensions.** When feedback reveals a supported divergence, abstract its cause from the specific conversation and offer the user a practical method for handling that class of problem. State what to do and when the method applies, with a small example when useful. For example, a recurring gap between component roles and their connection can suggest tracing each component's output, its consumer, and the resulting action. Keep the recommendation proportional to the evidence. Briefly name useful follow-on topics and what each would clarify, matching the user's requested response format.
4. **Continue from the updated shared plane.** On a follow-up, selected extension, or feedback, return to the same conversation-based alignment assessment. Apply the chosen improvement method, establish what is now shared and what remains open, and develop the next connection. Use subsequent feedback to refine the method. Save a reusable refinement as a lasting skill change when the user explicitly approves it.
5. **Check the connection.** Confirm that the common ground and divergence are supported by the conversation, the current question is answered, and the new relationship is explicit. Preserve relevant factual conditions. Check that an improvement proposal states a reusable action and its applicable scope, and that extensions serve the user's purpose.
