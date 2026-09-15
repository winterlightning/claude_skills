#!/usr/bin/env python3
"""Whole-library report for the integrated parallel-line validation engine.

Run: python3 icon_set/scripts/audit_parallel_midpoints.py --out work/parallel-midpoint-audit
Exact straight geometry only; curves, near-parallel lines and dots are excluded.
The proposed 8 centerline / 4 ink threshold applies to every audited family,
with each family's current threshold reported separately. The report shares the analyzer used by the blocking validation check.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from collections import Counter, defaultdict
import hashlib
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from icon_set.model.primitives import Line
from icon_set.model.profiles import STROKE_WIDTH

EPS = 1e-9  # Local floating calculation guard, not a design allowance.


from icon_set.validation.parallel_midpoints import analyze


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'work/parallel-midpoint-audit')
    parser.add_argument('--family',choices=['solo','sub','container'],action='append')
    args=parser.parse_args(argv)
    from icon_set.model.icons.registry import factories
    rows=[]; errors=[]; started=datetime.now(timezone.utc).isoformat()
    # Use canonical registry. Discovery errors stop the audit rather than silently
    # skipping unregistered or duplicate models.
    for name,factory in factories().items():
        if args.family and factory.family not in args.family: continue
        try:
            icon=factory(); result=analyze(icon.draw()); preview_error=None
            try:
                svg=icon.to_svg()
            except Exception as error:
                preview_error=f'{type(error).__name__}: {error}'
                errors.append(dict(icon_id=name,family=icon.family,stage='preview',error=preview_error))
                canvas=icon.profile.spec.canvas_size
                lines=''.join(f'<line x1="{r["start"][0]}" y1="{r["start"][1]}" x2="{r["end"][0]}" y2="{r["end"][1]}"/>' for r in result['runs'])
                svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {canvas} {canvas}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round">{lines}</svg>'
            module=sys.modules[factory.__module__]
            source=Path(module.__file__)
            rows.append(dict(icon_id=name,family=icon.family,profile=icon.profile.name,
                             preview_error=preview_error,canvas=icon.profile.spec.canvas_size,current_required_centerline=icon.profile.spec.equal_stroke_centerline_min,
                             source=str(source.relative_to(ROOT)),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                             svg_sha256=hashlib.sha256(svg.encode()).hexdigest(),svg=svg,**result))
        except Exception as error:
            errors.append(dict(icon_id=name,family=factory.family,error=f'{type(error).__name__}: {error}'))
    summary=dict(icons_audited=len(rows),preview_errors=sum(bool(r['preview_error']) for r in rows),errors=len(errors),families=dict(Counter(r['family'] for r in rows)),
                 icons_with_measured_pairs=sum(bool(r['hits']) for r in rows),
                 icons_below_minimum=sum(bool(r['below_minimum_pair_count']) for r in rows),
                 measured_pairs=sum(r['measured_pair_count'] for r in rows),
                 below_minimum_pairs=sum(r['below_minimum_pair_count'] for r in rows),
                 blind_spot_pairs=sum(sum(p['reason']=='both-midpoints-miss' for p in r['unmeasured_overlaps']) for r in rows),
                 below_minimum_blind_spot_pairs=sum(sum(p['reason']=='both-midpoints-miss' and p['below_minimum'] for p in r['unmeasured_overlaps']) for r in rows),
                 collinear_overlap_pairs=sum(len(r['collinear_overlaps']) for r in rows))
    report=dict(mode='integrated-parallel-diagnostic',started_at=started,completed_at=datetime.now(timezone.utc).isoformat(),rules={'centerline_minimum':8,'ink_minimum':4,'stroke':4,'parallelism':'exact',
                'measurement':'nearest finite parallel line from each run midpoint in both normal directions',
                'merge':'touching collinear pieces in the same path','relations':'annotated, not exempted',
                'curves':'excluded','near_parallel':'excluded','other_geometry_occlusion':'not applied; rays seek parallel lines only'},
                summary=summary,errors=errors,icons=rows)
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/'results.json').write_text(json.dumps(report,indent=2)+'\n')
    template=Path(__file__).with_name('templates')/'parallel_midpoint_audit.html'
    data=json.dumps(report).replace('<','\\u003c').replace('&','\\u0026')
    (args.out/'index.html').write_text(template.read_text().replace('__AUDIT_DATA__',data))
    print(json.dumps(summary,indent=2)); print(args.out/'index.html')
    return 1 if errors else 0


if __name__=='__main__': raise SystemExit(main())
