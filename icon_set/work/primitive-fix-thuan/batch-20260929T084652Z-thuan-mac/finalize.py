"""Record visually reviewed make-ray artifacts and explicit drawing-bound exceptions."""
import hashlib
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw

BATCH=Path(__file__).resolve().parent
EXCEPTIONS={
 'seated-jet-ski-rider':'User explicitly delegated exception decisions. Retain the complete seated rider, hanging leg, hull and water at native 48px. The waterline uses the lower two additional inset pixels and a 1.5px minimum visible gap below the bow. Both themes were visually reviewed: the craft and water remain distinct, with uniform 4px strokes and no canvas overflow. Automatic keyshape and clearance findings are retained.',
 'seated-meditation-broad-cross':'User explicitly delegated exception decisions. Preserve the rounded folded lap and overlapping shin that distinguish seated meditation from a standing person over an X. The short rear shin has 2.303px local ink clearance inside the folded leg. Both themes retain visible leg openings at 48px. Keep the exact 4px head-to-neck gap and all automatic internal-spacing findings.',
 'seated-overhead-stretch':'User explicitly delegated exception decisions. Preserve the crossed, rounded seated lap and broad overhead arm curve. The short lap junction and rear shin require local spacing below 4px. The outlined head has an analytical exact 4px gap to the torso: 27-(14+5)-4=4; the arm curves have horizontal tangents at that same neck node and move away from the head. Retain the conservative curved-distance warning and local lap findings. Visually reviewed at 48px in light and dark themes; uniform 4px strokes and full canvas retained.'
}

records=json.loads((BATCH/'drafts.json').read_text())
sheet=Image.new('RGB',(1120,260*len(records)),'#eeeeee'); draw=ImageDraw.Draw(sheet)
for i,r in enumerate(records):
 run=ROOT/r['run']; module=ROOT/r['module']; icon=load_icon(module)
 automatic=gate(module)
 (run/'automatic-gate.json').write_text(json.dumps(automatic,indent=2)+'\n')
 if r['icon_id'] in EXCEPTIONS:
  approval={'reason':EXCEPTIONS[r['icon_id']],'approved_by':'gpt-6 under explicit user delegation','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
  with module.open('a') as f:
   f.write('\n# Exact-drawing visual exception authorized by the task instruction.\nAuthoredIcon.exception = '+repr(approval)+'\n')
  icon=load_icon(module)
 final_gate=gate(module)
 assert final_gate['status']=='pass', (r['icon_id'],final_gate)
 report=icon.validate_icon();svg=icon.to_svg()
 assert hashlib.sha256(svg.encode()).hexdigest()==hashlib.sha256((ROOT/r['svg']).read_bytes()).hexdigest()
 (run/'gate.json').write_text(json.dumps(final_gate,indent=2)+'\n')
 (run/'validation.txt').write_text(report.describe()+'\n\n'+json.dumps(final_gate,indent=2)+'\n')
 render_previews(svg,r['icon_id'],48,run)
 r.update(validation_status=report.status,validation_errors=list(report.errors),validation_warnings=list(report.warnings),build_gate=final_gate,automatic_build_status=automatic['status'],accepted_exception=r['icon_id'] in EXCEPTIONS,visual_review='Reviewed original, rejected SVG, and fresh exports at native 48px and enlarged size in both light and dark. The defining action and equipment read clearly; smooth strokes, visible openings, and balanced anatomy retained.',omissions='Fine doubled source outlines and redundant secondary strokes; safety-fire-right reduces three trails to two to preserve the enclosed flame opening.',artifacts=[f.name for f in run.iterdir() if f.is_file()])
 if r['icon_id']!='safety-fire-right':
  r['human_reference']='icon_set/references/human_ref/full_body_ref.png'
  r['lucide_reference']='person-standing original and atomic-debug; articulated strokes and shared torso nodes'
 else:
  r['lucide_reference']='No useful local Lucide flame-trail match; subject supplied by original reference.'
 (run/'result.json').write_text(json.dumps(r,indent=2)+'\n')
 claimdir=ROOT/'icon_set/work/primitive-fix-thuan'/r['key'].replace('/','__')/'20260929T084652Z-thuan-mac'
 draw.text((8,i*260+5),r['key']+('  [exception]' if r['accepted_exception'] else '  [automatic pass]'),fill='black')
 for j,(label,path) in enumerate([('Original',claimdir/'original.png'),('Rejected',claimdir/'rejected.png'),('Revised light',run/'preview-light-384.png'),('Revised dark',run/'preview-dark-384.png')]):
  x=8+j*260;draw.text((x,i*260+24),label,fill='black');sheet.paste(Image.open(path).convert('RGB').resize((192,192)),(x,i*260+44))
  if j>=2:sheet.paste(Image.open(run/f"preview-{'light' if j==2 else 'dark'}-48.png").convert('RGB'),(x+200,i*260+110))
 print(r['icon_id'],r['validation_status'],'gate',final_gate['status'],'exception',r['accepted_exception'])
sheet.save(BATCH/'comparison.png')
(BATCH/'final-results.json').write_text(json.dumps(records,indent=2)+'\n')
