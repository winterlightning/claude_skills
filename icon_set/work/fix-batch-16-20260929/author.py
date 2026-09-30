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
  run=Path('icon_set/work/primitive-make-ray')/uuid/('20260929-batch16-'+datetime.datetime.now().strftime('%H%M%S%f'));run.mkdir(parents=True)
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



add('police-avatar','SQUARE','The rejected police avatar removes the raised arm and V collar and changes the cap into a tall roof. Restore the raised left arm, broad cap and uniform collar.','human_ref/user.svg: circular jaw and broad shoulders; intentional raised-arm asymmetry.',"""
poly('cap',(24,16),(22,6),(42,8),(40,16),(24,16))
path('jaw',(40,16),[('A',(24,16),8,8,True)]);join('cap','jaw')
path('uniform',(18,42),[('L',(18,34)),('L',(10,28)),('A',(6,20),10,10,True),('L',(6,16)),('A',(14,16),4,4,True),('L',(14,20)),('C',(24,28),(14,25),(21,28)),('L',(32,36)),('L',(38,28)),('C',(42,36),(41,29),(42,32)),('L',(42,42))]);join('jaw','uniform')
""",'Omit cap insignia; source contains none.')
D['police-avatar']['bust']=True
add('police-officer-with-sunglasses-and-pocket','VRECT_L','The rejected glasses collapse into thick eye slits, the hat has sharp corners, and the pocket is a stray lower line. Restore a rounded hat, paired sunglass lenses and a real pocket.','human_ref/user.svg for circular jaw; Lucide user for rounded shoulder construction.',"""
path('hat',(12,16),[('L',(14,8)),('A',(18,4),4,4,True),('L',(30,4)),('A',(34,8),4,4,True),('L',(36,16))])
poly('brim',(8,16),(12,16),(24,16),(36,16),(40,16));join('hat','brim')
path('jaw',(36,16),[('A',(12,16),12,12,True)]);join('jaw','hat');join('jaw','brim')
for n,l,r in [('left',12,24),('right',24,36)]:
 path(n+'lens',(l,16),[('A',(r,16),6,6,False)]);join(n+'lens','brim');join(n+'lens','jaw');join(n+'lens','hat')
join('leftlens','rightlens')
path('body',(8,44),[('L',(8,40)),('A',(24,32),16,8,True),('A',(40,40),16,8,True),('L',(40,44))]);join('jaw','body')
path('pocket',(28,36),[('L',(28,40)),('A',(36,40),4,4,False),('L',(36,36)),('L',(28,36))],True);join('pocket','body')
""",'Omit central shirt seam if it crowds the pocket.')
D['police-officer-with-sunglasses-and-pocket']['bust']=True
add('real-estate-market-house-decrease','SQUARE','The rejected arrow has an almost horizontal shaft and short heavy head. Restore a clear descending diagonal above three decreasing outlined bars.','Lucide chart-no-axes-column-decreasing: common baseline and orderly descending heights.',"""
for i,(x,y) in enumerate(((6,18),(20,28),(34,34))):box('bar'+str(i),x,y,x+8,42)
line('trend',(10,6),(42,26));poly('arrow',(40,16),(42,26),(32,26));join('trend','arrow')
""")
add('smart-tv-and-phone','SQUARE','The rejected television is an open C and only one wireless arc survives. Restore the wide screen, its stand and two Wi-Fi arcs beside the phone.','Lucide monitor-smartphone: interrupted screen behind a separate phone and a T stand.',"""
path('screen',(26,18),[('L',(10,18)),('A',(6,22),4,4,False),('L',(6,30)),('A',(10,34),4,4,False),('L',(32,34))])
line('stand',(20,34),(20,42));line('foot',(12,42),(28,42));join('stand','screen');join('stand','foot')
box('phone',34,12,42,26,2)
path('wifi',(6,9),[('A',(26,9),14,10,True)])
path('wifi-inner',(14,10),[('A',(18,10),4,4,True)])
""",'Omit the phone lower divider to preserve its opening.')
add('spotify-logo-1','CIRCLE','The rejected sound lines are short symmetric arches. Restore three progressively shorter curved strokes slanting down toward the right inside the circular logo.','No useful direct Lucide match; original owns the three asymmetric broadcast curves.',"""
oval('disc',24,24,20,20)
path('wave-top',(13,15),[('C',(35,18),(20,12),(29,14))])
path('wave-middle',(15,24),[('C',(33,27),(21,22),(28,23))])
path('wave-bottom',(18,33),[('C',(29,35),(22,32),(27,33))])
""")
add('stressed-person','VRECT_L','The rejected stress marks are three right-facing chevrons and its head is undersized. Restore irregular lightning-like stress marks above a larger circular head and shoulders.','human_ref/user.svg: round head and smooth shoulders; exact detached head gap 4 ink.',"""
oval('head',24,24,7,7)
path('shoulders',(8,44),[('A',(24,39),16,5,True),('A',(40,44),16,5,True)])
poly('stress-left',(8,4),(12,8),(8,12));poly('stress-middle',(24,4),(21,8),(25,11));poly('stress-right',(40,4),(36,8),(40,12))
""")
add('three-balaclava-wearers','HRECT_L','The rejected top masks merge into one arch and lose their eye openings. Restore three mask silhouettes with distinct horizontal eye bands in the triangular arrangement.','human_ref/user.svg: equal rounded heads; original supplies masks and arrangement.',"""
for n,cx in [('left',12),('right',36)]:
 path(n,(cx-8,28),[('L',(cx-8,16)),('A',(cx+8,16),8,8,True),('L',(cx+8,16))])
 line(n+'band',(cx-8,16),(cx+8,16));join(n,n+'band')
path('front',(16,40),[('L',(16,32)),('A',(32,32),8,8,True),('L',(32,40))])
line('front-band',(16,32),(32,32));join('front','front-band')
""",'Simplify lower neck folds; keep three masked faces and visible eye bands.')
add('three-cell-row','HRECT_M','The rejected row is a capsule with semicircular end cells. Restore a rectangular row with modest rounded corners and three equal cells.','Lucide columns-3: shared rectangle and evenly spaced dividers.',"""
box('row',4,10,44,38,3)
for x in (17,31):line('divider'+str(x),(x,10),(x,38));join('divider'+str(x),'row')
""",'The SOLO48 horizontal keyshape makes the row taller than the source.')
add('tooth-with-dental-floss-upload-79ce34090d76e090','HRECT_L','Only the rejected drawing is available. Its roots are sharp spikes and the floss hugs the tooth. Round the molar roots and give the hooked floss tail a wider open bend.','No useful direct Lucide match; current reference supplies tooth and attached floss.',"""
path('tooth',(18,10),[('C',(8,8),(14,10),(10,6)),('C',(4,18),(5,8),(4,13)),('L',(6,26)),('L',(8,36)),('A',(14,36),3,3,False),('L',(17,28)),('A',(23,28),3,3,True),('L',(26,36)),('A',(32,36),3,3,False),('L',(34,24)),('L',(34,18)),('C',(30,8),(34,13),(33,8)),('C',(18,10),(28,6),(23,10))],True)
path('floss',(34,18),[('A',(42,26),8,8,True),('L',(42,36)),('A',(44,40),4,4,False)]);join('tooth','floss')
""")
add('traditional-japanese-mochi','CIRCLE','The rejected mochi becomes a nearly closed circular loop with an inner horseshoe. Restore the rounded dumpling silhouette with two open lower tips and a broad oval inset.','No useful direct Lucide match; source supplies nested rounded dumpling contours.',"""
path('dumpling',(20,44),[('A',(4,24),20,20,True),('A',(44,24),20,20,True),('A',(28,44),20,20,True)])
path('inset',(20,35),[('A',(13,28),11,7,True),('A',(35,28),11,7,True),('A',(28,35),11,7,True)])
""")
add('twisted-licorice-strands','SQUARE','The rejected licorice uses hard polygon corners and straight bands. Restore smooth interwoven diagonal strands with rounded ends.','No useful direct Lucide match; source supplies diagonal twist and soft contours.',"""
path('left-strand',(6,36),[('C',(14,22),(6,31),(10,25)),('C',(30,14),(20,19),(26,19)),('L',(36,6)),('A',(42,12),5,5,True),('C',(34,26),(42,18),(38,23)),('C',(18,34),(28,29),(22,29)),('L',(12,42)),('A',(6,36),5,5,True)],True)
path('wrap1',(6,36),[('C',(34,26),(14,36),(28,28))]);join('wrap1','left-strand')
path('wrap2',(14,22),[('C',(42,12),(23,22),(35,15))]);join('wrap2','left-strand')
""",'Reduce fine twists to two broad interwoven turns.')
add('twisted-rubber-band','SQUARE','The rejected elastic is two separate loops meeting at one point. Restore one elongated diagonal loop crossing an interrupted opposing loop.','No useful direct Lucide match; preserve the source crossing and occlusion.',"""
path('front',(8,40),[('C',(16,16),(2,34),(10,22)),('C',(40,8),(24,8),(36,2)),('C',(32,32),(46,14),(38,26)),('C',(8,40),(24,40),(12,46))],True)
path('rear-top',(6,26),[('C',(8,8),(3,18),(3,10)),('C',(24,6),(12,3),(18,3))])
path('rear-bottom',(24,42),[('C',(40,40),(30,45),(36,45)),('C',(42,24),(45,36),(45,30))])
""",'Omit the hidden crossing segments to keep the over-under structure readable.')
add('two-coin-stacks','HRECT_L','The rejected stacks have squashed black top rims and a crowded tall cylinder. Use wider coins, clear elliptical tops and fewer evenly spaced layers.','Lucide coins: clear circular/elliptic outlines; original supplies stacked cylinders.',"""
for n,l,r,t,b in [('tall',4,20,12,36),('short',28,44,24,36)]:
 cx=(l+r)//2;oval(n+'top',cx,t,8,4)
 path(n+'body',(l,t),[('L',(l,b)),('A',(r,b),8,4,False),('L',(r,t))]);join(n+'top',n+'body')
 if n=='tall':path('layer',(l,24),[('A',(r,24),8,4,False)]);join('layer',n+'body')
""",'Reduce the source tall stack to two broad tiers and the short stack to one; preserve unequal heights.')
add('two-eggs-in-decorated-bowl','SQUARE','The rejected bowl has narrow pointed eggs and only a short dash for its decorative wave. Restore round-topped eggs and a full-width wave across the bowl.','No useful direct Lucide match; original supplies eggs and waved bowl.',"""
path('bowl',(6,24),[('A',(42,24),18,18,False),('L',(30,24)),('L',(18,24)),('L',(6,24))],True)
for n,l,r in [('left',6,20),('right',28,42)]:
 path(n+'egg',(l,24),[('L',(l,16)),('A',(r,16),7,10,True),('L',(r,24))]);join(n+'egg','bowl')
path('wave',(8,32),[('C',(24,32),(13,23),(19,40)),('C',(40,32),(30,24),(35,38))]);join('wave','bowl')
""",'Omit individual egg patterns, absent in source.')
add('two-finger-swipe-right-upload-27a8bf31fe0cadb0','HRECT_L','Only the current drawing is available. Its arrow is a short bent mark and the finger arches are broad. Restore a long rightward shaft above two evenly sized fingers.','Lucide move-vertical: shaft and open arrowhead; original supplies two fingers.',"""
for n,l,r in [('first',4,20),('second',28,44)]:
 path(n,(l,40),[('L',(l,28)),('A',(r,28),8,8,True),('L',(r,40))])
line('shaft',(18,8),(38,8));poly('head',(32,4),(38,8),(32,12));join('shaft','head')
""")
add('two-overlapping-document-sheets','SQUARE','The rejected clone icon is a pair of angular octagons. Restore rounded sheet corners and a single clipped upper-right corner on the front sheet.','Lucide copy: rounded rear sheet partially occluded by a complete front sheet.',"""
path('front',(12,14),[('L',(26,14)),('A',(30,16),5,5,True),('L',(32,18)),('A',(34,22),5,5,True),('L',(34,36)),('A',(28,42),6,6,True),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,20)),('A',(12,14),6,6,True)],True)
path('rear',(14,14),[('L',(14,12)),('A',(20,6),6,6,True),('L',(36,6)),('A',(42,12),6,6,True),('L',(42,28)),('A',(36,34),6,6,True),('L',(34,34))]);join('rear','front')
""")
add('two-person-group-batch-078','HRECT_L','The rejected group has tiny heads and detached doorway-like bodies. Restore larger round heads and a broad foreground bust overlapping the smaller rear person.','human_ref/user.svg: circular heads and broad round shoulders; detached head gaps 4 ink.',"""
oval('head-front',16,13,5,5);oval('head-back',36,17,5,5)
path('body-front',(4,40),[('L',(4,36)),('A',(16,26),12,10,True),('A',(28,36),12,10,True),('L',(28,40)),('L',(4,40))],True)
path('body-back',(28,32),[('A',(36,30),12,6,True),('A',(44,36),8,6,True),('L',(44,40)),('L',(28,40))]);join('body-front','body-back')
""")
add('vertical-swipe-gesture','VRECT_L','The rejected arrows are tiny chevrons without shafts. Restore clear up/down arrows and a rounded horizontal finger between them.','Lucide move-vertical: aligned shafts and open arrowheads.',"""
path('finger',(8,20),[('L',(34,20)),('A',(34,28),4,4,True),('L',(8,28))])
for n,tip,base in [('up',4,12),('down',44,36)]:
 line(n+'shaft',(32,base),(32,tip));poly(n+'head',(26,base),(32,tip),(38,base));join(n+'shaft',n+'head')
""")
add('woman-with-halo','VRECT_L','The rejected portrait loses the long hair and garment and leaves disconnected side strokes. Restore a full circular jaw, long hair and rounded shoulders under the halo.','human_ref/user.svg: circular jaw and smooth shoulders with touching bust ink.',"""
oval('halo',24,8,16,4)
path('jaw',(32,22),[('A',(16,22),8,8,True)])
path('fringe',(16,22),[('L',(24,18)),('L',(32,22))]);join('jaw','fringe')
for n,x,s in [('left',8,-1),('right',40,1)]:
 path(n+'hair',(x,20),[('C',(x,32),(x-2*s,24),(x+2*s,28)),('L',(x,36))])
path('body',(8,44),[('A',(24,34),16,10,True),('A',(40,44),16,10,True)]);join('body','jaw')
""",'Omit clothing seam to keep the small portrait clear.')
D['woman-with-halo']['bust']=True
add('worker-wearing-ridged-hard-hat','VRECT_L','The rejected helmet has one short central stroke instead of its raised ridge, and the shoulders form a thin open arch. Restore an outlined helmet ridge and fuller shoulders.','Lucide hard-hat: outlined central ridge and curved shell; human_ref/user.svg: round jaw and shoulders.',"""
poly('ridge',(20,16),(20,4),(28,4),(28,16))
path('shell-left',(20,8),[('A',(8,20),12,12,False),('L',(40,20)),('A',(28,8),12,12,False)]);join('ridge','shell-left')
path('jaw',(34,20),[('A',(14,20),10,10,True)]);join('jaw','shell-left')
path('body',(8,44),[('L',(8,40)),('A',(24,34),16,6,True),('A',(40,40),16,6,True),('L',(40,44)),('L',(8,44))],True);join('body','jaw')
""",'Omit ears and narrow collar seam.')
D['worker-wearing-ridged-hard-hat']['bust']=True
if __name__=='__main__':generate(sys.argv[1:])
