#!/usr/bin/env python3
"""Validate the current Python icon library without publishing a release.

    python3 icon_set/scripts/validate_library.py --debug
    python3 icon_set/scripts/validate_library.py --no-report
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
from tempfile import TemporaryDirectory

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model.icons.registry import all_icons
from icon_set.validation.library_qa import artifact_key, inspect_icon, save_evidence
from icon_set.scripts.build import _publish, DEFAULT_DIST


def validate_library(output: Path = DEFAULT_DIST / 'qa', *, debug=False, report=True) -> int:
    rows = []
    if debug or report:
        output = output.resolve()
        if output.exists() and any(output.iterdir()) and not (output / 'results.json').is_file():
            raise ValueError('output must be empty or an existing QA snapshot containing results.json')
        output.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(prefix='.library-qa-', dir=output.parent) as temporary:
            staging = Path(temporary) / 'snapshot'
            staging.mkdir()
            for icon in all_icons():
                key = artifact_key(icon)
                row = inspect_icon(icon, debug_dir=staging / key if debug else None)
                row['_key'] = key
                rows.append(row)
            save_evidence(rows, staging, debug=debug, report=report)
            _publish([(staging, output)])
        print(f"QA evidence -> {output / ('index.html' if report else 'results.json')}")
    else:
        rows = [inspect_icon(icon) for icon in all_icons()]
    failures = [row for row in rows if row['status'] != 'pass']
    print(f'{len(rows)} icons checked; {len(failures)} failed, unresolved or errored')
    for row in failures:
        print(f"  {row['family']}/{row['icon_id']}: {row['status']}")
        for message in row['errors'] + row['warnings']:
            print(f'    {message}')
    return 1 if failures else 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--output', type=Path, default=DEFAULT_DIST / 'qa')
    parser.add_argument('--debug', action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument('--report', action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args(argv)
    try:
        return validate_library(args.output, debug=args.debug, report=args.report)
    except (OSError, ValueError) as error:
        print(f'QA failed: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
