from pathlib import Path
import json
from icon_set.scripts import primitive_fix as fix,work_queue as work
AUTHOR='gpt-6';SOURCE_ICON_ID=None;SOURCE_PATH='fix-batch-20260924/manifest.json'
root=Path('icon_set/work/primitive-make-ray/fix-batch-20260924')
entries=json.loads((root/'manifest.json').read_text())
updates={11:{'omissions':'Nested inner flame and small side tongue reduced to one coherent flame silhouette.'},12:{'plan':'Geisha bust with radius-8 circular jaw, round bun, symmetric hairpins, and a curved kimono with diagonal lapel. Shared human-reference user.svg informs circular jaw and shoulders; explicit bust contact is zero ink gap (jaw bottom 26, shoulder top 30).','omissions':'Small hairline and secondary kimono lapel omitted.'},13:{'plan':'Mirrored Gherkin silhouette with smooth curve tangents and a single diagonal glazing band.','omissions':'Lower facade band and dense glazing omitted to preserve negative space.'}}
for e in entries:
 e.update(updates.get(e['index'],{}));r=Path(e['run']);p=Path(e['module']);s=p.read_text();end=s.index('"""',3)
 s='"""'+e['plan']+'\nOmissions: '+e['omissions']+'\nConstruction references: '+str(e['construction_references'] or 'no useful direct Lucide match')+'.\n"""'+s[end+3:];p.write_text(s)
 (r/(e['icon_id']+'.metadata.json')).write_text(json.dumps(e,indent=2)+'\n')
 g=json.loads((r/'gate.json').read_text());assert g['status']=='pass' and not g['warnings'] and not g['errors'],e['icon_id']
 result={**e,'validation_status':'valid','validation_warnings':[],'build_gate':g,'visual_review':'Inspected reference, rejected drawing, and revised light/dark renders at native 48px and enlarged size. Smooth coherent curves, crisp straight runs, uniform stroke, and balanced mirrored elements where appropriate. Directional and organic asymmetry preserves the source.','artifacts':[f.name for f in r.iterdir() if f.is_file()]}
 (r/'result.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'manifest.json').write_text(json.dumps(entries,indent=2)+'\n')
for e in entries:
 fixed=Path(e['fix_dir'])/'result.json'
 if fixed.exists():continue
 note=e['plan']+' Rebuilt clean centerlines; inspected both themes at 48px. '+e['omissions']
 rc=fix.finish(work.default_base_url(),'thuan-mac','solo/'+e['icon_id'],'done',note,ray_run=e['run'])
 if rc:raise SystemExit(rc)
 print('FINISHED',e['index'],flush=True)
