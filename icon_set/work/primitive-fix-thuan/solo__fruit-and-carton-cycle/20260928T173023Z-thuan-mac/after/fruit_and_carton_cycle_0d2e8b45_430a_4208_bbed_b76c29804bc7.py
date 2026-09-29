'The cycle arrows were angular hooks; the carton fold was missing. Rebuilt curved directional arrows, shaped the apple and restored a gabled carton with a side fold.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: Lucide apple and milk. Keyshape SQUARE; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0d2e8b45-430a-4208-bbed-b76c29804bc7'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__fruit-and-carton-cycle/20260928T173023Z-thuan-mac/reference/supply chain distributor fruit juice_0d2e8b45-430a-4208-bbed-b76c29804bc7.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__fruit-and-carton-cycle/20260928T173023Z-thuan-mac/before/fruit_and_carton_cycle_0d2e8b45_430a_4208_bbed_b76c29804bc7.py'
class Drawing(Solo48):
    icon_id='fruit-and-carton-cycle'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('supply', 'chain', 'distributor', 'fruit', 'juice')

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
        # Four quadrant layout: apple, two curved arrows and gabled carton.
        self.path('apple',(13,10),[('C',(5,13),(9,7),(5,9)),('C',(13,24),(4,22),(10,25)),('C',(21,13),(16,25),(22,22)),('C',(13,10),(21,9),(17,7))],True)
        self.add_polyline('stem',(13,10),(13,7),(13,4));self.relate('connect','apple','stem')
        self.path('leaf',(13,7),[('C',(19,5),(15,5),(17,5))]);self.relate('connect','stem','leaf')
        self.path('upper-arrow',(42,19),[('C',(27,8),(40,12),(34,8))])
        self.add_polyline('upper-head',(32,4),(27,8),(32,12));self.relate('connect','upper-arrow','upper-head')
        self.path('lower-arrow',(4,28),[('C',(18,40),(4,35),(10,40))])
        self.add_polyline('lower-head',(14,36),(18,40),(14,44));self.relate('connect','lower-arrow','lower-head')
        self.add_polyline('carton',(28,44),(28,32),(32,26),(40,26),(44,32),(44,44),(36,44),closed=True)
        self.add_polyline('carton-fold',(32,26),(36,32),(36,44));self.relate('connect','carton','carton-fold')

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The apple, folded carton and paired cycle arrows retain the original meaning. Compact carton panels and arrow spacing remain visibly distinct at 48px; the wider bounds support recognizable silhouettes.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'c20c3a6cb5f38f3dcd3576acedac1f3b1637c18c5f6bb0d68c565174a82f6e8c'}
