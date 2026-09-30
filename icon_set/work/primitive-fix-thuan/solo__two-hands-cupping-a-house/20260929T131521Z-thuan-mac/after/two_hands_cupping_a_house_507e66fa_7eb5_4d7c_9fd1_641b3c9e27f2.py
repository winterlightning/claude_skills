"""Single strokes read like twigs rather than hands; restore rounded finger-and-palm contours around house.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: hand: rounded fingers; house: roof silhouette
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='507e66fa-7eb5-4d7c-9fd1-641b3c9e27f2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__two-hands-cupping-a-house/20260929T131521Z-thuan-mac/reference/real estate favorite hold house_507e66fa-7eb5-4d7c-9fd1-641b3c9e27f2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='two-hands-cupping-a-house'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('two', 'hands', 'cupping', 'a', 'house')
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

        poly('house',(15,16),(24,6),(33,16),(33,23),(15,23),closed=True)
        for s in (-1,1):
         x=lambda a:24+s*a
         path(f'hand{s}',(x(6),42),[('L',(x(6),39)),('L',(x(12),33)),('C',(x(18),33),(x(15),30),(x(18),30)),('L',(x(18),25)),('L',(x(18),34)),('C',(x(17),42),(x(18),37),(x(18),40))])
