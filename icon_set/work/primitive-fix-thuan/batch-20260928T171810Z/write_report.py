from pathlib import Path
import json
from PIL import Image,ImageDraw
B=Path(__file__).parent.resolve()
rows=json.loads((B/'completed.json').read_text());assert len(rows)==10
exceptions=sum(r['accepted_exception'] for r in rows)
def link(label,p):return f'[{label}](<{Path(p).resolve()}>)'
lines=['# Manual fix batch — 10 available icons','',f'Requested: 20. The first claim command returned 10. A second claim attempt for the remaining 10 returned exit 3: no claimable solo icons with reason manual-fix-request. All 10 claimed icons were completed.','',f'Worker: `thuan-mac`. Every finish receipt reports `done` and production status `ready`. All authored modules use `AUTHOR = "gpt-6"`. {10-exceptions} strict QA pass; {exceptions} drawing-bound visual exceptions under the user’s authorization. The exact SVG hashes and automatic findings are preserved.','',link('Final light/dark preview',B/'final-preview.png'),'','All originals and rejected drawings were compared before authoring. Fresh result folders hold the modules, SVGs, source metadata, reference renders, light/dark native and enlarged previews, and validation records. Registered modules and published output were not changed.','']
why={0:'natural upright profile',1:'tall message body and directional tail',2:'horizontal housing and extended tape',3:'lower horizontal tool proportions',4:'long narrow natural pod',5:'square plotting area',6:'full-height machine and box',7:'complete roof, figure and procession',8:'two square tiles and upper rotation arc',9:'low wide wearable visor'}
im=Image.new('RGB',(1000,400),'#ddd');d=ImageDraw.Draw(im)
for i,r in enumerate(rows):
 run=Path(r['run']);result=json.loads((run/'result.json').read_text());review=json.loads((run/'review.json').read_text());finish=json.loads((Path(r['fix'])/'result.json').read_text())
 assert finish['outcome']=='done' and finish['review_status']=='ready' and finish['author']=='gpt-6'
 assert finish['build_gate']['status']=='pass'
 assert not (Path(r['fix'])/'before-upload-error.txt').exists()
 status='Pass · visual exception (automatic '+r['automatic_status']+')' if r['accepted_exception'] else 'Strict pass · zero warnings'
 module=Path(r['module']);shape=module.read_text().split('keyshape=Keyshape.',1)[1].splitlines()[0]
 lines += [f'## {r["key"]}','',f'**Rejected drawing versus original:** {review["before_problem"]}',f'**Feedback:** {r["feedback"].replace(chr(10)," / ")}',f'**Revision:** {r["note"]}',f'**Keyshape:** `{shape}` for {why[i]}.',f'**Omissions:** {review["omissions"]}',f'**Author / validation / production:** `gpt-6` · {status} · Ready.',f'**Construction reference:** {review["construction_reference"]}. Directional/profile asymmetry follows the original; repeated nodes, busts and visor halves use shared geometry.',f'**RESULT_DIR:** {link("Run folder",run)} · {link("SVG",run/(r["icon_id"]+".svg"))} · {link("Python",module)} · {link("Validation",run/"validation.txt")} · {link("Production finish receipt",Path(r["fix"])/"result.json")}', '']
 if r['accepted_exception']:lines += [f'**Exception rationale:** {result["build_gate"]["exception"]["reason"]}','']
 if i==7:lines += ['**Human construction:** shared `human_ref/user.svg`; all heads have center y30/radius 3 and shoulders at y41: exactly 8 units between centerlines, 4 units visible clearance.','']
 x=(i%5)*200;y=(i//5)*200
 pic=Image.open(run/'preview-light-384.png');pic.thumbnail((130,130));im.paste(pic,(x,y+25))
 im.paste(Image.open(run/'preview-light-48.png'),(x+140,y+30));im.paste(Image.open(run/'preview-dark-48.png'),(x+140,y+95));d.text((x+5,y+2),f'{i}: '+r['icon_id'][:23],fill='black')
im.save(B/'final-preview.png');(B/'report.md').write_text('\n'.join(lines))
print(f'Verified {len(rows)} done/Ready receipts, {10-exceptions} strict passes, {exceptions} exceptions; no before-upload errors.')
print(B/'report.md')
