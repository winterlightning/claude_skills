"""A three-tier swirl with shared horizontal seams and a single broad curled top.
Reference comparison: Current poo has a tangled top curl and uneven tier shoulders. Rebuild three coherent rounded tiers with a readable smooth curl.
Construction reference: No useful exact match; smooth capsule base and coherent swirl.
SOLO48 keyshape SQUARE; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='c335382e-9874-5d16-95d4-344cff747084'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__pile-poo/20260928T172849Z-thuan-mac/reference/pile poo_c335382e-9874-5d16-95d4-344cff747084.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='pile-poo'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('pile', 'poo')

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
        path('base',(13,28),[('L',(35,28)),('A',(35,42),7,7,True),('L',(13,42)),('A',(13,28),7,7,True)],True)
        path('middle',(13,28),[('C',(17,18),(8,26),(10,18)),('L',(31,18)),('C',(35,28),(38,18),(40,26))]);join('middle','base')
        path('top',(17,18),[('C',(23,6),(12,11),(28,13)),('C',(31,18),(34,8),(38,17))]);join('top','middle')
