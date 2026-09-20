import json,sys,hashlib,inspect,sqlite3
from pathlib import Path
W=Path(__file__).parent;ROOT=W.resolve().parents[2];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create,factories
from icon_set.scripts.compose import compose
from icon_set.scripts.primitive_status import init_primitive_status,set_status
rows=json.loads((W/'batch.json').read_text());candidates=json.loads((W/'results.json').read_text());f=factories()
PARTS={
1:'Can body; actuator; two diverging spray marks.',2:'Horizontal airplane; two wings; two tail fins; round nose.',3:'Diagonal airplane; swept wing; tail; rounded nose; original flight direction.',4:'Document frame and three lines of different lengths.',5:'Counterclockwise circle arc and left-facing arrowhead.',6:'Pointer triangle and diagonal tail.',7:'Up arrowhead and broad stem.',8:'Trapezoid bag and arched handle; original has no side panel.',9:'Rounded tapered bag and arched handle; original has no flap.',10:'Balaclava outline, flared hem and crossing two-loop eye opening.',11:'Rounded square frame and FOUR vertical barcode bars.',12:'Laptop screen and trapezoid base.',13:'Battery outline and attached terminal.',14:'Battery outline, terminal and three-segment lightning bolt.',15:'Battery outline and rounded terminal.',16:'Round flask, narrow neck and rim.',17:'Headpost, footpost and two horizontal bed rails.',18:'Knob, dome, flared hem and curved clapper.',19:'Two open circular wheels, triangular frame, saddle, fork and handlebar.',20:'Three separate fingerprint ridges.',21:'Circular border, capital B and TWO vertical currency strokes.',22:'Oval speech bubble, tail, B and TWO vertical currency strokes.',23:'Almond eye and rising diagonal slash.',24:'Four bone lobes and central shaft.',25:'Closed book, cover, lower page seam and curved binding.',26:'Two curved pages and central fold; no extra page divider.',27:'Notebook outline, vertical binding and three binding marks.',28:'Case outline, handle, flap seam and central clasp.',29:'Invoice outline, pound sign and TWO text lines.',30:'Two broken rounded links and THREE break rays.',31:'Domed head, rounded body, TWO antennae and FOUR lateral legs.',32:'Two overlapping buildings, ground and one small window dash.',33:'Sloped building, projecting left wall, baseline and short entrance mark.',34:'Bus body, window separator, two headlights and two wheels.',35:'Calculator body, CLOSED rectangular display and FOUR keys.',36:'Camera body, raised housing and round lens.',37:'Car body, roof, chassis and TWO round wheels.',38:'Engine housing, top cap/stem and left shaft/end marker.',39:'Car body, roof, chassis and TWO round wheels.',40:'Rounded card and short horizontal mark.',41:'Hull, tall cargo block, small bridge, mast and multi-crest waterline.',42:'Carrot body, TWO upright pointed leaves and TWO short surface marks.',43:'Cat outline, two ears, two eyes and paired curved mouth; no added nose stem.',44:'Closed battery shell, attached terminal and lightning bolt.',45:'Oval speech bubble, tail, two short vertical eyes and smile.',46:'Rounded document, TWO square checkboxes and TWO text lines.',47:'Document, TWO checkmarks and TWO text lines.',48:'Open-bottom chicken head, comb, two eyes and CLOSED diamond beak.',49:'Circular child face, asymmetric hair part and two short slanted eyes.',50:'Curved chilli body and attached curling stalk.'}
BLOCKS={
3:'The smoother source-oriented candidate still fails parallel fuselage spacing: 5.65685 centerline units versus 8 required. Retained for another redraw; not activated.',
4:'Three parallel interior lines plus top and bottom frame require four 8-unit intervals: 32 centerline units, exceeding the maximum 28 available. Keeping all three lines prevents a compliant redraw.',
10:'Complete crossing eye loops still crowd the mask outline: 5.0427 centerline units versus 6 required. Retained candidate for further design review.',
11:'Source has four bars; old model omitted one. Four bars plus two frame sides require five 8-unit intervals (40), beyond the 28-unit canvas envelope. Do not publish the incomplete three-bar version as fixed.',
14:'Numeric checks pass, but the bolt collapses into a heavy blob at native size. Terminal consumes 8 units and the interior cannot currently give the three-segment bolt sufficient visual room. Visual rejection; original remains active.',
19:'Numeric checks pass, but fork/frame spokes fill the small wheel interiors. Source requires two visibly open wheels. Visual rejection; preserve the draft for a larger layout rethink.',
21:'The parent omitted both currency strokes, changing Bitcoin into B. No preferred Bitcoin glyph exists in the shared typeface. Preserve the whole coin reference; do not invent a replacement glyph or approve the incomplete parent.',
22:'The parent changed the oval bubble and shortened the currency strokes. No shared Bitcoin glyph exists; the complete framed layout is unresolved at 32px/4px stroke.',
27:'Three parallel binding marks plus top/bottom frame need at least 32 centerline units vertically, beyond the 28 available. Original source recovered from its relocated path.',
29:'The parent omitted both invoice lines. The shared typeface has no pound-sign glyph, so a complete shared-glyph repair is blocked. Keep the original document, currency mark and both lines in reference.',
35:'Original has a closed rectangular display, not a frame-spanning divider. Keeping that display and both rows of keys needs more than 28 centerline units vertically once frame and inter-row clearances are included. The old model omitted the display sides; not accepted as repaired.',
41:'Parent removed the waterline and changed hull shape. Two blocks with required separation, mast, hull and repeated wave clearance have no verified complete SUB32 layout in this batch. Retain for complete redraw; not declared geometrically impossible.',
42:'Parent changed the upright leaves to sideways leaves and removed both carrot marks. A complete slender-body layout with two separated marks and two open leaves is unresolved; do not approve the incomplete silhouette.',
44:'Parent opened the closed battery shell around the lightning bolt. Restoring the terminal and closed shell leaves too little room in the current layout for a legible bolt; needs a complete redraw, not an open-shell substitute.',
46:'Parent replaced both square checkboxes by circles, dropped the lines and added a dog-ear. Two 8-unit checkbox interiors, row gap and frame clearance require more than the available vertical space. Retain original complete document.',
48:'Small beak lost its diamond hole. Restoring an 8-unit diagonal-width diamond crowds both eyes: 3.53553 centerline units versus 6 required. Do not replace the closed diamond with a chevron.'}
audit=[];accepted=[];composition={}
for r in rows:
 n=r['number'];uid=r['icon'];mod=sys.modules[f[uid].__module__]
 assert hashlib.sha256(Path(r['python_source']).read_bytes()).hexdigest()==r['parent_sha256'],uid
 entry=dict(r,source_uuid=mod.SOURCE_ICON_ID,source_parts=PARTS[n],parent_preserved=True)
 if str(n) in candidates:
  c=candidates[str(n)];m=create(c['icon']);q=m.validate_icon();entry.update(candidate=c['icon'],candidate_python=c['python_source'],candidate_status=q.status,candidate_findings=q.describe(),repair=c['plan'],construction_reference=c['reference'])
 if n in BLOCKS:
  entry.update(outcome='unresolved',primitive_status='skip',reason=BLOCKS[n],source_coverage_pass=False)
 else:
  assert entry['candidate_status']=='valid',entry
  composed=compose('container-circle',entry['candidate']);cq=composed.validate_icon()
  composition[str(n)]=dict(status=cq.status,findings=cq.describe())
  assert cq.status=='valid',composition[str(n)]
  entry.update(outcome='repaired',source_coverage_pass=True,visual_review='Native light/dark and enlarged centerline reviewed; all original subject parts retained.',reason=entry['repair'])
  accepted.append(entry)
 audit.append(entry)
(W/'audit.json').write_text(json.dumps(audit,indent=2))
(W/'accepted.json').write_text(json.dumps(accepted,indent=2))
(W/'composition-checks.json').write_text(json.dumps(composition,indent=2))
# Batch-local primitive decisions: never overwrite the server's manual review state.
con=sqlite3.connect(W/'primitive-status.sqlite3');init_primitive_status(con)
for r in audit:
 if r['outcome']=='unresolved':set_status(con,[r['source_uuid']],'skip','other',r['reason'],user='gpt-6',record=lambda *a,**k:None)
con.commit();con.close()
(W/'primitive-status.json').write_text(json.dumps({r['source_uuid']:dict(status='skip',icon=r['icon'],note=r['reason']) for r in audit if r['outcome']=='unresolved'},indent=2))
print(len(accepted),'repaired;',len(audit)-len(accepted),'unresolved; all 50 parents intact')
