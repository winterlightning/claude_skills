"""Read-only diagnosis of the workspace: one tracked build root, no tracked runtime state."""
import argparse
import json
import subprocess
from .workspace import REPO_ROOT, DEFAULT_DIST, DEFAULT_PNG, DEFAULT_DATABASE, STATE_ROOT

# Never committed: runtime state, regenerated QA evidence, retired output folders.
RUNTIME_PATHS = ['icon_set/state', 'published/qa', 'published/build-progress.json',
                 'icon_set/dist', 'icon_set/assets/previews-png', 'icon_set/.local',
                 'icon_set/scripts/.codex-batch-runner', 'icon_set/progression.sqlite3',
                 ':(glob)icon_set/work/**/*.log', ':(glob)icon_set/work/**/*.pid',
                 ':(glob)icon_set/work/**/*.sqlite3', ':(glob)**/*.sqlite3', ':(glob)**/generator-key.txt']
# Always committed: the build root, datasets, experiments and reference assets.
TRACKED_PATHS = ['published', 'icon_set/data', 'icon_set/work', 'icon_set/assets']


def _git(*args):
    return [p for p in subprocess.run(['git', *args], cwd=REPO_ROOT, check=True,
                                      capture_output=True).stdout.decode().split('\0') if p]


def inspect_workspace():
    tracked_runtime = _git('ls-files', '-z', '--', *RUNTIME_PATHS)
    uncommitted = _git('ls-files', '-z', '--others', '--exclude-standard', '--', *TRACKED_PATHS)
    catalog = DEFAULT_DIST / 'gallery/icons.json'
    data = json.loads(catalog.read_text()) if catalog.exists() else {}
    return {
        'build_output': str(DEFAULT_DIST), 'previews': str(DEFAULT_PNG),
        'runtime_state': str(STATE_ROOT), 'database': str(DEFAULT_DATABASE),
        'tracked_runtime_files': len(tracked_runtime),
        'untracked_output_files': len(uncommitted),
        'catalog_available': catalog.exists(),
        'release_marker': (DEFAULT_DIST / 'release.json').exists(),
        'built_icons': len(data.get('icons', [])), 'failed_icons': len(data.get('failed_icons', [])),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args(argv)
    result = inspect_workspace()
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        for key, value in result.items():
            print(f'{key.replace("_", " ")}: {value}')
        if result['tracked_runtime_files']:
            print('Runtime state or regenerated output is tracked; move it to icon_set/state/ or remove it from Git.')
        if result['untracked_output_files']:
            print('Build output or datasets are not committed yet: git add published icon_set/data icon_set/work icon_set/assets')
        if not result['catalog_available']:
            print('Run python3 -m icon_set build to create the catalog.')
    return int(bool(result['tracked_runtime_files']))
