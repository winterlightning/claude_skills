"""A true circle behind an aligned square; the hidden quadrant is omitted.
Reference comparison: Current circle behind the square is visibly polygonal. Use a true circular arc interrupted by the square and exact shared occlusion endpoints.
Construction reference: Lucide circle: cardinal quarter arcs.
SOLO48 keyshape SQUARE; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='17f79cde-6e3f-435d-9f0d-3ea8fa026ef2'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pie-chart-and-square/20260928T172849Z-thuan-mac/reference/pie chart and square_17f79cde-6e3f-435d-9f0d-3ea8fa026ef2.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='pie-chart-and-square'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pie', 'chart', 'and', 'square')

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
        path('circle',(34,20),[('A',(20,6),14,14,False),('A',(6,20),14,14,False),('A',(20,34),14,14,False)])
        poly('square',(20,34),(20,20),(34,20),(42,20),(42,42),(20,42),(20,34),closed=True);join('circle','square')
