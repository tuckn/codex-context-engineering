# codex-context-engineering

Codex context engineering skills and support scripts for carrying useful working context across chats and repositories.

## Contents

- `.agents/plugins/marketplace.json`: Codex plugin marketplace manifest for GitHub-based installation.
- `dist/plugins/tkn-codex-context-engineering/`: Codex plugin bundle containing the managed Skills and support scripts.
- `.agents/skills/`: Source Skills used directly from this repository and available for legacy copy-based distribution.
- `.agents/skills/import-global-context/scripts/`: Python scripts for importing user-global `~/.codex-context` into repo-local `.codex-context/global-context/`.
- `.agents/skills/promote-global-context/scripts/`: Python scripts for promoting repo-local context into user-global `~/.codex-context`.
- `scripts/sync_skills/`: Legacy Skill copy distribution script and target manifest.

## Install As A Codex Plugin

Add this repository as a Codex plugin marketplace:

```sh
codex plugin marketplace add tuckn/codex-context-engineering --ref main
```

The marketplace installs `tkn-codex-context-engineering` from:

```text
dist/plugins/tkn-codex-context-engineering/
```

The plugin includes these Skills:

- `import-global-context`
- `maintain-session-note`
- `maintain-working-context`
- `organize-brain-dump`
- `promote-global-context`
- `record-decision`
- `resume-session`
- `review-decisions`

## Initial Distribution Targets

The distribution manifest uses Windows paths as canonical paths.

- `C:\Users\ExampleUser\workspaces\coding\Microsoft\PowerShell`
- `C:\Users\ExampleUser\workspaces\coding\Python\example-project`
- `C:\Users\ExampleUser\workspaces\writing\notes`
- `C:\Users\ExampleUser\workspaces\developing\example-platform`

## Current Policy

- The source of truth for Skills is `.agents/skills/`.
- The public plugin bundle is `dist/plugins/tkn-codex-context-engineering/`.
- The GitHub marketplace manifest is `.agents/plugins/marketplace.json`.
- Existing `plugins/tkn-codex-context-engineering/skills/` copies from the Notes Vault are intentionally not migrated.
- Distribution may overwrite target repository Skills without backup or mandatory confirmation.
- A dry-run option should exist in distribution tooling, but running dry-run before every update is not mandatory.
- Current preferred distribution is Codex plugin marketplace installation from GitHub.
- Copy-based `.agents/skills/<SKILL>` distribution remains available for environments where plugins are unavailable.
- Migration traceability was distilled into this README for the public plugin repository.

## Migration Summary

This repository was separated from the Notes Vault as the dedicated source repository for Codex context engineering work.

User-confirmed starting points:

- Repository name: `codex-context-engineering`.
- GitHub repository was prepared privately before public release.
- Git history from the Notes Vault plugin folder is not preserved; this repository starts from the current file state.
- Local path: `C:\Users\ExampleUser\workspaces\coding\repositories\codex-context-engineering`.
- Distribution manifests use Windows paths as canonical paths.
- Distribution scripts are Python.
- Distribution may overwrite target Skills without backup, mandatory confirmation, or mandatory diff display.
- Target repositories may hand-edit their local Skill copies, but source updates can overwrite them.

Migration outcomes:

- Eight managed context engineering Skills are currently kept under `.agents/skills/`.
- Legacy plugin Skill copies from `plugins/tkn-codex-context-engineering/skills/` were treated as discardable duplicates.
- Context bridge scripts were moved into the relevant Skill-local `scripts/` folders.
- Plugin metadata is packaged as `dist/plugins/tkn-codex-context-engineering/.codex-plugin/plugin.json`.
- `organize-brain-dump` has been intentionally promoted into this repository as a reusable context Skill.
- Other Vault-specific Skills and sessions stay in the Notes Vault unless intentionally promoted later.
- Detailed migration traceability was distilled before public release; this repository keeps the concise public summary.

## Sync Skills

`scripts/sync_skills/sync_skills.py` copies the managed Skills from this repository's `.agents/skills/` directory into one or more target repositories.

Create your local target manifest from the sample:

```powershell
Copy-Item scripts\sync_skills\targets_sample.json scripts\sync_skills\targets.json
```

Edit `scripts/sync_skills/targets.json` for your machine. This file is intentionally ignored by Git because it contains local absolute paths. Windows paths are canonical; when the script runs outside Windows, drive paths such as `C:\example\repo` are converted to `/mnt/c/example/repo`.

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

Arguments:

- `--manifest`: JSON manifest path. Defaults to `scripts/sync_skills/targets.json`.
- `--target`: target name from the manifest, or `all`. Defaults to `all`.
- `--skill`: one managed Skill to sync. Repeat to sync multiple Skills. Defaults to all managed Skills.
- `--repo-root`: source repository root override. Usually not needed.
- `--dry-run`: print planned copy operations without writing files.

Dry-run all targets:

```sh
python3 scripts/sync_skills/sync_skills.py --dry-run
```

Sync one target:

```sh
python3 scripts/sync_skills/sync_skills.py --target notes
```

Sync one Skill to one target:

```sh
python3 scripts/sync_skills/sync_skills.py --target notes --skill maintain-session-note
```

Use a non-default manifest:

```sh
python3 scripts/sync_skills/sync_skills.py --manifest scripts/sync_skills/targets_sample.json --dry-run
```
