"""Original plus sign was omitted from the rejected magnifier. Restore an evenly centered plus inside the circular lens.
Plan: SQUARE exact SOLO48 bounds; coherent contours and shared repeats.
Construction reference: search: circular lens and diagonal handle
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d2a83b3d-ee41-4915-81af-29e371bfd9b0'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__magnifying-glass-batch-04/20260929T135357Z-thuan-mac/reference/magnifying glass with plus_d2a83b3d-ee41-4915-81af-29e371bfd9b0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='magnifying-glass-batch-04'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    aliases=()
    keywords=('magnifying', 'glass', 'batch', '04')
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

        self.add_arc('lens-main',(30,33),(6,21),radius_x=15,large_arc=True,sweep=False)
        self.add_arc('lens-return',(6,21),(30,33),radius_x=15,sweep=False)
        self.add_contour('lens','lens-main','lens-return',closed=True)
        line('handle',(30,33),(42,42));join('handle','lens')
        line('plus-horizontal',(15,21),(27,21));line('plus-vertical',(21,15),(21,27));join('plus-horizontal','plus-vertical')
