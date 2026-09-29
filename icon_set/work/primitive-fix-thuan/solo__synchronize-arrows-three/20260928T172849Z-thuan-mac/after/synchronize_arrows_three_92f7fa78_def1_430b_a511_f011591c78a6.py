"""Three rotating arrow strokes with coherent circular arcs and simple two-arm heads.
Reference comparison: Current sync arrows have unequal arc radii and cramped bent arrowheads. Rebuild three smooth circular-direction strokes and clean arrowheads.
Construction reference: Lucide refresh-cw: smooth arcs with shared arrowhead nodes.
SOLO48 keyshape SQUARE; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='92f7fa78-def1-430b-a511-f011591c78a6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__synchronize-arrows-three/20260928T172849Z-thuan-mac/reference/synchronize arrows three_92f7fa78-def1-430b-a511-f011591c78a6.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='synchronize-arrows-three'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('synchronize', 'arrows', 'three')

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
        path('top-arc',(36,14),[('A',(14,12),16,16,False)])
        poly('top-head',(17,6),(14,12),(21,14));join('top-arc','top-head')
        path('left-arc',(8,19),[('A',(6,26),17,17,False),('A',(14,40),17,17,False)])
        poly('left-head',(7,42),(14,40),(12,33));join('left-arc','left-head')
        path('right-arc',(24,42),[('A',(40,23),19,19,False)])
        poly('right-head',(34,28),(40,23),(42,30));join('right-arc','right-head')
