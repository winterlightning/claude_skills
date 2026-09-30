"""Extreme inward notches make controllers look like handles; flatten notches and deepen bodies.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: gamepad-2: rounded grip silhouette
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='17820290-30de-49a4-8c9c-08bc95fae445'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-opposing-gamepads/20260929T131521Z-thuan-mac/reference/one vs one mode 1_17820290-30de-49a4-8c9c-08bc95fae445.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-opposing-gamepads'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'opposing', 'gamepads')
    def build(self):

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

        for j,s in enumerate((1,-1)):
         p=lambda x,y:(x,24+s*(y-24))
         path(f'pad{j}',p(6,12),[('A',p(18,12),6,6,s==1),('L',p(30,12)),('A',p(42,12),6,6,s==1),('L',p(42,15)),('A',p(37,20),5,5,s==1),('L',p(11,20)),('A',p(6,15),5,5,s==1),('L',p(6,12))],True)
