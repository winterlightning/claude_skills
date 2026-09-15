#!/usr/bin/env python3
"""Run core validation for every registered icon and isolate parallel failures."""
import argparse
from dataclasses import asdict
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import factories
from icon_set.validation.parallel_straight import check_parallel_straight, RULES


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'work/parallel-pipeline-results')
    args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
    rows=[];errors=[];started=datetime.now(timezone.utc).isoformat()
    for name,factory in factories().items():
        try:
            icon=factory();findings=check_parallel_straight(icon,icon.draw())
            row=dict(icon_id=name,family=icon.family,parallel_findings=[asdict(f) for f in findings])
            try:
                report=icon.validate_icon()
                row.update(core_status=report.status,core_errors=list(report.errors))
                if findings and report.status!='invalid':
                    raise AssertionError('parallel findings not blocking validation')
            except Exception as error:
                row.update(core_status='error',core_errors=[str(error)])
                errors.append(dict(icon_id=name,error=str(error)))
            rows.append(row)
        except Exception as error:
            errors.append(dict(icon_id=name,error=str(error)))
    failed=[r for r in rows if r['parallel_findings']]
    summary=dict(icons_scanned=len(rows),parallel_failing_icons=len(failed),
                 failing_pairs=sum(len(r['parallel_findings']) for r in failed),
                 errors=len(errors),by_family={f:sum(r['family']==f for r in failed) for f in ('solo','sub','container')})
    data=dict(started_at=started,completed_at=datetime.now(timezone.utc).isoformat(),rules=RULES,summary=summary,errors=errors,icons=rows)
    (args.out/'results.json').write_text(json.dumps(data,indent=2)+'\n')
    lines=['# Icons failing the integrated parallel-spacing check','',
           f"Scanned {len(rows)} models; **{len(failed)} icons fail**, with {summary['failing_pairs']} failing pairs.",
           '', 'Minimum: **8 centerline units / 4 ink units**. Exact parallel straight lines across all families; midpoint rays plus positive-overlap fallback. Connections do not exempt narrow facing edges. Other validation errors are separate.',
           '', '| Icon | Family | Smallest centerline gap | Ink gap | Failing pairs |',
           '|---|---|---:|---:|---:|']
    for row in failed:
        gaps=[f['detail']['centerline_distance'] for f in row['parallel_findings'] if 'centerline_distance' in f['detail']]
        gap=min(gaps) if gaps else float('nan')
        lines.append(f"| {row['icon_id']} | {row['family']} | {gap:.3f} | {gap-4:.3f} | {len(row['parallel_findings'])} |")
    lines+=['','## Validation errors','']+[f"- {r['icon_id']}: {r['error']}" for r in errors]
    (args.out/'failing-icons.md').write_text('\n'.join(lines)+'\n')
    (args.out/'failing-icon-ids.txt').write_text(''.join(r['icon_id']+'\n' for r in failed))
    print(json.dumps(summary,indent=2),flush=True)
    return int(bool(errors))

if __name__=='__main__':raise SystemExit(main())
