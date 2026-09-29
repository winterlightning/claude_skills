'The upper g bowl was squared and flattened, and the lower loop was undersized. Restored a circular upper bowl, broader oval descender, curved neck and evenly formed plus.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: No direct Lucide brand match; circular and oval letter construction. Keyshape SQUARE; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='96faaeef-c843-44fa-8d47-77cb3ec2c55b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__google-plus-lowercase-logo/20260928T173023Z-thuan-mac/reference/google plus logo 2_96faaeef-c843-44fa-8d47-77cb3ec2c55b.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__google-plus-lowercase-logo/20260928T173023Z-thuan-mac/before/google_plus_lowercase_logo_96faaeef_c843_44fa_8d47_77cb3ec2c55b.py'
class Drawing(Solo48):
    icon_id='google-plus-lowercase-logo'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('google', 'plus', 'logo', '2')

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

    def node(self,n,x,y,r,extra=()):
        import math
        offsets=set([(-r,0),(0,-r),(r,0),(0,r),*extra])
        offsets=sorted(offsets,key=lambda p:math.atan2(p[1],p[0]))
        pts=[(x+dx,y+dy) for dx,dy in offsets]
        self.path(n,pts[0],[('A',q,r,r,True) for q in pts[1:]+pts[:1]],True)

    def bubble(self):
        self.path('bubble',(22,38),[('L',(22,44)),('C',(40,22),(33,39),(40,31)),('C',(24,4),(40,12),(33,4)),('C',(8,21),(15,4),(8,11)),('C',(22,38),(8,31),(14,37))],True)
    def file(self):
        self.path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('fold',(28,4),[('L',(28,12)),('A',(32,16),4,4,False),('L',(40,16))]);self.relate('connect','page','fold')

    def build(self):
        # Double-storey lowercase g with true circular upper bowl and oval descender.
        self.circle('upper-bowl',16,13,9)
        self.add_line('ear',(16,4),(29,4));self.relate('connect','upper-bowl','ear')
        self.path('lower-loop',(5,37),[('A',(16,30),11,7,True),('A',(27,37),11,7,True),('A',(16,44),11,7,True),('A',(5,37),11,7,True)],True)
        self.path('neck',(16,22),[('C',(16,30),(9,23),(9,29))]);self.relate('connect','neck','upper-bowl');self.relate('connect','neck','lower-loop')
        self.add_polyline('plus-h',(32,22),(38,22),(44,22));self.add_polyline('plus-v',(38,16),(38,22),(38,28));self.relate('connect','plus-h','plus-v')

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The circular upper bowl, oval lower bowl, connecting neck and plus retain the source lowercase g logo. Native review confirms distinct open bowls and separate plus; its typographic proportions use expanded bounds.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': '44f8d81c6aa76fadbf1957a505c228685ba2074a6c0c8e8585e2331210ae007d'}
