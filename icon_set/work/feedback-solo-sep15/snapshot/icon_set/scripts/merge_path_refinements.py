"""Validate and merge saved manual graph refinements into the path repair report."""
import argparse
from collections import Counter
import json
from pathlib import Path
import shutil

from icon_set.model.icons.registry import create
from icon_set.model.keyshapes import Keyshape
from icon_set.model.primitives import primitive_from_dict, Point
from icon_set.model.path_repair import _partition
from icon_set.validation.library_qa import inspect_icon
from icon_set.scripts.audit_keyshape_fit import write_gallery


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report',type=Path,default=Path('icon_set/work/keyshape-path-repair'))
    parser.add_argument('--refinements',type=Path,default=Path('icon_set/work/keyshape-path-repair-manual'))
    parser.add_argument('--retry',type=Path,default=Path('icon_set/work/keyshape-path-repair-visible-holes'))
    args=parser.parse_args()
    data=json.loads((args.report/'results.json').read_text())
    rows={r['source_icon_id']:r for r in data['icons']}
    retry_file=args.retry/'results.json'
    if retry_file.exists():
        retry=json.loads(retry_file.read_text())
        for updated in retry['icons']:
            name=updated['source_icon_id']
            earlier=rows[name]
            updated['earlier_repair_attempt']=earlier.get('earlier_repair_attempt',earlier['repair'])
            updated['notes'].append('Retried with visible ring openings preserved.')
            for relative in updated['previews'].values():
                shutil.copyfile(args.retry/relative,args.report/relative)
            shutil.copyfile(args.retry/'svg'/f'{name}-after.json',args.report/'svg'/f'{name}-after.json')
            earlier.clear();earlier.update(updated)
            print(name,'ring-preserving retry merged:',earlier['validation']['status'])
    for file in sorted(args.refinements.glob('*-changes.json')):
        change=json.loads(file.read_text());name=change['source_icon_id'];row=rows[name]
        graph=json.loads((args.refinements/f'{name}-after.json').read_text())
        source=create(name)
        candidate=source.fit_to_keyshape(Keyshape[row['target_keyshape']],force_stretch=True).icon
        baseline=inspect_icon(candidate)
        candidate.primitives=[primitive_from_dict(p) for p in graph['primitives']]
        candidate.anchors={name:Point(*point) for name,point in graph['anchors'].items()}
        assert candidate.to_record()==graph, f'{name}: metadata or topology changed'
        qa=inspect_icon(candidate);qa.pop('_svg',None)
        assert qa['status']=='pass',(name,qa['errors'])
        assert _partition(qa['spacing'])==_partition(baseline['spacing'])
        assert qa['negative_space']['hole_count']==baseline['negative_space']['hole_count']
        assert candidate.to_svg()==(args.refinements/f'{name}-after.svg').read_text()
        candidate.export_icon_to(args.report/row['previews']['after'])
        candidate.export_json_graph(args.report/'svg'/f'{name}-after.json')
        row['validation']=qa
        row['manual_refinement']=change
        row['notes']=[f"Manual refinement: {s['path']}: {s['operation']}" for s in change['changes']]
        row['repair']['remaining_status']='pass'
        print(name,'manual refinement validated and merged')
    notes_path=args.refinements/'visual-notes.json'
    if notes_path.exists():
        for name,note in json.loads(notes_path.read_text()).items():
            rows[name]['visual_review_note']=note
            if note not in rows[name]['notes']:rows[name]['notes'].append(note)
    counts=Counter(r['validation']['status'] for r in rows.values())
    summary=data['summary']
    summary['statuses']={s:counts[s] for s in ('pass','fail','review','error')}
    summary['repaired_to_pass']=sum(r['previous_status']=='fail' and r['validation']['status']=='pass' for r in rows.values())
    summary['manual_refinements']=sum('manual_refinement' in r for r in rows.values())
    summary['evaluations']=sum(r['repair']['evaluations']+r.get('earlier_repair_attempt',{}).get('evaluations',0) for r in rows.values())
    summary['numeric_pass_with_internal_spacing_advisory']=sum(r['validation']['status']=='pass' and bool(r['validation'].get('needs_review')) for r in rows.values())
    failures=Counter()
    for row in rows.values():failures.update({e.split(':',1)[0].split(' [',1)[0] for e in row['validation']['errors']})
    summary['icons_by_failure_check']=dict(failures)
    (args.report/'results.json').write_text(json.dumps(data,indent=2)+'\n')
    write_gallery(args.report,summary,data['icons'])
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
