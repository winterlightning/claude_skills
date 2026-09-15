"""Second group of fifty: individually planned SOLO48 review variants."""
from pathlib import Path
import ast,json,sys,textwrap,runpy
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import factories
SOURCE_ICON_ID=None # Exact per-icon identities are retained in selected.json and each module.
SOURCE_PATH='icon_set/work/solo-ai-next50/selected.json'
AUTHOR='gpt-6'
WORK=Path(__file__).parent
HELPERS=runpy.run_path(str(ROOT/'icon_set/work/solo-ai-first50/author_batch.py'))['HELPERS']
D={}
def design(name,key,ref,plan,body):D[name]=(key,ref,plan,textwrap.dedent(body))
design('binoculars','HRECT_L','binoculars','Two broad objectives share a baseline and radius, with taller rounded eyepieces and a narrow center bridge. The bridge uses exact attachment nodes; distinct from the prior angular binocular design.', '''
for side in (-1,1):
 x=lambda d:24+side*d
 circle(f'lens-{side}',x(12),32,8)
 path(f'barrel-{side}',(x(20),32),[('C',(x(16),18),(x(20),26),(x(16),23)),('L',(x(16),12)),('A',(x(8),12),4,4,side<0),('L',(x(8),20)),('L',(x(4),20)),('L',(x(4),32))])
 join(f'barrel-{side}',f'lens-{side}')
line('bridge',(20,20),(28,20));join('bridge','barrel--1');join('bridge','barrel-1')
''')
design('bird-house','VRECT_L','birdhouse','A symmetric roof and tapered nesting box surround one true circular entrance. Shared roof junctions and a broad lower body keep the entrance clear.', '''
poly('roof',(8,20),(12,16),(24,4),(36,16),(40,20))
poly('house',(12,16),(12,44),(36,44),(36,16));join('roof','house')
circle('entrance',24,27,4)
''')
design('blood-bag','VRECT_L','droplet','A smooth IV blood bag has four matching body corners and a broad centered outlet. The empty reservoir preserves the source rather than adding a medical modifier.', '''
path('bag',(18,36),[('L',(16,36)),('A',(8,28),8,8,True),('L',(8,12)),('A',(16,4),8,8,True),('L',(32,4)),('A',(40,12),8,8,True),('L',(40,28)),('A',(32,36),8,8,True),('L',(30,36)),('L',(30,44)),('L',(18,44)),('L',(18,36))],True)
''')
design('blood-cell','SQUARE','circle','One softly lobed cell outline replaces the jagged conversion. Four identical quarters share their extrema and tangent directions; no decorative inner marks.', '''
quarter=[('C',(34,10),(29,6),(29,10)),('C',(38,16),(38,10),(38,12)),('C',(42,24),(38,20),(42,20))]
turn=lambda p,n: p if n==0 else turn((48-p[1],p[0]),n-1)
commands=[]
for n in range(4):
 for kind,end,c1,c2 in quarter:commands.append((kind,turn(end,n),turn(c1,n),turn(c2,n)))
path('cell',(24,6),commands,True)
''')
design('boat','HRECT_L','ship','A side-view cabin cruiser retains the source sloping bow and rear cabin. A level gunwale and smooth bow use precise cabin attachments; deliberate travel direction.', '''
path('hull',(8,24),[('L',(16,24)),('L',(32,24)),('L',(36,24)),('L',(44,24)),('C',(32,40),(42,32),(38,40)),('L',(4,40)),('L',(8,24))],True)
poly('cabin',(16,24),(20,8),(28,8),(36,24));join('cabin','hull')
''')
design('boat-transportation','HRECT_L','ship','A frontal motorboat has symmetric cabin, a tapered hull and a single shallow water rhythm at its base. Replaced uneven scallops with matching curves.', '''
poly('cabin',(12,24),(16,8),(32,8),(36,24))
path('hull',(4,24),[('L',(12,24)),('L',(36,24)),('L',(44,24)),('L',(38,40)),('C',(24,40),(32,40),(31,34)),('C',(10,40),(17,34),(16,40)),('L',(4,24))],True)
join('cabin','hull')
''')
design('bomb-explosive','VRECT_L','bomb','The source is a tied cylindrical explosive charge: a rounded canister and central strap with a short curved fuse. Kept that subject rather than substituting a spherical bomb.', '''
path('case',(12,16),[('L',(18,16)),('L',(30,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(30,44)),('L',(18,44)),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,20)),('A',(12,16),4,4,True)],True)
for x in (18,30):
 line(f'band-{x}',(x,16),(x,44));join(f'band-{x}','case')
path('fuse',(24,16),[('C',(30,4),(24,8),(24,4)),('C',(40,8),(36,4),(36,8))]);join('fuse','case')
''')
design('bone','HRECT_L','bone','A horizontal bone uses four matching rounded lobes and a broad shaft. Both axes mirror exactly; removed the traced pinched dents.', '''
path('bone',(14,18),[('C',(9,8),(14,11),(13,8)),('C',(4,14),(5,8),(4,10)),('C',(7,24),(4,19),(7,20)),('C',(4,34),(7,28),(4,29)),('C',(9,40),(4,38),(5,40)),('C',(14,30),(13,40),(14,37)),('L',(34,30)),('C',(39,40),(34,37),(35,40)),('C',(44,34),(43,40),(44,38)),('C',(41,24),(44,29),(41,28)),('C',(44,14),(41,20),(44,19)),('C',(39,8),(44,10),(43,8)),('C',(34,18),(35,8),(34,11)),('L',(14,18))],True)
''')
design('bone-1','SQUARE','bone','A diagonal bone keeps broad rounded ends and an uninterrupted diagonal shaft. The opposite end is a half-turn copy, preserving deliberate orientation.', '''
path('bone',(16,24),[('C',(6,24),(12,20),(6,18)),('C',(10,32),(6,28),(7,31)),('C',(16,42),(10,39),(12,42)),('C',(24,32),(21,42),(23,37)),('L',(32,24)),('C',(42,24),(36,28),(42,30)),('C',(38,16),(42,20),(41,17)),('C',(32,6),(38,9),(36,6)),('C',(24,16),(27,6),(25,11)),('L',(16,24))],True)
''')
# Closed books: independent binding, format and page-block designs.
design('book','VRECT_L','book','Tall hardback with its page block at the top. A rounded left binding flows into the lower cover; exact split rim nodes keep page joins clean.', '''
path('cover',(40,4),[('L',(14,4)),('A',(8,10),6,6,False),('L',(8,14)),('L',(8,38)),('A',(14,44),6,6,False),('L',(40,44)),('L',(40,16)),('L',(40,4))],True)
path('pages',(8,10),[('A',(14,16),6,6,False),('L',(40,16))]);join('pages','cover')
''')
design('book-close','VRECT_L','book','A classic tall hardback uses a rounded lower page roll and square fore-edge. Kept a single generous page band rather than adding small decoration.', '''
path('cover',(40,4),[('L',(14,4)),('A',(8,10),6,6,False),('L',(8,38)),('A',(14,44),6,6,False),('L',(40,44)),('C',(40,34),(37,42),(37,36)),('L',(40,4))],True)
path('pages',(8,38),[('A',(14,34),6,4,True),('L',(40,34))]);join('pages','cover')
''')
design('book-close-1','VRECT_L','notebook','A clothbound notebook has a clear vertical spine and a broad curved lower page edge. This binding differs from the left-roll hardback.', '''
path('cover',(12,4),[('L',(18,4)),('L',(36,4)),('A',(40,8),4,4,True),('L',(40,34)),('L',(40,40)),('A',(36,44),4,4,True),('L',(18,44)),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
poly('spine',(18,4),(18,34),(18,44));join('spine','cover')
path('page-edge',(18,34),[('C',(40,34),(26,38),(32,38))]);join('page-edge','spine');join('page-edge','cover')
''')
design('book-close-2','SQUARE','book','A compact square journal has an upper rolled page edge and large rounded bottom corners. Its format and corner radii distinguish it from tall books.', '''
path('cover',(42,6),[('L',(14,6)),('A',(6,14),8,8,False),('L',(6,30)),('A',(18,42),12,12,False),('L',(30,42)),('A',(42,30),12,12,False),('L',(42,18)),('L',(42,6))],True)
path('pages',(6,14),[('A',(12,18),6,4,False),('L',(42,18))]);join('pages','cover')
''')
design('book-close-49781b64','VRECT_L','book-marked','A square-cornered hardback has a centered built-in ribbon and a narrow lower page block. The ribbon is physical book furniture and shares the top edge.', '''
poly('cover',(8,4),(20,4),(32,4),(40,4),(40,36),(40,44),(8,44),(8,36),closed=True)
line('pages',(8,36),(40,36));join('pages','cover')
poly('ribbon',(20,4),(20,20),(26,16),(32,20),(32,4));join('ribbon','cover')
''')
design('book-close-5a3d7973','HRECT_L','book','A landscape album has a curved spine and a broad lower page band. Horizontal keyshape preserves a distinct album proportion.', '''
path('cover',(44,8),[('L',(12,8)),('A',(4,16),8,8,False),('L',(4,34)),('A',(10,40),6,6,False),('L',(44,40)),('L',(44,30)),('L',(44,8))],True)
path('pages',(4,34),[('A',(10,30),6,4,True),('L',(44,30))]);join('pages','cover')
''')
design('book-close-content','SQUARE','notebook','A square bound notebook uses a straight upper page band and an offset vertical spine. Equal corner radii keep the cover clean.', '''
path('cover',(10,6),[('L',(16,6)),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,18)),('L',(42,38)),('A',(38,42),4,4,True),('L',(16,42)),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,18)),('L',(6,10)),('A',(10,6),4,4,True)],True)
line('spine',(16,6),(16,42));line('pages',(16,18),(42,18));join('spine','cover');join('pages','spine');join('pages','cover')
''')
design('book-content','VRECT_L','book','An upright softcover has a concave exposed page edge at the top-right and a rounded spine. The visible notch distinguishes it from solid hard covers.', '''
path('cover',(40,4),[('L',(14,4)),('A',(8,10),6,6,False),('L',(8,38)),('A',(14,44),6,6,False),('L',(40,44)),('L',(40,16)),('C',(40,4),(36,13),(36,7))],True)
path('pages',(8,10),[('A',(14,16),6,6,False),('L',(40,16))]);join('pages','cover')
''')
# Open books keep native readable spreads with deliberately different leaf shapes.
design('book-book-pages','HRECT_L','book-open','A broad open book with gently arched pages. Shared left-page controls are reflected for exactly balanced page widths and a centered spine.', '''
path('spread',(24,14),[('C',(12,8),(20,10),(16,8)),('C',(4,10),(8,8),(6,9)),('L',(4,36)),('C',(12,34),(6,35),(8,34)),('C',(24,40),(16,34),(20,36)),('C',(36,34),(28,36),(32,34)),('C',(44,36),(40,34),(42,35)),('L',(44,10)),('C',(36,8),(42,9),(40,8)),('C',(24,14),(32,8),(28,10))],True)
line('spine',(24,14),(24,40));join('spine','spread')
''')
design('book-open','SQUARE','book-open','A tall rounded open volume uses a deeper central fold and matching curled upper and lower pages. Square bounds create a substantial upright spread.', '''
path('spread',(24,12),[('C',(12,6),(21,8),(17,6)),('L',(6,6)),('L',(6,36)),('L',(12,36)),('C',(24,42),(17,36),(21,38)),('C',(36,36),(27,38),(31,36)),('L',(42,36)),('L',(42,6)),('L',(36,6)),('C',(24,12),(31,6),(27,8))],True)
line('spine',(24,12),(24,42));join('spine','spread')
''')
design('book-open-1','HRECT_L','book-open','A broad flat-topped open book has softly rounded outer corners and shallow spine transitions. Matching radii replace conversion dents.', '''
path('spread',(24,12),[('A',(20,8),4,4,False),('L',(8,8)),('A',(4,12),4,4,False),('L',(4,32)),('A',(8,36),4,4,False),('L',(16,36)),('C',(24,40),(20,36),(22,38)),('C',(32,36),(26,38),(28,36)),('L',(40,36)),('A',(44,32),4,4,False),('L',(44,12)),('A',(40,8),4,4,False),('L',(28,8)),('A',(24,12),4,4,False)],True)
line('spine',(24,12),(24,40));join('spine','spread')
''')
design('book-open-1-6ed65acc','VRECT_L','book-open','A narrow pocket-sized open book has tall leaves and a shallow curved fold. Vertical proportions distinguish it from wide spreads.', '''
path('spread',(24,10),[('C',(8,4),(20,4),(14,4)),('L',(8,38)),('C',(24,44),(14,38),(20,38)),('C',(40,38),(28,38),(34,38)),('L',(40,4)),('C',(24,10),(34,4),(28,4))],True)
line('spine',(24,10),(24,44));join('spine','spread')
''')
design('book-open-1-899601b3','HRECT_L','book-open','An angular shallow spread has parallel sloping top and bottom edges. A single shared fold preserves exact mirror symmetry.', '''
poly('spread',(4,8),(24,14),(44,8),(44,34),(24,40),(4,34),closed=True)
line('spine',(24,14),(24,40));join('spine','spread')
''')
design('book-open-1-df25e3f8','HRECT_L','book-open','A raised open book uses steep page planes and a short central fold. Deliberate geometric corners preserve the original V-shaped subject.', '''
poly('spread',(4,8),(24,18),(44,8),(44,30),(24,40),(4,30),closed=True)
line('spine',(24,18),(24,40));join('spine','spread')
''')
design('book-open-1421392c','HRECT_L','book-open','An open volume with one leaf lifting on the left. The asymmetric turning leaf is intentional; broad empty pages retain clarity.', '''
path('spread',(24,16),[('L',(14,8)),('L',(4,12)),('L',(4,34)),('L',(14,32)),('L',(24,40)),('C',(44,34),(30,34),(38,34)),('L',(44,10)),('C',(24,16),(38,10),(30,10))],True)
line('spine',(24,16),(24,40));line('leaf',(14,8),(14,32));join('spine','spread');join('leaf','spread')
''')
design('book-open-a147931e','SQUARE','book-open-text','A square open reader adds one sparse text line per page to a matched arched spread. Text placement derives from the same axis and leaves generous wall clearance.', '''
path('spread',(24,10),[('C',(6,6),(18,6),(12,6)),('L',(6,38)),('C',(24,42),(12,38),(18,38)),('C',(42,38),(30,38),(36,38)),('L',(42,6)),('C',(24,10),(36,6),(30,6))],True)
line('spine',(24,10),(24,42));join('spine','spread')
for side in (-1,1):
 x=lambda d:24+side*d
 line(f'text-{side}',(x(9),24),(x(10),24))
''')
design('book-open-b5768591','HRECT_L','book-open','An open book with an exposed lower page layer. The secondary contour follows the spread eight units below its principal edge; outer attachments remain exact.', '''
path('spread',(24,12),[('C',(4,8),(18,8),(10,8)),('L',(4,24)),('L',(4,32)),('C',(24,40),(12,32),(18,34)),('C',(44,32),(30,34),(36,32)),('L',(44,24)),('L',(44,8)),('C',(24,12),(38,8),(30,8))],True)
path('page-edge',(4,24),[('C',(24,32),(12,24),(18,26)),('C',(44,24),(30,26),(36,24))]);line('spine',(24,12),(24,32));join('page-edge','spread');join('spine','spread');join('spine','page-edge')
''')
design('book-open-e1dee87f','HRECT_L','book-open','A soft open book has bowed outer edges and level inner leaves. Its flared silhouette and broad centered lower arc create a distinct flexible binding.', '''
path('spread',(24,12),[('C',(8,8),(18,8),(12,8)),('C',(4,28),(6,14),(4,22)),('L',(4,36)),('C',(24,40),(12,34),(18,36)),('C',(44,36),(30,36),(36,34)),('L',(44,28)),('C',(40,8),(44,22),(42,14)),('C',(24,12),(36,8),(30,8))],True)
line('spine',(24,12),(24,40));join('spine','spread')
''')
design('book-pages','HRECT_L','book-open','A low wide book has rounded page corners and a short recessed center fold. The lower spine is squared, producing a quiet broad spread.', '''
path('spread',(24,16),[('C',(12,8),(21,10),(17,8)),('L',(4,8)),('L',(4,32)),('A',(12,40),8,8,False),('L',(24,40)),('L',(36,40)),('A',(44,32),8,8,False),('L',(44,8)),('L',(36,8)),('C',(24,16),(31,8),(27,10))],True)
line('spine',(24,16),(24,40));join('spine','spread')
''')
design('bowl','HRECT_L','soup','A plain footed bowl keeps a continuous elliptical basin and broad flat foot. One shared axis controls both sides, with no unnecessary steam or utensils.', '''
path('bowl',(4,8),[('L',(44,8)),('C',(32,32),(44,20),(38,28)),('L',(32,40)),('L',(16,40)),('L',(16,32)),('C',(4,8),(10,28),(4,20))],True)
''')
# Cartons preserve physical package identity, with distinct closures and perspectives.
design('box','SQUARE','package','A frontal taped carton has pitched folded shoulders and a central top seam. The closed front remains broad and uncluttered.', '''
poly('carton',(6,18),(16,6),(24,6),(32,6),(42,18),(42,42),(6,42),closed=True)
poly('rim',(6,18),(24,18),(42,18));line('top-seam',(24,6),(24,18));join('rim','carton');join('top-seam','rim');join('top-seam','carton')
''')
design('box-25bec113','SQUARE','package','A rounded tuck-top carton has a broad central closing tab. Matching radii soften the package without copying a flat frame.', '''
path('carton',(12,6),[('L',(18,6)),('L',(18,18)),('L',(30,18)),('L',(30,6)),('L',(36,6)),('A',(42,12),6,6,True),('L',(42,36)),('A',(36,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,12)),('A',(12,6),6,6,True)],True)
''')
design('box-45b3bf7f','SQUARE','box','A three-quarter cube uses one top diamond and two equal visible sides. Every meeting edge shares an integer node; perspective is intentional.', '''
poly('carton',(6,16),(15,11),(24,6),(42,16),(42,32),(24,42),(6,32),closed=True)
poly('rim',(6,16),(24,26),(33,21),(42,16));line('corner',(24,26),(24,42));join('rim','carton');join('corner','rim');join('corner','carton')
''')
design('box-45de01b0','VRECT_L','package','A tall parcel keeps the source hanging tape end as a broad integral closure. The rectangular package and shallow V-cut tape are centered.', '''
poly('carton',(8,4),(18,4),(30,4),(40,4),(40,44),(8,44),closed=True)
poly('tape',(18,4),(18,22),(24,18),(30,22),(30,4));join('tape','carton')
''')
design('box-805cc175','HRECT_L','package','A wide lidded storage carton has a centered short lid seam and rounded lower corners. Horizontal format makes it distinct from the tall parcels.', '''
path('carton',(8,8),[('L',(24,8)),('L',(40,8)),('A',(44,12),4,4,True),('L',(44,18)),('L',(44,34)),('A',(38,40),6,6,True),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,18)),('L',(4,12)),('A',(8,8),4,4,True)],True)
poly('lid',(4,18),(24,18),(44,18));line('seam',(24,8),(24,18));join('lid','carton');join('seam','lid');join('seam','carton')
''')
design('box-a4589238','VRECT_L','package','A tall paper carton has a pitched top and a visible right-side gusset. Its asymmetry describes real package depth, not random offset.', '''
poly('carton',(8,14),(16,4),(30,4),(40,14),(40,44),(30,44),(8,44),closed=True)
poly('fold',(8,14),(30,14),(40,14));poly('side',(30,4),(30,14),(30,44));join('fold','carton');join('side','carton');join('side','fold')
''')
design('box-bfb848d1','HRECT_L','package','A landscape taped parcel has a wide integral closure with a square end. The shallow box and flat tape distinguish it from the V-cut vertical package.', '''
poly('carton',(4,8),(18,8),(30,8),(44,8),(44,40),(4,40),closed=True)
poly('tape',(18,8),(18,24),(30,24),(30,8));join('tape','carton')
''')
design('box-shipping','SQUARE','package','A sealed shipping cube shows a narrow band crossing its top plane. Two sloping faces and a single front corner preserve the package perspective.', '''
poly('carton',(6,16),(15,11),(24,6),(42,16),(42,32),(24,42),(6,32),closed=True)
poly('rim',(6,16),(24,26),(33,21),(42,16));line('corner',(24,26),(24,42));join('rim','carton');join('corner','rim');join('corner','carton')
# A second top-panel seam keeps the tape broad enough to read.
line('tape',(15,11),(33,21));join('tape','carton');join('tape','rim')
''')
design('boxing-glove','VRECT_L',None,'A boxing glove has a broad smooth knuckle dome, an inward thumb and a rounded cuff. Preserved the source hand silhouette and removed uneven corners.', '''
path('glove',(16,36),[('C',(8,26),(10,34),(8,31)),('L',(8,16)),('A',(20,4),12,12,True),('L',(28,4)),('A',(40,16),12,12,True),('L',(40,26)),('C',(32,36),(40,32),(36,36)),('L',(16,36))],True)
path('thumb',(40,26),[('L',(33,19)),('C',(28,27),(28,17),(24,22))]);join('thumb','glove')
path('cuff',(16,36),[('L',(12,36)),('L',(12,40)),('A',(16,44),4,4,False),('L',(32,44)),('A',(36,40),4,4,False),('L',(36,36)),('L',(32,36))]);join('cuff','glove')
''')
# Brain views retain anatomical lobes without the source jagged dent pattern.
design('brain','SQUARE','brain','A frontal brain has paired smooth hemispheres and a central division. Two broad inward folds carry anatomy without a row of tiny teeth.', '''
left=[('C',(14,6),(22,6),(18,6)),('C',(9,16),(10,6),(8,11)),('C',(6,26),(6,17),(6,21)),('C',(10,34),(6,30),(8,33)),('C',(16,42),(10,39),(12,42)),('C',(24,38),(20,42),(22,40))]
path('left',(24,10),left+[('L',(24,10))],True)
mirror=lambda p:(48-p[0],p[1])
right=[(k,mirror(e),mirror(a),mirror(b)) for k,e,a,b in left]
path('right',(24,10),right+[('L',(24,10))],True);join('left','right')
''')
design('brain-1','CIRCLE','brain','A top-view brain uses a smooth lobed perimeter and a short central fold, replacing the flower-like jagged conversion. The circular envelope keeps the mass balanced.', '''
path('brain',(24,4),[('C',(36,8),(30,4),(34,4)),('C',(44,24),(42,12),(44,18)),('C',(36,40),(44,30),(42,36)),('C',(24,44),(34,44),(30,44)),('C',(12,40),(18,44),(14,44)),('C',(4,24),(6,36),(4,30)),('C',(12,8),(4,18),(6,12)),('C',(24,4),(14,4),(18,4))],True)
line('fold',(24,14),(24,34))
''')
design('brain-f98adc76','HRECT_L','brain','A side-view brain has three broad overlapping-looking lobes resolved as one continuous outline, plus one internal fold. Natural anatomical asymmetry is retained.', '''
path('brain',(4,28),[('C',(10,16),(4,21),(6,17)),('C',(22,8),(10,8),(16,8)),('C',(34,12),(28,8),(32,8)),('C',(44,24),(42,12),(44,17)),('C',(34,40),(44,34),(40,40)),('C',(24,36),(29,40),(26,39)),('C',(12,38),(20,40),(15,40)),('C',(4,28),(6,38),(4,34))],True)
path('fold',(34,12),[('C',(26,26),(27,13),(26,19))]);join('fold','brain')
''')
# Four breads with different loaf, crust and slice silhouettes.
design('bread','SQUARE','sandwich','A square sandwich-loaf slice has a wide softly domed crown and straight lower sides. Both sides derive from one axis; no tiny crust texture.', '''
path('bread',(12,42),[('L',(12,22)),('C',(6,14),(8,22),(6,19)),('C',(16,6),(6,8),(10,6)),('L',(32,6)),('C',(42,14),(38,6),(42,8)),('C',(36,22),(42,19),(40,22)),('L',(36,42)),('L',(12,42))],True)
''')
design('bread-loaf','HRECT_L','sandwich','A loaf in perspective keeps a rounded crown and a single visible slice seam. The right end is deliberately shorter to show depth.', '''
path('loaf',(8,40),[('L',(10,22)),('C',(4,16),(6,22),(4,19)),('C',(14,8),(4,10),(8,8)),('L',(34,8)),('C',(44,16),(40,8),(44,10)),('C',(38,22),(44,19),(42,22)),('L',(40,40)),('L',(8,40))],True)
path('slice',(26,8),[('C',(26,22),(34,10),(34,18)),('L',(30,40))]);join('slice','loaf')
''')
design('bread-slice','VRECT_L','sandwich','A tall rounded toast slice has a smoothly arched top and four-unit lower corner radii. Its narrower body distinguishes it from the square sandwich slice.', '''
path('slice',(16,44),[('A',(12,40),4,4,True),('L',(12,20)),('C',(8,14),(10,18),(8,17)),('C',(24,4),(8,7),(16,4)),('C',(40,14),(32,4),(40,7)),('C',(36,20),(40,17),(38,18)),('L',(36,40)),('A',(32,44),4,4,True),('L',(16,44))],True)
''')
design('bread-slice-food','HRECT_L','sandwich','A broad toast slice keeps a low dome and an inset shallow crust stroke. The landscape format and visible crust distinguish it from the other bread variants.', '''
path('slice',(12,40),[('L',(12,24)),('C',(4,16),(7,24),(4,21)),('C',(24,8),(4,9),(16,8)),('C',(44,16),(32,8),(44,9)),('C',(36,24),(44,21),(41,24)),('L',(36,40)),('L',(12,40))],True)
line('crust',(21,28),(27,28))
''')
design('bricks','HRECT_L','brick-wall','A brick wall has two broad courses and staggered vertical joints. Exact shared endpoints and one course-height parameter keep mortar gaps consistent.', '''
poly('wall',(4,8),(18,8),(44,8),(44,24),(44,40),(30,40),(4,40),(4,24),closed=True)
poly('course',(4,24),(18,24),(30,24),(44,24));line('top-joint',(18,8),(18,24));line('bottom-joint',(30,24),(30,40))
for n in ('course','top-joint','bottom-joint'):join(n,'wall')
join('top-joint','course');join('bottom-joint','course')
''')
design('building','VRECT_L','building','A single sloping-roof building has a clear broad doorway and a short roof mast. Deliberate asymmetric roof direction preserves the source.', '''
poly('building',(12,44),(12,10),(36,24),(36,44),(28,44),(20,44),(12,44))
line('mast',(12,4),(12,10));join('mast','building')
poly('door',(20,44),(20,32),(28,32),(28,44));join('door','building')
poly('ground',(8,44),(12,44),(36,44),(40,44));join('ground','building')
''')
design('building-1','VRECT_L','building','A wider asymmetrical wedge building uses a flat entrance threshold and a small upper window. It remains a separate architectural variant.', '''
poly('building',(8,44),(8,4),(40,22),(40,44),(8,44))
line('window',(19,23),(27,23))
''')
design('building-68b98b76','VRECT_L','building-2','A tall sloped tower stands beside a short annex, with a simple entrance between their shared baseline nodes. Keep the stepped silhouette and remove tiny junction kinks.', '''
poly('tower',(24,44),(24,14),(40,4),(40,44),(24,44))
poly('annex',(24,24),(8,24),(8,44),(24,44));join('annex','tower')
''')
design('building-735a4c8f','VRECT_L','building-2','Two angled building faces share a central vertical corner. Their tops and bases are complete, with a taller right face; deliberate perspective remains.', '''
poly('left',(8,44),(8,28),(16,22),(16,8),(28,16),(28,44),(8,44))
poly('right',(28,16),(40,4),(40,44),(28,44));join('left','right')
''')

# Native-size review refinements: widen openings and restore recognizable anatomy.
design('bird-house','VRECT_L','birdhouse','A symmetric roof sits over a broader nesting box and a clearly open circular entrance. The opening has nine units of centerline clearance from both side walls.', """
poly('roof',(8,20),(10,18),(24,4),(38,18),(40,20))
poly('house',(10,18),(10,44),(38,44),(38,18));join('roof','house')
circle('entrance',24,28,5)
""")
design('book-open-a147931e','HRECT_L','book-open-text','A wide open reader has two sparse text rules per page. Shared page and text parameters keep mirrored margins and eight-unit row spacing.', """
path('spread',(24,12),[('C',(4,8),(18,8),(10,8)),('L',(4,36)),('C',(24,40),(10,36),(18,36)),('C',(44,36),(30,36),(38,36)),('L',(44,8)),('C',(24,12),(38,8),(30,8))],True)
line('spine',(24,12),(24,40));join('spine','spread')
for side in (-1,1):
 x=lambda d:24+side*d
 for y in (20,28):line(f'text-{side}-{y}',(x(9),y),(x(11),y))
""")
design('building-1','VRECT_L','building','A wide wedge building uses a level baseline and a small window comfortably below the sloping roof. The asymmetric roof preserves the source architectural direction.', """
poly('building',(8,44),(8,4),(40,22),(40,44),(8,44))
line('window',(19,28),(27,28))
""")
design('bone-1','SQUARE','bone','A diagonal bone uses four equal semicircular end lobes and a broad diagonal shaft. Shared lobe radius and half-turn symmetry replace the lumpy traced ends.', """
path('bone',(24,12),[('A',(36,12),6,6,True),('A',(36,24),6,6,True),('L',(32,24)),('L',(24,32)),('L',(24,36)),('A',(12,36),6,6,True),('A',(12,24),6,6,True),('L',(16,24)),('L',(24,16)),('L',(24,12))],True)
""")
design('brain','SQUARE','brain','A frontal brain has matching lobed hemispheres and one inward fold per side. Broad curved lobes and a shared central division retain the anatomical reading.', """
left=[('C',(14,6),(22,6),(18,6)),('C',(9,16),(10,6),(8,11)),('C',(6,26),(6,17),(6,21)),('C',(10,34),(6,30),(8,33)),('C',(16,42),(10,39),(12,42)),('C',(24,38),(20,42),(22,40))]
path('left',(24,10),left+[('L',(24,10))],True)
mirror=lambda p:(48-p[0],p[1])
right=[(k,mirror(e),mirror(a),mirror(b)) for k,e,a,b in left]
path('right',(24,10),right+[('L',(24,10))],True);join('left','right')
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'fold-{side}',(x(15),16),[('C',(x(8),21),(x(10),16),(x(8),18)),('C',(x(11),27),(x(8),24),(x(9),26))])
 join(f'fold-{side}','left' if side<0 else 'right')
""")
design('brain-1','SQUARE','brain','A top-view brain uses a lobed outer mass and a gently winding central fissure. Shared mirrored outlines give a different anatomical view without the original gear-like teeth.', """
left=[('C',(14,6),(22,6),(18,6)),('C',(8,16),(8,6),(8,12)),('C',(6,24),(8,18),(6,20)),('C',(10,32),(6,28),(6,32)),('C',(16,42),(8,38),(10,42)),('C',(24,38),(21,42),(23,40))]
# The right side is the exact reverse traversal of the reflected left side.
segments=[];start=(24,8)
for kind,end,c1,c2 in left:segments.append((start,end,c1,c2));start=end
mirror=lambda p:(48-p[0],p[1])
commands=left+[('C',mirror(a),mirror(c2),mirror(c1)) for a,b,c1,c2 in reversed(segments)]
path('brain',(24,8),commands,True)
path('fissure',(24,8),[('C',(24,24),(18,14),(30,18)),('C',(24,38),(18,30),(30,33))]);join('fissure','brain')
""")
design('brain-f98adc76','HRECT_L','brain','A side-view brain has three broad lobes and two smooth folds. Its left and right folds differ intentionally to describe a lateral anatomical view.', """
path('brain',(4,28),[('C',(10,16),(4,21),(6,17)),('C',(22,8),(10,8),(16,8)),('C',(34,12),(28,8),(32,8)),('C',(44,24),(42,12),(44,17)),('C',(34,40),(44,34),(40,40)),('C',(24,36),(29,40),(26,39)),('C',(12,38),(20,40),(15,40)),('C',(4,28),(6,38),(4,34))],True)
path('fold-right',(34,12),[('C',(28,27),(29,13),(28,20))]);join('fold-right','brain')
path('fold-left',(22,8),[('C',(16,22),(16,11),(16,17))]);join('fold-left','brain')
""")

design('box-a4589238','VRECT_L','package','A tall paper carton has pitched shoulders and a right-side gusset. The gusset starts below the top fold, removing a tiny triangular opening while preserving real package depth.', """
poly('carton',(8,14),(16,4),(30,4),(40,14),(40,44),(30,44),(8,44),closed=True)
poly('fold',(8,14),(30,14),(40,14));line('side',(30,14),(30,44));join('fold','carton');join('side','carton');join('side','fold')
""")
design('brain','SQUARE','brain','A frontal brain has matching rounded hemispheres and two shallow folds branching from the central fissure. The folds open toward the lobes rather than forming ear-like loops.', """
left=[('C',(18,6),(24,8),(22,6)),('C',(12,14),(12,6),(10,10)),('C',(6,24),(8,14),(6,19)),('C',(10,32),(6,28),(6,31)),('C',(18,42),(8,38),(12,42)),('C',(24,36),(22,42),(24,40))]
path('left',(24,12),left+[('L',(24,18)),('L',(24,12))],True)
mirror=lambda p:(48-p[0],p[1])
right=[(k,mirror(e),mirror(a),mirror(b)) for k,e,a,b in left]
path('right',(24,12),right+[('L',(24,18)),('L',(24,12))],True);join('left','right')
for side in (-1,1):
 x=lambda d:24+side*d
 path(f'fold-{side}',(24,18),[('C',(x(8),26),(24,23),(x(4),26))])
 join(f'fold-{side}','left');join(f'fold-{side}','right')
""")

def main():
 rows=json.loads((WORK/'selected.json').read_text());reg=factories();prior={r['parent']:r for r in json.loads((WORK/'batch.json').read_text())} if (WORK/'batch.json').exists() else {};out=[]
 for row in rows:
  name=row['icon_id'];key,ref,plan,body=D[name]
  if name in prior:p=ROOT/prior[name]['path'];new=prior[name]['icon_id'];tree=ast.parse(p.read_text())
  else:
   dest,new,source=prepare_variant(name,'solo','AI review · next 50');tree=ast.parse(source);uuid=getattr(sys.modules[reg[name].__module__],'SOURCE_ICON_ID',None);p=dest.with_name(dest.stem+'_'+uuid.replace('-','_')+'.py') if uuid else dest
  cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));tree.body=[n for n in tree.body if not isinstance(n,ast.Expr)]
  for n in tree.body:
   if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='AUTHOR' for t in n.targets):n.value=ast.Constant(AUTHOR)
  for n in cls.body:
   if isinstance(n,ast.Assign):
    for t in n.targets:
     if isinstance(t,ast.Name) and t.id=='keyshape':n.value=ast.Attribute(ast.Name('Keyshape',ast.Load()),key,ast.Load())
     if isinstance(t,ast.Name) and t.id=='keywords':n.value=ast.Tuple([ast.Constant(x) for x in tuple(row.get('keywords',[]))+('solo-ai-next50',)],ast.Load())
  cls.body=[n for n in cls.body if not isinstance(n,ast.FunctionDef)]
  func='    def build(self):\n        # Plan: '+plan+'\n        # Reference: '+('Lucide '+ref+' original and atomic-debug construction.' if ref else 'No useful exact Lucide match; supplied boxing glove silhouette.')+'\n'+HELPERS+textwrap.indent(body.strip(),'        ')+'\n'
  cls.body.append(ast.parse(textwrap.dedent(func)).body[0]);ast.fix_missing_locations(tree);src=ast.unparse(tree);src=src[:src.index('    def build(')]+func;output=f'"""{name}: next fifty AI review; original preserved."""\n'+src
  if not p.exists() or p.read_text()!=output:p.write_text(output)
  out.append(dict(parent=name,icon_id=new,path=str(p.relative_to(ROOT)),keyshape=key,reference=ref,plan=plan))
 (WORK/'batch.json').write_text(json.dumps(out,indent=2));print('Authored',len(out))
if __name__=='__main__':main()
