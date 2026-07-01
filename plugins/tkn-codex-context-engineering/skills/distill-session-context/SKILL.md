---
name: distill-session-context
description: Distill a repo-local Codex session note into a short review candidate for reusable context. Use when the user asks to distill, summarize, extract reusable learning, turn a session note into context, prepare context candidates, review pending distillationStatus, or create decision/working-context/Skill/AGENTS candidates from `.codex-context/sessions`.
---

# Distill Session Context

Use this skill to turn one session note into a reviewable context candidate.

Default to candidate generation. Do not mark the source session as distilled, update working context, create decision records, promote global context, or edit AGENTS.md/Skills unless the user explicitly asks for that follow-up.

## Workflow

1. Identify the source session note.
   - Prefer a user-specified `.codex-context/sessions/*.md` file.
   - If none is specified, inspect `.codex-context/working-context.md` or ask for the intended session note when multiple candidates are plausible.
2. Optionally run `audit-context-freshness` first when the session is old or `distillationStatus` is pending/partial.
3. Run a dry-run distillation to confirm the output path and extracted sections.
4. Use `--write` only when a durable candidate file is useful.
5. Review the generated candidate before promoting anything.

## Commands

Dry-run distillation:

```bash
python <plugin-root>/scripts/context_bridge/distill_session_context.py \
  --session .codex-context/sessions/<session-note>.md \
  --dry-run
```

Write a candidate under ignored local work files:

```bash
python <plugin-root>/scripts/context_bridge/distill_session_context.py \
  --session .codex-context/sessions/<session-note>.md \
  --write
```

The default destination is `.local/codex-context/distilled-session-candidates/`.

Classify the candidate when the likely destination is already clear:

```bash
python <plugin-root>/scripts/context_bridge/distill_session_context.py \
  --session .codex-context/sessions/<session-note>.md \
  --kind decision-candidate \
  --write
```

Supported `--kind` values:

- `candidate`
- `decision-candidate`
- `working-context-update`
- `skill-candidate`
- `agents-candidate`

## Promotion Boundary

The generated file is only a review candidate. Promotion is a separate step.

- Use `record-decision` for accepted repository decisions.
- Use `maintain-working-context` for accepted repository current truth.
- Use `promote-global-context` for explicit global writes.
- Update AGENTS.md or Skills only after checking current repository behavior and public/private path safety.

## Safety

- Treat session notes as raw or silver context, not current truth.
- Do not copy full chat transcripts or full session notes into candidates.
- Do not distill a session note that contains secrets, credentials, tokens, private keys, full env vars, large logs, or unnecessary personal/customer data.
- Keep candidate output in `.local/` unless the user explicitly requests a repository artifact.
