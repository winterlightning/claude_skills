from pathlib import Path
import json,textwrap,sys
from icon_set.scripts.primitive_fix import load_icon,render_previews
AUTHOR='gpt-6'
RUN='20260924T150246Z-thuan-redraw'
ROOT=Path('icon_set/work/primitive-fix-thuan/batch-20260924T150246Z-thuan-mac')
claims=[Path(p) for p in json.loads((ROOT/'claims.json').read_text())]
# Each item retains its exact original source ID and path in metadata and module.
SOURCE_ICON_ID=[next((p/'reference').glob('*.svg')).stem[-36:] for p in claims]
SOURCE_PATH=[str(next((p/'reference').glob('*.svg'))) for p in claims]
HELPERS='''
        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
D=[]
def add(keyshape,plan,ref,omissions,body):D.append(dict(keyshape=keyshape,plan=plan,ref=ref,omissions=omissions,body=textwrap.dedent(body)))
add('SQUARE','Broad crescent curls around the lower-left of a separate upright five-point star. Directional crescent follows the source.','moon and star: coherent crescent curves and five-point contour','None.', '''
path('moon',(24,6),[('C',(6,24),(14,6),(6,14)),('C',(24,42),(6,34),(14,42)),('C',(42,34),(32,42),(38,39)),('C',(15,24),(27,42),(15,34)),('C',(24,6),(15,16),(18,10))],True)
poly('star',(33,9),(36,16),(42,16),(37,21),(39,26),(33,23),(27,26),(29,21),(26,16),(31,16),closed=True)
''')
add('SQUARE','Crossed short swords with equal blade widths, pointed tips, straight guards and rounded outlined grips. Back blade is occluded at the crossing.','swords: scoped crossing and paired guards; pill: rounded grips','Blade center ridges omitted.', '''
path('front',(12,30),[('L',(34,8)),('L',(42,6)),('L',(40,14)),('L',(18,36)),('L',(12,42)),('C',(6,36),(8,42),(6,40)),('L',(12,30))],True)
path('back-upper',(18,24),[('L',(8,14)),('L',(6,6)),('L',(14,8)),('L',(24,18))]);join('back-upper','front')
path('back-grip',(24,30),[('L',(36,42)),('C',(42,36),(40,42),(42,40)),('L',(30,24))]);join('back-grip','front')
line('guard-front',(8,26),(22,40));join('guard-front','front')
line('guard-back',(26,40),(40,26));join('guard-back','back-grip')
''')
add('SQUARE','Five equal circular beads on a U-shaped cord; larger bead openings replace the tiny rejected loops.','No useful exact Lucide necklace match; source supplies five beads and U arrangement.','U is deepened to fit five beads and strict clearance.', '''
centers=((10,10),(10,28),(24,38),(38,28),(38,10));radius=4
for i,(x,y) in enumerate(centers):ellipse(f'bead-{i}',x,y,radius,radius)
links=(((10,14),(10,24)),((14,28),(20,38)),((28,38),(34,28)),((38,24),(38,14)))
for i,(a,b) in enumerate(links):
 line(f'cord-{i}',a,b);join(f'cord-{i}',f'bead-{i}');join(f'cord-{i}',f'bead-{i+1}')
''')
add('VRECT_L','Upright diagonal capsule with matching rounded ends, parallel sides and a centered transverse seam.','pill: paired rounded ends and perpendicular seam','None; steeper source tilt restored.', '''
path('capsule',(21,9),[('C',(30,4),(23,5),(26,4)),('A',(40,14),10,10,True),('C',(39,19),(40,16),(40,17)),('L',(27,39)),('C',(18,44),(25,43),(22,44)),('A',(8,34),10,10,True),('C',(9,29),(8,32),(8,31)),('L',(21,9))],True)
line('seam',(15,19),(33,29));join('seam','capsule')
''')
add('SQUARE','Diagonal chalk stick with rounded upper end, beveled lower end and a detached horizontal chalk mark.','pencil and pill: coherent diagonal body and round terminal','None; missing chalk mark restored.', '''
path('chalk',(6,34),[('C',(10,26),(6,31),(7,28)),('L',(32,6)),('L',(36,6)),('C',(42,12),(39,6),(42,9)),('L',(18,32)),('L',(6,34))],True)
line('bevel',(10,26),(18,32));join('bevel','chalk')
line('mark',(18,42),(36,42))
''')
add('SQUARE','Diagonal toothbrush with a rounded outlined handle and two evenly spaced bristles on its inner head edge.','brush and pill: parallel diagonal tool edges with rounded terminal','Two separated bristle strokes retained; dense extra bristles omitted.', '''
path('body',(6,36),[('L',(30,12)),('C',(42,12),(34,8),(38,8)),('L',(12,42)),('A',(6,36),6,6,True)],True)
for i,(x,y) in enumerate(((22,20),(30,12))):
 line(f'bristle-{i}',(x,y),(x-6,y-6));join(f'bristle-{i}','body')
''')
add('SQUARE','Diagonal satellite with rounded main capsule, two broad solar panels and a curved dish at the lower-left end.','satellite: paired diagonal panels, body and attached dish','Fine panel divisions and radiating waves omitted to protect the body/dish spacing.', '''
path('body',(20,22),[('L',(30,12)),('C',(36,18),(34,8),(40,14)),('L',(26,28)),('L',(20,22))],True)
poly('panel-left',(20,22),(10,12),(16,6),(26,16));join('panel-left','body')
poly('panel-right',(30,24),(36,30),(42,24),(36,18));join('panel-right','body')
path('dish',(6,30),[('C',(12,30),(8,28),(10,28)),('C',(18,42),(17,33),(20,38)),('L',(6,30))],True)
line('dish-link',(20,22),(12,30));join('dish-link','body');join('dish-link','panel-left');join('dish-link','dish')
''')
add('SQUARE','Broad scraper blade with rounded shoulders and a diagonal rounded grip. Blade and grip share a real shoulder seam.','brush and pill: smooth diagonal grip; source governs broad blade','Fine blade band omitted.', '''
path('blade',(6,28),[('L',(16,18)),('C',(22,18),(18,16),(20,16)),('L',(30,26)),('C',(30,32),(32,28),(32,30)),('L',(20,42)),('L',(6,28))],True)
path('handle',(22,18),[('L',(30,8)),('C',(36,6),(32,6),(34,6)),('A',(42,12),6,6,True),('C',(40,18),(42,14),(42,16)),('L',(30,26))]);join('handle','blade')
''')
add('SQUARE','Diagonal shovel with a softly rounded digging blade, long shaft and broad open D grip.','shovel: diagonal shaft, distinct blade and D-grip','Blade ridge omitted.', '''
path('blade',(6,42),[('L',(6,31)),('C',(10,24),(6,28),(8,26)),('L',(14,20)),('L',(28,34)),('L',(24,38)),('C',(17,42),(22,40),(20,42)),('L',(6,42))],True)
line('shaft',(18,30),(33,15));join('shaft','blade')
path('grip',(26,10),[('C',(32,6),(28,7),(30,6)),('C',(42,16),(38,6),(42,10)),('L',(40,22)),('L',(26,10))],True);join('shaft','grip')
''')
add('SQUARE','Five-point magic star atop a diagonal wand with an outlined rounded handle.','star and wand: star outline and diagonal shaft; pill: rounded handle','None.', '''
poly('star',(26,6),(32,14),(42,12),(38,22),(42,32),(30,30),(24,40),(20,28),(12,24),(23,19),closed=True)
path('handle',(20,28),[('L',(6,36)),('C',(13,42),(6,42),(10,42)),('L',(27,35))]);join('handle','star')
''')
add('HRECT_M','Complete battery outline with a right terminal and one diagonal disabling slash, without arrow-like corners.','battery: continuous outline and right terminal','None.', '''
path('battery',(4,38),[('L',(4,14)),('A',(8,10),4,4,True),('L',(36,10)),('L',(36,34)),('A',(32,38),4,4,True),('L',(4,38))],True)
line('slash',(4,38),(36,10));join('slash','battery')
poly('terminal',(36,22),(44,22),(44,30),(36,30));join('terminal','battery')
''')
add('HRECT_L','Smooth outer ear with a round hearing device and two evenly separated sound waves.','ear: continuous helix and lower lobe; human reference checked for consistent rounded anatomy','Interior canal curl omitted to keep the hearing device and waves clear.', '''
path('ear',(4,12),[('C',(14,8),(5,9),(8,8)),('C',(24,18),(21,8),(24,11)),('C',(18,31),(24,25),(20,27)),('C',(14,40),(17,36),(18,40)),('C',(4,37),(8,40),(4,39))])
ellipse('device',8,24,4,4)
path('wave-inner',(33,18),[('C',(35,24),(34,20),(35,22)),('C',(33,30),(35,26),(34,28))])
path('wave-outer',(40,8),[('C',(44,24),(43,13),(44,18)),('C',(40,40),(44,30),(43,35))])
''')
add('SQUARE','Exploration rover with two full circular wheels, a low deck, small equipment housing and a tall capped antenna.','tractor: full wheels below chassis and clear vehicle silhouette','Tiny wheel hubs and secondary sloping deck details omitted.', '''
box('deck',6,20,42,30,2)
for i,x in enumerate((12,36)):
 ellipse(f'wheel-{i}',x,36,6,6);join(f'wheel-{i}','deck')
poly('equipment',(10,20),(12,12),(18,12),(18,20));join('equipment','deck')
ellipse('antenna-tip',28,8,2,2)
line('antenna',(28,10),(28,20));join('antenna','antenna-tip');join('antenna','deck')
''')
add('SQUARE','Flared console rises behind a broad gamepad with rounded grips and its source horizontal control mark.','gamepad-2: rounded grips and centered controls','Small console inset ridge omitted; defining flared silhouette retained.', '''
path('console',(20,22),[('L',(18,8)),('C',(32,6),(24,6),(28,6)),('L',(42,6)),('C',(42,42),(37,21),(37,33)),('L',(28,42))])
path('pad',(12,22),[('L',(26,22)),('C',(30,28),(29,22),(30,24)),('L',(32,39)),('C',(28,42),(32,42),(30,42)),('L',(24,40)),('L',(14,40)),('L',(10,42)),('C',(6,39),(8,42),(6,42)),('L',(8,28)),('C',(12,22),(8,24),(9,22))],True);join('console','pad')
line('control',(17,31),(21,31))
''')
add('VRECT_L','Six grape regions form a tapered bunch below a pointed leaf; shared junctions preserve the clustered arrangement.','grape: repeated rounded fruit regions and tapered bunch','Small curling stem omitted.', '''
path('bunch',(8,22),[('C',(19,21),(8,14),(17,13)),('C',(24,14),(19,17),(20,14)),('C',(29,21),(28,14),(29,17)),('C',(40,22),(31,13),(40,14)),('C',(36,32),(40,27),(39,30)),('C',(30,36),(37,36),(34,38)),('C',(24,44),(30,42),(28,44)),('C',(18,36),(20,44),(18,42)),('C',(12,32),(14,38),(11,36)),('C',(8,22),(9,30),(8,27))],True)
path('leaf',(24,14),[('C',(40,4),(24,6),(32,4)),('C',(24,14),(40,11),(32,14))],True);join('leaf','bunch')
path('top-seams',(19,21),[('C',(18,28),(20,24),(20,26)),('C',(30,28),(21,33),(27,33)),('C',(29,21),(28,26),(28,24))]);join('top-seams','bunch')
path('lower-seam',(12,32),[('C',(18,28),(12,29),(15,28)),('C',(18,36),(20,31),(20,34))]);join('lower-seam','bunch');join('lower-seam','top-seams')
path('right-seam',(36,32),[('C',(30,28),(36,29),(33,28)),('C',(30,36),(28,31),(28,34))]);join('right-seam','bunch');join('right-seam','top-seams')
''')
add('CIRCLE','Round happy face with curved closed eyes, a true curved smile and a small rounded tongue below it.','Shared human_ref/user.svg: circular head construction; no useful exact Lucide tongue-face match','None; head-only icon has no body-gap requirement.', '''
ellipse('face',24,24,20,20)
for i,x in enumerate((18,30)):
 path(f'eye-{i}',(x-2,17),[('A',(x+2,17),2,2,True)])
path('smile',(14,25),[('C',(20,27),(15,26),(17,27)),('C',(28,27),(22,28),(26,28)),('C',(34,25),(31,27),(33,26))])
path('tongue',(20,27),[('L',(20,31)),('A',(28,31),4,4,False),('L',(28,27))]);join('tongue','smile')
''')
add('HRECT_L','Cheese wedge with a curved rind, shallow sloped top seam and two open circular holes.','No useful local Lucide cheese match; source governs wedge and round perforations','Three holes reduced to two; small edge bite omitted for clearance.', '''
path('wedge',(4,18),[('L',(26,8)),('C',(44,14),(34,8),(40,10)),('L',(44,40)),('L',(4,40)),('L',(4,18))],True)
line('top-seam',(4,18),(44,14));join('top-seam','wedge')
for i,(x,y) in enumerate(((16,28),(32,27))):ellipse(f'hole-{i}',x,y,3,3)
''')
add('SQUARE','House with a doorway shares a baseline with a surrounding clockwise renewal arrow.','house and rotate-cw: closed roof/body and continuous circular arrow','Roof lowered to leave clearance beneath the arrowhead.', '''
path('renewal-left',(10,42),[('C',(6,26),(6,38),(6,32)),('C',(24,10),(6,16),(14,10)),('C',(31,12),(27,10),(29,11))])
poly('arrowhead',(25,6),(31,12),(25,18));join('arrowhead','renewal-left')
path('renewal-right',(40,20),[('C',(42,26),(41,22),(42,24)),('C',(38,42),(42,34),(41,39))])
line('baseline',(10,42),(38,42));join('baseline','renewal-left');join('baseline','renewal-right')
poly('house',(12,42),(12,34),(24,26),(36,34),(36,42));join('house','baseline')
poly('door',(20,42),(20,34),(28,34),(28,42));join('door','baseline')
''')
add('SQUARE','Child cycle with two full wheels, a rounded high-back seat, connecting frame and small front basket below a raised handlebar.','bike: paired full circular wheels; source governs child seat and basket','Wheel hubs omitted.', '''
for name,x in [('rear',13),('front',35)]:ellipse(name,x,35,7,7)
path('seat',(8,28),[('L',(8,10)),('A',(12,6),4,4,True),('A',(16,10),4,4,True),('L',(16,20)),('L',(21,20)),('A',(24,23),3,3,True),('L',(24,25)),('A',(21,28),3,3,True),('L',(8,28))],True);join('seat','rear')
poly('frame',(24,25),(34,24),(35,28));join('frame','seat');join('frame','front')
poly('handlebar',(28,6),(34,6),(34,24));join('handlebar','frame')
poly('basket',(34,14),(42,14),(40,22),(34,22));join('basket','handlebar')
''')
add('VRECT_L','Blackberry with rounded outer drupelets, central fruit cell, lower paired lobes and one pointed leaf.','grape: overlapping rounded regions; source governs elongated blackberry cluster','Fine extra cell boundaries and tiny stem curl omitted.', '''
path('berry',(24,14),[('C',(38,22),(30,12),(38,14)),('C',(35,34),(40,26),(40,31)),('C',(24,44),(35,40),(31,44)),('C',(13,34),(16,44),(12,40)),('C',(8,25),(8,33),(8,29)),('C',(24,14),(8,17),(15,12))],True)
path('leaf',(24,14),[('C',(40,4),(24,6),(32,4)),('C',(24,14),(40,11),(32,14))],True);join('leaf','berry')
path('center',(24,14),[('A',(30,22),6,8,True),('A',(24,30),6,8,True),('A',(18,22),6,8,True),('A',(24,14),6,8,True)],True);join('center','berry')
path('left-seam',(8,25),[('C',(18,22),(12,30),(16,28))]);join('left-seam','berry');join('left-seam','center')
path('right-seam',(38,22),[('C',(30,22),(38,30),(32,29))]);join('right-seam','berry');join('right-seam','center')
path('lower-seam',(13,34),[('C',(24,30),(17,38),(22,36)),('C',(35,34),(26,36),(31,38))]);join('lower-seam','berry');join('lower-seam','center')
line('bottom-seam',(24,30),(24,44));join('bottom-seam','center');join('bottom-seam','berry');join('bottom-seam','lower-seam')
''')

def generate(indices=None):
 records=[]
 for i,(claim,design) in enumerate(zip(claims,D)):
  item=json.loads((claim/'claim.json').read_text())['item']; ref=next((claim/'reference').glob('*.svg'))
  uuid=ref.stem[-36:];concept=ref.stem[:-37];ident=item['icon_id']
  out=Path('icon_set/work/primitive-make-ray')/uuid/RUN
  out.mkdir(parents=True,exist_ok=True)
  record={'index':i+1,'key':item['key'],'icon_id':ident,'source_uuid':uuid,'reference_path':str(ref),'concept':concept,'author':AUTHOR,'result_dir':str(out),**design}
  records.append(record)
  if indices is not None and i+1 not in indices: continue
  (out/f'{ident}.metadata.json').write_text(json.dumps({k:record[k] for k in ['concept','source_uuid','reference_path']},indent=2))
  module=out/(ident.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  code=f'''"""{design['plan']}\nKeyshape {design['keyshape']}: exact SOLO48 contract envelope.\nConstruction: {design['ref']}\nOmissions: {design['omissions']}\nFeedback: Bad stroke drawn. Fresh reference-based revision."""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR={AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id={ident!r}\n    keyshape=Keyshape.{design['keyshape']}\n    semantic_role='MAIN'\n    semantic_kind='noun'\n    category='objects'\n    aliases=()\n    keywords={tuple(ident.split('-'))!r}\n    def build(self):\n'''+HELPERS+textwrap.indent(design['body'],'        ')
  if module.exists():
   import shutil,time
   backup=out/'attempts'/str(time.time_ns());backup.mkdir(parents=True)
   for prior in out.iterdir():
    if prior.is_file():shutil.copy(prior,backup/prior.name)
  module.write_text(code)
  import cairosvg
  cairosvg.svg2png(url=str(ref),write_to=str(out/'reference.png'),output_width=384,output_height=384,background_color='white')
  try:
   icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
   (out/f'{ident}.svg').write_text(svg);(out/'validation.txt').write_text(report.describe());render_previews(svg,ident,48,out)
   print(i+1,ident,report.describe(),flush=True)
  except Exception as e: print(i+1,ident,'ERROR',repr(e),flush=True)
 ROOT.joinpath('drawings.json').write_text(json.dumps(records,indent=2))
if __name__=='__main__':generate({int(x) for x in sys.argv[1:]} if len(sys.argv)>1 else None)
