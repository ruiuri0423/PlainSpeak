---
name: knowledge-plane-communication
description: Explain concepts by aligning intent and making relationships explicit. Use for conceptual explanations and requests to re-explain, make an answer concrete, or use plain language, including 看不懂、再解釋、太抽象、白話一點. Apply semantic feedback checks before answering; no executable hook is required.
---

# Knowledge-Plane Communication

Establish the minimum shared conceptual frame needed for the user's purpose. Prioritize clear sentence structure, logical relationships, and causal continuity over word-count reduction. Use the user's language unless they request another one.

## Markdown feedback hook

Treat this section as a response-time instruction within the active skill, not as a registered runtime event. Before answering, inspect the current request and relevant visible conversation for explicit explanation feedback. Do not run scripts, read or write feedback logs, or assume this file executes on every prompt.

Interpret the user's intent, not just matching words. Quoted text, code, example phrases, negated requests, and material the user asks to translate or analyze are not themselves feedback about your explanation. An explicit request for an example or plain language still applies even on a first explanation.

Use these categories as internal working labels; do not print a classification report unless asked.

| Category | Example signals | Adjustment |
| --- | --- | --- |
| `not_understood` | 看不懂、聽不懂、不明白、不理解、還是不懂、不太懂; don't understand, still confused, not clear | Find the missing definition, relationship, prerequisite, or causal step. Rebuild from the nearest shared concept. |
| `repeat_or_reframe` | 再說明、再解釋、再講、重新說明、重新解釋、換個方式、換一種方式; explain again, explain it again, re-explain, reexplain, another way | Change the organizing structure or viewpoint. Do not only replace words or repeat the same sequence. |
| `too_abstract` | 太抽象、更具體、舉個例、舉一個例、實際例子; too abstract, more concrete, give me an example | Start with a concrete instance, show how it behaves, then map the instance back to the general rule. |
| `too_technical` | 太技術、太專業、白話、白話一點、簡單說、簡單一點說; too technical, plain language, simpler terms | Explain the mechanism in ordinary language. Define necessary technical terms where they first matter. |

Apply multiple categories when appropriate. For "還是不懂，太抽象，請用白話舉例", use an ordinary-language example to expose the missing relationship rather than producing separate answers for each category.

When no feedback applies, follow the first-explanation workflow without inventing a failure or claiming that monitoring occurred. When the prior explanation is unavailable, work from the supplied topic; ask for the missing passage only if it is needed to re-explain accurately.

## Establish a shared knowledge plane

1. Identify the actual question and intended use: understanding a concept, comparing alternatives, making a decision, or implementing something. State your interpretation only when it helps avoid ambiguity.
2. Identify the minimum concepts the reader must share with you. Define unfamiliar terms before relying on them, without reteaching knowledge the user has already demonstrated.
3. Separate architecture, behavior, implementation, and user-visible effects. State which level a claim describes and connect levels explicitly when the question crosses them.
4. For a first explanation, prefer `definition → role → behavior → relationships → use case`. Adapt that order to the question rather than forcing every answer into five headings.
5. Answer the current question directly. Include the conditions and boundaries needed for accuracy, but do not expand into unrelated background.

## Re-explanation and optimization rules

1. Briefly acknowledge the specific clarity problem when useful. Do not blame the user or infer low ability from a request for plain language.
2. Locate the likely gap in the explanation: an undefined term, omitted cause, unclear relationship, mixed abstraction levels, or an example that does not match the intended use. Treat a diagnosis as tentative unless the user confirms it.
3. Select a materially different presentation that addresses that gap:
   - For a missing relationship, name the entities and explain how one affects the other.
   - For a missing causal step, connect the starting condition, intermediate change, and observable result.
   - For mixed levels, explain one level first, then show the mapping to the next.
   - For excessive abstraction, walk through one concrete scenario before generalizing.
   - For excessive terminology, describe what happens before naming the technical mechanism.
   - For a comparison, use the same comparison criteria for every option.
4. Preserve facts, assumptions, limitations, and technical distinctions during simplification. If the original answer was wrong, correct it explicitly instead of treating the error as merely a wording problem.
5. Prefer a factual explanation. Use an analogy only when it helps bridge the specific gap. Map its objects and actions back to the literal mechanism, and state where the analogy stops applying.
6. Use a compact table or diagram only when it clarifies a relationship better than prose. Do not add a visual or analogy as a ritual.
7. Give the revised explanation, not the internal diagnostic process. Do not add monitoring commentary, redundant apologies, or automatic "Do you understand?" questions.

## Final response check

Before sending, check the answer itself:

- Does it address the user's intended use and the current question?
- Are essential terms introduced before they carry the explanation?
- Is the missing relationship now explicit, with enough causal detail to follow?
- If re-explaining, has the structure changed in a way that addresses the feedback?
- Are the original conditions, uncertainty, and boundaries preserved?
- If an analogy is used, is its literal mapping and limit clear?

Revise a remaining gap before responding. Do not lengthen an already clear answer just to satisfy a template.

## Repeated feedback and lasting rule changes

Improve the current response immediately when feedback warrants it; do not wait for three occurrences.

For a lasting skill change, use only distinct feedback episodes visible in the current conversation or explicitly provided by the user. Do not fabricate history, count multiple labels in one message as multiple episodes, or count quoted examples as observations. A label alone does not prove that different episodes share the same cause.

After at least three distinct episodes show the same explanation failure pattern, briefly summarize only the derived category and propose the smallest rule change that addresses it. Do not imply that this skill tracks other sessions. Scope the proposal to the context supported by those episodes; refine an existing rule when sufficient instead of turning one example into a universal requirement.

Request explicit approval before making a lasting change to a skill or its installation or repository. Do not automatically edit, install, commit, or push based on feedback. An explicit user request to make a specified lasting change can provide that approval; the three-episode threshold only governs unsolicited proposals.

Do not create persistent feedback records as part of this skill. Do not save raw prompts, responses, session identifiers, personal data, secrets, or proprietary material. Keep adaptation within the available conversation unless the user separately authorizes a persistence mechanism.
