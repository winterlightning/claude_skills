"""Sharp low-rise bottom and angular cups differ from rounded fabric shapes; soften curves and deepen bottom.
Plan: VRECT_L exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful exact Lucide match; source garment contour.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5002effe-d0b9-44d4-bf7e-f04e426d4473'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-piece-bikini-set/20260929T131521Z-thuan-mac/reference/bikini_5002effe-d0b9-44d4-bf7e-f04e426d4473.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-piece-bikini-set'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'piece', 'bikini', 'set')
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

        path('cups',(14,12),[('C',(24,22),(19,15),(22,18)),('C',(34,12),(26,18),(29,15)),('C',(40,22),(37,15),(40,19)),('C',(24,22),(40,28),(30,28)),('C',(8,22),(18,28),(8,28)),('C',(14,12),(8,19),(11,15))],True)
        for x in (14,34):line(f'strap{x}',(x,4),(x,12));join(f'strap{x}','cups')
        path('bottom',(8,35),[('C',(40,35),(18,37),(30,37)),('C',(28,44),(34,37),(31,41)),('L',(20,44)),('C',(8,35),(17,41),(14,37))],True)
