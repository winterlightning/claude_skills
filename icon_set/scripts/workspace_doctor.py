"""Read-only diagnosis of development storage and generated-file tracking."""
import argparse
import json
import subprocess
from .workspace import REPO_ROOT, DEFAULT_DIST, DEFAULT_PNG, DEFAULT_DATABASE, PUBLISHED_DIST


def inspect_workspace():
    tracked = subprocess.run(
        ['git', 'ls-files', '-z', '--', 'icon_set/dist', 'icon_set/assets/previews-png', 'icon_set/.local',
         'icon_set/scripts/.codex-batch-runner', 'icon_set/progression.sqlite3',
         ':(glob)icon_set/work/**/*.log', ':(glob)icon_set/work/**/*.pid',
         ':(glob)icon_set/work/**/*.sqlite3'],
        cwd=REPO_ROOT, check=True, capture_output=True).stdout.split(b'\0')
    catalog = DEFAULT_DIST / 'gallery/icons.json'
    data = json.loads(catalog.read_text()) if catalog.exists() else {}
    return {
        'development_assets': str(DEFAULT_DIST), 'development_previews': str(DEFAULT_PNG),
        'development_database': str(DEFAULT_DATABASE),
        'published_assets': str(PUBLISHED_DIST),
        'tracked_generated_files': sum(bool(path) for path in tracked),
        'catalog_available': catalog.exists(),
        'built_icons': len(data.get('icons', [])), 'failed_icons': len(data.get('failed_icons', [])),
        'legacy_assets_preserved': (REPO_ROOT / 'icon_set/dist').exists(),
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
        if result['tracked_generated_files']:
            print('Generated files are still tracked; complete the repository migration.')
        if not result['catalog_available']:
            print('Run python3 -m icon_set build to create the development catalog.')
    return int(bool(result['tracked_generated_files']))
