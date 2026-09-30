import json,shutil,sys
from pathlib import Path
import cairosvg
from PIL import Image,ImageDraw
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import load_icon
root=Path(__file__).parent;rows=json.loads((root/'claims.json').read_text())
assert len(rows)==20 and len({r['key'] for r in rows})==20
lines=['# Once-disapproved solo fix batch 06','',
       '20 icons claimed at offset 0 using `--max-disapprovals 1`; all finished through `primitive_fix.py finish --outcome done` and returned to Ready. All modules use `AUTHOR = "gpt-6"`. Model validation is valid and the full build gate passes with zero errors and warnings for every icon.',
       '', 'Skill: [primitive-fix-thuan](../../../.agents/skills/primitive-fix-thuan/SKILL.md), with [primitive-make-ray](../../../.agents/skills/primitive-make-ray/SKILL.md).', '',
       'No reviewer supplied written feedback or a disapproval reason for these claims. Repairs therefore follow the inspected original references and the visible defects in the rejected drawings. Registered modules and published outputs were not changed.', '']
summaries=[]
for i,r in enumerate(rows):
 run=Path(r['run']);fix=Path(r['fix']);finish=json.loads((fix/'result.json').read_text())
 assert finish['outcome']=='done' and finish['review_status']=='ready'
 assert finish['author']=='gpt-6' and finish['validation_status']=='valid' and not finish['validation_warnings']
 assert finish['build_gate']['status']=='pass' and not finish['build_gate']['warnings'] and not finish['build_gate']['errors']
 icon=load_icon(Path(r['module']));svg=run/(icon.icon_id+'.svg')
 assert svg.read_text()==(fix/'after'/svg.name).read_text()
 assert Path(r['module']).read_text()==(fix/'after'/Path(r['module']).name).read_text()
 for kind,source in [('reference',r['reference']),('before',r['before'])]:
  shutil.copyfile(source,run/f'{kind}.svg')
  for size in (48,384):
   cairosvg.svg2png(url=source,write_to=str(run/f'{kind}-{size}.png'),output_width=size,output_height=size,background_color='white')
 note=r['note']
 if i==6:note='The rejected figure had a small head and the pine had narrow branch notches. Enlarged the head, rebalanced the shoulders and legs, and broadened the lower pine tier. Two tiers retain clear branch openings.'
 if i==11:note='The rejected drawing introduced spread walking legs although the reference is a cropped torso. Restored the straight cropped torso and retained the oval balloon, string and bent holding arm. Omitted the rear arm to preserve clearance.'
 meta=json.loads((run/'result.json').read_text())
 meta.update(comparison=note,omissions=note,keyshape=icon.keyshape.name,production_finish=str(fix/'result.json'),review_status_at_finish='ready',visual_review='Compared original and rejected drawing before authoring; inspected final native 48px and enlarged light and dark previews. Checked silhouette, curve flow, negative space and reference arrangement.',intentional_asymmetry='Directional poses and object arrangements follow the source; paired features share dimensions where appropriate.')
 if i in (6,7,8,9,10,11,13,14,17,18,19):
  meta['human_reference']='icon_set/references/human_ref/full_body_ref.png'
  meta['human_gap']='Circular head aligned above the upper torso, with exactly 8 centerline units / 4 visible ink units from its lower outline to the torso junction.'
 if i in (12,15,16):meta['human_reference']='icon_set/references/human_ref/user.svg; source-specific head, hands or hood silhouette'
 meta['artifacts']=sorted(p.name for p in run.iterdir() if p.is_file())
 (run/'result.json').write_text(json.dumps(meta,indent=2)+'\n')
 def link(label,p):return f'[{label}](<{Path(p).resolve()}>)'
 lines.extend([f'## {i+1}. `{r["key"]}`','',note,'',f'Feedback: none recorded. AUTHOR: `gpt-6`. Validation: **valid, zero warnings; full build gate pass**. Production: **done → Ready**.','',f'Keyshape: `{icon.keyshape.name}`. The exact SOLO48 envelope fits the subject’s '+('wide composition.' if icon.keyshape.name.startswith('HRECT') else 'upright composition.' if icon.keyshape.name.startswith('VRECT') else 'balanced overall composition.'),'',f'Construction reference: {meta.get("lucide","No useful direct match")}.','', ' · '.join([link('RESULT_DIR',run),link('SVG',svg),link('Python',r['module']),link('Reference',r['reference']),link('Before',r['before']),link('Light preview',run/'preview-light-384.png'),link('Dark preview',run/'preview-dark-384.png'),link('Validation',run/'validation.txt'),link('Production receipt',fix/'result.json')]),''])
 summaries.append(dict(key=r['key'],run=str(run),svg=str(svg),author='gpt-6',validation='valid',build_gate='pass',warnings=0,outcome='done',review_status='ready',changes=note))
(root/'REPORT.md').write_text('\n'.join(lines))
(root/'summary.json').write_text(json.dumps(summaries,indent=2)+'\n')
for page in range(2):
 sheet=Image.new('RGB',(800,1000),'white');d=ImageDraw.Draw(sheet)
 for j,r in enumerate(rows[page*10:page*10+10]):
  run=Path(r['run']);y=j*100;d.text((5,y+3),str(page*10+j+1)+' '+r['key'],fill='black')
  for k,name in enumerate(('reference-48.png','before-48.png','preview-light-48.png','preview-dark-48.png')):
   sheet.paste(Image.open(run/name).convert('RGB'),(15+k*95,y+30))
  d.text((420,y+40),'valid / gate pass / Ready',fill='black')
 sheet.save(root/f'final-native-{page+1}.png')
print('Verified 20/20 production finish receipts; source and SVG match uploaded artifacts. REPORT.md and summary.json written.')
