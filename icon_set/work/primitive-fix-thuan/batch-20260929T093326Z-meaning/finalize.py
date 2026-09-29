from author import *
import shutil,cairosvg
REASONS={
1:'Preserve the complete standing statue, divided robe, substantial plinth and wide leaning flag; compact robe openings and the natural composition envelope remain clear at 48px.',
4:'Preserve the tilted orbital ring with globe occlusion and a smooth curved silhouette; small orbital junctions and natural extrema are intentional.',
5:'Preserve a recognizable outlined airplane above separate fork and knife. Compact wing/tail openings and the natural scene envelope remain readable at 48px.',
6:'Preserve a recognizable outlined airplane above a coupe cocktail glass with a visible stem. Compact wing openings, bowl clearance and natural scene envelope are intentional.',
7:'The shoulder arcs intentionally converge into the counter; the broad shoulder opening and full counter remain legible at 48px despite internal-spacing advisories near their joins.',
8:'Preserve the cloud, complete sun with distinct ray dots and person. Compact ray gaps and the natural scene envelope are necessary to retain the weather context at 48px.',
9:'Preserve a left-facing pistol with a distinct grip, complete bust and reaction marks. Compact grip/ray spacing and natural envelope remain clear at 48px.',
10:'Preserve the head approaching the bubbler and the arcing water above the basin. Water/head proximity and the exact curved bowl spacing retain the drinking action.',
11:'Preserve the airborne pose, raised arms, bent legs and elliptical trampoline; compact air gap and natural envelope retain the complete scene.',
12:'Preserve the butterfly, oval net with bag, raised handle and catcher. Small net/head gaps and intentional butterfly wing/antenna joins remain legible at 48px.',
13:'Preserve the descending step pose with three visible stair levels; natural scene envelope and compact bent knee/step junctions remain legible.',
14:'Preserve the larger bust, bent holding sleeve and slender capped bottle silhouette. Natural scene envelope and the sleeve opening are intentional.',
15:'Preserve the full-height outlined measuring ruler and complete standing person; the natural scene envelope and compact ruler-to-hand gap are clear at 48px.',
16:'Preserve a curved seat shell and a person reaching forward with bent knees; the arm/lap opening is intentionally compact and remains visibly open.',
17:'Preserve the dragon prow, passenger bust, rounded hull and rectangular flag; compact attached contours and prow/head spacing retain the complete boat scene.',
19:'Preserve the long diagonal mop handle, open capsule pad and leaning cleaner; natural scene envelope and attached pad junction retain recognizability.',
20:'Preserve the hands held at the groin and visibly crossed legs; compact hand/leg contact and natural shoulder envelope communicate urgency at 48px.'}
OMISSIONS={1:'Facial details and one arm contour omitted; pedestal, robed statue and leaning flag retained.',2:'The misleading letter F was removed; the reference bubble and square were restored.',3:'Diagonal arrow replaced by the reference vertical arrow.',4:'Hidden globe portions omitted behind the ring; no solid diagonal slash.',5:'Separator rule and middle fork tine omitted for room; plane and both utensils retained.',6:'Separator rule and citrus garnish omitted for room; plane and stemmed coupe retained.',7:'No text or facial details added.',8:'Horizon marks omitted to retain the cloud, sun and person without crowding.',9:'No trigger detail; left-facing barrel, grip, full bust and reaction marks retained.',10:'Finger/anatomy details omitted; bent posture, water and pedestal retained.',11:'No extra motion marks; airborne pose and trampoline support retained.',12:'Fine net mesh omitted; oval rim, hanging bag, handle and butterfly retained.',13:'One secondary arm omitted to keep the descending legs and stairs distinct.',14:'Cap separator omitted to keep the neck opening clear; cap-like square top retained.',15:'Body simplified to shared human stick construction, with complete arms and legs.',16:'No wheel added; seated reach and curved seat preserve the given reference.',17:'Water wave row omitted to give the hull and passenger more room.',18:'One leg is occluded in profile; head, bent back, reaching arm, kneeling leg and bucket retained.',19:'Mop fibers omitted; capsule head and long shaft retained.',20:'Facial details omitted; hands-at-groin and crossed legs retained.'}
REFERENCES={2:'Lucide message-square: rounded enclosure and continuous tail contour.',3:'Lucide message-square: rounded enclosure construction.',4:'Lucide orbit: circle arcs and deliberate occlusion; original source owns the tilted ring.',5:'Lucide plane: coherent outlined fuselage, swept wings and tail.',6:'Lucide plane and martini: airplane silhouette and a glass with a separate stem and foot.',7:'Shared human user.svg: round head and smooth open shoulders; Lucide message-square for rounded counter.',16:'Lucide armchair: smooth seat shell; shared human full_body_ref.png for the seated figure.'}
HUMAN={1:'Head center (14,7), radius 4; shoulders peak at (14,19): 19-(7+4)-4 = 4px visible gap.',7:'Head center (24,10), radius 6; shoulders peak at (24,24): 24-(10+6)-4 = 4px.',8:'Head center (24,25), radius 4; shoulders peak at (24,37): 37-(25+4)-4 = 4px.',9:'Head center (14,17), radius 7; shoulders peak at (14,32): 32-(17+7)-4 = 4px.',10:'Head center (25,11), radius 5; upper torso junction (13,16): sqrt(12^2+5^2)-5-4 = 4px. Torso tangent continues away from the head.',11:'Head center (24,8), radius 4; upper torso junction (24,20): 20-(8+4)-4 = 4px.',12:'Head center (35,25), radius 4; upper torso junction (35,37): 37-(25+4)-4 = 4px.',13:'Head center (18,8), radius 4; upper torso junction (18,20): 20-(8+4)-4 = 4px.',14:'Head center (16,12), radius 5; shoulders peak at (16,25): 25-(12+5)-4 = 4px.',15:'Head center (32,10), radius 5; upper torso junction (32,23): 23-(10+5)-4 = 4px.',16:'Head center (23,12), radius 6; upper torso junction (23,26): 26-(12+6)-4 = 4px.',17:'Head center (24,13), radius 4; shoulders peak at (24,25): 25-(13+4)-4 = 4px.',18:'Head center (17,11), radius 5; upper torso junction (29,16): sqrt(12^2+5^2)-5-4 = 4px. Torso tangent continues away from the head.',19:'Head center (28,11), radius 5; upper torso junction (28,24): 24-(11+5)-4 = 4px.',20:'Head center (24,8), radius 4; shoulders peak at y20: 20-(8+4)-4 = 4px.'}

def finalize():
 selected=json.loads((BATCH/'selected.json').read_text());out=[]
 for i,e in enumerate(selected,1):
  if i==9:e['notes']='The rejected pistol was an oversized block beside a partial shoulder, with no reaction marks. Restore a clear left-facing barrel and grip, complete the bust and add the source reaction marks.'
  old=Path(e['run']);run=old.parent/(datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')+'-reviewed');run.mkdir()
  module=run/Path(e['module']).name;source=Path(e['module']).read_text();module.write_text(source)
  icon=load_icon(module);svg=icon.to_svg();sha=hashlib.sha256(svg.encode()).hexdigest()
  automatic=gate(module);exception=None
  if automatic['status']!='pass':
   exception={'reason':REASONS[i],'approved_by':'user (exception discretion explicitly delegated); visual review by gpt-6','approved_on':'2026-09-29','svg_sha256':sha}
   source+='\n# User-authorized visual exception, bound to this reviewed SVG; automatic findings remain recorded.\nDrawing.exception = '+repr(exception)+'\n';module.write_text(source)
  icon=load_icon(module);assert icon.to_svg()==svg
  report=icon.validate_icon();g=gate(module)
  assert g['status']=='pass',g
  assert all(x.startswith(('mic ','canvas/keyshape bounds:')) for x in report.errors+report.warnings),(i,report.describe())
  (run/(e['icon_id']+'.svg')).write_text(svg);render_previews(svg,e['icon_id'],48,run)
  for name,path in [('reference',Path(e['reference'])),('before',Path(e['fix_dir'])/'before'/(e['icon_id']+'.svg'))]:
   shutil.copyfile(path,run/(name+'.svg'))
   for size in (48,384):cairosvg.svg2png(url=str(path),write_to=str(run/f'{name}-{size}.png'),output_width=size,output_height=size,background_color='white')
  meta={k:e[k] for k in ('concept','source_uuid','reference_path')};(run/(e['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
  (run/'validation.txt').write_text(report.describe()+'\n\nFull gate: '+json.dumps(g,indent=2)+'\n')
  (run/'automatic-gate.json').write_text(json.dumps(automatic,indent=2));(run/'gate.json').write_text(json.dumps(g,indent=2))
  refs=REFERENCES.get(i,'Shared human full_body_ref.png and user.svg: circular heads, coherent limbs and smooth shoulders. No useful exact Lucide subject match.' if i in HUMAN else 'No useful exact Lucide match; use coherent rounded geometric construction.')
  findings='Inspected at 48px and enlarged size in light and dark themes. Defining action/objects and remaining openings are readable. '+REASONS.get(i,'Geometry and full QA gate pass without an exception.')
  notes=f"# {e['key']}\n\nComparison: {e['notes']}\n\nReviewer feedback: {e['feedback']}\n\nSymbol plan: {e['plan']}\n\nOmissions: {OMISSIONS[i]}\n\nConstruction references: {refs}\n\nHuman proportions: {HUMAN.get(i,'Not applicable.')}\n\nVisual review: {findings}\n\nAUTHOR: gpt-6\n\nAutomatic validation: {report.status}. Full gate: pass"+(' with user-authorized exception; all automatic findings retained.' if exception else ' without exception.')
  (run/'comparison.md').write_text(notes+'\n')
  final={**e,'run':str(run),'module':str(module),'previous_attempt':str(old),'svg':e['icon_id']+'.svg','validation_status':report.status,'validation_errors':report.errors,'validation_warnings':report.warnings,'gate':g,'accepted_exception':bool(exception),'exception':exception,'visual_review':findings,'human_proportions':HUMAN.get(i),'construction_references':refs,'omissions':OMISSIONS[i],'artifacts':sorted(p.name for p in run.iterdir())}
  (run/'result.json').write_text(json.dumps(final,indent=2)+'\n');out.append(final)
  print(i,e['key'],'PASS '+('EXCEPTION' if exception else 'STRICT'),flush=True)
 (BATCH/'final-runs.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':finalize()
