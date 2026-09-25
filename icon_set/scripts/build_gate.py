"""Run the build's full QA gate on a standalone work-folder module.

``validate_icon()`` alone misses the build's hole/pinch, internal-spacing and
symmetry gates, so a run can report ``valid`` and still land in the Failing
bucket after promotion. This runs ``inspect_icon`` exactly as the build does.

    python3 icon_set/scripts/build_gate.py RESULT_DIR/<module>.py [--debug RESULT_DIR/gate]

Prints PASS or FAIL with every error and warning; exits 0 only on a pass with
no warnings. ``--debug`` writes the hole, spacing and internal-spacing overlays.
"""
from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def gate(module_path: Path, debug_dir: Path | None = None) -> dict:
    from icon_set.validation.library_qa import inspect_icon
    spec = importlib.util.spec_from_file_location(f'_gate_{module_path.stem}', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    classes = [v for v in vars(module).values()
               if isinstance(v, type) and v.__module__ == module.__name__ and getattr(v, 'icon_id', None)]
    if len(classes) != 1:
        return {'status': 'error', 'errors': [f'expected one icon class in {module_path}, found {len(classes)}'], 'warnings': []}
    qa = inspect_icon(classes[0](), debug_dir=debug_dir)
    result = {'icon_id': qa['icon_id'], 'status': qa['status'], 'errors': qa['errors'], 'warnings': qa['warnings']}
    # Keep the approval and automatic verdict together; findings are never erased.
    for key in ('exception', 'automatic_status'):
        if key in qa:
            result[key] = qa[key]
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('module', type=Path)
    parser.add_argument('--debug', type=Path, help='directory for hole/spacing overlay PNGs')
    args = parser.parse_args(argv)
    result = gate(args.module, args.debug)
    ok = result['status'] == 'pass' and not result['warnings']
    print(f"BUILD GATE {'PASS' if ok else 'FAIL'} ({result['status']}, {len(result['errors'])} errors, "
          f"{len(result['warnings'])} warnings)")
    for line in result['errors']:
        print('  error:', line)
    for line in result['warnings']:
        print('  warning:', line)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
