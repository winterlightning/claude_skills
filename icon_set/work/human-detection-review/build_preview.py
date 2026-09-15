"""Read-only, pose-reviewed part detections; never modifies authored icons."""
from pathlib import Path
import json, hashlib, html, math, sys, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from icon_set.model.primitives import primitive_from_dict
from icon_set.renderers.svg import _move_to,_segment
OUT=Path(__file__).resolve().parent
rows=json.loads((OUT/'source-models.json').read_text())
# Each entry is (head geometry, torso geometry, neck endpoint). Lists denote silhouettes.
# These choices follow visual review and the existing source geometry, not nearest-object guessing.
specs={
1:[('head','torso','start')],11:[('head',['shoulders','waist-left','waist-right','diaper-band'],None)],
15:[('head','torso',None)],16:[('head','torso','start')],22:[('head','paddler-1','end')],
26:[('head','torso-1','start')],27:[('head','person-2','start')],30:[('head','rider-1','start')],
34:[('adult-head','adult-back-1','start'),('baby-head','baby-body',None)],35:[('head','torso-0','start')],
42:[('head','body-0','start')],47:[('head','body','start')],52:[('face','body',None)],
60:[('central-head','central-bust',None),('left-head',['left-shoulder','left-base'],None),('right-head',['right-shoulder','right-base'],None)],
66:[('face','shoulders',None)],68:[('head','torso','start')],69:[('skier-head','skier-1','start')],70:[('rider-head','rider-1','start')],
75:[('head','torso','start')],77:[('head','rider-2','end')],79:[('head','torso','start')],80:[('head','torso','start')],
90:[('front-head','front-body',None),(['rear-crown','rear-jaw'],['rear-neck','rear-shoulder','rear-side','rear-base'],None)],
93:[('head',['body-2','body-3','body-4','body-5'],None)],96:[('left-head','left-body-0','start'),('right-head','right-body-0','start')],
99:[('head','torso-1','start')],100:[('person-head','person-body-1','start')],
101:[('carrier-head','carrier-1','start'),('director-head','director-1','start')],
102:[('head','body','start')],103:[('head','body-1','start')],104:[('head','person-1','start')],
105:[('person-head','person-torso-1','start')],106:[('head','body-leg-1','start')],107:[('person-head','person-torso-1','start')],
114:[('head','body-2','start')],118:[('head','torso','start')],121:[('head','rider-1','start')],125:[('head','torso','start')],
131:[('head','torso','start')],132:[('head',['torso-0','torso-1'],'start')],133:[('face','torso',None)],
137:[('head','rider-1','start')],138:[('head','torso-0','start')],139:[('head','body-2','end')],142:[('head','torso','start')],
144:[],149:[('head','rider-1','start')],150:[('person-head','person-body-1','start')],152:[('head','body',None)],
153:[('head','body-1','start')],154:[('head','body-1','start')],158:[('head','body-1','start')],
167:[('left-head','left-torso','start'),('right-head','right-torso','start')],
168:[('front-head','front-body',None),(['rear-crown','rear-jaw'],['rear-neck','rear-shoulder','rear-side','rear-base'],None)],
169:[('front-head','front-body',None),(['rear-crown','rear-jaw'],['rear-neck','rear-shoulder','rear-side','rear-base'],None)],
173:[('head','body-1','start')],174:[('person-head','person-body-1','start')],175:[('head','body-1','start')],176:[('head','body-1','start')],
177:[('groom-head','groom-body',None),('bride-head','bride-body',None)],180:[('head','gown',None)]}
notes={
11:'Outlined baby body: shoulder and waist edges are highlighted. No single torso axis exists.',
15:'Ambiguous anatomy: the path named torso forms an outline. Review the body region before choosing a neck junction.',
27:'Proposed neck at the bend between the extended arm and descending torso. Please confirm the pose.',
34:'Adult back is identifiable. Baby body overlaps the adult arm and needs manual interpretation.',
52:'Human-faced sphinx with an animal body; shown for completeness. Not a detached stick-figure torso.',
60:'Three small busts; side heads are partial arcs. No single torso axis.',
66:'Face and shoulder arc only. This is a bust, not a stick figure.',
77:'Proposed upper torso is the sloping stroke from the seated hip to the upper bend; its endpoint is the neck candidate.',
90:'Two busts. Rear head and shoulder share one contour; highlighted by individual segments.',
93:'Body is an outline, not a single centerline. Seat belt is excluded from the torso region.',
101:'Carrier torso is separate. Director torso and leg share one unsplit vertical stroke; a torso-only segment is not yet available.',
114:'Tucked/inverted pose: proposed torso runs leftward from the arm junction. Confirm this reading before any repair.',
133:'Uniformed bust: face arc and clothing outline. No stick-figure torso axis.',
139:'Unusual seated pose: the last body segment is the torso candidate; confirm the neck endpoint.',
144:'Only legs, shoe and starting block are drawn. No head or torso detected; nothing has been invented.',
152:'Outlined torso. Shoulder edges, waist and body sides are highlighted as one region.',
168:'Two busts. Rear head and body are sections of one continuous contour.',
169:'Two busts. Rear head and body are sections of one continuous contour.',
177:'Two tiny outlined figures; highlight body outlines, not inferred torso axes.',
180:'Head and gown outline. Clothing defines the body region; no single torso line.'}
uncertain={15,27,34,77,101,114,139,144}
feedback={
52: ('Detection rejected', 'incorrect', 'User flagged this detection as wrong. Previous head/body pairing withdrawn; a replacement has not been identified.'),
60: ('Detection rejected', 'incorrect', 'User flagged this detection as wrong. Previous three head/body pairings withdrawn; re-detect the people before proceeding.'),
66: ('Different torso handling', 'unsure', 'User identified a different torso type. Face and shoulder arc form a bust; handle shoulder geometry separately from a stick-figure torso line.'),
15: ('Different torso handling', 'incorrect', 'User flagged this detection. The previous torso outline is not an accepted torso detection; re-identify the anatomy before choosing a neck junction.'),
11: ('Different torso handling', 'incorrect', 'User flagged this detection. The outlined baby body needs separate anatomical handling; the previous shoulder/waist selection is withdrawn.'),
}
results=[]
for x in rows:
 n=x['number'];record=x['record'];r=x['row'];ps={p['element_id']:p for p in record['primitives']};cs={c['contour_id']:c for c in record['contours']}
 def ids(ref):
  refs=[ref] if isinstance(ref,str) else ref
  return [p for name in refs for p in (cs[name]['members'] if name in cs else [name])]
 figures=[]
 for j,(h,t,junction) in enumerate(specs[n],1):
  hi,ti=ids(h),ids(t)
  assert all(p in ps for p in hi+ti),(n,hi,ti)
  neck=ps[ti[0]][junction] if junction else None
  figures.append(dict(figure_id=f'person-{j}',head=h,torso=t,head_members=hi,torso_members=ti,torso_junction=junction,neck=neck))
 source=ROOT/'icon_set/dist/failed/solo48'/r['svg']; raw=source.read_text(); sha=hashlib.sha256(source.read_bytes()).hexdigest()
 assert sha==r['svg_sha256'],f'Gallery snapshot mismatch: {r["icon_id"]}'
 root=ET.fromstring(raw); original_paths=[e.attrib['d'] for e in root.iter() if e.tag.endswith('path')]
 # Exact authored paths are retained in SVG; annotations are a separate layer.
 from icon_set.model.primitives import ResolvedDrawing,Contour
 from icon_set.renderers.svg import build_paths
 drawing=ResolvedDrawing(tuple(primitive_from_dict(p) for p in ps.values()),tuple(Contour(c['contour_id'],tuple(c['members']),c['closed']) for c in cs.values()),(),())
 assert [p['d'] for p in build_paths(drawing)]==original_paths, f'Model differs from gallery: {r["icon_id"]}'
 silhouette=any(f['torso_junction'] is None for f in figures)
 status='Needs interpretation' if n in uncertain else ('Body outline / bust' if silhouette else 'Torso identified')
 note=notes.get(n,'Head outline and upper torso identified from the existing geometry. The pink point marks the proposed neck endpoint.')
 prior_figures=[]
 review='unreviewed'
 if n in feedback:
  status,review,note=feedback[n]
  prior_figures=figures
  figures=[]
 results.append(dict(number=n,icon_id=r['icon_id'],source_path=r['source_path'],svg_sha256=sha,status=status,note=note,figures=figures,original_svg=raw,
  primitive_paths={k:_move_to(primitive_from_dict(p))+_segment(primitive_from_dict(p)) for k,p in ps.items()},
  targets={'centerline_gap':8,'ink_gap':4} if status=='Torso identified' else None,
  review=review,review_revision=1 if n in feedback else 0,
  user_feedback=note if n in feedback else None,previous_figures=prior_figures))
(OUT/'detections.json').write_text(json.dumps([{k:v for k,v in x.items() if k not in ('original_svg','primitive_paths')} for x in results],indent=2)+'\n')
payload=json.dumps(results).replace('</','<\\/')
template=(OUT/'template.html').read_text()
(OUT/'index.html').write_text(template.replace('__DATA__',payload))
print(json.dumps({'icons':len(results),'figures':sum(len(x['figures']) for x in results),'statuses':{s:sum(x['status']==s for x in results) for s in sorted(set(x['status'] for x in results))}},indent=2))
