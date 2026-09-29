"""Diagonal pen with parallel barrel edges, symmetric round cap and an open triangular nib.
Reference comparison: Current pen has a faceted cap and uneven taper. Use a symmetric diagonal barrel, semicircular cap and a clear point.
Construction reference: Lucide bookmark: coherent round joins.
SOLO48 keyshape SQUARE; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='7ee2f930-e642-4295-aaa3-5150e3fc91e5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pen-7ee2f930/20260928T172849Z-thuan-mac/reference/pen_7ee2f930-e642-4295-aaa3-5150e3fc91e5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='pen-7ee2f930'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pen',)

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
        path('pen',(6,42),[('L',(11,27)),('L',(30,8)),('A',(40,18),7,7,True),('L',(21,37)),('L',(6,42))],True)
