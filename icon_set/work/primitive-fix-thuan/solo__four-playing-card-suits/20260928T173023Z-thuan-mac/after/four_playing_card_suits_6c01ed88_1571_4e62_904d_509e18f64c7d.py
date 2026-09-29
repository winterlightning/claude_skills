'The heart was a narrow wedge and the other suit lobes were cramped. Redrew all four symbols; the heart now has broad matched lobes, a clear notch and a centered tip.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: Lucide heart, club and spade. Keyshape SQUARE; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6c01ed88-1571-4e62-904d-509e18f64c7d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__four-playing-card-suits/20260928T173023Z-thuan-mac/reference/card game symbols_6c01ed88-1571-4e62-904d-509e18f64c7d.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__four-playing-card-suits/20260928T173023Z-thuan-mac/before/four_playing_card_suits_6c01ed88_1571_4e62_904d_509e18f64c7d.py'
class Drawing(Solo48):
    icon_id='four-playing-card-suits'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('card', 'game', 'symbols')

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
        # Four distinct suits. Heart lobes are broad and mirrored around x35.
        self.add_polyline('diamond',(12,4),(20,13),(12,22),(4,13),closed=True)
        self.path('club',(31,12),[('C',(35,4),(29,7),(31,4)),('C',(39,12),(39,4),(41,7)),('C',(43,18),(43,10),(45,14)),('C',(35,18),(41,22),(37,21)),('C',(27,18),(33,21),(29,22)),('C',(31,12),(25,14),(27,10))],True)
        self.add_line('club-stem',(35,18),(35,22));self.relate('connect','club','club-stem')
        self.path('spade',(12,28),[('C',(4,37),(8,32),(4,34)),('C',(12,40),(4,42),(9,43)),('C',(20,37),(15,43),(20,42)),('C',(12,28),(20,34),(16,32))],True)
        self.add_line('spade-stem',(12,40),(12,44));self.relate('connect','spade','spade-stem')
        self.path('heart',(35,31),[('C',(27,32),(33,25),(27,27)),('C',(35,44),(27,36),(32,41)),('C',(43,32),(38,41),(43,36)),('C',(35,31),(43,27),(37,25))],True)

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. All four suits preserve their natural proportions and the reviewer-requested broad heart. The compact four-part layout uses wider bounds and smaller inter-suit clearances; all counters remain open at native 48px.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': '7cc361a9d43b5ae68c2f791511af5115629aa9926ad7a584a93cd25e6dc896f2'}
