---
name: maintain-working-context
description: .codex-context/working-context.md を lightweight repository dashboard として作成、確認、更新する。非自明な作業開始、active work changes、important decision changes、または working context 更新依頼で使う。
---

# Maintain Working Context

`.codex-context/working-context.md` を repository の lightweight current-truth dashboard として有用に保つために、この skill を使う。

目的は、future human または Codex session がすべての session notes や decision records を読まずに、現在の repository state を素早く理解できるようにすることだ。

## File location

Default location:

`.codex-context/working-context.md`

repository が別の working context path を定義している場合、その repository instruction に従う。

## Role

`.codex-context/working-context.md` は repository の current working truth を要約する。

簡潔に記録する内容:

- current purpose
- active work
- important constraints
- recent decisions
- 次に確認すべき session notes、decision records、plans、specs

含めない内容:

- detailed chronological logs
- full conversation transcripts
- large command outputs
- secrets、credentials、tokens、private keys、full env vars、不要な personal/customer data

detail は `.codex-context/sessions/`、`.codex-context/decisions/`、または関連する repository notes に置き、working context からそれらの path へ link する。

## When to inspect

非自明な作業を始めるとき、かつ relevant current repository truth を含む可能性がある場合、`.codex-context/working-context.md` を確認する。

ユーザーが次を依頼した場合も確認する。

- work の resume
- repository context の利用
- current active work の確認
- context の更新
- decisions または session notes の review

repository を理解するためだけに `.codex-context/` 全体を読まない。working context を dashboard として使い、関連する link だけをたどる。

## When to update

repository current truth が変わる場合、特に次の場合に `.codex-context/working-context.md` を更新する。

- active work changes
- important decision の accepted、deprecated、superseded、promoted
- 新しい session note が最適な resumption point になる場合
- 新しい plan、spec、plugin、skill、script が key file になる場合
- important constraints changes
- ユーザーによる working context 更新の明示依頼

現在の task が非自明だが durable repository state を変えない場合、working context 更新が不要な理由を session note に記録する。

## Update workflow

1. repository `AGENTS.md` と必須の repository specs の確認。
2. `.codex-context/working-context.md` が存在する場合の確認。
3. 直接関連する session notes、decisions、plans、specs だけの確認。
4. chronological log ではなく、concise current state として working context を更新。
5. detail の重複より path 参照の優先。
6. `maintain-session-note` を使う場合、session note も更新し、working context 変更有無を記録。

## Suggested structure

repository により良い構造がない限り、この構造を使う。

```md
---
type: workingContext
title: <working-context-title>
description: <short-summary>
generator: Codex
status: active
promotionStatus: pending
promotedTo: []
date: YYYY-MM-DDTHH:mm:ss<system-timezone-offset-with-colon>
updated: YYYY-MM-DDTHH:mm:ss<system-timezone-offset-with-colon>
---

# Working Context

## Purpose

## Current Truth

## Active Work

## Important Constraints

## Recent Decisions

## Key Files

## Next Maintenance
```

本文冒頭に `Last updated:` は置かない。machine-readable metadata は Frontmatter に集約する。

### Frontmatter policy

- `type`: 必ず `workingContext`。
- `title`: working context の表示用タイトル。
- `description`: repository current truth の概要。空欄は `""` とするが、scan できる短い説明をできるだけ書く。
- `generator`: 必ず `Codex`。
- `status`: working context の状態。`active`、`stale`、`archived` のいずれかを使う。
- `promotionStatus`: silver artifact である working context から gold global context への昇格状態。`pending`、`partial`、`promoted`、`no-action` のいずれかを使う。
- `promotedTo`: 昇格先の paths。未昇格なら `[]`。`~/.codex-context/working-context.md`、`.codex-context/global-context/working-context.md` などを列挙する。
- `date`: working context の生成日時。既存 file で生成日時が不明な場合、filesystem の生成日時または migration 時点の日時を使う。
- `updated`: working context の内容を最後に更新した日時。Skill が本文または Frontmatter を更新したら必ず更新する。

`status` は working context 自体の鮮度・有効性だけを表す。global context へ取り込まれたかは `promotionStatus` と `promotedTo` で表す。

各 section は短く保つ。dashboard であり detailed report ではない。

## Style

- repository の primary language での記述。
- future sessions が scan しやすい stable headings の維持。
- repository files には relative paths の利用。
- absolute paths は repository 外の file を意図的に参照する場合のみ。
- scanability のための bullets 優先。
- stale items が真でなくなった場合の削除または置換。
