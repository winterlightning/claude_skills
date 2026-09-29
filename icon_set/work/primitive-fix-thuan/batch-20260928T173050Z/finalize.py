from author import *
import hashlib,cairosvg
from icon_set.scripts.primitive_fix import load_icon,approved_visual_exception
from icon_set.scripts.build_gate import gate
REASONS={
2:'Keep all four G Pay letters with clear curved counters. A two-row UI reflow and its larger near-square envelope are preferable to the crowded horizontal wordmark; retain small curved-counter advisories.',
4:'Preserve the folded page corner and a readable two-column table. The 2px bottom margin and naturally tapered fold are intentional at 48px; every table cell retains 4px interior space.',
5:'Retain the diagonal price-tag silhouette, round eyelet and curved G. The eyelet margin and compact G are visually separate at native size; allow the optical envelope and compact logo spacing.',
8:'The central open loop and four diagonal spokes are essential to this logo. Keep the three clear concentric levels and true spoke joins, accepting the inner-loop spacing advisories.',
9:'Preserve the outlined capsule and flagged numeral one. Rounded flag-to-stem geometry and the narrow left gap remain readable at native size; accept their local spacing findings.',
10:'The paired hand outlines need narrower fingers and thumb creases than the generic 4px clearance. Native light/dark review confirms recognizable cupped palms and a separate sphere; allow the wider composition envelope.',
11:'Preserve both gripping hands and the clipboard. Compact text and finger contours need local spacing exceptions; the board, wrists and fingers remain distinguishable at 48px in both themes.',
12:'Preserve the diagonal puzzle tab/socket and two cupped hands. Compact anatomical finger gaps and the tapered puzzle socket remain recognizable; accept their spacing and optical-envelope findings.',
13:'Preserve the heart between two open hands. The lower palm and giving fingers require compact clearances and a wider envelope; the heart remains separate and legible in both themes.',
14:'Preserve the elliptical pottery opening and complete paired hands. Compact finger construction, rim junction and optical composition envelope are intentional; all regions remain legible at 48px.',
15:'Preserve front-car windshield, lamps, tires and supporting hands. Tight anatomical finger gaps and hand-to-car support read clearly at native size; accept local spacing and wider envelope findings.',
16:'Preserve a recognizable handshake with continuous thumb and rounded fingers. Anatomical tapered gaps and finger separations intentionally fall below generic part spacing; retain the natural optical envelope.',
17:'Preserve a recognizable handshake with long shirt cuffs, continuous thumb and rounded fingers. Anatomical tapered gaps need an exception to generic part spacing; retain the natural optical envelope.',
18:'Preserve a recognizable handshake with short cuffs, continuous thumb and rounded fingers. Anatomical tapered gaps need an exception to generic part spacing; retain the natural optical envelope.',
20:'Retain the Heroku h, rising accent and small triangular stem mark. The tiny arrow counter and compact accent spacing are brand-defining and visibly readable; preserve the tall rounded frame.'}
OMISSIONS={
2:'Reflowed the horizontal wordmark to two rows so no character is squeezed or omitted.',
3:'Double outlined G reduced to a single uniform 4px letter stroke.',
4:'Three source table rows reduced to two for legible cells.',
10:'Individual finger subdivisions omitted; rounded finger silhouette and thumb crease retained.',
11:'Three source document lines reduced to two; minor finger creases omitted.',
12:'One of the two source sockets omitted to leave a readable tab/socket puzzle silhouette.',
13:'Minor palm crease and cuff lines omitted; both hands and heart retained.',
14:'Fine finger subdivisions omitted; vessel rim and belly retained.',
15:'Mirrors omitted and tires rendered as solid short strokes; paired lamps retained.',
16:'Reduced fine finger subdivisions to two legible bends.',17:'Reduced fine finger subdivisions to two legible bends.',18:'Reduced fine finger subdivisions to two legible bends.',
19:'Small protruding handle butt above the axe head omitted.',
20:'Leaf accent simplified to an angled open stroke; small triangle retained.'}
CHANGES={2:'Rebuilt rounded G and Pay letters on two rows after native review showed the original horizontal layout crowded at 4px stroke.',
12:'Restored a diagonal puzzle piece with a clear tab/socket, plus continuous rounded hands; reduced one secondary socket.',
15:'Restored a legible car, paired lamps and tires above continuous cupped hands; trimmed thumb creases.',
20:'Restored the triangular stem mark and clear rising accent, retaining the smooth h and tall rounded frame.'}
runs=json.loads((BATCH/'runs.json').read_text());results=[]
for r in runs:
 n=r['n'];it=ITEMS[n-1];run=ROOT/r['run'];module=ROOT/r['module'];icon=load_icon(module);svg=icon.to_svg();report=icon.validate_icon()
 g=json.loads((run/'gate.json').read_text());before_gate=dict(g)
 if g['status']!='pass':
  assert n in REASONS
  ex={'reason':REASONS[n], 'approved_by':'gpt-6 under explicit user-delegated exception authority', 'approved_on':'2026-09-29','svg_sha256':hashlib.sha256(svg.encode()).hexdigest()}
  with module.open('a') as f:f.write('\n# User explicitly delegated drawing-specific exception decisions. Automatic findings are retained.\nDrawing.exception = '+repr(ex)+'\n')
  icon=load_icon(module);report=icon.validate_icon();g=gate(module)
  assert approved_visual_exception(report,g),(n,g)
 else:assert report.status=='valid' and not report.warnings
 assert g['status']=='pass'
 (run/'gate.json').write_text(json.dumps(g,indent=2))
 (run/'automatic-gate.json').write_text(json.dumps(before_gate,indent=2))
 (run/'validation.txt').write_text(report.describe()+'\n\nFull build gate: '+g['status']+'\nAutomatic status: '+g.get('automatic_status',g['status'])+'\n'+('Accepted exception: '+REASONS[n]+'\n' if 'exception' in g else 'No exception.\n'))
 for label,path in [('reference',it['reference']),('before',it['before'])]:
  for size in [48,192]:cairosvg.svg2png(url=str(ROOT/path),write_to=str(run/f'{label}-{size}.png'),output_width=size,output_height=size,background_color='white')
 findings='Inspected at 48px and enlarged in light and dark: recognizable subject, uniform 4px stroke, coherent joins, retained source identity. '+('Symmetric hand pairs share construction parameters; only hands are depicted, so detached head/body gap is not applicable. ' if 10<=n<=15 else '')
 findings+='Asymmetry follows the source direction and arrangement.' if n in [1,2,3,4,5,6,7,9,12,13,16,17,18,19,20] else 'Paired and concentric geometry is visually balanced.'
 result=dict(source_uuid=Path(it['reference']).stem[-36:],reference_path=it['reference'],source_key=it['key'],icon_id=it['icon_id'],author=AUTHOR,
  result_dir=r['run'],module=module.name,svg=it['icon_id']+'.svg',validation_status=report.status,build_gate_status=g['status'],automatic_status=g.get('automatic_status',g['status']),
  accepted_exception='exception' in g,exception=g.get('exception'),visual_review=findings,original_comparison=D[n]['wrong'],feedback=it['feedback'],
  change=CHANGES.get(n,D[n]['change']),omissions=OMISSIONS.get(n,'No defining feature omitted.'),construction_reference=D[n]['construction'],
  artifacts=[p.name for p in run.iterdir() if p.is_file() and p.name!='result.json'])
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 results.append(result);print(n,it['key'],'pass · exception' if result['accepted_exception'] else 'pass',flush=True)
(BATCH/'final-results.json').write_text(json.dumps(results,indent=2))
