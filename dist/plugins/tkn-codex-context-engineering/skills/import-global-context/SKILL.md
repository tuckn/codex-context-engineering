---
name: import-global-context
description: user-global Codex context のうち選択した内容を ~/.codex-context から現在の repository の .codex-context/global-context へ import する。global Codex context を現在の repo に読み込み、load、import、apply する依頼で使う。
---

# Import Global Context

ユーザーが user-global Codex context を現在の repository に読み込むよう依頼したときに、この skill を使う。

目的は、global context を自動 instruction に変えずに、chat と repository をまたいだ repository 作業を DRY にすることだ。

## Source and destination

Source:

`~/.codex-context`

Destination:

`<repo>/.codex-context/global-context`

import したファイルは historical reference として扱う。現在の user request、system/developer instructions、repository `AGENTS.md`、現在の file contents、git state を上書きしない。

## When to use

ユーザーが次のように依頼したときに、この skill を使う。

- "global contextを読み込んで"
- "`~/.codex-context` をこのrepoに取り込んで"
- "他チャットのCodex文脈を使って"
- "import global context"

すべての task で自動的に使わない。Global context は意図的に import するものだ。

## Workflow

1. repository `AGENTS.md` と必須の repository specs の事前確認。
2. `.codex-context/working-context.md` が存在し、関連する場合の確認。
3. `~/.codex-context` の存在確認。
4. 関連する global materials の判断。
   - `working-context.md`
   - accepted global decisions
   - relevant candidates
5. script の dry-run mode での実行。
6. ユーザーが import または write を依頼している場合、`--write` 付きでの script 実行。
7. 生成された import manifest の確認。
8. 現在の repo state と比較したうえでの imported context の利用。
9. 非自明な作業での、import した内容と利用方法の session note への記録。

## Script

repository root から実行する推奨 command:

```bash
python3 plugins/tkn-codex-context-engineering/scripts/context_bridge/import_context.py \
  --source ~/.codex-context \
  --dest .codex-context/global-context \
  --include working-context,decisions,candidates \
  --dry-run
```

Write mode:

```bash
python3 plugins/tkn-codex-context-engineering/scripts/context_bridge/import_context.py \
  --source ~/.codex-context \
  --dest .codex-context/global-context \
  --include working-context,decisions,candidates \
  --write
```

global store が大きい場合は、`--decision <filename>` または `--candidate <filename>` で選択した file だけを import する。

## Import destination contract

script が書き込む内容:

```text
.codex-context/global-context/
  README.md
  working-context.md
  decisions/
  candidates/
  imports/
    YYYYMMDDTHHMMSS+0900-import-manifest.md
```

manifest に記録する内容:

- source path
- destination path
- imported files
- skipped files
- warnings
- timestamp

## Safety

- secrets、credentials、tokens、private keys、full env vars、large logs、不要な personal/customer data の import 禁止。
- imported context 全体の盲目的な読み込み禁止。manifest と user request に関連する specific files の優先。
- global source に sensitive に見える内容がある場合、停止して user への確認。
- imported context が repository rules と矛盾する場合、repository rules の優先と session note への conflict 記録。
