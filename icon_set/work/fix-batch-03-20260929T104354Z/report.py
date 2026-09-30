import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
rows=json.loads((ROOT/'batch.json').read_text())
omissions={
 'bearded-pirate-with-hook-hand':'Fine facial and shoulder lines omitted; pirate hat, pointed beard and hook retained.',
 'bell-knob-curved-clapper':'Top knob reduced to a round mark; no essential bell component omitted.',
 'bird-in-flight':'Tiny talon and feather lines omitted; both wings, broad tail and hooked profile retained.',
 'body-scanner-gate':'Scanner sensors reduced to short marks; anatomical outlines reduced to a standing figure.',
 'bowler-hat':'No identifying element omitted; dome, band and upturned brim retained.',
 'boxcar-on-rails':'Four small wheels reduced to two readable bogie wheels; two vertical panel marks retained.',
 'boy-figure-with-circular-head':'No essential silhouette element omitted; shirt and tapered body retained.',
 'braille-cell':'None; all six outlined circles retained.',
 'bug-beetle':'None of the original round-body, middle division or six radial appendages omitted.',
 'confused-face':'No essential expression element omitted; two brows, eyes and frown retained.',
 'downhill-skier':'Anatomical outline reduced to coherent pose strokes; forward pole and ski retained.',
 'rope-climber':'Fine anatomical contour and harness detail reduced; raised grip, bent limbs and vertical climbing support retained.',
 'thinking-person-with-hand-at-chin':'Fingers and inner sleeve line omitted; head, shoulder and hand-at-chin arm retained.',
 'three-people-behind-banner':'Clothing outlines reduced to shoulder/torso strokes and short legs; all three people and banner retained.',
 'three-people-on-winners-podium':'Anatomical outlines reduced to head/shoulder/torso marks; raised central rank and three people retained.',
 'three-people-with-central-foreground-figure':'Inner side-torso edges omitted as occluded; three heads and broad central foreground torso retained.',
 'three-person-team-busts':'Inner side-torso edges omitted as occluded; three heads and broad central bust retained.',
 'three-tower-castle-with-flags':'Two side flags omitted and the central pennant simplified to an open turned edge; three roofed towers and doorway retained.',
 'thumbs-down-hand':'Multiple finger creases reduced to one; longer downward thumb and cuff retained.',
 'user-avatar':'Fine neckline omitted; circular head and closed shirt torso retained.',
}
lines=['# Once-disapproved solo fix batch 03 of 34','',
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
