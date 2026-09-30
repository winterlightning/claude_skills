"""The rejected seat is a generic rounded box with a U mark. Restore a broad seat shell, diagonal harness branches and a central seat seam.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful direct match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c89b9f39-b2b3-4cf2-9e69-42a9bec8626c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__padded-infant-car-seat/20260929T135627Z-thuan-mac/reference/baby family baby seat car extention_c89b9f39-b2b3-4cf2-9e69-42a9bec8626c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='padded-infant-car-seat'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('padded', 'infant', 'car', 'seat')
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

        path('shell',(24,6),[('C',(38,18),(38,6),(38,12)),('L',(38,22)),('C',(42,32),(38,28),(42,29)),('A',(32,42),10,10,True),('L',(24,42)),('L',(16,42)),('A',(6,32),10,10,True),('C',(10,22),(6,29),(10,28)),('L',(10,18)),('C',(24,6),(10,12),(10,6))],True)
        poly('harness',(10,18),(24,30),(38,18));join('harness','shell')
        line('seat-seam',(24,30),(24,42));join('seat-seam','harness');join('seat-seam','shell')
