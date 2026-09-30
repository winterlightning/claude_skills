from pathlib import Path
import json,re,textwrap,sys,datetime
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts import build_gate
B=Path(__file__).parent
# Input identity is assigned per reference; every emitted module retains exact source identity.
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
HELPERS='''
        def path(n,start,steps,closed=False):
            members=[];here=start
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L':self.add_line(m,here,end)
                elif kind=='A':self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(m,here,(args[0],args[1],end))
                members.append(m);here=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry):path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=0):
            if not rad:self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True);return
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
D={}
def add(key,shape,issue,ref,code,omissions='None'):
 D[key]=dict(shape=shape,issue=issue,lucide=ref,code=textwrap.dedent(code),omissions=omissions)

def generate(keys=None):
 rows=json.loads((B/'staged.json').read_text());index=json.loads((B/'runs.json').read_text()) if (B/'runs.json').exists() else {}
 for row in rows:
  key=row['key'].split('/')[-1]
  if key not in D or keys and key not in keys:continue
  d=D[key];ref=Path(row['reference']);uuid=re.search(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}$',ref.stem).group()
  run=Path('icon_set/work/primitive-make-ray')/uuid/('20260929-batch14-'+datetime.datetime.now().strftime('%H%M%S%f'));run.mkdir(parents=True)
  meta={'concept':ref.stem[:-37],'source_uuid':uuid,'reference_path':str(ref),'author':AUTHOR,'icon_id':key,'comparison':d['issue'],'feedback':row['item'].get('feedback') or 'No written feedback; correct fidelity against original.','lucide':d['lucide'],'omissions':d['omissions']}
  (run/(key+'.metadata.json')).write_text(json.dumps(meta,indent=2))
  (run/'review-before.txt').write_text(d['issue']+'\n'+meta['feedback'])
  mod=run/(key.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  code=f'"""{d["issue"]}\nPlan: {d["shape"]} exact SOLO48 bounds; coherent contours and shared repeats.\nConstruction reference: {d["lucide"]}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR={AUTHOR!r}\nclass Drawing(Solo48):\n    icon_id={key!r}\n    keyshape=Keyshape.{d["shape"]}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="primitives-generate"\n    aliases=()\n    keywords={tuple(key.split("-"))!r}\n    def build(self):\n'+HELPERS+textwrap.indent(d['code'],'        ')
  
  if key in ('person-with-monocle-and-necktie','portrait-with-bob-hair-and-pendant-collar-batch-086','portrait-construction-sketch'):code=code.replace('    def build(self):','    human_construction = \"bust\"\n    def build(self):')
  mod.write_text(code);icon=load_icon(mod);r=icon.validate_icon();(run/'validation.txt').write_text(r.describe());(run/(key+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),key,48,run)
  g=build_gate.gate(mod);(run/'gate.json').write_text(json.dumps(g,indent=2));print(key,r.status,g['status'],r.errors,r.warnings,g['errors'],g['warnings'],flush=True)
  index[key]={'run':str(run),'module':str(mod),'metadata':meta,'valid':r.status=='valid' and not r.warnings and g['status']=='pass'}
  (B/'runs.json').write_text(json.dumps(index,indent=2))


add('mobile-phone-long-outgoing-arrow','VRECT_L','The rejected phone was wide and squat, and its arrow dwarfed the device. Restore a taller phone with a long outgoing shaft.','No additional useful Lucide match; inspected source defines device.',"""
path('phone',(28,11),[('L',(28,8)),('A',(24,4),4,4,False),('L',(12,4)),('A',(8,8),4,4,False),('L',(8,35)),('L',(8,40)),('A',(12,44),4,4,False),('L',(24,44)),('A',(28,40),4,4,False),('L',(28,35))])
line('bezel',(8,35),(28,35));join('bezel','phone')
line('shaft',(17,23),(40,23));poly('arrow',(34,17),(40,23),(34,29));join('shaft','arrow')
""")
add('multi-directional-expansion-touch-gesture','SQUARE','The rejected side arrows have no shafts and look like chevrons; the upper and lower shafts disappear. Restore four visible shafts around the fingertip.','No useful additional match.',"""
path('finger',(20,28),[('L',(20,24)),('A',(28,24),4,4,True),('L',(28,28))])
for name,tip,wing1,wing2,tail in [('up',(24,6),(18,12),(30,12),(24,12)),('down',(24,42),(18,36),(30,36),(24,36)),('left',(6,24),(12,18),(12,30),(12,24)),('right',(42,24),(36,18),(36,30),(36,24))]:
 poly(name,wing1,tip,wing2);line(name+'-shaft',tip,tail);join(name,name+'-shaft')
""")
add('multiple-file-folders','SQUARE','The rejected folders had clipped polygon corners and an incomplete rear folder. Restore rounded overlapping folders with offset tabs.','Lucide folders: rounded tabbed enclosures and a partial rear outline.',"""
path('rear',(16,34),[('L',(10,34)),('A',(6,30),4,4,True),('L',(6,10)),('A',(10,6),4,4,True),('L',(17,6)),('L',(23,12)),('L',(30,12)),('A',(34,16),4,4,True),('L',(34,22))])
path('front',(20,16),[('L',(23,16)),('L',(29,22)),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(20,42)),('A',(16,38),4,4,True),('L',(16,20)),('A',(20,16),4,4,True)],True)
join('rear','front')
""")
add('map-location-pin-marker-upload-5e650aa4122b9417','SQUARE','The available reference is the rejected drawing itself. Its lower pin is narrow and the internal diagonal bend is cramped. Broaden the pin and separate the diagonal bands.','No useful direct match for this striped pin emblem.',"""
path('pin',(24,6),[('C',(36,10),(29,6),(33,7)),('C',(42,24),(40,13),(42,18)),('C',(34,35),(42,29),(38,32)),('C',(24,42),(30,39),(27,42)),('C',(17,38),(22,42),(19,40)),('C',(10,32),(14,36),(12,34)),('C',(6,24),(7,29),(6,27)),('C',(24,6),(6,14),(12,6))],True)
poly('slash',(10,32),(23,21),(36,10));join('slash','pin')
poly('bend',(23,21),(29,27),(17,38));join('bend','slash');join('bend','pin')
""")
add('open-horseshoe','VRECT_L','The rejected horseshoe is a rigid U with parallel uprights. Restore subtly flared tips and bowed outer sides.','No useful direct match.',"""
path('shoe',(10,4),[('L',(18,4)),('C',(17,27),(18,12),(17,20)),('A',(31,27),7,7,False),('C',(30,4),(31,20),(30,12)),('L',(38,4)),('C',(40,28),(38,12),(40,20)),('A',(8,28),16,16,True),('C',(10,4),(8,20),(10,12))],True)
""")
add('open-drainage-channel','HRECT_L','The rejected drainage channel has flat square sidewall tops and no front sidewall seam. Round the wall caps and show the recessed channel behind its curved front edge.','No useful direct match.',"""
path('channel',(4,28),[('L',(8,12)),('A',(16,12),4,4,True),('L',(16,24)),('A',(20,28),4,4,False),('L',(28,28)),('A',(32,24),4,4,False),('L',(32,12)),('A',(40,12),4,4,True),('L',(44,28)),('A',(32,40),12,12,True),('L',(16,40)),('A',(4,28),12,12,True)],True)
line('back',(16,19),(32,19));join('back','channel')
line('front-left',(4,28),(16,28));line('front-right',(32,28),(44,28));join('front-left','channel');join('front-right','channel')
""")
add('open-infinity-loop-batch-015-02','HRECT_M','The rejected infinity closes both source breaks and forms a central junction. Restore a single flowing open S-shaped loop with two free ends.','No additional match needed; inspected source owns the open topology.',"""
path('loop',(18,14),[('C',(14,10),(17,12),(16,10)),('A',(4,24),10,14,False),('A',(14,38),10,14,False),('C',(34,10),(22,38),(26,10)),('A',(44,24),10,14,True),('A',(34,38),10,14,True),('C',(30,34),(32,38),(31,36))])
""")
add('open-end-maintenance-wrench','VRECT_L','The reference is the current wrench. Its head occupies most of the height and leaves a short handle. Shorten the jaw and lengthen the handle while retaining the U-shaped open end.','No useful direct match for this tuning-fork-like wrench.',"""
path('jaw',(8,4),[('L',(18,4)),('L',(18,12)),('A',(30,12),6,6,False),('L',(30,4)),('L',(40,4)),('L',(40,12)),('A',(24,28),16,16,True),('A',(8,12),16,16,True),('L',(8,4))],True)
line('handle',(24,28),(24,44));join('handle','jaw')
""")
add('human-skull-symbol','SQUARE','The rejected skull is too tall and has abrupt square cheek-to-jaw steps. Broaden the domed cranium and soften the cheek transitions while retaining the blank face and two tooth divisions.','Lucide skull: broad cranium and smooth cheek-to-jaw transition; source has no eye holes.',"""
path('skull',(6,24),[('A',(42,24),18,18,True),('L',(42,28)),('C',(36,34),(42,33),(36,31)),('L',(36,38)),('A',(32,42),4,4,True),('L',(28,42)),('L',(20,42)),('L',(16,42)),('A',(12,38),4,4,True),('L',(12,34)),('C',(6,28),(12,31),(6,33)),('L',(6,24))],True)
for x in (20,28):line('tooth'+str(x),(x,34),(x,42));join('tooth'+str(x),'skull')
""")
add('padded-infant-car-seat','SQUARE','The rejected seat is a generic rounded box with a U mark. Restore a broad seat shell, diagonal harness branches and a central seat seam.','No useful direct match.',"""
box('shell',6,6,42,42,12)
poly('harness',(15,17),(24,29),(33,17))
line('seat-seam',(24,29),(24,42));join('seat-seam','harness');join('seat-seam','shell')
""",'Omit the secondary inner padding outline to keep the harness legible.')


add('pair-of-rubber-boots-batch-051','SQUARE','The rejected boots have square toes and an open rear sole. Restore rounded projecting toes, curved insteps and a rear sole meeting the foreground boot.','No useful direct match.',"""
path('front',(6,16),[('L',(18,16)),('L',(18,24)),('C',(30,34),(18,32),(24,31)),('A',(34,38),4,4,True),('L',(34,42)),('L',(6,42)),('L',(6,16))],True)
path('rear',(14,6),[('L',(28,6)),('L',(28,18)),('C',(38,26),(28,24),(33,24)),('A',(42,30),4,4,True),('L',(42,34)),('L',(30,34))]);join('rear','front')
""",'Omit the thin heel and sole bands.')
add('paired-adjustable-suspender-straps','SQUARE','The rejected straps replace both buckles with divider bars. Restore two protruding outlined buckles and matched rounded strap ends.','No useful direct match.',"""
for j,l in enumerate((6,28)):
 n='strap'+str(j)
 path(n+'top',(l+2,26),[('L',(l+2,10)),('A',(l+6,6),4,4,True),('L',(l+8,6)),('A',(l+12,10),4,4,True),('L',(l+12,26))])
 box(n+'buckle',l,26,l+14,34,2)
 path(n+'bottom',(l+2,34),[('L',(l+2,38)),('A',(l+6,42),4,4,False),('L',(l+8,42)),('A',(l+12,38),4,4,False),('L',(l+12,34))])
 join(n+'top',n+'buckle');join(n+'bottom',n+'buckle')
""")
add('pair-of-rounded-house-slippers','SQUARE','The rejected slippers are uniform capsules with straight bars. Restore bulbous toes, tapered heels and curved vamp seams.','No useful direct match.',"""
for j,l in enumerate((6,28)):
 n='slipper'+str(j)
 path(n,(l,18),[('A',(l+14,18),7,12,True),('C',(l+13,29),(l+14,22),(l+13,26)),('L',(l+12,36)),('C',(l+7,42),(l+11,41),(l+10,42)),('C',(l+2,36),(l+4,42),(l+3,41)),('L',(l+1,29)),('C',(l,18),(l+1,26),(l,22))],True)
 path(n+'vamp',(l+1,29),[('C',(l+13,29),(l+5,25),(l+9,25))]);join(n,n+'vamp')
""")
add('person-with-flower','SQUARE','The rejected flower is a plain ring and the person has an angular shoulder. Restore four distinct flower lobes, two leaves and rounded shoulders beneath the circular head.','human_ref/user.svg: circular head and rounded shoulders; exact detached head gap 4 ink units.',"""
oval('head',14,12,6,6)
path('body',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('L',(18,26)),('A',(22,30),4,4,True),('L',(22,42))])
path('flower',(32,13),[('A',(38,13),3,3,True),('A',(38,21),4,4,True),('A',(32,21),3,3,True),('A',(32,13),4,4,True)],True)
poly('stem',(35,24),(35,34),(35,42));join('stem','flower')
poly('leaves',(28,30),(35,34),(42,30));join('leaves','stem')
""",'Omit tiny flower center and sleeve marks; leaves remain open strokes.')
add('person-with-monocle-and-necktie','VRECT_L','The rejected portrait has a short bar for a necktie and reads as a circular symbol. Preserve its single eyeglass and add a pointed outlined necktie beneath a circular face.','human_ref/user.svg: circular face and broad rounded shoulders; touching bust ink.',"""
oval('face',24,18,14,14)
path('shoulders',(8,44),[('A',(16,36),8,8,True),('L',(24,36)),('L',(32,36)),('A',(40,44),8,8,True)]);join('face','shoulders')
oval('monocle',26,18,3,3);line('temple',(29,18),(38,18));join('temple','face');join('temple','monocle')
poly('tie',(24,36),(20,40),(24,44),(28,40),(24,36));join('tie','shoulders')
""",'Omit swept hair and collar points to retain clear eyeglass and necktie.')
add('person-with-circular-object','SQUARE','The rejected person loses the entire right shoulder. Restore a complete symmetrical shoulder arch and retain the circular object at lower right.','human_ref/user.svg: circular head and broad shoulders; exact detached head gap 4 ink units.',"""
oval('head',24,12,6,6)
path('body',(6,42),[('L',(6,34)),('A',(14,26),8,8,True),('L',(34,26)),('A',(42,34),8,8,True),('L',(42,42))])
oval('object',28,38,4,4)
""")
add('paired-plain-shoe-sole-prints','SQUARE','The rejected soles are uniform pill shapes. Restore broad rounded toes, inward-curved waists and separated heels.','No useful direct match.',"""
for j,l in enumerate((6,28)):
 n='sole'+str(j)
 path(n,(l,18),[('A',(l+14,18),7,12,True),('C',(l+12,30),(l+14,23),(l+12,26)),('L',(l+12,33)),('L',(l+12,36)),('C',(l+7,42),(l+12,40),(l+10,42)),('C',(l+2,36),(l+4,42),(l+2,40)),('L',(l+2,33)),('L',(l+2,30)),('C',(l,18),(l+2,26),(l,23))],True)
 line(n+'heel',(l+2,33),(l+12,33));join(n,n+'heel')
""")
add('oval-amulet-with-teardrop-inset','VRECT_M','The rejected amulet is flattened with a pin-like top and a tiny flat inset. Restore an upright pendant, open suspension loop and taller pointed teardrop.','No useful direct match.',"""
path('pendant',(20,12),[('L',(28,12)),('C',(38,28),(34,12),(38,20)),('C',(24,44),(38,37),(32,44)),('C',(10,28),(16,44),(10,37)),('C',(20,12),(10,20),(14,12))],True)
path('loop',(20,12),[('L',(20,8)),('A',(28,8),4,4,True),('L',(28,12))]);join('loop','pendant')
path('drop',(24,21),[('C',(30,32),(27,24),(30,29)),('C',(18,32),(30,38),(18,38)),('C',(24,21),(18,29),(21,24))],True)
""")
add('portrait-with-bob-hair-and-pendant-collar-batch-086','VRECT_L','The rejected bob is an open hair arch and its pendant is just a detached dot. Restore flat bob ends and a prominent pointed pendant attached to the collar.','human_ref/user.svg: circular jaw and rounded shoulder arch; touching bust ink.',"""
path('bob',(15,28),[('L',(8,28)),('L',(8,20)),('A',(40,20),16,16,True),('L',(40,28)),('L',(33,28))])
oval('face',24,20,7,7)
path('shoulders',(8,40),[('A',(24,31),16,9,True),('A',(40,40),16,9,True)]);join('face','shoulders')
poly('pendant',(24,31),(20,39),(24,44),(28,39),(24,31));join('pendant','shoulders')
""",'Reduce three ornaments to one pendant and omit the tiny facial mark.')
add('portrait-construction-sketch','VRECT_L','The rejected sketch is a rigid cross in a circle on square shoulders. Curve the horizontal face guide and shoulders while preserving both construction axes.','human_ref/user.svg: circular face and broad shoulder arcs; touching bust ink.',"""
path('head',(24,4),[('A',(36,16),12,12,True),('A',(24,28),12,12,True),('A',(12,16),12,12,True),('A',(24,4),12,12,True)],True)
poly('vertical',(24,4),(24,14),(24,28));join('head','vertical')
path('horizontal',(12,16),[('C',(24,14),(16,15),(20,14)),('C',(36,16),(28,14),(32,15))]);join('horizontal','head');join('horizontal','vertical')
path('shoulders',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('head','shoulders')
""",'Use the shared circular-jaw construction instead of the source pointed chin.')
if __name__=='__main__':generate(sys.argv[1:])
