# tkn-codex-plugins

[English](README.md) | 日本語

Tuckn の公開 Codex plugin marketplace です。

## インストール

このリポジトリを Codex plugin marketplace として追加します。

```sh
codex plugin marketplace add tuckn/tkn-codex-plugins --ref main
```

Codex は marketplace manifest を次の場所から読み込みます。

```text
.agents/plugins/marketplace.json
```

## Marketplace の構成

- `.agents/plugins/marketplace.json`: このリポジトリの marketplace catalog。
- `plugins/`: 公開可能な Codex plugin bundle。
- `scripts/sync_skills/`: plugin bundle を元にした旧来の Skill copy-distribution tooling。

このリポジトリには完成済みの plugin bundle を置きます。開発用の source tree は別の
リポジトリに置き、完成した bundle を `plugins/<plugin-name>/` に反映します。

## Plugins

### Tuckn Codex Context Engineering

この plugin は、Codex が前回の作業の続きを理解しやすくするためのものです。リポジトリ
の状況、進行中の作業、重要な判断を軽量なメモとして残し、次の chat で同じ背景説明を
繰り返さずに再開できるようにします。

Path:

```text
plugins/tkn-codex-context-engineering/
```

詳細:

- [Plugin README](plugins/tkn-codex-context-engineering/README.md)
- [日本語 README](plugins/tkn-codex-context-engineering/README_ja.md)

## Plugin の追加

新しい plugin は次の場所に追加します。

```text
plugins/<plugin-name>/
```

各 plugin には次の manifest が必要です。

```text
plugins/<plugin-name>/.codex-plugin/plugin.json
```

次に、対応する entry を以下に追加します。

```text
.agents/plugins/marketplace.json
```

marketplace path には、次のような repo-relative path を使います。

```json
{
  "name": "plugin-name",
  "source": {
    "source": "local",
    "path": "./plugins/plugin-name"
  },
  "policy": {
    "installation": "AVAILABLE",
    "authentication": "ON_INSTALL"
  },
  "category": "Productivity"
}
```

## Legacy Skill Sync

推奨される配布方法は Codex plugin marketplace です。plugin が使えない環境では、
`scripts/sync_skills/sync_skills.py` を使って
`plugins/tkn-codex-context-engineering/skills/` を対象リポジトリへ copy できます。

sample から local target manifest を作成します。

```powershell
Copy-Item scripts\sync_skills\targets_sample.json scripts\sync_skills\targets.json
```

自分の環境に合わせて `scripts/sync_skills/targets.json` を編集します。この file は local
absolute paths を含むため、意図的に Git から無視されます。Windows paths を canonical とし、
script を Windows 以外で実行する場合は `C:\example\repo` のような drive path が
`/mnt/c/example/repo` に変換されます。

Manifest shape:

```json
{
  "targets": [
    {
      "name": "notes",
      "path": "C:\\example\\workspaces\\notes",
      "skillsPath": ".agents\\skills"
    }
  ]
}
```

よく使う commands:

```sh
python3 scripts/sync_skills/sync_skills.py --dry-run
python3 scripts/sync_skills/sync_skills.py --target notes
python3 scripts/sync_skills/sync_skills.py --target notes --skill maintain-session-note
python3 scripts/sync_skills/sync_skills.py --manifest scripts/sync_skills/targets_sample.json --dry-run
```
