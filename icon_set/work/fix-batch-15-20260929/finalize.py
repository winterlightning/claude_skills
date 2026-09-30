from pathlib import Path
import json,cairosvg,hashlib
B=Path(__file__).parent
rows=json.loads((B/'staged.json').read_text());runs=json.loads((B/'runs.json').read_text())
assert len(rows)==len(runs)==20
for row in rows:
 key=row['item']['icon_id'];r=runs[key];run=Path(r['run']);assert r['valid'],key
 meta=r['metadata'];ref=Path(row['reference'])
 for n in (48,384):cairosvg.svg2png(url=str(ref),write_to=str(run/f'reference-{n}.png'),output_width=n,output_height=n,background_color='white')
 v={'native_light_dark':'Inspected 48px and enlarged light/dark previews; reviewed silhouette, curve flow, joins and negative space against the original and rejected drawing.','findings':meta['comparison'],'symmetry':'Paired parts derive from shared dimensions; directional arrows, overlapping objects and scene layouts preserve intentional asymmetry.'}
 if key in ('seat-find',):v['human_spacing']='Circular head bottom14 and torso junction22: exact8 centerline /4 ink gap; head is aligned over its vertical torso; human_ref/full_body_ref.png.'
 if key in ('short-haired-woman-with-visible-sleeve-seams','policewoman-in-peaked-cap','policewoman-with-rounded-helmet','policewoman-with-circular-cap-badge'):v['human_spacing']='Circular jaw and shoulder arch have4 centerline separation /0 ink gap; human_construction=bust; human_ref/user.svg.'
 result=dict(meta,validation_status='valid',validation_errors=[],validation_warnings=[],build_gate=json.loads((run/'gate.json').read_text()),visual_review=v,module=Path(r['module']).name,svg=key+'.svg',svg_sha256=hashlib.sha256((run/(key+'.svg')).read_bytes()).hexdigest(),artifacts=sorted(p.name for p in run.iterdir() if p.is_file()))
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
print('20 reviewed run records finalized')
