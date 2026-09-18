#!/usr/bin/env python3
"""Repeatable container/solo previews with ink-edge padding validation."""
from pathlib import Path
import argparse
import html
import json
import re
import sys

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from icon_set.scripts.container_placement import Artwork, place


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', help='Container icon ID')
    parser.add_argument('--sub', help='Solo icon ID')
    parser.add_argument('--batch', type=Path, help='Existing container-solo-trials.json pairing manifest')
    parser.add_argument('--areas', type=Path, default=ROOT/'icon_set/data/container-content-areas.json', help='JSON with areas keyed by container icon ID')
    parser.add_argument('--padding', type=float, default=2)
    parser.add_argument('--sizes', type=float, nargs='+', default=[32, 28, 24])
    parser.add_argument('--max-shift', type=float, default=10)
    parser.add_argument('--limit', type=int)
    parser.add_argument('--out', type=Path, default=ROOT/'icon_set/work/container-placement')
    args = parser.parse_args()
    if bool(args.batch) == bool(args.host or args.sub) or (not args.batch and not (args.host and args.sub)):
        parser.error('Choose --host ID --sub ID, or --batch MANIFEST.')
    if args.limit is not None and args.limit < 1:
        parser.error('--limit must be positive.')
    pairs = list(json.loads(args.batch.read_text())['results'].values()) if args.batch else [
        {'main_key': f'container/{args.host}', 'sub_key': f'solo/{args.sub}'}]
    areas = json.loads(args.areas.read_text())['areas'] if args.areas else {}
    args.out.mkdir(parents=True, exist_ok=True)
    results, cards, cache = [], [], {}
    for pair in pairs[:args.limit]:
        main_key, sub_key = pair['main_key'], pair['sub_key']
        if not re.fullmatch(r'container/[a-zA-Z0-9_-]+', main_key) or not re.fullmatch(r'solo/[a-zA-Z0-9_-]+', sub_key):
            raise ValueError('Expected container/ID and solo/ID keys.')
        host_id, sub_id = main_key.split('/')[1], sub_key.split('/')[1]
        filename = f'{host_id}--{sub_id}'
        metadata = {k: pair[k] for k in ('pair_id', 'concept', 'main_source_id', 'sub_source_id') if k in pair}
        if filename not in cache:
            try:
                host_path = development_dist(ROOT) / f'container64/{host_id}.svg'
                sub_path = development_dist(ROOT) / f'solo48/{sub_id}.svg'
                host = Artwork.read(host_path.read_text(), 64)
                sub = Artwork.read(sub_path.read_text(), 48)
                result = place(host, sub, padding=args.padding, sizes=args.sizes,
                               max_shift=args.max_shift, area=areas.get(host_id))
                (args.out/f'{filename}.svg').write_text(result.pop('svg'))
                (args.out/f'{filename}-buffer.svg').write_text(result.pop('debug_svg'))
                result.update(main_key=main_key, sub_key=sub_key, main_sha256=host.sha256,
                              sub_sha256=sub.sha256, main_path=str(host_path), sub_path=str(sub_path),
                              svg_file=f'{filename}.svg', buffer_file=f'{filename}-buffer.svg', native_sub32=False)
                cards.append(f'<article><h2>{html.escape(host_id)} + {html.escape(sub_id)}</h2>'
                    f'<img src="{filename}.svg"><img src="{filename}-buffer.svg">'
                    f'<p>{result["status"]} · minimum gap {args.padding:g} units</p></article>')
            except (ValueError, OSError) as error:
                result = {'main_key': main_key, 'sub_key': sub_key, 'status': 'blocked', 'error': str(error)}
                cards.append(f'<article><h2>{html.escape(filename)}</h2><p>{html.escape(str(error))}</p></article>')
            cache[filename] = result
        results.append({**cache[filename], **metadata})
    (args.out/'results.json').write_text(json.dumps({'version': 1, 'padding': args.padding, 'results': results}, indent=2)+'\n')
    (args.out/'index.html').write_text('<!doctype html><meta charset="utf-8"><title>Container placement</title>'
        '<style>body{font:15px system-ui;margin:32px;background:#fafafa}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px}article{background:white;padding:20px;border:1px solid #ddd}h2{font-size:14px}img{width:128px;height:128px;margin:8px}</style>'
        '<h1>Container placement</h1><p>Left: combination. Right: orange padding buffer and green saved content area. '
        'Review-area means the detected area still needs visual review. These are composition trials.</p><main>'+''.join(cards)+'</main>')
    print(json.dumps({'pairs': len(results), 'unique_pairs': len(cache), 'preview': str(args.out/'index.html'),
                      'statuses': {s: sum(r['status']==s for r in results) for s in sorted({r['status'] for r in results})}}, indent=2))

if __name__ == '__main__':
    main()
