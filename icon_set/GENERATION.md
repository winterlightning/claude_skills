# Generate and fix icons

Run the full repository on the server (a dist-only copy cannot generate Python icons). Install this project's Python dependencies, install Codex CLI, and sign in as the account running deploy.py. Ensure `codex` is on that account's PATH, or set `CODEX_BIN` to its executable path. Start `python3 icon_set/scripts/deploy.py --host 0.0.0.0 --port 8000`.

Open **Generate icon**. Enter a name, prompt, and Auto/sub/solo/container. Model is optional and defaults to the server's Codex configuration. In an icon popup, **Fix with AI** includes the existing Python path and family automatically. The agent reads that Python file in its candidate workspace and creates a new variant; the original stays intact.

Runs use `codex -a never exec --sandbox workspace-write --skip-git-repo-check`. The no-approval setting is supported by Codex's [non-interactive mode](https://developers.openai.com/codex/noninteractive/). Normal Codex account usage applies when a user starts an agent.

Submit either mission directly to the running review app:

```bash
bash icon_set/scripts/run_icon_agent.sh generate --name "Document" --family solo --prompt "A single sheet with a folded corner"
bash icon_set/scripts/run_icon_agent.sh fix --icon sub/plus --prompt "Adjust the proportions while preserving the stroke style"
```

Use `--family auto` to let the agent choose the skill, `--model MODEL_NAME` to specify a model, or `--server http://HOST:8000` for your server. These commands use the same review queue and acceptance controls as the browser.

The reusable low-level shell runner also accepts a workspace and a prompt file, plus an optional model:

```bash
bash icon_set/scripts/run_icon_agent.sh /path/to/candidate-workspace /path/to/prompt.txt
bash icon_set/scripts/run_icon_agent.sh /path/to/candidate-workspace /path/to/prompt.txt MODEL_NAME
```

The app prepares the prompt with the mission (generate or fix), icon name, requested family/skill, instructions, and fix source path. It copies the model, scripts, contracts and skills into `icon_set/data/generation-jobs/<job-id>/workspace`, then invokes the shell runner. It does not copy the feedback database or account credentials into that workspace. The model selects a unique Python filename and (for Auto) the type. Only one new Python icon module is eligible for acceptance; edits to existing files are rejected. A successful build is required to present the candidate.

**Add to grid** writes the new Python file without overwriting an existing file and builds its family. It enters the grid as Ready, not Approved. **Discard** removes the candidate workspace and preview; a small job history and run log remain. Build failures roll back the newly added file and leave the candidate available for retry/discard. Restarted in-progress jobs are marked failed; check the library if a restart interrupted acceptance. Keep the data directory to preserve pending candidates. One job/build runs at a time within each server process; run a single deploy.py instance per repository and avoid external builds while accepting candidates.
