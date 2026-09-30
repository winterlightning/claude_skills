"""The rejected bowl has narrow pointed eggs and only a short dash for its decorative wave. Restore round-topped eggs and a full-width wave across the bowl.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct Lucide match; original supplies eggs and waved bowl.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d84437e5-b92a-4000-9da9-a5a11a87f9bb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-eggs-in-decorated-bowl/20260929T145934Z-thuan-mac/reference/easter egg basket_d84437e5-b92a-4000-9da9-a5a11a87f9bb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-eggs-in-decorated-bowl'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'eggs', 'in', 'decorated', 'bowl')
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

        path('bowl',(6,24),[('A',(42,24),18,18,False),('L',(30,24)),('L',(18,24)),('L',(6,24))],True)
        for n,l,r in [('left',6,20),('right',28,42)]:
         path(n+'egg',(l,24),[('L',(l,16)),('A',(r,16),7,10,True),('L',(r,24))]);join(n+'egg','bowl')
        path('wave',(8,32),[('C',(24,32),(13,23),(19,40)),('C',(40,32),(30,24),(35,38))]);join('wave','bowl')
