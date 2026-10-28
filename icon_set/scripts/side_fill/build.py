"""Build every fill side-pair variant into icon_set/state/side-fill (ignored build output).

    python3 -m icon_set side-fill build                 # reviews, recombine, duplicates, layouts
    python3 -m icon_set side-fill build --steps recombine,layouts --ids ID …

Steps, in order (each reads what the earlier ones wrote):
  reviews     sub32 and main48 region-fill reviews and their stroke-fill rework (the combine reads the
              rework manifests to keep reverse fills flat)
  mains       each main's variants on their own (48px), for the main icon page
  baseline    each pair at its saved placement with the current fills (combine_fill_side_layouts),
              the reference the gallery rows and graph checks come from
  recombine   every side pair with every visible main variant (adaptive_overlap), in parallel chunks
  duplicates  hide region / group variants that draw the same picture as current
  layouts     render the pairs' remaining layout records (pair_layout_review), in parallel chunks
  gallery     the combined review rows (build_gallery: gallery-data.js) the icon export and D1 import read
Nothing under icon_set/data/side-fill is written.
"""
import argparse
import json
import shutil
import tempfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from .paths import DATA, WORK

STEPS = ('reviews', 'mains', 'baseline', 'recombine', 'duplicates', 'layouts', 'gallery')
RECOMBINED = WORK / 'recombined-all'
LAYOUT_OUT = WORK / 'ai-layout-proposals'


def pair_ids():
    return [item['reference_id'] for item in json.loads((DATA / 'data/production-layouts.json').read_text())['items']]


def chunks(ids, size):
    return [ids[i:i + size] for i in range(0, len(ids), size)]


def reviews(workers):
    from .build_main48_region_fill_review import build as build_main48
    from .build_sub32_region_fill_review import DEFAULT_DECISIONS, DEFAULT_OUTPUT, DEFAULT_SOURCE, build as build_sub32
    from .stroke_fill_rework import rework_review
    build_sub32(DEFAULT_SOURCE, DEFAULT_OUTPUT, workers, decisions_path=DEFAULT_DECISIONS)
    rework_review(DEFAULT_OUTPUT.resolve())
    build_main48(workers)
    rework_review((WORK / 'main48-region-fill-review').resolve())


def _recombine_chunk(args):
    ids, out = args
    from .adaptive_overlap import main as recombine
    recombine(['--out', out, '--summary-only', '--ids', *ids])
    return out


def recombine(ids, workers):
    """Chunks recombine into their own folders; rows and SVGs merge into recombined-all."""
    whole = ids is None
    ids = ids or pair_ids()
    with tempfile.TemporaryDirectory(prefix='side-fill-recombine-') as tmp:
        jobs = [(chunk, str(Path(tmp) / f'chunk-{n}')) for n, chunk in enumerate(chunks(ids, max(1, -(-len(ids) // (workers * 4)))))]
        with ProcessPoolExecutor(workers) as pool:
            outs = list(pool.map(_recombine_chunk, jobs))
        fresh, errors = {}, []
        (RECOMBINED / 'variants').mkdir(parents=True, exist_ok=True)
        for out in map(Path, outs):
            report = json.loads((out / 'report.json').read_text())
            errors += report.get('errors', [])
            for row in report['rows']:
                fresh[row['id']] = row
                for candidate in row['candidates']:
                    shutil.copy2(out / candidate['svg'], RECOMBINED / candidate['svg'])
    path = RECOMBINED / 'report.json'
    old = json.loads(path.read_text()) if path.exists() and not whole else {'rows': [], 'errors': []}
    rows = [fresh.pop(row['id'], row) for row in old['rows']] + list(fresh.values())
    keep = set(ids)
    old_errors = [e for e in old.get('errors', []) if e.get('id') not in keep]
    path.write_text(json.dumps({'rows': rows, 'errors': old_errors + errors}, indent=2) + '\n')
    print(f'recombined {len(ids)} pairs: {len(errors)} errors')


def duplicates():
    from .mark_duplicate_variants import mark, move_decisions
    report, marked = mark(RECOMBINED / 'report.json')
    print(f'duplicates hidden: {sum(len(v) for v in marked.values())} in {len(marked)} pairs')


def _layout_chunk(args):
    ids, out = args
    from .pair_layout_review import render_one
    failed = {}
    for pair_id in ids:
        try:
            render_one(pair_id, out=Path(out))
        except Exception as error:    # one pair must not stop the batch
            failed[pair_id] = str(error)[:200]
    return out, failed


def layouts(ids, workers):
    from .pair_layout_review import DEFAULT_SPECS
    specs = json.loads(DEFAULT_SPECS.read_text())['pairs']
    whole = ids is None
    ids = [i for i in (ids or specs) if specs.get(i)]
    with tempfile.TemporaryDirectory(prefix='side-fill-layouts-') as tmp:
        jobs = [(chunk, str(Path(tmp) / f'chunk-{n}')) for n, chunk in enumerate(chunks(ids, max(1, -(-len(ids) // (workers * 4)))))]
        with ProcessPoolExecutor(workers) as pool:
            results = list(pool.map(_layout_chunk, jobs))
        path = LAYOUT_OUT / 'report.json'
        report = json.loads(path.read_text()) if path.exists() and not whole else {'schema': 'side-ai-layout-renderings/v1', 'pairs': {}}
        failed = {}
        for out, chunk_failed in results:
            failed.update(chunk_failed)
            out = Path(out)
            if not (out / 'report.json').exists():
                continue
            part = json.loads((out / 'report.json').read_text())
            report['pairs'].update(part['pairs'])
            for folder in ('svg', 'stress'):
                if (out / folder).is_dir():
                    shutil.copytree(out / folder, LAYOUT_OUT / folder, dirs_exist_ok=True)
        LAYOUT_OUT.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2) + '\n')
    print(f'layouts rendered for {len(ids) - len(failed)} pairs; failed {len(failed)}')
    if failed:
        (LAYOUT_OUT / 'failed.json').write_text(json.dumps(failed, indent=1) + '\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--steps', default=','.join(STEPS), help=f'comma list of {", ".join(STEPS)}')
    parser.add_argument('--ids', nargs='*', help='only these pairs (recombine and layouts)')
    parser.add_argument('--workers', type=int, default=8)
    args = parser.parse_args(argv)
    steps = [s for s in args.steps.split(',') if s]
    unknown = set(steps) - set(STEPS)
    if unknown:
        parser.error(f'unknown steps: {sorted(unknown)}')
    WORK.mkdir(parents=True, exist_ok=True)
    if 'reviews' in steps:
        reviews(args.workers)
    if 'mains' in steps:
        from .build_main_variant_previews import main as build_mains
        build_mains(['--workers', str(args.workers)])
    if 'baseline' in steps:
        from .combine_fill_side_layouts import main as baseline
        baseline(['build'])
    if 'recombine' in steps:
        recombine(args.ids, args.workers)
    if 'duplicates' in steps:
        duplicates()
    if 'layouts' in steps:
        layouts(args.ids, args.workers)
    if 'gallery' in steps:
        from .build_gallery import build as gallery
        print(json.dumps(gallery(), indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
