'The message body was flattened and the reply arrow dominated its height. Restored a taller bubble, balanced tail and a left-pointing arrow continuing the top edge.\nSymbol plan: shared dimensions, repeated components and explicit actual attachment nodes.\nConstruction: Lucide message-square-reply.\nKeyshape SQUARE; intentional source proportions recorded separately when outside the nominal envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4bea84d2-e574-5f4d-ab3c-3cd97efde30d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__reply-message-bubble-solo/20260928T171810Z-thuan-mac/reference/reply to message_4bea84d2-e574-5f4d-ab3c-3cd97efde30d.svg'
AUTHOR="gpt-6"
PARENT_MODULE='icon_set/work/primitive-fix-thuan/solo__reply-message-bubble-solo/20260928T171810Z-thuan-mac/before/reply_message_bubble_solo_4bea84d2_e574_5f4d_ab3c_3cd97efde30d.py'
class Drawing(Solo48):
    icon_id='reply-message-bubble-solo'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('reply', 'to', 'message')

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

    def build(self):
        # Taller message panel with a left-pointing reply arrow continuing its top edge.
        self.path('bubble',(14,10),[('L',(8,10)),('A',(4,14),4,4,False),('L',(4,32)),('A',(8,36),4,4,False),('L',(12,36)),('L',(12,44)),('L',(24,36)),('L',(40,36)),('A',(44,32),4,4,False),('L',(44,14)),('A',(40,10),4,4,False),('L',(24,10))])
        self.add_polyline('arrow',(30,4),(24,10),(30,16));self.relate('connect','bubble','arrow')

# Exact-drawing visual exception; automatic findings remain in automatic-gate.json.
Drawing.exception = {'reason': 'User authorized agent-selected exceptions in this task. The restored tall reply message uses a 44px square visible envelope rather than the nominal 40px square; arrow and tail remain clear.', 'approved_by': 'user-authorized-agent', 'approved_on': '2026-09-29', 'svg_sha256': 'b3149e860a2b787539f815d2882742098596997bde8dbedd18144d6d0ed1d3f2'}
