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
  run=Path('icon_set/work/primitive-make-ray')/uuid/('20260929-batch15-'+datetime.datetime.now().strftime('%H%M%S%f'));run.mkdir(parents=True)
  meta={'concept':ref.stem[:-37],'source_uuid':uuid,'reference_path':str(ref),'author':AUTHOR,'icon_id':key,'comparison':d['issue'],'feedback':row['item'].get('feedback') or 'No written feedback; correct fidelity against original.','lucide':d['lucide'],'omissions':d['omissions']}
  (run/(key+'.metadata.json')).write_text(json.dumps(meta,indent=2))
  (run/'review-before.txt').write_text(d['issue']+'\n'+meta['feedback'])
  mod=run/(key.replace('-','_')+'_'+uuid.replace('-','_')+'.py')
  code=f'"""{d["issue"]}\nPlan: {d["shape"]} exact SOLO48 bounds; coherent contours and shared repeats.\nConstruction reference: {d["lucide"]}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID={uuid!r}\nSOURCE_PATH={str(ref)!r}\nAUTHOR={AUTHOR!r}\nclass Drawing(Solo48):\n    icon_id={key!r}\n    keyshape=Keyshape.{d["shape"]}\n    semantic_role="MAIN"\n    semantic_kind="noun"\n    category="primitives-generate"\n    aliases=()\n    keywords={tuple(key.split("-"))!r}\n    def build(self):\n'+HELPERS+textwrap.indent(d['code'],'        ')
  
  if d.get('bust'):code=code.replace('    def build(self):','    human_construction = \"bust\"\n    def build(self):')
  mod.write_text(code);icon=load_icon(mod);r=icon.validate_icon();(run/'validation.txt').write_text(r.describe());(run/(key+'.svg')).write_text(icon.to_svg());render_previews(icon.to_svg(),key,48,run)
  g=build_gate.gate(mod);(run/'gate.json').write_text(json.dumps(g,indent=2));print(key,r.status,g['status'],r.errors,r.warnings,g['errors'],g['warnings'],flush=True)
  index[key]={'run':str(run),'module':str(mod),'metadata':meta,'valid':r.status=='valid' and not r.warnings and g['status']=='pass'}
  (B/'runs.json').write_text(json.dumps(index,indent=2))



add('right-indentation-action','VRECT_L','The rejected indentation control replaces the two outlined rows with solid strokes. Restore two rounded outlined rows beneath a rightward arrow.','Lucide list-indent-increase: separate directional chevron and aligned rows.',"""
box('upper-row',8,20,28,28,2);box('lower-row',16,36,28,44,2)
line('shaft',(30,10),(40,10));poly('arrow',(34,4),(40,10),(34,16));join('arrow','shaft')
""")
add('rounded-square-dash','SQUARE','The rejected border has large curved corners and dot-like middle dashes. Restore a clearly dashed square with short rounded corners and equal central dashes.','Lucide square-minus: shared corner radii and square enclosure.',"""
path('nw',(6,10),[('L',(6,8)),('A',(8,6),2,2,True),('L',(10,6))])
path('ne',(38,6),[('L',(40,6)),('A',(42,8),2,2,True),('L',(42,10))])
path('se',(42,38),[('L',(42,40)),('A',(40,42),2,2,True),('L',(38,42))])
path('sw',(10,42),[('L',(8,42)),('A',(6,40),2,2,True),('L',(6,38))])
for y in (6,42):line('horizontal'+str(y),(20,y),(28,y))
for x in (6,42):line('vertical'+str(x),(x,20),(x,28))
""",'Reduce the source dash count to preserve full 4-unit clearances.')
add('rounded-staggered-task-bars','HRECT_L','The rejected schedule uses short solid dashes instead of outlined task bars. Restore rounded outlined tasks in a staggered layout.','Lucide list-todo: distinct outlined task enclosures and repeated rows.',"""
box('task-top',4,8,20,16,3)
box('task-middle',28,20,44,28,3)
box('task-bottom',4,32,20,40,3)
""",'Reduce six crowded task bars to three staggered outlined tasks.')
add('row-selected-point','HRECT_L','The rejected selection arrow has no readable shaft, and the row is compressed into a pill. Restore a shafted arrow, a divided selected row and partial neighboring rows.','Lucide list-indent-increase: distinct arrow and aligned content rows.',"""
box('row',20,20,44,28,2);line('divider',(32,20),(32,28));join('divider','row')
poly('arrow',(6,18),(12,24),(6,30));line('shaft',(4,24),(12,24));join('arrow','shaft')
path('above',(28,12),[('L',(28,10)),('A',(30,8),2,2,True),('L',(44,8))])
path('below',(28,36),[('L',(28,38)),('A',(30,40),2,2,False),('L',(44,40))])
""")
add('science-apple-gravity','VRECT_L','The rejected apple is a flattened bean and its arrows are stubs. Restore a tall lobed apple with a stem above three downward arrows.','Lucide apple: coherent lobes, stem and bottom cleft.',"""
path('apple',(24,12),[('C',(10,18),(16,6),(10,10)),('C',(18,28),(10,23),(14,28)),('C',(24,27),(20,28),(22,27)),('C',(30,28),(26,27),(28,28)),('C',(38,18),(34,28),(38,23)),('C',(24,12),(38,10),(32,6))],True)
path('stem',(24,12),[('C',(28,4),(24,8),(26,5))]);join('stem','apple')
for x,top,tip in ((12,34,42),(24,36,44),(36,34,42)):
 n='fall'+str(x);line(n,(x,top),(x,tip));poly(n+'head',(x-4,tip-4),(x,tip),(x+4,tip-4));join(n,n+'head')
""")
add('search-bar','HRECT_L','The rejected search field is too tall and its magnifier handle is a bump. Widen the field and give its circular lens a distinct diagonal handle.','Lucide search: circular lens with a diagonal handle meeting the rim at an exact point.',"""
box('field',4,8,44,40,12)
path('lens',(23,22),[('A',(28,17),5,5,True),('A',(33,22),5,5,True),('A',(31,26),5,5,True),('A',(23,22),5,5,True)],True)
line('handle',(31,26),(34,30));join('handle','lens')
""")
add('rounded-square-keyboard-key-upload-d2dede8249ae89f0','SQUARE','Only the current keycap is available as a reference. Its heavy corner rounding reduces the straight key edges. Rebuild it with balanced, tighter rounded corners.','Lucide square-minus: matched quarter-circle corner construction.',"""
box('keycap',6,6,42,42,6)
""")
add('shaped-armor-breastplate','VRECT_L','The rejected breastplate has a W-shaped chest mark and an angular straight hem. Restore paired breast curves, a scooped neckline and a curved lower armor band.','No useful direct Lucide match; source owns the shaped armor silhouette.',"""
path('armor',(8,6),[('L',(16,4)),('A',(32,4),8,8,False),('L',(40,6)),('C',(40,20),(38,12),(38,16)),('L',(36,34)),('L',(40,40)),('A',(8,40),16,4,True),('L',(12,34)),('L',(8,20)),('C',(8,6),(10,16),(10,12))],True)
path('breast',(17,22),[('C',(24,22),(17,28),(24,28)),('C',(31,22),(24,28),(31,28))])
path('hem',(12,34),[('C',(36,34),(20,36),(28,36))]);join('hem','armor')
""",'Omit the short center chest seam while retaining the paired breast shapes.')
add('shopping-bag-with-attached-tag','HRECT_L','The rejected price tag is upright and squared off. Restore a diagonal tag attached to the bag rim, with a curved handle and tapered bag.','Lucide shopping-bag: coherent bag outline and handle attachment.',"""
path('bag',(8,24),[('L',(20,24)),('L',(28,24)),('L',(32,36)),('A',(28,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(8,24))],True)
path('handle',(8,24),[('L',(8,14)),('A',(20,14),6,6,True),('L',(20,24))]);join('handle','bag')
poly('tag',(28,16),(36,8),(44,16),(36,24),(28,24),(28,16));join('tag','bag')
""",'Omit the tiny tag hole.')


add('seat-find','SQUARE','The rejected scene uses a stiff frontal figure and an angular chair. Restore a walking step, a forward arm and a smoothly rounded seat corner while retaining the direction arrow.','human_ref/full_body_ref.png: round head and coherent limbs; Lucide armchair: rounded seat junctions.',"""
oval('head',14,10,4,4)
line('torso',(14,22),(14,32));poly('arms',(8,28),(14,22),(20,26));join('torso','arms')
poly('legs',(6,40),(14,32),(18,36),(22,42));join('torso','legs')
self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
line('shaft',(23,18),(30,18));poly('arrow',(26,14),(30,18),(26,22));join('shaft','arrow')
path('chair',(40,12),[('L',(42,20)),('L',(40,30)),('C',(36,34),(40,33),(39,34)),('L',(30,34))])
line('base',(30,42),(40,42))
""",'Keep person and chair as coherent strokes; omit their material thickness. Head bottom14 to torso22 is exactly8 centerline /4 ink.')
add('shoe-resting-on-open-rack','SQUARE','The rejected shoe is a box with a wavy top and the rack has heavy rectangular divisions. Restore a recognizable shoe heel, raised tongue and sloping toe on the shelf.','No useful direct Lucide match for this shoe-and-rack scene.',"""
poly('rack',(6,42),(6,32),(6,14),(6,6),(42,6),(42,14),(42,32),(42,42))
for y in (14,32,40):line('shelf'+str(y),(6,y),(42,y));join('shelf'+str(y),'rack')
path('shoe',(14,32),[('L',(14,24)),('C',(21,24),(16,27),(18,27)),('C',(24,23),(22,23),(23,23)),('C',(34,27),(27,25),(29,26)),('L',(34,32))]);join('shoe','shelf32')
""")
add('short-haired-woman-with-visible-sleeve-seams','VRECT_L','The rejected portrait omits the named sleeve seams and reduces the bob to a hair arch. Extend the bob, retain the swept fringe and restore two visible sleeve seams on a closed blouse.','human_ref/user.svg: circular jaw and rounded shoulders with touching bust ink.',"""
path('face',(17,15),[('A',(31,15),7,7,False),('C',(26,13),(29,15),(28,14)),('C',(17,15),(24,15),(20,15))],True)
path('hair',(8,24),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,24))])
path('body',(8,44),[('L',(8,34)),('A',(24,26),16,8,True),('A',(40,34),16,8,True),('L',(40,44)),('L',(32,44)),('L',(16,44)),('L',(8,44))],True);join('face','body')
for x in (16,32):line('sleeve'+str(x),(x,36),(x,44));join('sleeve'+str(x),'body')
""")
D['short-haired-woman-with-visible-sleeve-seams']['bust']=True
add('six-legged-termite','VRECT_L','The rejected termite loses the thorax and gathers straight legs at one point. Restore three body regions and six legs attached at separate levels, with bent outer legs.','No additional Lucide match; source owns the three-part termite body.',"""
path('insect',(24,8),[('C',(30,12),(28,8),(30,9)),('C',(28,16),(30,14),(30,15)),('C',(32,20),(30,17),(32,18)),('L',(32,28)),('L',(32,36)),('A',(24,44),8,8,True),('A',(16,36),8,8,True),('L',(16,28)),('L',(16,20)),('C',(20,16),(16,18),(18,17)),('C',(18,12),(18,15),(18,14)),('C',(24,8),(18,9),(20,8))],True)
line('neck',(20,16),(28,16));line('thorax',(16,28),(32,28));join('neck','insect');join('thorax','insect')
poly('antennae',(18,4),(24,8),(30,4));join('antennae','insect')
for side,x,end in [('l',16,8),('r',32,40)]:
 poly(side+'upper',(x,20),(end,16),(end,10));line(side+'middle',(x,28),(end,28));poly(side+'lower',(x,36),(end,40),(end,44))
 for n in ('upper','middle','lower'):join(side+n,'insect')
""")
add('skirt-beside-tailor-square','HRECT_L','The rejected tailor square is just an L stroke and the skirt loses the tool proportions. Restore an outlined L ruler with marked divisions beside a flared skirt and broad waistband.','No useful direct Lucide match.',"""
poly('ruler',(4,40),(4,8),(44,8),(44,16),(12,16),(12,40),(4,40))
for x in (24,36):line('top-mark'+str(x),(x,8),(x,16));join('top-mark'+str(x),'ruler')
line('side-mark',(4,28),(12,28));join('side-mark','ruler')
poly('skirt',(24,24),(36,24),(40,32),(44,40),(20,40),(22,32),(24,24))
line('waistband',(22,32),(40,32));join('waistband','skirt')
""",'Omit fine ruler ticks and skirt pleats; preserve outlined tool, flared skirt and waistband.')
add('smiling-tree-trunk-batch-086','HRECT_L','The rejected tree closes the roots with a bottom bar and omits both side branches. Restore outward branches, open flared roots, narrow eyes and a shallow smile.','No useful direct match for this character trunk.',"""
path('trunk',(4,40),[('C',(11,30),(8,40),(11,36)),('L',(11,20)),('L',(11,8)),('C',(24,8),(15,14),(20,14)),('C',(37,8),(28,14),(33,14)),('L',(37,20)),('L',(37,30)),('C',(44,40),(37,36),(40,40))])
path('branch-left',(4,8),[('L',(4,13)),('A',(11,20),7,7,False)]);join('branch-left','trunk')
path('branch-right',(44,8),[('L',(44,13)),('A',(37,20),7,7,True)]);join('branch-right','trunk')
for x in (20,28):line('eye'+str(x),(x,21),(x,22))
path('smile',(20,31),[('A',(28,31),4,3,False)])
""",'Omit the short bark scratch; preserve the cropped upper branches.')
add('spool-wrapped-with-thread','VRECT_L','The rejected spool has one slash and an open lower outline. Restore multiple alternating diagonal wraps and complete both projecting spool ends.','No useful direct match.',"""
box('thread-body',8,12,40,36,4)
poly('top-core',(16,12),(16,4),(32,4),(32,12));join('top-core','thread-body')
poly('bottom-core',(16,36),(16,44),(32,44),(32,36));join('bottom-core','thread-body')
poly('wraps',(36,12),(8,20),(40,28),(12,36));join('wraps','thread-body')
line('tail',(32,44),(40,44));join('tail','bottom-core')
""")
add('spiral-vortex-in-square-frame','SQUARE','The rejected vortex closes into a circle and sends a bar through its center. Restore an open inward curl connected to a square frame, with no closed circular loop.','No useful direct match for the framed spiral; source owns its topology.',"""
poly('frame',(6,20),(6,6),(42,6),(42,42),(6,42),(6,34))
path('spiral',(6,20),[('C',(24,15),(12,12),(20,15)),('A',(33,24),9,9,True),('A',(24,33),9,9,True),('A',(15,24),9,9,True),('C',(24,24),(15,23),(20,24))]);join('spiral','frame')
""",'Reduce the source turn count to one broad inward sweep to retain clear spacing.')
add('policewoman-in-peaked-cap','VRECT_L','The rejected peaked cap is triangular and the chest pocket becomes a stray bottom stroke. Restore a broad shallow crown and curved visor over the circular jaw, with clean uniform shoulders.','human_ref/user.svg: circular jaw and shoulder arch with touching bust ink.',"""
poly('crown',(14,18),(8,6),(24,4),(40,6),(34,18))
path('brim',(14,18),[('A',(34,18),10,2,False)]);join('brim','crown')
path('jaw',(34,18),[('A',(14,18),10,10,True)]);join('jaw','brim');join('jaw','crown')
for side,s in [('l',-1),('r',1)]:
 path('hair'+side,(24+s*10,18),[('C',(24+s*16,28),(24+s*10,23),(24+s*12,26))]);join('hair'+side,'jaw');join('hair'+side,'brim');join('hair'+side,'crown')
path('shoulders',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)]);join('jaw','shoulders')
line('seam',(24,32),(24,44));join('seam','shoulders')
""",'Omit the small chest badge and secondary cap band.')
D['policewoman-in-peaked-cap']['bust']=True
add('policewoman-with-rounded-helmet','VRECT_L','The rejected helmet has a bowl-like visor and a plain central uniform stripe. Restore a straight helmet band and an open V collar under the round face.','human_ref/user.svg: circular jaw and rounded shoulders with touching bust ink.',"""
path('helmet',(12,16),[('A',(36,16),12,12,True)])
line('brim',(12,16),(36,16));join('brim','helmet')
path('jaw',(36,16),[('A',(12,16),12,12,True)]);join('jaw','helmet');join('jaw','brim')
for side,s in [('l',-1),('r',1)]:
 path('hair'+side,(24+s*12,16),[('C',(24+s*16,26),(24+s*12,21),(24+s*14,25))]);join('hair'+side,'jaw');join('hair'+side,'brim');join('hair'+side,'helmet')
path('shoulders',(8,44),[('L',(8,40)),('C',(16,34),(8,36),(12,34)),('C',(24,32),(18,32),(21,32)),('C',(32,34),(27,32),(30,32)),('C',(40,40),(36,34),(40,36)),('L',(40,44))]);join('jaw','shoulders')
poly('collar',(16,34),(24,42),(32,34));join('collar','shoulders')
""",'Omit the narrow second helmet band.')
D['policewoman-with-rounded-helmet']['bust']=True
add('policewoman-with-circular-cap-badge','VRECT_L','The rejected circular cap badge is a solid dot. Restore an outlined circular badge on a fuller cap and remove the unrelated central chest stripe.','human_ref/user.svg: circular jaw and broad shoulders with touching bust ink.',"""
path('cap',(8,28),[('A',(24,4),16,24,True),('A',(40,28),16,24,True)])
poly('brim',(8,28),(16,28),(32,28),(40,28));join('brim','cap')
path('jaw',(32,28),[('A',(16,28),8,8,True)]);join('jaw','brim')
oval('badge',24,16,3,3)
for side,s in [('l',-1),('r',1)]:
 path('hair'+side,(24+s*8,28),[('C',(24+s*16,34),(24+s*10,31),(24+s*12,33))]);join('hair'+side,'jaw');join('hair'+side,'brim')
path('shoulders',(8,44),[('A',(24,40),16,4,True),('A',(40,44),16,4,True)]);join('jaw','shoulders')
""",'Omit the narrow visor insert; enlarge cap to keep the circular badge open.')
D['policewoman-with-circular-cap-badge']['bust']=True
if __name__=='__main__':generate(sys.argv[1:])
