from pathlib import Path
import json,textwrap,sys
from icon_set.scripts.primitive_fix import load_icon,render_previews
AUTHOR='gpt-6'
RUN='20260924T-redraw-thuan-mac'
ROOT=Path('icon_set/work/primitive-fix-thuan/batch-20260924-thuan-mac')
claims=[Path(p) for p in ['icon_set/work/primitive-fix-thuan/solo__plover-standing-in-profile/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__angle-down/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__armadillo/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__arrow-bottom-symbol/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__arrow-thick-top-symbol/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__arrows-converging-on-a-horizontal-guide/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__arrows-toward-horizontal-divider/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__asthma-inhaler/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__balloon-dog-with-oval-twisted-segments/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__barbecue-fork-two-tines/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__barred-birdcage-with-a-round-top-knob/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__bench-lathe/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__binoculars/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__bladder-with-connecting-tubes/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__blank-face-wearing-cowboy-hat/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__book-open-e1dee87f/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__bottle-with-burning-wick/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__braille-book-batch-020-09/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__bulb-syringe/20260924T142441Z-thuan-mac', 'icon_set/work/primitive-fix-thuan/solo__calligraphy-nib-beside-ink-stroke/20260924T142441Z-thuan-mac']]
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
add('SQUARE','Shorebird with long sloping back, rounded head and breast, folded wing and two feet. Directional asymmetry follows reference.','bird: coherent sloping back and round breast','Tiny eye omitted to avoid crowding the head.', '''
path('bird',(6,34),[('L',(12,28)),('L',(22,18)),('C',(30,6),(23,10),(25,6)),('A',(38,14),8,8,True),('L',(42,16)),('L',(38,19)),('C',(30,33),(38,27),(35,31)),('C',(24,34),(28,34),(26,34)),('L',(6,34))],True)
path('wing',(12,28),[('C',(29,22),(23,30),(29,28))]);join('wing','bird')
poly('leg-left',(20,34),(20,42),(16,42));join('leg-left','bird')
poly('leg-right',(30,33),(32,42),(36,42));join('leg-right','bird')
''')
add('SQUARE','One diagonal shaft and a joined right-angle arrowhead; common endpoint removes the tiny spurious arc.','arrow-down-right: shared arrowhead vertex','None.', '''
poly('head',(20,42),(42,42),(42,20))
line('shaft',(6,6),(42,42));join('shaft','head')
''')
add('HRECT_L','Low domed shell with two curved bands, pointed head, ear, two feet and tapered tail.','No useful exact Lucide match; source silhouette and shared shell parameters.','Far-side feet omitted at native size.', '''
path('shell',(14,32),[('C',(15,22),(14,29),(14,25)),('C',(24,8),(17,13),(18,8)),('C',(34,12),(28,8),(32,9)),('C',(40,28),(38,17),(40,21)),('C',(32,32),(40,31),(36,32)),('L',(14,32))],True)
path('head',(15,22),[('L',(9,15)),('L',(9,22)),('L',(4,28)),('C',(14,32),(6,31),(10,32))]);join('head','shell')
path('band-one',(24,8),[('C',(24,24),(26,12),(26,18))]);join('band-one','shell')
path('band-two',(34,12),[('C',(34,24),(35,16),(35,20))]);join('band-two','shell')
poly('front-foot',(17,32),(15,40),(19,40));join('front-foot','shell')
poly('rear-foot',(31,32),(33,40),(37,40));join('rear-foot','shell')
path('tail',(40,28),[('C',(44,36),(40,33),(41,36))]);join('tail','shell')
''')
add('HRECT_M','Symmetric broad downward chevron, with one coherent rounded join.','chevron-down: mirrored two-segment contour','None; shallowest available horizontal keyshape selected.', '''
axis=24; half_width=20
poly('chevron',(axis-half_width,10),(axis,38),(axis+half_width,10))
''')
add('VRECT_L','Mirrored outlined up arrow with a broad head and softly rounded stem base.','arrow-big-up: continuous outline and rounded stem corners','None.', '''
path('arrow',(24,4),[('L',(40,24)),('L',(30,24)),('L',(30,41)),('A',(27,44),3,3,True),('L',(21,44)),('A',(18,41),3,3,True),('L',(18,24)),('L',(8,24)),('L',(24,4))],True)
''')
for index in range(2):
 add('SQUARE','Two vertically mirrored arrows point toward a detached horizontal guide. Longer shafts preserve reference proportions.','arrow-down-right and chevron-down: common arrow vertices; align-vertical-justify-center: central guide spacing','None.', '''
line('guide',(6,24),(42,24))
for side in (-1,1):
 y=lambda d:24+side*d
 name=f'arrow-{side}'
 poly(name,(17,y(15)),(24,y(8)),(31,y(15)))
 line(name+'-shaft',(24,y(18)),(24,y(8)));join(name,name+'-shaft')
''')
add('VRECT_L','Rounded L-shaped inhaler with a cap seam and separate mouthpiece seam.','cooking-pot: tangent rounded body corners','Tilt normalized upright to preserve grid and clear openings.', '''
path('body',(8,4),[('L',(24,4)),('L',(24,28)),('L',(36,28)),('A',(40,32),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(16,44)),('A',(8,36),8,8,True),('L',(8,4))],True)
line('cap',(8,12),(24,12));join('cap','body')
line('mouthpiece',(32,28),(32,44));join('mouthpiece','body')
''')
add('SQUARE','Balloon dog built from elongated oval lobes at shared twist junctions; rounded muzzle, ear, body, two legs and rising tail.','bone: smooth rounded lobes; source governs balloon arrangement','Far-side legs omitted as in source.', '''
# Each balloon lobe meets a true twist node; shared nodes own all attachments.
path('muzzle',(16,18),[('C',(6,14),(13,13),(6,10)),('C',(16,18),(6,20),(12,20))],True)
path('ear',(16,18),[('C',(16,6),(10,14),(10,6)),('C',(16,18),(22,6),(22,14))],True)
path('neck',(16,18),[('C',(22,29),(22,18),(25,23)),('C',(16,18),(16,27),(13,22))],True)
path('body',(22,29),[('C',(36,29),(25,23),(33,23)),('C',(22,29),(33,35),(25,35))],True)
path('front-leg',(22,29),[('C',(15,42),(23,36),(20,42)),('C',(22,29),(10,42),(15,32))],True)
path('rear-leg',(36,29),[('C',(39,42),(42,32),(44,42)),('C',(36,29),(34,42),(32,35))],True)
path('tail',(36,29),[('C',(42,16),(35,22),(38,16)),('C',(36,29),(42,23),(40,27))],True)
for a,b in [('muzzle','ear'),('muzzle','neck'),('ear','neck'),('neck','body'),('neck','front-leg'),('body','front-leg'),('body','rear-leg'),('body','tail'),('rear-leg','tail')]:join(a,b)
''')
add('SQUARE','Diagonal barbecue fork with equal parallel tines, rounded U bend and oval-ended handle.','syringe and pill: diagonal parallel sides and smooth end cap','None.', '''
path('tines',(34,6),[('L',(22,18)),('C',(22,26),(18,22),(18,24)),('C',(30,26),(25,29),(27,29)),('L',(42,14))])
line('shaft',(22,26),(17,31));join('shaft','tines')
path('handle',(13,27),[('L',(21,35)),('L',(16,40)),('C',(12,42),(15,41),(14,42)),('A',(6,36),6,6,True),('C',(8,32),(6,34),(7,33)),('L',(13,27))],True);join('shaft','handle')
''')
# Further drawings appended below.
add('VRECT_L','Rounded birdcage with a true circular knob, hanging stem, domed roof and three evenly spaced bars.','cooking-pot: continuous rounded enclosure; source governs dome and bars','Extra lower rail omitted to keep open bar cells.', '''
ellipse('knob',24,6,2,2)
line('stem',(24,8),(24,16));join('stem','knob')
path('cage',(8,28),[('A',(24,16),16,12,True),('A',(40,28),16,12,True),('L',(40,44)),('L',(8,44)),('L',(8,28))],True)
join('stem','cage')
line('roof-rail',(8,28),(40,28));join('roof-rail','cage')
for x in (16,24,32):
 name=f'bar-{x}';line(name,(x,28),(x,44));join(name,'roof-rail');join(name,'cage')
''')
add('HRECT_L','Bench lathe with rounded rectangular headstock, supported tailstock, spindle and bed.','cooking-pot: tangent rounded rectangular construction','Small spindle cap and foot recess omitted to preserve open gaps.', '''
box('bed',4,32,44,40,2)
path('headstock',(6,32),[('L',(6,11)),('A',(9,8),3,3,True),('L',(15,8)),('A',(18,11),3,3,True),('L',(18,32))]);join('headstock','bed')
box('tailstock',32,12,44,22,2)
line('spindle',(18,17),(32,17));join('spindle','headstock');join('spindle','tailstock')
line('support',(38,22),(38,32));join('support','tailstock');join('support','bed')
''')
add('HRECT_L','Two matched circular objectives and tapered barrels with rounded upper ends, joined by a horizontal bridge.','binoculars: mirrored barrels and bridge; source retains circular objectives','None.', '''
for side in (-1,1):
 x=lambda d:24+side*d
 name=f'barrel-{side}'
 # Separate coherent barrel outline joins the circular lens at its lateral extremes.
 ellipse('lens'+name,x(12),32,8,8)
 path(name,(x(20),32),[('L',(x(16),14)),('C',(x(10),8),(x(15),10),(x(14),8)),('C',(x(4),14),(x(6),8),(x(4),10)),('L',(x(4),32))]);join(name,'lens'+name)
line('bridge',(20,18),(28,18));join('bridge','barrel--1');join('bridge','barrel-1')
''')
add('VRECT_L','Round reservoir narrows smoothly into an open lower outlet; paired ureters join its shoulders.','No useful exact Lucide match; original bladder contour governs anatomy.','None; upper tubes remain intentionally open.', '''
path('bladder',(20,44),[('L',(20,39)),('C',(15,32),(20,35),(18,34)),('C',(8,22),(10,29),(8,26)),('C',(12,16),(8,19),(9,17)),('C',(24,12),(15,13),(20,12)),('C',(36,16),(28,12),(33,13)),('C',(40,22),(39,17),(40,19)),('C',(33,32),(40,26),(38,29)),('C',(28,39),(30,34),(28,35)),('L',(28,44))])
path('left-ureter',(8,4),[('C',(12,16),(8,10),(8,14))]);join('left-ureter','bladder')
path('right-ureter',(40,4),[('C',(36,16),(40,10),(40,14))]);join('right-ureter','bladder')
''')
add('SQUARE','Blank circular face with broad curled cowboy brim and a smooth dipped crown, mirrored about x24.','Shared human_ref/user.svg: circular head; source governs headwear. No useful Lucide cowboy match.','No face details in source. Head-only subject has no head/body gap.', '''
# Circular jaw radius 16; the brim meets its endpoints at y26.
self.add_arc('jaw',(8,26),(40,26),radius_x=16,sweep=False)
path('brim',(6,16),[('C',(8,26),(6,21),(6,24)),('C',(40,26),(18,30),(30,30)),('C',(42,16),(42,24),(42,21))]);join('jaw','brim')
path('crown',(12,20),[('L',(15,9)),('C',(18,6),(16,6),(17,6)),('C',(24,8),(20,6),(22,8)),('C',(30,6),(26,8),(28,6)),('C',(33,9),(31,6),(32,6)),('L',(36,20))])
path('brim-top',(6,16),[('C',(12,20),(7,16),(9,19)),('C',(36,20),(20,24),(28,24)),('C',(42,16),(39,19),(41,16))]);join('brim-top','brim');join('brim-top','crown')
''')
add('HRECT_L','Open book with straight outer sides, rounded corners, curved paired leaves and a central binding.','book-open: straight sides, paired leaf curves and shared spine','None.', '''
path('spread',(24,14),[('C',(8,8),(20,10),(15,8)),('L',(6,8)),('A',(4,10),2,2,False),('L',(4,34)),('A',(6,36),2,2,False),('L',(8,36)),('C',(24,40),(15,36),(20,37)),('C',(40,36),(28,37),(33,36)),('L',(42,36)),('A',(44,34),2,2,False),('L',(44,10)),('A',(42,8),2,2,False),('L',(40,8)),('C',(24,14),(33,8),(28,10))],True)
line('spine',(24,14),(24,40));join('spine','spread')
''')
add('VRECT_L','Rounded bottle with a narrow neck and a flowing burning cloth wick, with a pointed fluttering end.','cooking-pot: tangent rounded body corners; source governs asymmetric wick','Mouth collar omitted to preserve 8-unit neck opening.', '''
path('bottle',(12,44),[('A',(8,40),4,4,True),('L',(8,29)),('C',(14,20),(8,25),(14,24)),('L',(14,14)),('L',(24,14)),('L',(24,20)),('C',(30,29),(24,24),(30,25)),('L',(30,40)),('A',(26,44),4,4,True),('L',(12,44))],True)
path('wick',(19,14),[('C',(27,4),(19,8),(21,4)),('C',(40,16),(35,4),(32,14)),('L',(35,20)),('C',(27,12),(29,20),(29,17))]);join('wick','bottle')
''')
add('VRECT_L','Braille book with rounded binding and six tactile dots arranged in a clear two-column series.','book: continuous spine and rounded lower page turn','Reference dots regularized as generic Braille cells, no text transcription.', '''
path('right-bottom',(40,4),[('L',(40,44)),('L',(12,44)),('A',(8,40),4,4,True),('A',(12,36),4,4,True)])
path('spine',(8,40),[('L',(8,10)),('A',(14,4),6,6,True)]);join('spine','right-bottom')
line('top',(14,4),(40,4));join('top','spine');join('top','right-bottom')
line('page',(12,36),(40,36));join('page','right-bottom')
for col in range(2):
 for row in range(3):self.add_dot(f'dot-{col}-{row}',(19+10*col,12+8*row))
''')
add('SQUARE','Circular squeeze bulb and slender diagonal nozzle joined with smooth shoulders and a rounded tip.','syringe and pill: parallel diagonal nozzle and curved tip','Neck ridges omitted; continuous silhouette retains bulb identity.', '''
path('outline',(6,28),[('A',(20,14),14,14,True),('C',(26,14),(24,14),(24,16)),('L',(34,6)),('C',(42,12),(37,6),(42,9)),('L',(32,22)),('C',(34,28),(30,24),(34,24)),('A',(20,42),14,14,True),('A',(6,28),14,14,True)],True)
''')
add('SQUARE','Diagonal calligraphy nib beside an elongated curled ink stroke; broad nib shoulders and one central slit.','pen-tool: joined outline and nib slit; source governs separate ink curl','Tiny vent omitted to keep slit clear.', '''
path('nib',(24,25),[('L',(30,8)),('L',(36,6)),('L',(42,12)),('L',(40,19)),('L',(24,25))],True)
line('slit',(24,25),(33,16));join('slit','nib')
path('ink',(16,20),[('C',(6,30),(8,23),(6,23)),('L',(6,36)),('A',(12,42),6,6,False),('A',(18,36),6,6,False)])
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
