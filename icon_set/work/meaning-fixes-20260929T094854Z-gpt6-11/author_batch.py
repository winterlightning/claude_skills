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

def write(i,attempt='01'):
 r=BATCH[i];s=SPECS[i];dest=REPO/'icon_set/work/primitive-make-ray'/r['uuid']/f'20260929T094854Z-gpt6-{attempt}'
 dest.mkdir(parents=True,exist_ok=False)
 r['result_dir']=str(dest.relative_to(REPO))
 (ROOT/'batch.json').write_text(json.dumps(BATCH,indent=2))
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

define(0,'SQUARE','The second person was omitted; the scene became one person holding a small square beside an unrelated box.','Restored the two people facing each other, an angled document held up by the visitor, and the attendant reaching across a tapered counter.', '''
# Human construction: both heads r4 at y8; actual upper torso junction y20 gives 20-(8+4)=8 centerline /4 ink.
for who,cx in (('visitor',7),('attendant',41)):
    circle(self,who+'-head',cx,8,4)
    self.add_line(who+'-torso',(cx,20),(cx,44))
    self.mark_human_figure(who,head=who+'-head',torso=who+'-torso',torso_junction='start')
self.add_polyline('paper',(21,4),(30,6),(27,20),(18,18),closed=True)
curve(self,'visitor-arm',(7,20),((11,20),(13,26),(17,23)),((19,22),(20,20),(18,18)))
self.relate('connect','visitor-arm','visitor-torso');self.relate('connect','visitor-arm','paper')
self.add_polyline('counter',(26,30),(37,30),(35,44),(28,44),closed=True)
self.add_polyline('attendant-arm',(41,20),(34,30),(30,30))
self.relate('connect','attendant-arm','attendant-torso');self.relate('connect','attendant-arm','counter')
''','human_ref/full_body_ref.png: outlined circular heads and round-ended limbs; original supplies the facing people and paper exchange','Two full figures, an angled document and a counter require compact spacing at 48px; retain their roles and exact 4px detached head gaps with 4px strokes.')

define(1,'SQUARE','The helper and seated user were reduced to disconnected-looking heads, a horizontal bar and cramped angular limbs; the wheel was too small.','Restored a walking helper, bent pushing arm, larger open wheelchair wheel and a clear seated figure with a forward leg.', '''
# Shared human reference. Left head (10,7),r4 -> torso(10,19); right head(33,11),r4 -> torso(33,23): both gaps exactly4 ink.
circle(self,'helper-head',10,7,4)
curve(self,'helper-torso',(10,19),((10,23),(8,26),(8,30)))
self.add_line('helper-back-leg',(8,30),(4,44))
self.add_polyline('helper-front-leg',(8,30),(14,35),(17,43))
self.add_polyline('pushing-arm',(10,19),(17,24),(33,23))
for part in ('helper-back-leg','helper-front-leg','pushing-arm'):self.relate('connect','helper-torso',part)
self.relate('connect','helper-back-leg','helper-front-leg')
circle(self,'user-head',33,11,4)
self.add_line('user-torso',(33,23),(33,32))
self.add_polyline('user-leg',(33,32),(40,32),(45,43))
self.relate('connect','user-torso','user-leg');self.relate('connect','pushing-arm','user-torso')
curve(self,'wheel',(21,27),((14,31),(15,41),(24,44)),((31,46),(38,42),(38,36)))
self.mark_human_figure('helper',head='helper-head',torso='helper-torso-curve',torso_junction='start')
self.mark_human_figure('wheelchair-user',head='user-head',torso='user-torso',torso_junction='start')
''','human_ref/full_body_ref.png: coherent limbs and circular heads; accessibility: open wheelchair arc and seated leg','Preserve two people in a legible pushing pose with a full wheel. Compact arm/seat/wheel spacing is intentional; both head-to-torso gaps remain exactly4px.')

define(2,'SQUARE','The overhead danger was reduced to a hanging zigzag and the figure lost its raised forearm and reaching gesture.','Restored the stepped overhead wire, angular electrical discharge and a person raising a bent arm toward it.', '''
self.add_polyline('wire',(4,4),(32,4),(32,10),(44,10))
self.add_polyline('discharge',(32,4),(24,11),(29,13),(26,18),(34,15))
self.relate('connect','wire','discharge')
# Head(16,22),r4; torso starts(16,34): 34-(22+4)=8 centerline,4 ink.
circle(self,'head',16,22,4)
self.add_line('torso',(16,34),(16,44))
curve(self,'raised-arm',(16,34),((25,34),(33,35),(33,28)),((33,26),(33,24),(33,22)))
self.add_line('lower-arm',(16,34),(6,43))
self.relate('connect','torso','raised-arm');self.relate('connect','torso','lower-arm');self.relate('connect','raised-arm','lower-arm')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: circular head and bent arm; original supplies the wire and discharge','The overhead wire and electrical discharge must remain above the raised hand. Preserve compact scene spacing and the exact4px human head gap.')

define(3,'SQUARE','The profile face became an open C with a dot eye; it lost the distressed X eye and the body cue.','Restored the open-mouth profile, distressed X eye and a tall flame beside the face.', '''
# Face shown in profile rather than a generic floating circle; original X eye carries the reaction.
curve(self,'flame',(10,4),((10,10),(15,13),(19,11)),((19,7),(17,5),(17,5)),((25,9),(27,20),(19,25)),((12,29),(5,22),(5,16)),((5,12),(8,7),(10,4)),closed=True)
curve(self,'face',(29,16),((41,12),(46,21),(43,30)),((41,38),(30,40),(23,34)),((22,33),(22,30),(22,29)),((31,28),(32,21),(29,16)),closed=True)
self.add_line('eye-a',(34,22),(38,26));self.add_line('eye-b',(38,22),(34,26));self.relate('connect','eye-a','eye-b')
curve(self,'shoulders',(22,46),((25,42),(39,42),(43,46)))
''','flame: asymmetric tongue and rounded lower lobe; supplied original: open-mouth profile and X eye','The distressed profile, flame and shoulder cue need compact spacing. Keep all strokes4px while retaining the expression rather than substituting a generic dot eye.')

define(4,'SQUARE','The chart bars floated above a flat empty envelope and the trend became a detached tiny arrow.','Restored three outlined columns rising out of an open envelope and a continuous upward trend with arrowhead.', '''
# Bars terminate exactly on the two envelope-flap diagonals.
self.add_polyline('envelope',(4,28),(10,31),(16,34),(22,37),(24,38),(28,36),(34,33),(40,30),(44,28),(44,44),(4,44),closed=True)
for name,x0,x1,top,y0,y1 in [('low',10,16,22,31,34),('mid',22,28,18,37,36),('high',34,40,14,33,30)]:
    self.add_polyline(name,(x0,y0),(x0,top),(x1,top),(x1,y1))
    self.relate('connect','envelope',name)
self.add_polyline('trend',(6,16),(14,9),(21,12),(29,6),(34,9),(44,3))
self.add_polyline('arrowhead',(36,3),(44,3),(44,11));self.relate('connect','trend','arrowhead')
''','mail: envelope flap; chart-no-axes-combined: rising columns with an ascending polyline','Three visible columns and the trend arrow are the defining meaning. Their compact2px column interiors and gaps are intentional within the complete48px envelope composition.')

MONITOR='''
# Frame4,4–44,33; a true11-unit stand reaches y44 and keeps the screen distinct from its base.
rounded(self,'monitor',4,4,44,33,4)
self.add_line('stand',(24,33),(24,44));self.add_line('base',(15,44),(33,44))
self.relate('connect','monitor','stand');self.relate('connect','stand','base')
'''
define(5,'SQUARE','The shuttlecock became a solid three-pronged blob and the monitor stand was too short.','Lengthened the stand and rebuilt the shuttlecock with a distinct circular cork and outlined feather fan.', MONITOR+'''
circle(self,'cork',15,25,3)
curve(self,'feather-outline',(15,22),((16,18),(17,13),(18,10)),((19,7),(23,9),(22,13)),((25,8),(30,11),(27,16)),((32,11),(36,16),(32,19)),((28,21),(22,24),(18,25)))
self.relate('connect','cork','feather-outline')
self.add_line('feather-rib',(27,16),(18,25));self.relate('connect','feather-rib','feather-outline');self.relate('connect','feather-rib','cork')
''','monitor: rounded frame with centered long pedestal; original supplies cork and fanned feather silhouette','Preserve the feather fan and its separate cork within the monitor. Compact feather spacing is retained at4px stroke; the11-unit stand directly addresses the reviewer.')

define(6,'SQUARE','A plain oval and diagonal stroke replaced the artist palette and brush, and the stand was too short.','Restored a kidney-shaped palette, paint mark and pointed brush head; lengthened the monitor stand.', MONITOR+'''
curve(self,'palette',(23,11),((14,7),(8,14),(10,22)),((12,29),(24,30),(24,24)),((21,24),(21,19),(26,18)),((28,14),(27,12),(23,11)),closed=True)
self.add_dot('paint',(16,17))
curve(self,'brush-head',(35,10),((34,14),(30,16),(32,19)),((36,23),(40,18),(35,10)),closed=True)
self.add_line('brush-handle',(34,21),(29,28))
''','palette: kidney contour and thumb recess; monitor: rounded display and centered pedestal','The palette and pointed brush must both remain recognizable inside the screen. Preserve compact inner marks and the longer11-unit monitor stand at4px stroke.')

define(7,'VRECT_M','The phone was too square and blocky, making the locked-mobile concept read as a generic framed lock.','Restored a tall rounded phone silhouette, bottom screen divider and clear closed padlock.', '''
# VRECT_M extremes10,4–38,44: phone proportions own the composition.
rounded(self,'phone',10,4,38,44,5)
self.add_line('screen-divider',(10,35),(38,35));self.relate('connect','phone','screen-divider')
rounded(self,'lock-body',17,22,31,29,2)
self.add_line('shackle-left',(19,22),(19,19))
self.add_arc('shackle-top',(19,19),(29,19),radius_x=5)
self.add_line('shackle-right',(29,19),(29,22))
self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
self.relate('connect','lock-body','shackle')
''','smartphone: portrait rounded enclosure; lock-keyhole: rounded shackle and distinct lock body','The complete closed padlock and phone footer need compact gaps. Preserve the tall phone and lock identity with4px strokes rather than broadening the body into a generic frame.')

define(8,'HRECT_M','The robotic hand lost its closed palm and folded finger joints, becoming an open tool or gripper.','Restored a closed palm, curved wrist cuff, folded finger segment and articulated extended thumb.', '''
# Natural asymmetry: side-view hand with thumb pointing up-right.
curve(self,'outline',(4,12),((6,10),(8,9),(11,10)),((14,10),(17,11),(19,12)),((22,13),(25,14),(28,15)),((31,16),(33,19),(31,23)),((31,23),(36,18),(36,18)),((36,18),(38,16),(38,16)),((42,12),(47,18),(42,23)),((42,23),(40,25),(40,25)),((40,25),(32,33),(32,33)),((30,35),(28,36),(25,36)),((20,36),(14,35),(10,34)),((10,34),(4,33),(4,33)),((4,33),(4,12),(4,12)),closed=True)
curve(self,'cuff',(11,10),((16,18),(15,27),(10,34)))
self.add_polyline('folded-finger',(19,12),(19,23))
curve(self,'knuckle',(19,23),((22,24),(24,26),(27,26)),((29,26),(31,26),(31,23)))
self.relate('connect','folded-finger','knuckle')
self.relate('connect','outline','folded-finger');self.relate('connect','outline','knuckle')
self.relate('connect','outline','cuff')
self.relate('connect','knuckle','palm-seam')
self.add_line('palm-seam',(27,26),(25,36));self.relate('connect','outline','palm-seam')
self.add_line('thumb-joint',(36,18),(40,25));self.relate('connect','outline','thumb-joint')
''','hand: continuous rounded palm and finger construction; original supplies mechanical joints and side-view pose','Mechanical wrist, palm and thumb seams need compact connected panels; preserve the side-view hand silhouette and4px strokes.')

define(9,'VRECT_L','The globe lost its meridians and became a headset-like arch; the microphone lost its stand.','Restored globe latitude/longitude lines over a capsule microphone, curved cradle and pedestal.', '''
# Hemisphere is open below, as in the reference, and centered over the microphone.
curve(self,'globe',(6,20),((6,17),(7,14),(9,12)),((12,7),(17,4),(24,4)),((31,4),(36,7),(39,12)),((41,14),(42,17),(42,20)))
self.add_line('latitude',(9,12),(39,12));self.relate('connect','globe','latitude')
for side in (-1,1):
    curve(self,'meridian-'+str(side),(24,4),((24+side*6,4),(24+side*8,11),(24+side*8,20)))
    self.relate('connect','globe','meridian-'+str(side));self.relate('connect','latitude','meridian-'+str(side))
self.relate('connect','meridian--1','meridian-1')
rounded(self,'microphone',19,20,29,34,5)
curve(self,'cradle',(10,27),((10,29),(10,30),(10,31)),((10,36),(17,39),(24,39)),((31,39),(38,36),(38,31)),((38,30),(38,29),(38,27)))
self.add_line('stand',(24,39),(24,44));self.add_line('base',(16,44),(32,44))
self.relate('connect','cradle','stand');self.relate('connect','stand','base')
''','globe: meridians and latitude; mic: capsule, supporting cradle and stand','The globe grid and microphone pedestal are essential to international podcast meaning. Preserve compact globe-grid and capsule/cradle spacing at4px stroke.')

define(10,'VRECT_L','The phone lost its top edge and the dollar sign became a zigzag, obscuring contactless payment.','Restored a complete rounded phone, a smooth dollar sign and two centered wireless arcs.', '''
curve(self,'wifi-outer',(7,7),((17,0),(31,0),(41,7)))
curve(self,'wifi-inner',(15,12),((20,7),(28,7),(33,12)))
rounded(self,'phone',13,18,35,45,4)
curve(self,'dollar',(28,25),((26,22),(20,22),(20,27)),((20,30),(28,29),(28,33)),((28,37),(22,38),(20,35)))
self.add_line('currency-stem',(24,23),(24,39));self.relate('connect','dollar','currency-stem')
''','smartphone: closed portrait enclosure; original supplies two wireless arcs and a dollar mark','A complete phone plus legible dollar sign and wireless arcs needs compact detail spacing. Preserve4px strokes and the currency curves rather than replacing the dollar with a zigzag.')

if __name__=='__main__':
 for i in map(int,sys.argv[1:]):write(i)
