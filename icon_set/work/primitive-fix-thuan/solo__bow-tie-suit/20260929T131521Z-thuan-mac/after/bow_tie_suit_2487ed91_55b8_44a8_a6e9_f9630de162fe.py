"""Short lapels and tiny bow openings weaken the tuxedo; lengthen the V and broaden bow.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: shirt: continuous jacket outline
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='2487ed91-55b8-44a8-a6e9-f9630de162fe'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__bow-tie-suit/20260929T131521Z-thuan-mac/reference/tuxedo_2487ed91-55b8-44a8-a6e9-f9630de162fe.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='bow-tie-suit'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('bow', 'tie', 'suit')
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

        poly('bow',(14,6),(24,12),(34,6),(34,18),(24,12),(14,18),closed=True)
        poly('lapels',(14,18),(24,36),(34,18));join('lapels','bow')
        for s in (-1,1):
         x=lambda a:24+s*a
         poly(f'jacket{s}',(x(10),18),(x(18),22),(x(17),42));join(f'jacket{s}','bow')
        line('seam',(24,36),(24,42));join('seam','lapels')
