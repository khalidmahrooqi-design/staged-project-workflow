---
name: staged-project-workflow
description: Carry tasks and projects through briefing, architecture, a phased plan with checklists, execution, evidence-based verification, and a follow-up update plan when needed. Use when starting, building, repairing, reviewing, or continuing work; scale the stages to the task's complexity.
license: MIT
metadata:
  author: Khalid Hamad Al Mahrouqi
  version: "1.0.0"
---

# Staged Project Workflow

Make the requested outcome concrete, plan how to reach it, execute the plan, and check the actual result. Keep the user informed when a decision or finding affects the work.

## Scale and authorization

For a small task, combine the stages into a short explanation and a direct check. For substantive work, show the architecture and phased checklist before implementation and keep their status current. Architecture means the structure appropriate to the work: software components, document sections, analysis inputs and calculations, or operational roles and flows.

Follow the user's current scope, instructions, permissions, save locations, and source-handling requirements. This skill grants no authority to publish, deploy, spend money, send messages, install dependencies, delegate, or change unrelated systems. Reuse authorization already given. Keep plans in chat or available planning tools unless saving them is authorized. Do not create files or folders merely to satisfy the workflow.

## 1. Brief and establish the baseline

- State the objective, intended users, deliverables, boundaries, constraints, and observable acceptance criteria.
- Inspect relevant instructions, authoritative sources, existing work, and the current state. Separate verified facts, historical state, assumptions, and missing evidence.
- Ask only for information or choices that materially affect correctness, scope, destination, cost, or authorization. Where supported, use a structured prompt with a recommendation and alternatives. Continue independent work while a required answer is pending; do not treat silence as approval.
- If the brief is clear, proceed without an unnecessary briefing interview.

Exit: the outcome and acceptance criteria are clear enough to design; any dependent work awaiting input is identified.

## 2. Design the architecture

Describe how the result will be structured: components or workstreams, their responsibilities, inputs and outputs, dependencies, source and destination locations, and relevant interfaces. Explain decisions that affect maintainability, correctness, or the user's choice. For an existing project, map its current structure and identify the changes required. Use a diagram or table only when it helps understanding.

Include material risks and their controls, such as preserving source documents, reconciling totals, protecting credentials, or retaining a recovery path. Avoid adding unrelated features or infrastructure.

Exit: the proposed structure connects the objective to an implementable result.

## 3. Make the execution plan and checklists

Break the architecture into ordered stages with dependencies. Each stage needs a deliverable, concrete steps, acceptance checks, and the evidence that will establish completion. Choose the smallest useful checklist; add owners or estimates only when known or requested.

Use `pending`, `in progress`, `completed`, `blocked`, and `skipped` accurately. Check off an item only after its completion evidence exists. Explain skipped checks and blocking dependencies. The [plan template](references/plan-template.md) is optional for substantive work and handoffs.

Present the plan, then proceed within existing authorization. A visible plan does not itself require another approval. Pause dependent actions only for a genuinely unresolved decision or required authorization.

Exit: the next steps and their completion checks are clear.

## 4. Execute and maintain the plan

Work through the stages in dependency order. Preserve existing and concurrent work. Give concise updates at meaningful checkpoints, including what changed, what remains uncertain, and what comes next.

Revise the architecture or plan when findings invalidate an assumption. Explain material deviations; do not silently widen scope. Repair failures within the task's authority and rerun affected checks. If the same attempt keeps failing, investigate the cause or change approach; avoid blind retries. Stop the dependent action when access, a required decision, or an external change is needed, and continue useful independent work.

Exit: the requested deliverables exist and each implemented stage has its completion evidence or an explicit limitation.

## 5. Verify the actual results and relevant logs

Compare the final result with the acceptance criteria. Inspect the artifact, behavior, calculation, or live operation that the task requires. Review relevant build, test, runtime, conversion, deployment, audit, or change logs where available and appropriate. A command's success code or a file's existence alone does not prove the requested outcome.

Use checks proportional to the change. For software, test affected behavior and required builds; for documents, check content and permitted layout/rendering; for analysis, reconcile sources, calculations, and totals; for operations, confirm actual state and an audit trail. Follow the user's permitted reading and verification routes. Do not invent logs, fabricate passing checks, or claim a blocked check ran.

Record each acceptance check as passed, failed, or not run, with evidence and limitations. Fix in-scope failures and verify again. If evidence is unavailable, report partial or unverified completion instead of complete success. Keep secrets and unnecessary personal data out of logs and summaries.

Exit: the evidence establishes the result, or the unresolved criteria and their consequences are explicit.

## 6. Close and plan the next update when needed

Report the outcome, completed deliverables, verification, material limitations, and any unresolved action. Link to artifacts where available. Save a concise handoff only in an authorized location.

If verification exposes defects, maintenance needs, or justified improvements, prepare a prioritized next plan stating the finding, reason, proposed change, dependencies, acceptance checks, and any authorization needed. Complete required in-scope fixes now when possible; do not defer them as optional improvements. Label optional enhancements separately and do not implement expanded scope without authorization.

If no next update is justified, say so briefly. Do not create an automatic recurring loop or keep expanding a completed project.
