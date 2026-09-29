'The rear cap and horn had stepped, angular stroke joins. Restored rounded rear corners and horn tips, plus one continuous sound-wave curve.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: Lucide volume-1. Keyshape HRECT_L; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f2722b0f-fff4-493b-8f5d-619316ae89e6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__volume-control/20260928T173023Z-thuan-mac/reference/volume control_f2722b0f-fff4-493b-8f5d-619316ae89e6.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__volume-control/20260928T173023Z-thuan-mac/before/volume_control_f2722b0f_fff4_493b_8f5d_619316ae89e6.py'
class Drawing(Solo48):
    icon_id='volume-control'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('volume', 'control')

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
        # Smooth rear cap and gently rounded horn corners; waveform is a coherent symmetric curve.
        self.path('horn',(14,17),[('L',(30,6)),('C',(34,8),(32,4),(34,5)),('L',(34,40)),('C',(30,42),(34,43),(32,44)),('L',(14,31)),('L',(14,17))],True)
        self.path('rear',(14,17),[('L',(8,17)),('A',(4,21),4,4,False),('L',(4,27)),('A',(8,31),4,4,False),('L',(14,31))]);self.relate('connect','horn','rear')
        self.path('sound-wave',(40,14),[('C',(44,24),(42,16),(44,20)),('C',(40,34),(44,28),(42,32))])

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The original tapered speaker and curved sound wave require an asymmetric envelope and compact local clearance. Both the hollow speaker and detached wave remain clear at 48px.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': '5dfcc2f56c617618cc6388f9bdf5233cf43c76750e5d5305e99dae358563eb85'}
