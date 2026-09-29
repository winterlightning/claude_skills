"""Two equal circular loops, each with one tangent tail; rotational symmetry about the canvas center.
Reference comparison: Current loops are uneven and the top-left loop has a flat diagonal. Feedback specifically requests smooth curve circles. Use exact equal circles with tangent horizontal tails.
Construction reference: Lucide circle: circular arcs.
SOLO48 keyshape HRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b90476b0-fb60-4264-993a-bffbb01cd2c8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__astrology-pisces/20260928T172849Z-thuan-mac/reference/astrology pisces_b90476b0-fb60-4264-993a-bffbb01cd2c8.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='astrology-pisces'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('astrology', 'pisces')

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
        circle('upper-loop',12,16,8);circle('lower-loop',36,32,8)
        line('upper-tail',(12,8),(44,8));line('lower-tail',(36,40),(4,40))
        join('upper-loop','upper-tail');join('lower-loop','lower-tail')
