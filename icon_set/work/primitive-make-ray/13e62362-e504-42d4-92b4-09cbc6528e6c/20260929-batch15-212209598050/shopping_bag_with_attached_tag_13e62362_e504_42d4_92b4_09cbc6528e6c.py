"""The rejected price tag is upright and squared off. Restore a diagonal tag attached to the bag rim, with a curved handle and tapered bag.
Plan: HRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: Lucide shopping-bag: coherent bag outline and handle attachment.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='13e62362-e504-42d4-92b4-09cbc6528e6c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__shopping-bag-with-attached-tag/20260929T141814Z-thuan-mac/reference/shopping bag tag_13e62362-e504-42d4-92b4-09cbc6528e6c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='shopping-bag-with-attached-tag'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('shopping', 'bag', 'with', 'attached', 'tag')
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

        path('bag',(8,24),[('L',(20,24)),('L',(28,24)),('L',(32,36)),('A',(28,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(8,24))],True)
        path('handle',(8,24),[('L',(8,14)),('A',(20,14),6,6,True),('L',(20,24))]);join('handle','bag')
        poly('tag',(28,16),(36,8),(44,16),(36,24),(28,24),(28,16));join('tag','bag')
