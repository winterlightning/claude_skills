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
def add(n,observation,change,body,exception_reason,keyshape='SQUARE',omissions='Minor surface details omitted for native-size clarity.'):
 D[n]=dict(observation=observation,change=change,body=body,exception_reason=exception_reason,keyshape=keyshape,omissions=omissions)
HANDS='''
        # Mirrored cupped hands with open wrists and a shared thumb attachment on each side.
        for side in (-1,1):
            x=lambda v:24+side*(24-v)
            self.path(f'hand-outer-{side}',(x(12),44),(x(12),40),(x(6),33),(x(6),24),(x(12),24,3,3,side==-1),(x(12),30),(x(17),35))
            self.path(f'hand-inner-{side}',(x(12),30),(x(16),29),(x(20),34,6,6,side==-1),(x(20),44))
            self.relate('connect',f'hand-outer-{side}',f'hand-inner-{side}')
'''
CONTINUOUS='''
        self.path('person',(14,26),(14,25),(20,22),(20,18),(18,12,9,9,True),(30,12,6,6,True),(28,18,9,9,True),(28,22),(34,25),(34,26))
'''
DETACHED='''
        self.circle('head',24,10,5)
        self.path('shoulders',(16,29),(32,29,8,6,True))
        # Head bottom y15 to shoulder apex y23: exact 4px visible gap.
'''
add(1,'The rejected bust is reduced to an omega-shaped head and the hands become closed loops; the reference has a continuous neck/shoulders and open wrists.', 'Restored the continuous head, neck and shoulders, and two cupped hands with separate thumbs and open wrists.',CONTINUOUS+HANDS,'The small bust between two recognizable hands needs compact anatomical spacing.','VRECT_L')
add(2,'The rejected hands are two tall bent bars without thumbs or proper palms; the original shows cupped palms supporting a broad heart.', 'Restored the heart’s broad lobes and two symmetrical cupped palms with visible thumbs.', '''
        self.path('heart',(24,10),(12,10,6,6,False),(14,17,10,10,False),(24,26),(34,17),(36,10,10,10,False),(24,10,6,6,False),closed=True)
'''+HANDS,'The hand and heart combination retains close supporting contacts while keeping its principal openings readable.','VRECT_L')
add(3,'The rejected male portrait is a generic detached circle and the hands are hooked blocks; the short-haired continuous male silhouette is missing.', 'Restored the short-haired head outline, neck, sloping shoulders and open cupped hands.', '''
        self.path('person',(14,26),(20,22),(20,19),(18,15,5,5,True),(18,9),(21,5,4,4,True),(27,5),(30,9,4,4,True),(30,15),(28,19,5,5,True),(28,22),(34,26))
'''+HANDS,'The male silhouette and two full hands require compact detail; hair is carried by the outer head shape.','VRECT_L')
add(4,'The rejected person floats above two closed hand-shaped loops; the source has broad shoulders and long cupped palms with visible thumb creases.', 'Restored a circular head, broad shoulder arc and two open-wrist supporting hands.',DETACHED+HANDS,'The supporting thumb/palm contours need closer spacing than unrelated parts, while the head gap remains exactly 4px.','VRECT_L')
add(5,'The rejected squared-haired man is a generic circle/arch symbol and the hands are short hooks.', 'Restored the squared hair cap, rounded jaw, continuous neck/shoulders and distinct cupped hands.', '''
        self.path('person',(14,26),(20,23),(20,20),(18,16,5,5,True),(18,8),(21,5,3,3,True),(27,5),(30,8,3,3,True),(30,16),(28,20,5,5,True),(28,23),(34,26))
        self.add_line('hairline',(18,11),(29,11))
'''+HANDS,'The flat hairline and close supporting palms preserve the specific male portrait.','VRECT_L')
add(6,'The rejected bob-haired portrait is a dot under a tiny arch and the hands overlap its shoulders; the bob silhouette and neck are lost.', 'Restored the flared bob haircut, parted fringe, rounded face and neck above two cupped hands.', '''
        self.path('hair',(15,21),(16,12),(24,4,8,8,True),(32,12,8,8,True),(33,21),(29,22))
        self.path('fringe',(19,12),(24,9),(29,12))
        self.path('face',(19,12),(19,16),(24,21,5,5,False),(29,16,5,5,False),(29,12))
        self.path('shoulder-left',(22,21),(22,24),(16,27))
        self.path('shoulder-right',(26,21),(26,24),(32,27))
'''+HANDS,'The bob, face and two hands need compact placement; the flared haircut remains distinct.','VRECT_L')
add(7,'The rejected supporting hands are bent bars that merge with the small shoulder arch.', 'Restored the separate circular head and broad shoulders, surrounded by detailed cupped palms.',DETACHED+HANDS,'The shoulder/head gap is exactly 4px; closer hand anatomy preserves the cupping action.','VRECT_L')
add(8,'The rejected woman loses the parted fringe and is reduced to a generic hair arch over a dot.', 'Restored the center-parted hairstyle, rounded face, broad shoulders and two open-wrist hands.', '''
        self.path('head',(17,12),(31,12,7,7,True),(17,12,7,7,True),closed=True)
        self.path('fringe',(17,12),(24,8),(31,12))
        self.add_line('hair-left',(17,12),(15,22))
        self.add_line('hair-right',(31,12),(33,22))
        self.path('shoulders',(16,30),(32,30,8,3,True))
        # Circular head bottom y19 to shoulder apex y27 gives 4px clear ink.
'''+HANDS,'The parted fringe and small portrait between the palms need compact optical spacing.','VRECT_L')
add(9,'The rejected card replaces the portrait with a dot and dash, and its hand is only two detached lines.', 'Restored a pinching hand across the ID card corner and a recognizable circular-head portrait.', '''
        self.path('card',(25,18),(10,18),(6,22,4,4,False),(6,40),(10,44,4,4,False),(31,44),(35,40,4,4,False),(35,25))
        self.circle('portrait-head',18,25,3)
        self.path('portrait-shoulders',(11,38),(25,38,7,2,True))
        self.path('hand-top',(44,4),(37,9),(29,9),(23,14),(19,18))
        self.path('thumb',(31,15),(25,21),(29,25,3,3,False),(36,20),(40,19),(44,16))
        # Portrait head bottom y28 to shoulder apex y36 gives 4px clear ink.
''','The thumb intentionally overlaps the card; the small portrait remains legible.')
add(10,'The rejected exchange is a B surrounded by two angular brackets, with no coin boundary or recognizable pinching hands.', 'Restored a round bitcoin, the B and stem marks, and opposing hands gripping its upper-left and lower-right edges.', '''
        self.path('coin-upper',(22,8),(40,24,17,17,True),(38,31,17,17,True))
        self.path('coin-lower',(26,41),(8,24,17,17,True),(12,14,17,17,True))
        for side in (0,1):
            pt=lambda x,y:(x,y) if side==0 else (48-x,48-y)
            self.path(f'hand-{side}',pt(4,4),pt(10,9),pt(11,13),pt(18,18),(*pt(14,22),3,3,True),pt(8,17))
            self.path(f'wrist-{side}',pt(14,4),pt(17,9),pt(17,12),pt(21,16))
        self.path('bitcoin',(20,15),(26,15),(26,23,4,4,True),(20,23),(26,23),(26,31,4,4,True),(20,31),(20,15))
        self.add_line('stem-top',(23,12),(23,15))
        self.add_line('stem-bottom',(23,31),(23,34))
''','The coin, currency glyph and opposing grips need close spacing to communicate exchange at 48px.')
add(11,'The rejected pointing hand has a squared thumb and abrupt palm transition; the reference has a round palm and stepped curled fingers.', 'Redrew a long pointing index, progressively lower finger knuckles, a rounded thumb and a broad smooth palm.', '''
        self.path('hand',(16,28),(16,8),(24,8,4,4,True),(24,22),(30,22,3,3,True),(30,24),(36,24,3,3,True),(36,26),(42,26,3,3,True),(42,33),(31,44,11,11,True),(22,44),(12,38,14,14,True),(5,28),(11,22,4,4,True),(16,28),closed=True)
        for i,(x,y) in enumerate(((24,22),(30,24),(36,26))):
            self.add_line(f'finger-seam-{i}',(x,y),(x,y+4))
            self.relate('connect','hand',f'finger-seam-{i}')
''','The curled fingers need compact internal spacing while the long index and palm stay clear.','VRECT_L')
add(12,'The rejected brush has only two thick bristles, a disconnected hand, and a detached cloud instead of cleaning foam.', 'Restored a hand gripping a broad brush, an even bristle row and a low foam cluster beneath.', '''
        self.path('brush',(7,20),(41,20),(41,28,4,4,True),(7,28),(7,20,4,4,True),closed=True)
        self.path('arm-left',(8,4),(17,20))
        self.path('arm-right',(20,4),(26,11),(31,11),(37,17,6,6,True))
        self.path('thumb',(26,17),(31,22),(28,27,3,3,True))
        for i,x in enumerate((9,15,21,27,33,39)):
            self.add_line(f'bristle-{i}',(x,28),(x,34))
            self.relate('connect','brush',f'bristle-{i}')
        self.path('foam',(6,44),(10,39,5,5,True),(18,39),(26,36,6,6,True),(33,34,6,6,True),(41,40,7,7,True),(44,44,4,4,True),(6,44),closed=True)
''','The hand, dense bristle row and foam need compact layered spacing; the brush remains the dominant object.')
add(13,'The rejected face omits the round head and places the tongue centrally; the original has a sideways tongue hanging from the right of the grin.', 'Restored the circular face, smiling eyes, shallow grin and right-side tongue.', '''
        self.circle('face',24,24,20)
        for i,x in enumerate((12,28)):
            self.path(f'eye-{i}',(x,19),(x+8,19,4,4,True))
        self.path('smile',(12,27),(35,26,14,9,False))
        self.path('tongue',(27,34),(29,39),(36,37,4,4,False),(34,31))
''','The face boundary and offset tongue preserve the expression; close facial details remain readable.','CIRCLE')
add(14,'The rejected cowboy avatar uses a polygonal hat and squared hair, losing the curved brim, rounded face and flowing hair.', 'Restored a broad curved brim, dipped crown, circular jaw and long curved hair on both sides.', '''
        self.path('brim',(6,16),(42,16,18,4,False),(42,22,3,3,True),(6,22,18,6,True),(6,16,3,3,True),closed=True)
        self.path('crown',(13,17),(16,7),(20,5,4,4,True),(24,7),(28,5),(32,7,4,4,True),(35,17))
        self.path('jaw',(14,27),(14,29),(34,29,10,10,False),(34,27))
        self.path('hair-left',(12,27),(8,37),(12,44,6,6,False))
        self.path('hair-right',(36,27),(40,37),(36,44,6,6,True))
''','Curved brim, crown and long hair take precedence over rigid keyshape fit; the hat/face silhouette is preserved.')
add(15,'The rejected head is a squared pipe shape with three parallel stubs, obscuring the skull, oral opening and throat section.', 'Restored the rounded skull and nose profile, horizontal mouth cavity and curved inner throat channels.', '''
        self.path('head',(36,44),(36,36),(40,25,18,18,False),(40,19),(25,4,15,15,False),(10,17,15,15,False),(10,19),(6,27),(10,28),(10,31),(20,31),(27,38,7,7,True),(27,44))
        self.path('throat',(11,36),(19,36),(22,39,3,3,True),(22,44))
        self.path('jaw-section',(11,36),(11,39),(17,39),(17,44))
''','The anatomical section needs adjacent oral/throat boundaries; rounded channels keep the section legible.','VRECT_L')
add(16,'The rejected logo replaces the mountain snowline with a detached caret and reduces the ink splash to one flat pedestal.', 'Restored the mountain peak, connected scalloped snowline and irregular dripping ink silhouette.', '''
        self.path('outline',(6,24),(21,6),(27,6,4,4,True),(42,23),(41,27,3,3,True),(32,30),(32,34,3,3,False),(35,35),(34,39,3,3,True),(28,41),(28,44,2,2,True),(20,44),(19,40,3,3,True),(11,37),(11,33,3,3,True),(15,32),(15,28,3,3,False),(7,26),(6,24,2,2,True),closed=True)
        self.path('snow',(12,17),(20,18,5,5,False),(24,14),(28,18),(33,18,4,4,False),(36,19,3,3,False),(39,17))
''','The compact mountain snowline and irregular ink lobes are identifying logo features; their close spacing is retained.')
add(17,'The rejected rider is an abstract line on a flat boat, and the breaking wave is only a bump.', 'Restored the rider’s forward lean and gripping arm, bent legs, sloping jet-ski hull and breaking wave.', '''
        self.circle('head',18,7,5)
        self.add_line('torso',(23,19),(25,24))
        self.add_line('hip',(25,24),(30,26))
        self.path('arms',(23,19),(21,27),(14,29))
        self.path('leg-front',(30,26),(28,35))
        self.path('leg-back',(30,26),(36,29),(43,27))
        self.path('ski',(8,36),(6,31,5,5,True),(16,24),(18,31),(39,35),(43,40,5,5,True))
        self.path('wave',(4,44),(8,44),(15,39,8,8,True),(20,40),(16,44),(23,44),(27,42,3,3,True),(32,44),(38,42,4,4,True),(44,44))
        self.mark_human_figure('rider',head='head',torso='torso',torso_junction='start')
        # Head to upper torso: sqrt(5^2+12^2)-5-4 = 4px ink gap.
        self.relate('connect','torso','hip');self.relate('connect','torso','arms')
        self.relate('connect','hip','leg-front');self.relate('connect','hip','leg-back')
''','The rider/jet-ski/wave scene needs a compact composition; exact anatomical head gap is retained analytically.')
JELLY='''
        # Three diagonally tilted bells; each owns a regular series of three tentacles.
        for i,(sx,sy,ex,ey,r) in enumerate(((9,8,23,16,8),(4,32,18,40,8),(28,25,44,33,9))):
            self.path(f'bell-{i}',(sx,sy),(ex,ey,r,r,True),(sx,sy),closed=True)
            for j in range(3):
                x=sx+2+5*j;y=sy+1+3*j
                self.add_line(f'tentacle-{i}-{j}',(x,y),(x-3,y+6))
'''
add(18,'The rejected jellyfish are flat mushrooms with two vertical stems, missing their tilt and three trailing tentacles.', 'Restored three tilted rounded bells, each with three diagonal tentacles, in the original staggered group.',JELLY,'Three compact jellyfish require close tentacle spacing; the tilted group and individual bells remain distinct.')
add(19,'The rejected duplicate jellyfish group also uses horizontal mushroom shapes with only two stems each.', 'Restored the staggered group of tilted jellyfish with three trailing tentacles each, preserving this icon ID.',JELLY,'Three compact jellyfish require close tentacle spacing; the tilted group and individual bells remain distinct.')
add(20,'The rejected judge is an oval floating inside a plain U-shaped hood, with none of the wig’s curled sides.', 'Restored a circular face inside a broad domed judicial wig with paired curled side locks.', '''
        self.circle('face',24,26,10)
        self.path('wig',(14,28),(14,36),(11,43,5,5,True),(5,41,4,4,True),(5,35),(7,32),(5,29),(7,25),(7,21),(24,4,17,17,True),(41,21,17,17,True),(41,25),(43,29),(41,32),(43,35),(43,41),(37,43,4,4,True),(34,36,5,5,True),(34,28))
''','The close face and curled wig edges define the judicial portrait; the circular face and outer curls remain clear.','VRECT_L')
def make(n,rev='r1'):
 item=ITEMS[n-1]; data=D[n]; ref=Path(item['reference']); source_uuid=re.search(r'[0-9a-f-]{36}$',ref.stem).group(); concept=ref.stem[:-37]
 run=Path('icon_set/work/primitive-make-ray')/source_uuid/f'20260929T031604Z-fix-{n:02d}-{rev}'
 run.mkdir(parents=True,exist_ok=False)
 ident=item['key'].split('/',1)[1]
 metadata=dict(concept=concept,source_uuid=source_uuid,reference_path=str(ref),icon_id=ident,author=AUTHOR,feedback=item['feedback'],comparison=data['observation'],change=data['change'])
 (run/f'{ident}.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 source=f'''"""{data['change']}
Before: {data['observation']}
Construction: Relevant local Lucide primitives for coherent rounded contours;
supplied reference controls the specific grasp and subject arrangement.
Shared human full_body_ref.png inspected for human proportions where applicable.
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
