"""Fresh primitive-make-ray revisions. All source IDs/paths retained per record."""
from pathlib import Path
import json,re,sys,textwrap
ROOT=Path.cwd();sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from PIL import Image,ImageDraw
BATCH=Path(__file__).parent
claims=json.loads((BATCH/'claims.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID={r['index']:re.search(r'([a-f0-9-]{36})\.svg$',r['reference']).group(1) for r in claims}
SOURCE_PATH={r['index']:r['reference'] for r in claims}
HELPERS='''
    def path(self,n,p,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';q=c[1]
            if c[0]=='L':self.add_line(k,p,q)
            elif c[0]=='A':self.add_arc(k,p,q,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,p,(c[2],c[3],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4,split=None):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        commands=[]
        for i in range(8):
            q=pts[(i+1)%8]
            if i%2:commands.append(('A',q,rad,rad,True))
            else:
                for p in (split or {}).get(i,[]):commands.append(('L',p))
                commands.append(('L',q))
        self.path(n,pts[0],commands,True)
    def phone(self,l=10,r=38,t=4,b=44,footer=36):
        self.box('phone',l,t,r,b,4,{2:[(r,footer)],6:[(l,footer)]})
        self.add_line('bezel',(l,footer),(r,footer));self.relate('connect','phone','bezel')
    def monitor(self):
        self.box('screen',4,4,44,34,4,{4:[(24,34)]})
        self.add_line('stand',(24,34),(24,44))
        self.add_polyline('base',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','base')
    def dollar(self,cx=24,top=13):
        # Tangent semicircular bowls; centered currency ticks attach at split nodes.
        y=top
        self.path('dollar',(cx+4,y),[('L',(cx,y)),('L',(cx-1,y)),('A',(cx-1,y+8),4,4,False),('L',(cx+1,y+8)),('A',(cx+1,y+16),4,4,True),('L',(cx,y+16)),('L',(cx-4,y+16))])
        self.add_line('currency-top',(cx,y-3),(cx,y));self.add_line('currency-bottom',(cx,y+16),(cx,y+19))
        self.relate('connect','dollar','currency-top');self.relate('connect','dollar','currency-bottom')
'''
BODIES={
0:'''self.phone()
# Round insect abdomen; legs attach to six distinct perimeter nodes.
self.path('bug',(19,16),[('A',(24,11),5,5,True),('A',(29,16),5,5,True),('L',(29,22)),('A',(24,27),5,5,True),('A',(19,22),5,5,True),('L',(19,16))],True)
for side,x in [(-1,19),(1,29)]:
    for label,y,end_y in [('upper',16,13),('middle',19,19),('lower',22,25)]:
        name=f'leg-{side}-{label}'
        self.add_line(name,(x,y),(x+side*3,end_y))
        self.relate('connect','bug',name)
''',
1:'''self.phone()
self.dollar(top=12)
''',
2:'''self.phone()
''',
3:'''self.phone()
self.path('pin',(17,19),[('A',(31,19),7,7,True),('C',(24,29),(31,23),(27,27)),('C',(17,19),(21,27),(17,23))],True)
self.add_dot('pin-center',(24,19))
''',
4:'''self.phone()
# Two finder squares and two complementary corner marks reproduce the QR motif.
for name,x,y in [('finder-a',17,12),('finder-b',25,24)]:
    self.add_polyline(name,(x,y),(x+6,y),(x+6,y+6),(x,y+6),closed=True)
self.add_polyline('corner-upper',(29,12),(32,12),(32,16))
self.add_polyline('corner-lower',(16,26),(16,30),(19,30))
''',
5:'''self.phone()
self.circle('record-ring',24,20,8)
self.add_dot('record-dot',(24,20))
''',
6:'''self.phone()
self.add_line('earpiece',(22,10),(26,10))
''',
7:'''self.phone()
self.add_polyline('yen-fork',(18,12),(24,21),(30,12))
self.add_polyline('yen-stem',(24,21),(24,25),(24,30))
self.add_polyline('yen-bar',(19,25),(24,25),(29,25))
self.relate('connect','yen-fork','yen-stem');self.relate('connect','yen-stem','yen-bar')
''',
8:'''self.phone()
# Circular face and long hair; shoulders maintain exact 4u detached ink gap.
self.circle('face',24,18,5)
self.path('hair-left',(19,18),[('C',(17,26),(19,22),(19,24))])
self.path('hair-right',(29,18),[('C',(31,26),(29,22),(29,24))])
self.relate('connect','face','hair-left');self.relate('connect','face','hair-right')
self.path('shoulders',(16,36),[('A',(24,31),8,5,True),('A',(32,36),8,5,True)])
self.relate('connect','shoulders','bezel')
''',
9:'''self.phone()
self.add_polyline('yen-fork',(18,12),(24,21),(30,12))
self.add_polyline('yen-stem',(24,21),(24,25),(24,30))
self.add_polyline('yen-bar',(19,25),(24,25),(29,25))
self.relate('connect','yen-fork','yen-stem');self.relate('connect','yen-stem','yen-bar')
''',
10:'''self.phone()
''',
11:'''self.phone(l=12,r=36,t=6,b=42,footer=34)
self.add_line('home',(23,38),(25,38))
''',
12:'''self.phone()
self.circle('head',24,18,5)
# Exactly 8u from head outline y23 to shoulder apex y31, i.e. 4u visible gap.
self.path('shoulders',(16,36),[('A',(24,31),8,5,True),('A',(32,36),8,5,True)])
self.relate('connect','shoulders','bezel')
''',
13:'''# Broad chat panel and original lower-right speech tail.
self.path('bubble',(8,4),[('L',(40,4)),('A',(44,8),4,4,True),('L',(44,32)),('A',(40,36),4,4,True),('L',(36,36)),('L',(36,44)),('L',(26,36)),('L',(8,36)),('A',(4,32),4,4,True),('L',(4,8)),('A',(8,4),4,4,True)],True)
self.dollar(cx=16,top=12)
for y in (17,25):self.add_line(f'text-{y}',(30,y),(36,y))
''',
14:'''# Upper sensor and a continuous anatomical pointing-hand perimeter.
self.path('sensor',(18,28),[('L',(16,28)),('A',(10,22),6,6,True),('L',(10,14)),('A',(34,14),12,10,True),('L',(34,22)),('A',(28,28),6,6,True),('L',(24,28))])
self.add_polyline('pulse',(10,14),(16,14),(19,10),(24,19),(27,14),(34,14))
self.relate('connect','sensor','pulse')
self.path('hand',(14,44),[('L',(7,37)),('A',(13,31),4,4,True),('L',(18,36)),('L',(18,27)),('L',(18,25)),('A',(24,25),3,3,True),('L',(24,28)),('L',(24,34)),('L',(32,34)),('A',(40,42),8,8,True),('L',(40,44))])
self.relate('connect','sensor','hand')
''',
15:'''self.monitor()
# Reduce ABC to AB so the two characters have real separation at native size.
self.add_polyline('a',(12,27),(16,11),(20,27))
self.add_line('a-bar',(14,21),(18,21));self.relate('connect','a','a-bar')
self.path('b',(28,11),[('L',(31,11)),('A',(31,19),4,4,True),('L',(28,19)),('L',(31,19)),('A',(31,27),4,4,True),('L',(28,27)),('L',(28,19)),('L',(28,11))],True)
''',
16:'''self.monitor()
self.add_polyline('plus-h',(12,23),(17,23),(22,23))
self.add_polyline('plus-v',(17,18),(17,23),(17,28));self.relate('connect','plus-h','plus-v')
self.add_line('division-bar',(29,17),(36,17))
self.add_dot('division-top',(32,10));self.add_dot('division-bottom',(32,24))
''',
17:'''self.monitor()
for i,y in enumerate((11,23)):
    self.add_polyline(f'square-{i}',(13,y),(19,y),(19,y+6),(13,y+6),closed=True)
''',
18:'''# Four elongated fingers: shared 6u width/radius3; thumb points right.
class Mirror:
    def __init__(s,icon):s.icon=icon
    def add_line(s,n,a,b):s.icon.add_line(n,(48-a[0],a[1]),(48-b[0],b[1]))
    def add_arc(s,n,a,b,**kw):
        kw['sweep']=not kw.get('sweep',True);s.icon.add_arc(n,(48-a[0],a[1]),(48-b[0],b[1]),**kw)
    def add_bezier(s,n,a,cs):s.icon.add_bezier(n,(48-a[0],a[1]),tuple((48-p[0],p[1]) for p in cs))
    def add_contour(s,*a,**kw):s.icon.add_contour(*a,**kw)
s=Mirror(self)
self.draw_hand(s)
''',
19:'''self.draw_hand(self)
'''
}
HAND='''
    def draw_hand(self,s):
        # Four fingers share 6u centerline width; their tall proportions retain anatomy.
        cmds=[];heights=(10,7,10,16);first=16;pitch=6
        for i,y in enumerate(heights):
            x=first+i*pitch;cmds += [('L',(x,y)),('A',(x+pitch,y),3,3,True)]
        cmds += [('L',(40,31)),('A',(27,44),13,13,True),('L',(24,44)),('C',(15,40),(20,44),(17,43)),('L',(6,29)),('C',(11,25),(2,24),(7,21)),('L',(16,30))]
        # Emit with the same path construction, optionally reflected for the stop palm.
        ids=[];p=(16,30)
        for i,c in enumerate(cmds):
            n=f'hand-{i}';q=c[1]
            if c[0]=='L':s.add_line(n,p,q)
            elif c[0]=='A':s.add_arc(n,p,q,radius_x=c[2],radius_y=c[3],sweep=c[4])
            else:s.add_bezier(n,p,(c[2],c[3],q))
            p=q;ids.append(n)
        s.add_contour('hand',*ids,closed=True)
        for i in range(3):
            x=first+(i+1)*pitch;y=max(heights[i],heights[i+1])
            s.add_line(f'crease-{i}',(x,y),(x,23))
            self.relate('connect','hand',f'crease-{i}')
'''
NOTES={
0:('The wide phone and overlapping diagonal legs made the bug look like a gear.','Narrower rounded phone; oval insect body with six separately positioned legs.'),
1:('The phone was broad and the dollar crowded its screen.','Narrower device and compact dollar with smooth equal bowls and currency ticks.'),
2:('The phone was too broad and the lower band too tall relative to the reference.','Slender device silhouette with consistent corners and lower bezel.'),
3:('The phone had nearly square corners and its location pin lost the center mark.','Rounded slender phone, tapered pin and restored center dot.'),
4:('The QR shapes and thick device were cramped.','Slender rounded phone and rebalanced finder squares/corner marks.'),
5:('The current record ring omitted the reference center dot.','Slender phone and restored centered recording dot in a larger ring.'),
6:('The phone and earpiece were too wide.','Narrowed the device and shortened the earpiece.'),
7:('The broad phone compressed the yuan sign into a heavy fork.','Narrower phone, longer fork/stem and clearly placed yuan crossbar.'),
8:('The current phone omitted the lower bezel and reduced the woman to a small floating head.','Restored bezel, larger circular face, long hair and fuller shoulders.'),
9:('Square corners and wide frame differed from the original rounded smartphone.','Rounded narrower frame and rebalanced yuan sign.'),
10:('The current device was broader than the supplied screen silhouette.','Slimmer phone with softer corners and lower screen divider.'),
11:('The device was too large and its divider much too high, as the feedback says.','Smaller 28×40 visible body, lower divider and subtle home mark.'),
12:('The avatar head and shoulders were undersized within a wide phone.','Narrower phone, larger head, natural open shoulder arch and exact 4u head/body gap.'),
13:('The current bubble was narrow, omitted both text lines and reversed the source tail.','Wider/taller message panel, right-hand tail, dollar and two restored text lines.'),
14:('The short hooked thumb and broad finger did not read as the source hand.','Longer pointing finger, diagonal thumb and coherent rounded palm.'),
15:('ABC ran together; B and C overlapped.','Two separated letters AB with readable counters; omitted C to preserve UI legibility.'),
16:('The monitor was narrow and short, and its source proportions were lost.','Broader/taller screen with rounded corners and longer stand; retained plus and divide.'),
17:('The narrow monitor and short stand compressed the source layout.','Broader/taller rounded monitor, longer stand and two vertically spaced squares.'),
18:('The stop hand was squat with short fingers and a sideways thumb.','Tall four-finger anatomy, diagonal right thumb and rounded palm.'),
19:('The hand was squat, with a block-like upright thumb.','Elongated fingers, diagonal left thumb and a tapered rounded palm.')}

def author(indices=None,rev=1):
 for rec in claims:
    i=rec['index']
    if indices is not None and i not in indices:continue
    ref=Path(rec['reference']);sid=SOURCE_ICON_ID[i];concept=ref.stem[:-37]
    run=Path('icon_set/work/primitive-make-ray')/sid/f'20260928T170716Z-fix-{i:02d}-r{rev}'
    run.mkdir(parents=True,exist_ok=False)
    meta=dict(concept=concept,source_uuid=sid,reference_path=str(ref))
    (run/f"{rec['icon_id']}.metadata.json").write_text(json.dumps(meta,indent=2))
    keyshape='VRECT_M' if i<13 else 'SQUARE'
    if i in (14,18,19):keyshape='VRECT_L'
    before,change=NOTES[i];reason=f'{before} {change}'
    lucide='smartphone' if i<13 else 'hand' if i in (14,18,19) else 'monitor' if i in (15,16,17) else 'dollar-sign'
    module=run/(rec['icon_id'].removesuffix('-'+sid).replace('-','_')+'_'+sid.replace('-','_')+'.py')
    doc=f'{reason}\nSymbol plan: enclosure owns content; shared dimensions, radii, repetition and actual attachment nodes.\nConstruction: local Lucide {lucide} original and atomic-debug. Human busts use human_ref/user.svg.\nKeyshape {keyshape}: intended proportional envelope; any departure is separately recorded as a drawing-bound exception.'
    source=f'{doc!r}\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {sid!r}\nSOURCE_PATH = {str(ref)!r}\nAUTHOR = {AUTHOR!r}\nPARENT_MODULE = {str(next((Path(rec["fix"])/"before").glob("*.py")))!r}\nclass Drawing(Solo48):\n    icon_id = {rec["icon_id"]!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "primitives-generate"\n    aliases = ()\n    keywords = {tuple(concept.split())!r}\n'+HELPERS+(HAND if i in (18,19) else '')+'\n    def build(self):\n'+textwrap.indent(BODIES[i],'        ')
    module.write_text(source)
    icon=load_icon(module);svg=icon.to_svg();(run/(rec['icon_id']+'.svg')).write_text(svg)
    report=icon.validate_icon();(run/'validation.txt').write_text(report.describe())
    render_previews(svg,rec['icon_id'],48,run)
    for kind in ('original','before'):
        import shutil
        shutil.copyfile(Path(rec['fix'])/(kind+'.png'),run/(kind+'.png'))
    (run/'review.json').write_text(json.dumps(dict(before_problem=before,feedback=rec['feedback'],changes=change,construction_reference=lucide,omissions='C omitted from ABC for clear spacing.' if i==15 else 'Woman collar and fringe omitted at 48px.' if i==8 else 'None'),indent=2))
    rec.update(run=str(run),module=str(module),note=change)
    print(i,rec['icon_id'],report.status,len(report.errors),len(report.warnings),flush=True)
 (BATCH/'authored.json').write_text(json.dumps(claims,indent=2))

def sheets():
 for start in range(0,20,5):
    im=Image.new('RGB',(840,5*230),'#ddd');d=ImageDraw.Draw(im)
    for row,rec in enumerate(claims[start:start+5]):
        y=row*230;run=Path(rec['run']);d.text((8,y+2),f"{rec['index']} {rec['icon_id']}",fill='black')
        for col,name in enumerate(['original.png','before.png','preview-light-384.png','preview-dark-384.png']):
            pic=Image.open(run/name).convert('RGB');pic.thumbnail((174,174));im.paste(pic,(8+col*206,y+26))
        for col,theme in enumerate(['light','dark']):im.paste(Image.open(run/f'preview-{theme}-48.png').convert('RGB'),(420+col*206,y+178))
    im.save(BATCH/f'after-{start//5}.png')
if __name__=='__main__':
 author();sheets()
