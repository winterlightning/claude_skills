"""Repair each failed stretched draft locally, preserving the previous audit.

python3 -m icon_set.scripts.repair_keyshape_paths
"""
import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

from icon_set.model.icons.registry import create
from icon_set.model.keyshapes import Keyshape
from icon_set.model.path_repair import repair_paths
from icon_set.scripts.audit_keyshape_fit import write_gallery


def repair_one(row, source, budget):
    row = dict(row)
    previous = row['validation']['status']
    row['previous_status'] = previous
    before = (Path(source) / row['previews']['after']).read_text()
    row['_before_svg'] = before
    if previous != 'fail':
        row['_after_svg'] = before
        row['repair'] = {'evaluations':0,'changes':[], 'reason':'Not a failed candidate'}
        return row
    icon = create(row['source_icon_id'])
    stretched = icon.fit_to_keyshape(Keyshape[row['target_keyshape']],force_stretch=True).icon
    if hashlib.sha256(stretched.to_svg().encode()).hexdigest() != row['validation']['svg_sha256']:
        raise ValueError(f"{icon.icon_id}: source changed since the stretch audit; rerun it first")
    candidate, qa, log = repair_paths(stretched,max_evaluations=budget)
    # Separate work artifacts retain deterministic identity; no source registry writes.
    row['validation'] = qa
    row['repair'] = log
    row['_after_svg'] = candidate.to_svg()
    row['_graph'] = candidate.to_record()
    row['notes'] = [f"{step['path']}: {step['operation']}" for step in log['changes']]
    row['notes'].append(f"Path repair: {log['evaluations']} candidates checked; visual review required.")
    return row


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,default=Path('icon_set/work/keyshape-stretch-audit'))
    p.add_argument('--output',type=Path,default=Path('icon_set/work/keyshape-path-repair'))
    p.add_argument('--workers',type=int,default=3)
    p.add_argument('--budget',type=int,default=600)
    p.add_argument('--icons',nargs='+')
    p.add_argument('--resume',action='store_true',help='Continue from completed progress records')
    a=p.parse_args(argv)
    if a.workers<1 or a.budget<0:p.error('workers must be positive and budget nonnegative')
    source=json.loads((a.source/'results.json').read_text())
    inputs=[r for r in source['icons'] if not a.icons or r['source_icon_id'] in a.icons]
    if a.icons and {r['source_icon_id'] for r in inputs}!=set(a.icons):p.error('unknown icon ID')
    a.output.mkdir(parents=True,exist_ok=True)
    progress_path=a.output/'progress.jsonl'
    rows=[]
    if a.resume and progress_path.exists():
        rows=[json.loads(line) for line in progress_path.read_text().splitlines() if line]
        if len({r['source_icon_id'] for r in rows})!=len(rows):
            p.error('duplicate progress records')
        if not {r['source_icon_id'] for r in rows}<={r['source_icon_id'] for r in inputs}:
            p.error('progress records are outside the selected input set')
    completed={r['source_icon_id'] for r in rows}
    print(f"Checking {len(inputs)} icons; repairing {sum(r['validation']['status']=='fail' for r in inputs)} failures",flush=True)
    with progress_path.open('a' if a.resume else 'w') as progress, ProcessPoolExecutor(max_workers=a.workers) as pool:
        futures={pool.submit(repair_one,row,str(a.source),a.budget):row['source_icon_id'] for row in inputs if row['source_icon_id'] not in completed}
        for future in as_completed(futures):
            row=future.result()
            icon_id=row['source_icon_id']
            folder=a.output/'svg';folder.mkdir(exist_ok=True)
            row['previews']={}
            for name in ('before','after'):
                rel=f'svg/{icon_id}-{name}.svg'
                (a.output/rel).write_text(row.pop(f'_{name}_svg'),encoding='utf-8')
                row['previews'][name]=rel
            graph=row.pop('_graph',None)
            if graph is not None:
                (folder/f'{icon_id}-after.json').write_text(json.dumps(graph,indent=2)+'\n')
            rows.append(row);progress.write(json.dumps(row)+'\n');progress.flush()
            if len(rows)%10==0 or row['repair']['changes'] or len(rows)==len(inputs):
                counts=Counter(r['validation']['status'] for r in rows)
                fixed=sum(r['previous_status']=='fail' and r['validation']['status']=='pass' for r in rows)
                print(f"{len(rows)}/{len(inputs)}; repaired {fixed}; {dict(counts)}; last {icon_id}: {row['validation']['status']}",flush=True)
    rows.sort(key=lambda r:r['source_icon_id'])
    counts=Counter(r['validation']['status'] for r in rows)
    failures=Counter()
    for row in rows:failures.update({e.split(':',1)[0].split(' [',1)[0] for e in row['validation']['errors']})
    summary={'completed_at':datetime.now(timezone.utc).isoformat(),'mode':'path repair',
             'scope':'Each failed force-stretched solo candidate: bounded path resizing/movement, then full validation.',
             'total':len(rows),'statuses':{k:counts[k] for k in ('pass','fail','review','error')},
             'repaired_to_pass':sum(r['previous_status']=='fail' and r['validation']['status']=='pass' for r in rows),
             'attempted_failed_icons':sum(r['previous_status']=='fail' for r in rows),
             'evaluations':sum(r['repair']['evaluations'] for r in rows),
             'icons_by_failure_check':dict(failures),
             'numeric_pass_with_internal_spacing_advisory':sum(r['validation']['status']=='pass' and bool(r['validation'].get('needs_review')) for r in rows),
             'before_label':'Stretched candidate','after_label':'After path repair',
             'note':'Local search is not proof that unresolved icons are impossible to repair. All results need visual review; originals and rules are preserved.'}
    (a.output/'results.json').write_text(json.dumps({'summary':summary,'icons':rows},indent=2)+'\n')
    write_gallery(a.output,summary,rows)
    print(json.dumps(summary,indent=2),flush=True)


if __name__=='__main__':main()
