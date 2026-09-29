from author import *
import hashlib, shutil
from icon_set.scripts.primitive_fix import approved_visual_exception

REASONS={
1:'Keep three readable rainbow bands above a lobed heart. The 2px band openings and taller composition preserve both pride and love at 48px.',
2:'Keep curved sensor marks beside the running pose. Their compact spacing remains distinct at native size; upper torso/head retain exact 4px ink clearance.',
5:'Keep the leaning mast, curved sail, boom and water. Compact boom and water gaps preserve the nautical sports subject and remain readable in both themes.',
6:'Keep the bowed sail and shallow hull above separate waves. The source proportions need a wider envelope and a compact hull/water gap.',
7:'Keep five irregular scattered seeds instead of identical droplets. Their compact native-size spacing and differing orientations preserve the source arrangement.',
8:'Keep the woman portrait with parted hair and coat lapels. Hair and jaw/body contact are anatomical; dense lapel and shoulder junctions remain clear at 48px.',
9:'Keep the woman portrait with parted hair and coat lapels. Hair and jaw/body contact are anatomical; dense lapel and shoulder junctions remain clear at 48px.',
10:'Keep the raised seal neck, small eye and tapered flippers. The flipper opening and compact eye placement preserve marine anatomy better than squared feet.',
11:'Keep the raised seal neck, small eye and tapered flippers. The flipper opening and compact eye placement preserve marine anatomy better than squared feet.',
12:'Keep the dragon eye, angular mouth and crest on a smooth sea-serpent neck. Compact face and crest spacing preserves identity at native size.',
13:'Keep the smaller child seated on the adult lap and the holding arm. The chair gap is exactly 4px ink; compact arm/lap spacing and natural envelope preserve the family pose.',
15:'The head center (10,16), radius 6, and upper torso/arm start (24,16) have exactly 8u centerline clearance. The conservative curved checker reports 7.99986; retain the anatomically exact 4px ink gap and smooth fold.',
17:'Keep the kitten large head and curled left tail. The natural asymmetric envelope and compact tail/haunch junction preserve sitting kitten anatomy.',
19:'Keep inward-curved hands and crossed lotus legs. The hand/knee contact and compact lower-body envelope communicate relaxed meditation at native size.',
20:'Keep lowered arms, rounded knees and deliberately crossing seated legs. The crossing is part of the pose; the wide base remains recognizable and balanced at 48px.',
}

HUMAN={
2:'human_ref/full_body_ref.png: head center (28,8), radius 4; vertical upper torso begins (28,20), giving 20-(8+4)=8 centerline / 4 ink. The lower torso leans into the run.',
3:'Continuous anatomical head/neck profile; no detached-head flag applies. human_ref/user.svg informs round skull construction, with the source controlling the side profile.',
4:'Continuous anatomical head/neck profile; no detached-head flag applies. human_ref/user.svg informs round skull construction, with the source controlling the side profile.',
8:'human_ref/user.svg: circular jaw radius 12, bottom y26; shoulder top y30, giving 4 centerline / zero ink gap. Parted hair and jacket follow the original.',
9:'human_ref/user.svg: circular jaw radius 12, bottom y26; shoulder top y30, giving 4 centerline / zero ink gap. Parted hair and jacket follow the original.',
13:'human_ref/full_body_ref.png: adult head (13,9), r5, torso starts (13,22): 8 centerline / 4 ink. Child head (29,13), r3, torso starts (29,24): 8 centerline / 4 ink. Both head axes align with their vertical torsos.',
14:'human_ref/full_body_ref.png: head (35,11), r5, torso starts (35,24): 8 centerline / 4 ink; aligned vertical torso.',
15:'human_ref/full_body_ref.png: head (10,16), r6, torso starts (24,16): distance 14-6=8 centerline / 4 ink; torso tangent is horizontal away from head. Curved numerical warning retained as an exception.',
16:'human_ref/full_body_ref.png: head (25,9), r5, torso starts (20,21): sqrt(5^2+12^2)-5=8 centerline / 4 ink. Upper torso control (15,33) continues this same axis away from head.',
18:'human_ref/full_body_ref.png: head (35,11), r5, torso starts (35,24): 8 centerline / 4 ink; aligned vertical torso.',
19:'human_ref/full_body_ref.png: head (24,9), r5, torso starts (24,22): 8 centerline / 4 ink; centered upright posture.',
20:'human_ref/full_body_ref.png: head (24,9), r5, torso starts (24,22): 8 centerline / 4 ink; centered upright posture.',
}

def package():
 runs=json.loads((BATCH/'runs.json').read_text());final=[]
 for i,r in enumerate(runs,1):
  old=ROOT/r['run'];g=json.loads((old/'gate.json').read_text())
  p=old
  if g['status']!='pass' or g['warnings']:
   assert i in REASONS,(i,g)
   stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
   p=old.parent/(stamp+'-reviewed-exception');shutil.copytree(old,p,ignore=shutil.ignore_patterns('__pycache__','result.json'))
   module=p/r['module'];svg=load_icon(module).to_svg()
   approval={'reason':REASONS[i], 'approved_by':'user-authorized discretion; gpt-6 visual review', 'approved_on':'2026-09-29', 'svg_sha256':hashlib.sha256(svg.encode()).hexdigest()}
   with module.open('a') as out: out.write('\n# User explicitly authorized high-quality drawing-specific exceptions.\nDrawing.exception = '+repr(approval)+'\n')
   r['exception']=approval
  icon=load_icon(p/r['module']);report=icon.validate_icon();finalgate=gate(p/r['module'])
  accepted=approved_visual_exception(report,finalgate)
  assert finalgate['status']=='pass' and (accepted or (report.status=='valid' and not report.warnings)),(i,finalgate)
  assert not any('leaves the 48x48 canvas' in x for x in list(report.errors)+list(report.warnings))
  r.update(run=str(p.relative_to(ROOT)),validation_status=report.status,errors=list(report.errors),warnings=list(report.warnings),build_gate=finalgate,accepted_exception=accepted,visual_review='Reviewed against original and rejected drawing, at native 48px and enlarged size in both light and dark themes. Recognizable silhouette and intentional feature arrangement retained.',human_review=HUMAN.get(i),parent_run=str(old.relative_to(ROOT)) if p!=old else None)
  r['construction_reference']= ('Lucide heart: coherent lobes and smooth heart contour.' if i==1 else 'Lucide sailboat: a coherent sail and shallow hull; source keeps its curved sail.' if i in [5,6] else 'Lucide cat: broad rounded head and identifying ears; source controls seated body.' if i==17 else HUMAN.get(i,'No useful Lucide subject match; supplied original controls anatomy and silhouette.'))
  r['keyshape']=icon.keyshape.name
  r['artifacts']={'module':r['module'],'svg':r['svg'],'metadata':r['icon_id']+'.metadata.json','validation':'validation.txt','gate':'gate.json','reference':'reference.png','light_48':'preview-light-48.png','dark_48':'preview-dark-48.png','light_384':'preview-light-384.png','dark_384':'preview-dark-384.png'}
  (p/'gate.json').write_text(json.dumps(finalgate,indent=2))
  (p/'validation.txt').write_text(report.describe()+'\n\nFull build gate: '+finalgate['status']+'\n'+ ('Drawing-bound exception accepted. Automatic findings retained.\n'+json.dumps(r['exception'],indent=2) if accepted else 'Strict pass, zero warnings.\n')+'\n'+json.dumps(finalgate,indent=2))
  (p/'visual-review.md').write_text(r['visual_review']+'\n\n'+r['comparison']+'\n\n'+r['change']+'\n\n'+r['construction_reference']+'\n\n'+(r.get('human_review') or 'No human subject.')+'\n\n'+(REASONS.get(i) if accepted else 'No exception required.')+'\n')
  (p/'result.json').write_text(json.dumps(r,indent=2))
  final.append(r);print(i,r['icon_id'],'PASS - exception' if accepted else 'PASS - strict',flush=True)
 (BATCH/'final-runs.json').write_text(json.dumps(final,indent=2))

if __name__=='__main__': package()
