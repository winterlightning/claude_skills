from pathlib import Path
import json, re, sys, io, hashlib
from datetime import datetime, timezone
from PIL import Image, ImageDraw
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts.build_gate import gate
BATCH=Path(__file__).resolve().parent
ITEMS=json.loads((BATCH/'items.json').read_text())
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
# Every generated module below stores its exact individual source UUID/path.
HELPER='''
    def path(self, name, start, *steps, closed=False):
        members=[]
        point=start
        for i, step in enumerate(steps):
            ident=f"{name}-{i}"
            end=tuple(step[:2])
            if len(step)==2:
                self.add_line(ident, point, end)
            else:
                self.add_arc(ident, point, end, radius_x=step[2], radius_y=step[3], sweep=step[4])
            members.append(ident)
            point=end
        self.add_contour(name, *members, closed=closed)

    def circle(self, name, cx, cy, r):
        self.path(name,(cx-r,cy),(cx+r,cy,r,r,True),(cx-r,cy,r,r,True),closed=True)
'''
D={}
def add(n,observation,change,body,exception_reason,keyshape='SQUARE',omissions='Fine finger creases and minor decorative detail omitted for 48px clarity.'):
 D[n]=dict(observation=observation,change=change,body=body,exception_reason=exception_reason,keyshape=keyshape,omissions=omissions)
add(1,'Rejected grain collapses into a three-pronged arrow and a baseline; the reference shows a pinching hand, grain ear and cultivated soil.',
 'Restored two paired grain barbs, a pinching thumb/index silhouette and curved soil ridge.', '''
        # Root: upper-right pinch, left grain series, lower soil; deliberately asymmetric action.
        self.path('hand',(42,6),(35,6),(26,11,12,12,False),(20,21),(24,25,3,3,False),(31,19))
        self.path('thumb',(31,19),(30,24,4,4,False),(34,25,4,4,False),(39,21),(42,14,12,12,False))
        self.add_line('grain-stem',(6,21),(20,21))
        for i,x in enumerate((8,15)):
            self.path(f'grain-{i}',(x,16),(x+5,21),(x,26))
        self.path('soil',(6,34),(12,34),(20,42,8,8,True),(35,42))
        self.add_line('soil-back',(6,42),(20,42))
        self.relate('connect','soil','soil-back')
        self.relate('connect','grain-stem','hand')
''','The compact repeated grain barbs and pinch retain the harvesting action; 4px stroke and open hand remain legible.')
add(2,'The rejected axe head is a small diamond and the hand reads as a zigzag rather than fingers wrapped around a handle.',
 'Redrew a broad flared axe blade, diagonal handle, rounded fist and thumb with two finger divisions.', '''
        # Root: broad flared blade, diagonal handle, enclosing fist; repeated finger separators.
        self.path('blade',(27,6),(31,15,13,13,False),(42,23),(36,29,5,5,True),(28,22),(20,18),(27,6,15,15,True),closed=True)
        self.path('handle-top',(24,22),(20,26))
        self.path('handle-bottom',(13,35),(6,42),(11,44),(18,37))
        self.path('fist',(12,36),(7,31),(7,27,3,3,True),(15,19),(19,19,3,3,True),(28,28))
        self.path('thumb',(22,24),(29,29),(31,34,7,7,True),(29,39),(31,44))
        for i,(x,y) in enumerate(((10,25),(15,21))):
            self.add_line(f'finger-{i}',(x,y),(x+7,y+7))
''','Diagonal grip needs closely spaced finger divisions; the broad blade, open fist and handle remain readable.','VRECT_L')
add(3,'The rejected banknote uses a solid dot and the hand looks like a letter B; the reference has a distinct thumb across the bill and a wrist cuff.',
 'Restored a tall bill with outlined denomination seal, horizontal thumb, cupped palm and cuff.', '''
        # Upright note behind the thumb; wrist and palm are one coherent outline.
        self.path('note',(20,28),(18,9),(21,6,3,3,True),(37,6),(40,9,3,3,True),(38,28))
        self.circle('seal',29,17,4)
        self.path('thumb',(6,28),(13,28),(18,24),(20,28),(36,28),(36,35,4,4,True),(25,35))
        self.path('palm',(39,32),(39,37),(34,42,5,5,True),(20,42),(12,38),(6,38))
        self.add_line('cuff',(12,28),(12,38))
        self.relate('connect','thumb','cuff')
        self.relate('connect','palm','cuff')
        self.relate('connect','note','thumb')
''','The note seal and thumb are necessary payment cues; compact thumb spacing is retained with clearly open negative space.')
add(4,'The rejected drawing changes the reference’s right-side pinch into a generic hand under a vertical card.',
 'Restored the landscape card and a right-side C-shaped grip, with index finger above and thumb in front.', '''
        # Landscape card; the index and thumb wrap its right edge.
        self.path('card',(23,6),(9,6),(6,9,3,3,False),(6,24),(9,27,3,3,False),(20,27))
        self.add_line('stripe',(6,14),(22,14))
        self.relate('connect','card','stripe')
        self.path('index',(34,14),(31,14),(31,6,4,4,True),(34,6),(42,18,12,12,True),(42,42))
        self.path('thumb',(30,31),(24,25),(20,29,3,3,False),(30,42))
        self.path('finger-inside',(34,14),(35,20),(30,27,7,7,True),(27,28))
        self.relate('connect','index','finger-inside')
''','The C-shaped pinch uses compact anatomical spacing to retain the reference action; card and thumb remain distinct at 48px.')
add(5,'The rejected nib looks like an arrow; three identical tall loops obscure the fist and omit the thumb.',
 'Made a broad split fountain nib, horizontal pen shaft, stepped rounded knuckles and a visible curled thumb.', '''
        # Pen passes behind upright gripping fingers; knuckles share one step/radius scheme.
        self.path('nib',(20,13),(13,10),(6,16),(13,22),(20,19))
        self.add_line('nib-slit',(6,16),(12,16))
        self.relate('connect','nib','nib-slit')
        self.path('pen-tail',(38,13),(42,13),(42,20),(38,20))
        self.path('fingers',(20,23),(20,12),(26,12,3,3,True),(26,9),(32,9,3,3,True),(32,11),(38,11,3,3,True),(38,30),(34,37,9,9,True),(34,42))
        self.path('thumb',(26,21),(20,21),(17,24,3,3,False),(17,29),(21,35,8,8,False),(23,38),(23,42))
        self.path('thumb-fold',(20,29),(24,27,4,4,False),(26,23,4,4,False),(26,21))
        self.add_line('finger-a',(26,12),(26,18))
        self.add_line('finger-b',(32,11),(32,19))
        self.relate('connect','finger-a','fingers')
        self.relate('connect','finger-b','fingers')
''','A three-finger grip and split nib require compact adjoining anatomy; rounded contours and openings remain readable.')
# Shared palm construction for horizontally supported objects, from the supplied originals.
PALM='''
        self.path('thumb',(6,34),(13,30),(24,30),(24,36,3,3,True),(18,36))
        self.path('palm',(6,42),(14,40),(25,42),(31,40,10,10,False),(41,32),(37,28,3,3,False),(27,35))
'''
add(6,'The rejected hand is reduced to a hook with two unrelated tails, and the gear center is a dot.',
 'Restored a circular toothed gear with central hole and an enclosing pinch hand with continuous wrist.', '''
        # Gear owns repeated teeth around its centre; the hand wraps the right half.
        self.path('gear',(15,6),(20,6),(21,11),(25,13),(29,12),(32,17),(28,21),(28,25),(23,29),(19,26),(15,27),(13,31),(8,29),(9,24),(6,20),(9,16),(8,12),(13,11),(15,6),closed=True)
        self.circle('hub',18,19,3)
        self.path('hand-back',(30,6),(35,7),(42,19,13,13,True),(42,42))
        self.path('finger',(30,6),(29,14,4,4,False),(34,19,6,6,True),(32,27,8,8,True),(28,30),(23,27),(18,31,4,4,False),(29,42))
        self.relate('connect','hand-back','finger')
''','Closely spaced gear teeth and gripping thumb preserve mechanical teamwork meaning; the hub and palm remain open.')
add(7,'The rejected claw hammer has a blocky diamond head and abstract zigzag grip.',
 'Rebuilt the distinct striking face and swept claw, diagonal shaft and wrapping fingers with a thumb.', '''
        # Diagonal shaft and fist, transverse striking face with a hooked claw.
        self.path('face',(26,6),(34,14),(28,20),(20,12),(26,6),closed=True)
        self.path('claw',(34,14),(40,21),(42,30,12,12,True),(36,34),(36,27,12,12,False),(28,20))
        self.path('shaft',(25,23),(20,28))
        self.path('shaft-end',(13,35),(6,42),(11,44),(18,37))
        self.path('fist',(12,36),(7,31),(7,27,3,3,True),(15,19),(19,19,3,3,True),(28,28))
        self.path('thumb',(22,24),(29,29),(31,34,7,7,True),(29,39),(31,44))
        for i,(x,y) in enumerate(((10,25),(15,21))):
            self.add_line(f'finger-{i}',(x,y),(x+7,y+7))
''','The hammer claw and two grip seams need compact spacing to preserve tool identity and action.','VRECT_L')
add(8,'The rejected heart sits on the thumb with no breathing room, and the angular hand loses the reference’s extended palm.',
 'Separated the rounded heart from the hand and restored the long thumb and rising supporting fingers.', '''
        # Symmetric heart floating above a deliberately asymmetric supporting hand.
        self.path('heart',(25,10),(15,10,5,5,False),(17,16,8,8,False),(25,23),(33,16),(35,10,8,8,False),(25,10,5,5,False),closed=True)
'''+PALM,'The supporting hand retains a narrow but clear thumb opening; heart and hand are distinctly separated.')
MASK='''
        # Mask contour has a shallow brow and rounded chin; hand occludes lower left.
        self.path('mask',(14,28),(14,9),(17,6,3,3,True),(27,8),(39,6),(42,9,3,3,True),(42,26),(35,35,10,10,True),(29,36))
        for side,x in enumerate((20,33)):
            self.path(f'eye-{side}',(x,17),(x+4,18),(x+2,22),(x,17),closed=True)
        self.path('hand',(6,42),(8,30),(13,27),(28,27),(29,33,3,3,True),(20,35))
        self.path('lower-fingers',(27,34),(28,39,3,3,True),(21,42),(14,42))
'''
add(9,'The rejected mask’s eyes are short hooks and the hand is only an arrowlike elbow.', 'Restored two almond eye openings and a hand wrapping the lower mask edge, with a separate thumb and curled fingers.',MASK,'Small eye openings and wrapping fingers are defining mask/hand cues; both holes remain visible at native size.')
add(10,'The rejected duplicate mask also uses hook eyes and an abstract lower-left pointer instead of a grip.', 'Restored the theatrical mask eye openings and lower-edge grip while preserving this icon’s ID.',MASK,'Small eye openings and wrapping fingers are defining mask/hand cues; both holes remain visible at native size.')
add(11,'The rejected megaphone is a horn above a letter-D loop; the hand is not recognizable and the handle is lost.',
 'Restored a tapered megaphone, distinct handle, thumb across the handle and curved lower palm.', '''
        # Horn flares right; separate handle and enclosing hand below its body.
        self.path('horn',(17,12),(28,11),(42,6),(42,28),(28,23),(17,22),(17,12),closed=True)
        self.path('rear',(17,12),(11,12),(6,17,5,5,False),(11,22,5,5,False),(17,22))
        self.path('handle',(17,22),(20,31),(27,31),(24,23))
        self.path('thumb',(7,31),(15,29),(28,29),(28,35,3,3,True),(22,35))
        self.path('palm',(7,42),(14,41),(22,42),(27,38,5,5,False),(28,35))
        self.relate('connect','rear','horn')
        self.relate('connect','horn','handle')
        self.relate('connect','thumb','palm')
''','The horn handle and wrapped fingers use compact spacing; their separation keeps the grasp clear.')
add(12,'The rejected wrench has a tiny U slot and the hand is reduced to parallel bars with dots.',
 'Widened the open jaw and restored a curved thumb mound, wrapping finger edge, and visible handle end.', '''
        # Open wrench head and vertical shaft; transverse fist encloses shaft.
        self.path('wrench',(19,6),(19,14),(27,14,4,4,False),(27,6),(35,17,11,11,True),(27,26),(27,29))
        self.path('wrench-left',(19,6),(11,17,11,11,False),(19,26),(19,29))
        self.path('hand',(6,35),(12,33),(17,26),(22,25),(22,29),(35,29),(35,35,3,3,True),(30,35))
        self.path('fingers',(35,35),(35,41,3,3,True),(22,42),(15,42),(9,44))
        self.path('handle-end',(20,42),(24,44,3,3,False),(27,42))
''','The open jaw and wrapped finger divisions take priority over uniform spacing; negative spaces remain visible.','VRECT_L')
add(13,'The rejected paper plane loses the long pointed nose and the hand becomes an angular block.',
 'Restored a long horizontal paper-plane silhouette, diagonal fold, and pinching thumb with curled fingers.', '''
        # Folded triangle points left; the thumb crosses in front of the lower fold.
        self.path('plane',(6,6),(42,10),(35,19),(6,6),closed=True)
        self.path('fold',(18,12),(35,19),(31,32))
        self.path('rear-fold',(12,12),(12,17,4,4,False),(23,27))
        self.path('thumb',(28,31),(26,23),(20,25,3,3,False),(22,35),(25,42))
        self.path('palm',(31,32),(32,42))
        self.path('fingers',(17,23),(13,23),(11,27,3,3,False),(16,31),(12,29),(10,32,3,3,False),(15,37),(19,42))
        self.relate('connect','plane','fold')
''','Plane folds and the pinching thumb require compact spacing; the pointed nose and hand silhouette stay legible.')
add(14,'The rejected rakhi loses its diagonal thread and the hand reads as a bent arrow.',
 'Restored the diagonal bracelet thread through a round medallion and a closed hand with rounded fingers.', '''
        # Circular rakhi on a diagonal thread; closed hand grasps the lower strand.
        self.circle('rakhi',34,14,6)
        self.add_line('thread-upper',(38,10),(42,6))
        self.add_line('thread-middle',(30,18),(24,24))
        self.add_line('thread-lower',(12,36),(6,42))
        self.path('hand',(13,37),(7,31),(7,25,5,5,True),(17,15),(22,20,4,4,True),(17,25),(21,22),(25,26,3,3,True),(22,29),(25,27),(29,31,3,3,True),(27,34),(29,32),(33,36,3,3,True),(26,42),(19,42),(13,37),closed=True)
        self.relate('connect','rakhi','thread-upper')
        self.relate('connect','rakhi','thread-middle')
''','Rounded finger steps are necessary to show the bracelet being held; the circular ornament and diagonal string are clear.')
add(15,'The rejected snake looks like a bird head above a hand and omits the coiled body and draped tail.',
 'Rebuilt the snake’s narrow head, S-shaped neck, body draped over the hand, and descending tail.', '''
        # Snake owns a smooth S neck and hanging tail; palm supports its coiled body.
        self.path('snake',(35,10),(31,6,5,5,False),(23,6),(20,13,6,6,False),(26,20),(29,25,6,6,True),(24,30),(17,27),(11,28,5,5,False),(14,37),(11,44))
        self.path('snake-back',(35,10),(32,16),(34,22,9,9,True),(30,32),(24,34),(18,32),(17,36),(16,42),(11,44))
        self.add_line('tongue',(35,10),(40,11))
        self.path('palm',(6,34),(11,34))
        self.path('fingers',(18,35),(25,37),(37,32),(42,35,3,3,True),(29,42),(20,42))
        self.add_line('wrist',(6,42),(11,42))
        self.relate('connect','snake','tongue')
''','The coiled snake and draped tail require compact spacing; the silhouette is serpentine and distinct from the supporting hand.','VRECT_L')
add(16,'The rejected teaspoon shows a round bowl and disconnected hooked hand; the reference has an oval bowl and a pinching grip.',
 'Restored an oval spoon bowl, diagonal handle, opposing index finger and thumb, and continuous wrist edges.', '''
        # Spoon bowl is oval, shaft diagonal; two continuous hand contours pinch it.
        self.path('bowl',(6,23),(20,23,7,5,True),(6,23,7,5,True),closed=True)
        self.add_line('shaft',(20,23),(42,12))
        self.path('index',(24,20),(23,14),(26,10,6,6,True),(36,6),(42,12,6,6,True))
        self.path('thumb',(35,29),(32,18),(26,20,3,3,False),(29,33),(35,42))
        self.path('fingers',(25,23),(22,26,3,3,False),(26,31),(29,33))
        self.add_line('wrist-back',(42,31),(42,42))
        self.relate('connect','shaft','bowl')
        self.relate('connect','index','shaft')
''','Opposing fingers and an oval spoon preserve the original action; compact grip spacing remains visually open.')
add(17,'The rejected wireless phone has a diagonal slash for a hand and only one pair of radio arcs.',
 'Restored two pairs of radio waves, a phone screen with bottom bezel, and a wrapping hand with thumb and wrist.', '''
        # Phone is upright; hand wraps its right edge, radio waves remain above both corners.
        self.path('phone',(26,42),(15,42),(12,39,3,3,True),(12,18),(15,15,3,3,True),(28,15),(31,18,3,3,True),(31,29))
        self.add_line('bezel',(12,34),(22,34))
        self.path('thumb',(34,34),(28,28),(23,32,3,3,False),(28,38),(30,42))
        self.path('back',(31,24),(38,31,8,8,True),(38,37),(42,42))
        for side in (-1,1):
            x=lambda a:24+side*a
            self.path(f'wave-outer-{side}',(x(18),13),(x(9),4,12,12,side==1))
            self.path(f'wave-inner-{side}',(x(12),13),(x(9),10,5,5,side==1))
        self.relate('connect','phone','bezel')
''','The two radio-wave tiers and hand grip are necessary cues; their compact spacing is reviewed at native size.','VRECT_L')
add(18,'The rejected kiosk lacks menu controls and the incomplete hand is just a vertical U.',
 'Restored the touchscreen controls, payment currency cue, pedestal, and complete raised index finger with palm.', '''
        # Kiosk screen/pedestal and hand are two main masses; index overlaps screen at lower right.
        self.path('screen',(24,30),(10,30),(6,26,4,4,True),(6,10),(10,6,4,4,True),(38,6),(42,10,4,4,True),(42,27))
        for i,y in enumerate((14,22)):
            self.add_line(f'menu-{i}',(13,y),(17,y))
        self.path('dollar',(34,13),(29,13),(29,18,3,3,False),(31,18),(31,23,3,3,True),(26,23))
        self.add_line('currency-stem',(30,10),(30,13))
        self.path('stand',(18,30),(14,38),(24,38))
        self.path('base',(6,42),(6,38),(14,38))
        self.path('hand',(29,42),(25,37),(29,33,3,3,True),(31,35),(31,28),(37,28,3,3,True),(37,34),(40,34),(42,38,4,4,True),(42,42))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','base')
        self.relate('connect','dollar','currency-stem')
''','Menu rows, currency and pointing finger must coexist on the kiosk; each remains legible with 4px stroke.')
add(19,'The rejected dryer removes every airflow stroke, so the upper object reads as a lid over an abstract hand.',
 'Restored a wall dryer housing, two downward airflow marks, and a recognizable cupped hand.', '''
        # Rounded upper dryer, repeated airflow series, open supporting palm.
        self.path('dryer',(8,17),(8,14),(16,6,8,8,True),(32,6),(40,14,8,8,True),(40,17),(8,17),closed=True)
        for i,x in enumerate((19,29)):
            self.add_line(f'air-{i}',(x,23),(x,26))
'''+PALM,'Airflow is essential for dryer meaning and needs closer vertical spacing; the two streams remain distinct from hand and housing.')
add(20,'The rejected IV bag is squat like a bottle and the stem looks like a stand rather than a tube into the hand.',
 'Restored an elongated hanging fluid bag, hanger loop, fluid level, outlet and a curved tube entering the hand.', '''
        # Tall IV bag and narrow tube above a receiving hand; bag owns hanger and fluid level.
        self.path('bag',(20,8),(31,8),(35,12,4,4,True),(35,23),(31,27,4,4,True),(20,27),(16,23,4,4,True),(16,12),(20,8,4,4,True),closed=True)
        self.path('hanger',(22,8),(22,4),(29,4),(29,8))
        self.add_line('fluid',(23,18),(28,18))
        self.path('tube',(26,27),(26,30),(21,35,5,5,True))
        self.path('thumb',(8,34),(15,31),(21,31),(24,34,3,3,True),(24,36),(18,36))
        self.path('palm',(8,44),(16,42),(26,44),(32,41),(39,35),(35,31,3,3,False),(27,37))
        self.relate('connect','bag','hanger')
        self.relate('connect','bag','tube')
''','Compact fluid bag fittings and the receiving hand preserve the transfusion action; bag, tube and palm remain distinguishable.','VRECT_L')

def make(n,rev='r1'):
 item=ITEMS[n-1]; data=D[n]; ref=Path(item['reference']); source_uuid=re.search(r'[0-9a-f-]{36}$',ref.stem).group(); concept=ref.stem[:-37]
 run=Path('icon_set/work/primitive-make-ray')/source_uuid/f'20260928T182143Z-fix-{n:02d}-{rev}'
 run.mkdir(parents=True,exist_ok=False)
 ident=item['key'].split('/',1)[1]
 metadata=dict(concept=concept,source_uuid=source_uuid,reference_path=str(ref),icon_id=ident,author=AUTHOR,feedback=item['feedback'],comparison=data['observation'],change=data['change'])
 (run/f'{ident}.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 source=f'''"""{data['change']}
Before: {data['observation']}
Construction: Lucide hand-heart/hand-grab for coherent thumb, knuckles and palm;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected; isolated hands have no detached head.
Keyshape {data['keyshape']}; complete drawing remains on 48x48 with 4px strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {source_uuid!r}
SOURCE_PATH = {str(ref)!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {ident!r}
    keyshape = Keyshape.{data['keyshape']}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hands'
    aliases = ()
    keywords = ('hand', {concept!r})
{HELPER}
    def build(self):
{data['body']}
'''
 module=run/(ident.replace('-','_')+'_'+source_uuid.replace('-','_')+'.py'); module.write_text(source)
 icon=load_icon(module); report=icon.validate_icon(); svg=icon.to_svg(); (run/f'{ident}.svg').write_text(svg)
 (run/'validation.txt').write_text(report.describe())
 render_previews(svg,ident,48,run)
 import cairosvg
 cairosvg.svg2png(url=str(ref),write_to=str(run/'reference.png'),output_width=384,output_height=384)
 entry=dict(metadata,run=str(run),module=str(module),svg=str(run/f'{ident}.svg'),validation=report.status,errors=report.errors,warnings=report.warnings,exception_reason=data['exception_reason'],omissions=data['omissions'],keyshape=data['keyshape'])
 (run/'draft.json').write_text(json.dumps(entry,indent=2))
 print(n,ident,report.status,len(report.errors),len(report.warnings),flush=True)
 return entry

def sheet(entries,filename):
 out=Image.new('RGB',(1000,len(entries)*210),'#e8e8e8'); draw=ImageDraw.Draw(out)
 for row,e in enumerate(entries):
  y=row*210; draw.text((10,y+2),e['icon_id'],fill='black')
  ref=Image.open(Path(e['run'])/'reference.png').convert('RGBA'); ref.thumbnail((165,165)); bg=Image.new('RGBA',ref.size,'white');bg.alpha_composite(ref);out.paste(bg.convert('RGB'),(10,y+25))
  for col,theme in enumerate(('light','dark')):
   p=Path(e['run'])/f'preview-{theme}-384.png'; im=Image.open(p).convert('RGB'); im.thumbnail((165,165));out.paste(im,(220+col*360,y+25))
   small=Image.open(Path(e['run'])/f'preview-{theme}-48.png');out.paste(small,(410+col*360,y+75))
 out.save(BATCH/filename)
if __name__=='__main__':
 nums=[int(a) for a in sys.argv[1:]] or list(D)
 entries=[make(n) for n in nums]
 (BATCH/'drafts.json').write_text(json.dumps(entries,indent=2))
 for p in range(0,len(entries),5): sheet(entries[p:p+5],f'drafts-{p//5+1}.png')
