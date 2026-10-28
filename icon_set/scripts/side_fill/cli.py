"""Fill side pairs: `python3 -m icon_set side-fill <command> …`.

  import    one-off copy of the fill-remake work into icon_set/data/side-fill (report unless --write)
  build     render every variant into icon_set/state/side-fill (reviews, mains, baseline, recombine,
            duplicates, layouts, gallery)
  icons     export the fill variant icons (SVGs + manifest) for cloud/migrate/upload_fill_parts.py
  d1-import write the SQL that fills fill_pairs / fill_parts / fill_counts and the picks (wrangler d1 execute)
  check     combine every pick from the icon files and compare it with the combined SVG reviewed in the gallery
  goldens   write the fixtures side-fill.test.mjs checks side-fill-combine.js against
"""
import importlib
import sys

COMMANDS = {
    'import': 'import_fill_remake',
    'build': 'build',
    'icons': 'fill_icons',
    'd1-import': 'd1_import',
    'check': 'pick_combine',
    'goldens': 'pick_combine',
}
# Commands of a module with several: it reads the command name itself.
NAMED = {'check', 'goldens'}


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ('-h', '--help') or argv[0] not in COMMANDS:
        print(__doc__)
        return 0 if argv and argv[0] in ('-h', '--help') else 2
    module = importlib.import_module(f'{__package__}.{COMMANDS[argv[0]]}')
    return module.main(argv if argv[0] in NAMED else argv[1:])
