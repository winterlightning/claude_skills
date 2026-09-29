"""Two triangular mountains with one clean shared baseline and one continuous foreground slope.
Reference comparison: Current mountain infantry has doubled peak vertices and malformed lower corners. Rebuild two clean triangular peaks with one shared baseline.
Construction reference: Lucide mountain: intentional angular peaks.
SOLO48 keyshape HRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='56fac8f8-8d3d-40b1-a35c-415b751a3a8b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__symbol-mountain-infantry/20260928T172849Z-thuan-mac/reference/symbol mountain infantry_56fac8f8-8d3d-40b1-a35c-415b751a3a8b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='symbol-mountain-infantry'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('symbol', 'mountain', 'infantry')

    def build(self):

        # Typed path helpers own continuous contours, repeated radii and real junctions.
        def path(name,start,commands,closed=False):
            here=start;members=[]
            for i,c in enumerate(commands):
                kind,end,*args=c; ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C':
                    c1,c2=args
                    self.add_bezier(ident,here,(c1,c2,end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        poly('outer',(4,40),(14,22),(20,29),(30,8),(44,40),(28,40),closed=True)
        line('ridge',(20,29),(28,40));join('outer','ridge')
