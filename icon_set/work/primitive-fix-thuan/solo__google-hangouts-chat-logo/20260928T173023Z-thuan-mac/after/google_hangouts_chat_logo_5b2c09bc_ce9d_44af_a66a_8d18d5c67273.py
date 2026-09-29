'The at-sign had a tiny counter and an incomplete lower curl; the bubble tail was squared off. Enlarged the counter, completed the curl and restored the round bubble with its flowing pointed tail.\nSymbol plan: typed contours, shared radii and exact attachment nodes; paired features use common dimensions.\nConstruction: Lucide at-sign. Keyshape VRECT_L; any proportional departure is recorded as an exact-drawing exception.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5b2c09bc-ce9d-44af-a66a-8d18d5c67273'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__google-hangouts-chat-logo/20260928T173023Z-thuan-mac/reference/google hangouts chat logo_5b2c09bc-ce9d-44af-a66a-8d18d5c67273.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__google-hangouts-chat-logo/20260928T173023Z-thuan-mac/before/google_hangouts_chat_logo_5b2c09bc_ce9d_44af_a66a_8d18d5c67273.py'
class Drawing(Solo48):
    icon_id='google-hangouts-chat-logo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('google', 'hangouts', 'chat', 'logo')

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
        self.bubble()
        # The complete @ curl retains the lower terminal omitted in the rejected version.
        self.circle('at-counter',23,20,4)
        self.path('at-curl',(26,31),[('C',(14,21),(17,34),(14,28)),('C',(24,11),(14,14),(17,11)),('C',(34,21),(31,11),(34,14)),('C',(27,22),(34,27),(27,27)),('L',(27,20)),('L',(27,17))])
        self.relate('connect','at-counter','at-curl')

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The reference at-sign requires compact counters and clearance inside the speech bubble. Native light/dark review confirms an open central counter, clear spiral termination and distinct bubble tail.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'a98e0845c10d50d33b3041bdb34e34cd89e631a626d7383491c534b62ac342f9'}
