"""diagram up double large head.
Before review: The inner arrowhead tips nearly touched, collapsing the gap between the paired upward arrows.
Feedback: Manual fix request
Revision: Separated the heads, lengthened both shafts and widened the smooth semicircular U while preserving symmetry.
Construction: Lucide move-up: equal open arrowheads and centered shafts.
Plan: coherent named contours; shared dimensions for mirrored or repeated parts.
SOLO48 SQUARE; 4px stroke. Native visual review required before acceptance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cada69c0-f437-4038-87b1-211bd013904e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-twin-upward-ends-on-u-curve/20260928T164556Z-thuan-mac/reference/diagram up double large head_cada69c0-f437-4038-87b1-211bd013904e.svg'
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = 'arrow-twin-upward-ends-on-u-curve'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('diagram', 'up', 'double', 'large', 'head')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for i,step in enumerate(steps):
                ident=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(ident,here,step); end=step
                elif step[0]=='C':
                    _,end,c1,c2=step
                    self.add_bezier(ident,here,(c1,c2,end))
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(ident,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def rounded(name,l,t,r,b,k):
            path(name,(l+k,t),[(r-k,t),((r,t+k),k,k,True),(r,b-k),((r-k,b),k,k,True),(l+k,b),((l,b-k),k,k,True),(l,t+k),((l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('u',(12,6),[(12,30),((36,30),12,12,False),(36,6)])
        poly('left',(6,12),(12,6),(18,12));poly('right',(30,12),(36,6),(42,12));join('u','left');join('u','right')
