"""The rejected side arrows have no shafts and look like chevrons; the upper and lower shafts disappear. Restore four visible shafts around the fingertip.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: No useful additional match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='72ae8ec4-64bb-45c4-a5c0-d263a783fa1d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__multi-directional-expansion-touch-gesture/20260929T135554Z-thuan-mac/reference/gesture expand_72ae8ec4-64bb-45c4-a5c0-d263a783fa1d.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='multi-directional-expansion-touch-gesture'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('multi', 'directional', 'expansion', 'touch', 'gesture')
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

        path('finger',(20,28),[('L',(20,24)),('A',(28,24),4,4,True),('L',(28,28))])
        for name,tip,wing1,wing2,tail in [('up',(24,6),(18,12),(30,12),(24,12)),('down',(24,42),(18,36),(30,36),(24,36)),('left',(6,24),(12,18),(12,30),(12,24)),('right',(42,24),(36,18),(36,30),(36,24))]:
         poly(name,wing1,tip,wing2);line(name+'-shaft',tip,tail);join(name,name+'-shaft')
