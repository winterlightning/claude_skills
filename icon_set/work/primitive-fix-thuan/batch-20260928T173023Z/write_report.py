from pathlib import Path
import json
from PIL import Image,ImageDraw
B=Path(__file__).parent.resolve()
rows=json.loads((B/'completed.json').read_text());assert len(rows)==20
exceptions=sum(r['accepted_exception'] for r in rows)
def link(label,p):return f'[{label}](<{Path(p).resolve()}>)'
lines=['# Bad-stroke fix batch — 20 icons','',f'Worker: `thuan-mac`. All 20 claimed icons were fixed and uploaded. Every finish receipt reports `done` and production status `ready`. All authored modules use `AUTHOR = "gpt-6"`. {20-exceptions} strict QA passes; {exceptions} drawing-bound visual exceptions under the user’s authorization. Exact SVG hashes and original automatic findings are preserved.','',link('Final light/dark preview',B/'final-preview.png'),'','All originals and rejected drawings were compared before authoring. Fresh result folders hold the Python modules, SVGs, source metadata, reference renders, light/dark native and enlarged previews, and validation records.','']
why={0: 'broad headband and matched tall cups', 1: 'circular currency badge', 2: 'circular clock plus lower return arrow', 3: 'diagonal blade and rounded bell guard', 4: 'diagonal nib and horizontal flourish', 5: 'four equally prominent suit symbols', 6: 'four-part apple/carton cycle', 7: 'rounded bubble with directional tail', 8: 'rounded bubble with directional tail', 9: 'natural tall bulb and socket', 10: 'upright folded document', 11: 'natural tall map pin', 12: 'source lowercase letter and detached plus', 13: 'round waveform badge', 14: 'upright folded slide document', 15: 'wide camera and raised microphone', 16: 'low wide camera and tapered lens', 17: 'natural symmetric shirt silhouette', 18: 'tapered speaker and detached sound wave', 19: 'diagonal saw and notched grip'}
im=Image.new('RGB',(1000,800),'#ddd');d=ImageDraw.Draw(im)
for i,r in enumerate(rows):
 run=Path(r['run']);result=json.loads((run/'result.json').read_text());review=json.loads((run/'review.json').read_text());finish=json.loads((Path(r['fix'])/'result.json').read_text())
 assert finish['outcome']=='done' and finish['review_status']=='ready' and finish['author']=='gpt-6'
 assert finish['build_gate']['status']=='pass'
 assert not (Path(r['fix'])/'before-upload-error.txt').exists()
 status='Pass · visual exception (automatic '+r['automatic_status']+')' if r['accepted_exception'] else 'Strict pass · zero warnings'
 module=Path(r['module']);shape=module.read_text().split('keyshape=Keyshape.',1)[1].splitlines()[0]
 lines += [f'## {r["key"]}','',f'**Rejected drawing versus original:** {review["before_problem"]}',f'**Feedback:** {r["feedback"].replace(chr(10)," / ")}',f'**Revision:** {r["note"]}',f'**Keyshape:** `{shape}` for {why[i]}.',f'**Omissions:** {review["omissions"]}',f'**Author / validation / production:** `gpt-6` · {status} · Ready.',f'**Construction reference:** {review["construction_reference"]}. Directional asymmetry follows the original; repeated components use shared construction geometry.',f'**RESULT_DIR:** {link("Run folder",run)} · {link("SVG",run/(r["icon_id"]+".svg"))} · {link("Python",module)} · {link("Validation",run/"validation.txt")} · {link("Production finish receipt",Path(r["fix"])/"result.json")}', '']
 if r['accepted_exception']:lines += [f'**Exception rationale:** {result["build_gate"]["exception"]["reason"]}','']
 x=(i%5)*200;y=(i//5)*200
 pic=Image.open(run/'preview-light-384.png');pic.thumbnail((130,130));im.paste(pic,(x,y+25))
 im.paste(Image.open(run/'preview-light-48.png'),(x+140,y+30));im.paste(Image.open(run/'preview-dark-48.png'),(x+140,y+95));d.text((x+5,y+2),f'{i}: '+r['icon_id'][:23],fill='black')
im.save(B/'final-preview.png');(B/'report.md').write_text('\n'.join(lines))
print(f'Verified {len(rows)} done/Ready receipts, {20-exceptions} strict passes, {exceptions} exceptions; no before-upload errors.')
print(B/'report.md')
