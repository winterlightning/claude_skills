from pathlib import Path
import json, textwrap, sys
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
BATCH=json.loads((ROOT/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[r['uuid'] for r in BATCH]
SOURCE_PATH=[r['reference'] for r in BATCH]
HELPERS='''
def circle(icon, name, cx, cy, r):
    icon.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-top',name+'-bottom',closed=True)

def rounded(icon,name,x0,y0,x1,y1,r):
    points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
    ids=[]
    for j,a in enumerate(points):
        b=points[(j+1)%8];n=f'{name}-{j}';ids.append(n)
        if j%2: icon.add_arc(n,a,b,radius_x=r)
        else: icon.add_line(n,a,b)
    icon.add_contour(name,*ids,closed=True)

def curve(icon,name,start,*segments,closed=False):
    icon.add_bezier(name+'-curve',start,*segments)
    icon.add_contour(name,name+'-curve',closed=closed)
'''
SPECS={}
def define(i,keyshape,problem,change,body,refs,exception=None):
 SPECS[i]=dict(keyshape=keyshape,problem=problem,change=change,body=textwrap.dedent(body).strip(),refs=refs,exception=exception)

define(0,'SQUARE','The thick compact recess and short slots read as a generic switch face.','Enlarged the flattened round recess, lengthened the two parallel Type A slots and opened the margins.', '''
rounded(self,'plate',4,4,44,44,6)
curve(self,'recess',(17,11),((9,16),(7,30),(17,37)),((21,37),(27,37),(31,37)),((41,30),(39,16),(31,11)),((27,11),(21,11),(17,11)),closed=True)
for x in (19,29): self.add_line(f'slot-{x}',(x,20),(x,28))
''','plug: rounded housing and paired terminal spacing','The nested plate and flattened recess need 2–3px visible margins at 48px; preserve both socket identity and plate silhouette with 4px strokes.')
define(1,'SQUARE','The tiny holes and heavy concentric frames read as a face; earth contacts are cramped.','Balanced the circular recess and clearly separated two pin holes with aligned earth contacts.', '''
rounded(self,'plate',4,4,44,44,6)
circle(self,'recess',24,24,14)
for x in (18,30): circle(self,f'pin-{x}',x,24,2)
self.add_line('earth-top',(24,10),(24,15))
self.add_line('earth-bottom',(24,33),(24,38))
self.relate('connect','recess','earth-top')
self.relate('connect','recess','earth-bottom')
''','plug: paired terminals and rounded housing','Retain the defining two circular holes and top/bottom earth tabs within a complete socket plate; compact concentric margins remain visibly open at 48px.')
HANDSET='''
# One smooth bowed spine and two rounded, forward-facing receiver cups.
curve(self,'handset',(29,4),((18,4),(10,12),(10,24)),((10,36),(18,44),(29,44)),((33,44),(38,44),(38,40)),((38,38),(36,34),(35,32)),((34,30),(28,32),(26,30)),((23,27),(23,21),(26,18)),((28,16),(34,18),(35,16)),((36,14),(38,8),(38,7)),((38,4),(33,4),(29,4)),closed=True)
'''
for i in (4,5):
 define(i,'VRECT_M','The receiver became a wide block letter C instead of a bowed handset.','Restored the narrow curved spine, cupped earpiece and mouthpiece, and tapered inner grip.',HANDSET,'phone: continuous rounded receiver contour and smooth inner bend')
define(6,'VRECT_L','The thermometer has an oversized blunt column and the scale became dots.','Restored a slender tube, round bulb, fluid stem and horizontal measurement ticks.', '''
curve(self,'thermometer',(12,10),((12,2),(26,2),(26,10)),((26,16),(26,22),(26,27)),((34,34),(30,44),(19,44)),((8,44),(4,34),(12,27)),((12,22),(12,16),(12,10)),closed=True)
self.add_line('mercury',(19,17),(19,35))
self.add_line('scale-top',(35,11),(40,11))
self.add_line('scale-middle',(35,21),(38,21))
''','thermometer: narrow stem and rounded bulb','A readable liquid column needs compact spacing inside the 14-unit tube; keep the 4px line and clearly open bulb instead of deleting the measuring cue.')
define(7,'SQUARE','Octagonal housings and a solid dot obscure the two switch types.','Replaced polygon corners with rounded switch housings and restored the circular left button and right rocker divider.', '''
rounded(self,'left-switch',4,4,20,44,4)
rounded(self,'right-switch',28,4,44,44,4)
circle(self,'left-button',12,35,3)
self.add_line('rocker-divider',(28,30),(44,30))
self.relate('connect','right-switch','rocker-divider')
''','toggle-left: rounded housing and circular knob','Two complete vertical controls require 16-unit housings and a 3-radius button; the button remains legible despite compact housing clearance.')
define(12,'HRECT_M','The reference almond eye was replaced by an oval with a heavy tiny pupil.','Restored pointed eye corners, a balanced almond contour and a larger circular iris.', '''
curve(self,'eye',(4,24),((11,14),(17,10),(24,10)),((31,10),(37,14),(44,24)),((37,34),(31,38),(24,38)),((17,38),(11,34),(4,24)),closed=True)
circle(self,'iris',24,24,6)
''','eye: pointed almond outline and centered circular iris')
define(18,'SQUARE','The distinctive outlined diagonal parallelogram was reduced to a slash.','Restored the closed slanted logo bar within its rounded square.', '''
rounded(self,'frame',6,6,42,42,5)
self.add_polyline('logo',(15,34),(25,14),(35,14),(25,34),closed=True)
''','monitor: consistent rounded frame','The WIP mark is an outlined parallelogram, not a slash. Its narrow diagonal opening and compact right frame gap are retained at 4px stroke to preserve the logo.')

def write(i,attempt='01'):
 r=BATCH[i];s=SPECS[i];dest=REPO/'icon_set/work/primitive-make-ray'/r['uuid']/f'20260929T090411Z-meaning-{attempt}'
 dest.mkdir(parents=True,exist_ok=False)
 metadata={k:r[k] for k in ('concept','reference','uuid')};metadata={'concept':r['concept'],'source_uuid':r['uuid'],'reference_path':r['reference']}
 (dest/f'{r["icon_id"]}.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 (dest/'review-before.md').write_text(f"Original: {r['reference']}\n\nRejected drawing: {r['claim_dir']}/before/{r['icon_id']}.svg\n\nObserved problem: {s['problem']}\n\nFeedback: {r['feedback']}\n\nRevision: {s['change']}\n\nConstruction reference: {s['refs']}\n\nKeyshape: {s['keyshape']}. Preserve natural proportions and defining details.\n")
 module=dest/(r['icon_id'].replace('-','_')+'_'+r['uuid'].replace('-','_')+'.py')
 content=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {r['uuid']!r}
SOURCE_PATH = {r['reference']!r}
AUTHOR = "gpt-6"

# Original/current comparison: {s['problem']}
# Revision plan: {s['change']}
# Construction reference: {s['refs']}
'''+HELPERS+f'''
class Drawing(Solo48):
    icon_id = {r['icon_id']!r}
    keyshape = Keyshape.{s['keyshape']}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ({r['concept']!r},)

    def build(self):
'''+textwrap.indent(s['body'],'        ')+'\n'
 module.write_text(content)
 (dest/'design.json').write_text(json.dumps(s,indent=2))
 print(i,dest.relative_to(REPO),flush=True)
 return dest
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):write(i)
