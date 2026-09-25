"""Finalize reviewed standalone drawings, then finish each production claim."""
import sys,json,hashlib,subprocess,ast
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
from icon_set.scripts import work_queue
HERE=Path(__file__).parent
rows=json.loads((HERE/'batch.json').read_text())
reasons={
2:'Retain the overlapping corn husks and tall cob. Local three-unit visible gaps at the leaf attachments remain clear at native 48px in both themes; no stroke or canvas change.',
6:'Retain outlined scissor blades and circular finger loops. The intentional front-over-back arrangement leaves a small but visible gap near the right loop; blade faces and eight-unit loop openings remain clear at 48px.',
7:'Retain the chess-piece collar, stem, finial and rounded foot. Two-unit slots in the collar and base remain open in both themes and preserve the source tiered silhouette.',
9:'Retain both rounded pedestal tiers beneath the orb. The stand has visible three-unit and two-unit interior bands at 48px; merging the tiers would lose the source pedestal.',
11:'Retain all three hollow nodes and the three-faced cube. Local narrow face and connector openings remain visibly distinct at 48px; the source arrangement is more informative than filled nodes.',
12:'Retain the uneven rounded icing drips. The two-unit internal drip opening is readable at 48px in both themes and preserves the source frosting pattern.',
14:'Retain the plough’s curved beam as an outlined component. Its two-unit opening remains clear at native size; the sloped handle and curved share preserve the agricultural-tool reading.',
19:'Retain the drum’s elliptical head, upper rim band and downward lacing triangle. Local roughly two-unit rim openings remain clear in both themes; the narrow lower rim was omitted for clarity.',
}
changed_path=HERE/'changed-production.json'
changed={r['icon']:r for r in json.loads(changed_path.read_text())} if changed_path.exists() else {}
base=work_queue.default_base_url()
for i,row in enumerate(rows):
    module=Path(row['module']);run=Path(row['run']);icon=load_icon(module)
    report=icon.validate_icon();automatic=gate(module)
    (run/'automatic-gate.json').write_text(json.dumps(automatic,indent=2)+'\n')
    exception=None
    if automatic['status']!='pass':
        assert i in reasons,(i,automatic)
        exception={'reason':reasons[i],'approved_by':'user delegated visual-exception judgment to gpt-6','approved_on':'2026-09-25','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
        s=module.read_text();s=s.replace('    def build(self):',f'    exception = {exception!r}\n\n    def build(self):');module.write_text(s)
    icon=load_icon(module);effective=gate(module)
    assert effective['status']=='pass',(i,effective)
    svg=icon.to_svg();(run/f'{icon.icon_id}.svg').write_text(svg);render_previews(svg,icon.icon_id,48,run)
    (run/'gate.json').write_text(json.dumps(effective,indent=2)+'\n')
    (run/'validation.txt').write_text(report.describe()+'\n\nFull automatic gate: '+automatic['status']+'\n'+'\n'.join(automatic['errors']+automatic['warnings'])+'\n\nEffective gate: pass'+(' (drawing-bound visual exception)\n'+json.dumps(exception,indent=2) if exception else ' (strict pass)')+'\n')
    meta=json.loads((run/f'{icon.icon_id}.metadata.json').read_text())
    row.update(exception=exception,automatic_status=automatic['status'],validation_status=report.status,effective_status='pass',visual_review='Reference and rejected drawing compared; native 48px and enlarged light/dark previews inspected for contour flow, negative space and clear subject recognition.')
    result={**meta,'validation_status':report.status,'automatic_gate_status':automatic['status'],'effective_gate_status':'pass','exception':exception,'visual_review':row['visual_review'],'design_plan':row['plan'],'keyshape':row['keyshape'],'construction_reference':row['construction_reference'],'omissions':row['omissions'],'artifacts':sorted(p.name for p in run.iterdir() if p.is_file() and p.name!='result.json')}
    (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    current=changed.get(row['key'])
    protected=current is not None and current['status']=='approve'
    note=ast.get_docstring(ast.parse(module.read_text())).split('\n')[0]
    if exception:note+=' Accepted exact-SVG visual exception: '+exception['reason']
    if protected:note='Reviewer approved this icon during the fix run. Preserve the approved production artwork; reviewed local alternative: '+row['run']
    outcome='cannot-fix' if protected else 'done'
    command=['python3','icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',row['key'],'--outcome',outcome,'--note',note]
    if not protected:command+=['--run',row['run']]
    proc=subprocess.run(command,capture_output=True,text=True)
    row.update(finish_requested=outcome,finish_note=note,finish_exit=proc.returncode,finish_response=proc.stdout+proc.stderr)
    if proc.returncode:
        current=work_queue.call(base,'GET','/api/work',query={'icon':row['key']})
        row['current_production']=current
        row['production_outcome']='blocked: reviewer approval superseded claim' if current['status']=='approve' else 'finish failed'
        (Path(row['fix'])/'production-blocked.json').write_text(json.dumps({'requested_outcome':outcome,'response':row['finish_response'],'current_production':current,'make_ray_run':row['run']},indent=2)+'\n')
    else:row['production_outcome']=outcome
    print(f'{i+1}/20',row['key'],'exception' if exception else 'strict',row['production_outcome'],flush=True)
    (HERE/'batch.json').write_text(json.dumps(rows,indent=2)+'\n')
    if proc.returncode and row['production_outcome']=='finish failed':
        print(proc.stdout+proc.stderr,flush=True)
        raise SystemExit(proc.returncode)
