"""One entry point for local authoring and explicit production releases."""
import argparse
import importlib
import sys


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    commands = {
        'build': 'build',
        'finish-icon': 'finish_icon',
        'dev': 'deploy',
        'release': 'release',
        'publish': 'publish',
        'production': 'deploy',
        'doctor': 'workspace_doctor',
        'typeface-sizes': 'typeface_sizes',
        'combinations': 'combination_library',
    }
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=commands)
    if not argv or argv[0] in ('-h', '--help'):
        parser.print_help()
        return 0
    args = parser.parse_args(argv[:1])
    rest = argv[1:]
    if args.command == 'production':
        rest.insert(0, '--production')
        if not any(arg == '--dist' or arg.startswith('--dist=') for arg in rest):
            from .scripts.workspace import PUBLISHED_DIST
            rest.extend(['--dist', str(PUBLISHED_DIST)])
    elif args.command == 'dev' and '--production' in rest:
        parser.error('Use the production command for production state.')
    module = importlib.import_module('icon_set.scripts.' + commands[args.command])
    return module.main(rest)


if __name__ == '__main__':
    raise SystemExit(main())
