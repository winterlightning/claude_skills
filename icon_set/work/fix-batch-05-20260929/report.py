import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
rows=json.loads((ROOT/'batch.json').read_text())
omissions={'horizontal-bullet-with-separate-base': 'No defining element omitted; separate base and curved tapered projectile retained.', 'horizontal-axial-fuse-with-rounded-end-caps': 'No defining element omitted; paired end caps, central tube and axial leads retained.', 'horizontal-adhesive-bandage': 'No defining element omitted; rounded strip and two curved pad boundaries retained.', 'human-brain-hemispheres-batch-001-r2': 'Fine internal folds omitted to keep the paired lobes and central fissure clear.', 'human-head-side-profile-scan-batch-001-r3': 'Small lip detail simplified; ear, curved profile and integrated scan boundary retained.', 'human-head-side-profile-scan-batch-001-r2': 'Ear and small lip details omitted in this profile variant; main profile and scan boundary retained.', 'heart-set-engagement-ring': 'Upper band reduced to a clear open curve beneath the heart jewel.', 'high-column-two-tick-thermometer': 'No defining element omitted; outlined reservoir, high column, bulb and two ticks retained.', 'empty-battery-content': 'None; empty body and attached rounded terminal retained.', 'empty-battery-level-indicator-solo': 'No defining element omitted; outer body, terminal and wide empty window retained.', 'face-blowing-into-tissue': 'Fine side folds reduced to one central cloth fold; gathered cloth, round face and closed eyes retained.', 'fairy-with-narrow-wings': 'Fine wing veins omitted; narrow paired wings, circular head, flared dress and two short legs retained.', 'figure-broad-rain-poncho': 'Fine neckline detail omitted; hood, curved lower face and broad flowing hem retained.', 'figure-wearing-headscarf-7530ebed': 'Torso seams omitted; wrapped scarf, circular face and broad shoulders retained.', 'inverted-freestyle-skier-batch-051': 'Fine clothing and pole-basket detail omitted; inverted figure, bent legs, long skis and pole arm retained.', 'isometric-room-grid-with-central-corner': 'Secondary floor subdivisions omitted; wall grid and separate floor plane retained.', 'jaguar': 'Four overlapping legs reduced to two readable leg openings and multiple spots reduced to one; rounded ear, muzzle and tail retained.', 'jumbo-jet': 'Small fuselage details omitted; rounded nose, swept wings, diagonal body and tail retained.', 'kendo-practitioner': 'Fine helmet band omitted to permit a smaller head and restore full-body robe proportions; sword and split garment retained.', 'kazoo': 'No defining element omitted; diagonal tube, round membrane housing and inner opening restored.'}
lines=['# Once-disapproved solo fix batch 05 of 34','',
       '20 claimed at offset 0 with `--max-disapprovals 1`, worker `thuan-mac`. All 20 uploaded through `primitive_fix.py finish`, reported done and returned to Ready. Repeat disapprovals were excluded by the queue history filter before claiming.','',
       'Every original and rejected SVG was rendered and compared before authoring. No claimed item contained a disapproval reason or written reviewer feedback; the specific repairs below follow the original/current visual comparison.','',
       'Every selected run has `AUTHOR = "gpt-6"`, `validate_icon(): valid`, full build gate `pass`, zero errors and zero warnings. No validation exceptions were used. Native 48px light/dark and enlarged previews were visually reviewed. Registered modules, published output and galleries were not edited.','',
       'Comparison sheets (columns: original, rejected, revised light, revised dark): '+', '.join(f'[sheet {n}](<{ROOT/f"after-{n}.png"}>)' for n in range(1,5)), '']
audit=[]
for row in rows:
    run=REPO/row['run'];fix=REPO/row['fix_dir']
    r=json.loads((fix/'result.json').read_text());plan=json.loads((run/'review-plan.json').read_text())
    assert r['outcome']=='done' and r['review_status']=='ready' and r['reported']['state']=='done'
    assert r['author']=='gpt-6' and r['validation_status']=='valid' and not r['validation_errors'] and not r['validation_warnings']
    assert r['build_gate']['status']=='pass' and not r['build_gate']['errors'] and not r['build_gate']['warnings']
    assert r['uploaded']['has_python'] and r['uploaded']['has_validation'] and not r['accepted_exception']
    result_path=run/'result.json';result=json.loads(result_path.read_text());result['omissions']=omissions[row['icon_id']]
    result['production_finish']={'outcome':'done','review_status':'ready','finished_at':r['finished_at'],'receipt':str(fix/'result.json')}
    result_path.write_text(json.dumps(result,indent=2)+'\n')
    svg=run/(row['icon_id']+'.svg');module=next(run.glob('*.py'))
    assert svg.read_bytes()==(fix/'after'/svg.name).read_bytes()
    assert module.read_bytes()==(fix/'after'/module.name).read_bytes()
    why='circular expression envelope' if plan['key']=='CIRCLE' else 'wide subject arrangement' if plan['key'].startswith('HRECT') else 'upright subject proportions' if plan['key'].startswith('VRECT') else 'balanced width and height'
    lines += [f'## {row["key"]}','',f'Before versus original: {plan["issue"]}',
              '', 'Reviewer request: no reason or written feedback recorded.', '',f'Changed: {plan["change"]}',
              '',f'Keyshape: `{plan["key"]}` for {why}; {plan["bounds"]}.',
              '',f'Construction reference: {plan["reference"]}', '',f'Reduction: {omissions[row["icon_id"]]}',
              '', 'AUTHOR: `gpt-6`. Validation: valid, full QA pass, zero warnings. Production: done → Ready.', '',
              f'[RESULT_DIR](<{run}>) · [SVG](<{svg}>) · [Python](<{module}>) · [validation](<{run/"validation.txt"}>) · [production receipt](<{fix/"result.json"}>)','']
    audit.append({'key':row['key'],'run':row['run'],'svg':str(svg.relative_to(REPO)),'author':r['author'],'outcome':r['outcome'],'review_status':r['review_status'],'validation_status':r['validation_status'],'build_gate':r['build_gate']['status'],'warnings':0})
(ROOT/'REPORT.md').write_text('\n'.join(lines))
(ROOT/'audit.json').write_text(json.dumps(audit,indent=2)+'\n')
print('Audited',len(audit),'done / Ready, with matching local and uploaded artifacts; zero warnings.')
print(ROOT/'REPORT.md')
