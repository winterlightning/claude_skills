"""Two clean angular mountain peaks, one partial foreground ridge.
Reference comparison: Current mountains have doubled peak vertices and kinked bottom corners. Use simple coherent slopes with a clean shared baseline and foreground ridge.
Construction reference: Lucide mountain: coherent angular contour.
SOLO48 keyshape HRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='1990b78d-fa2b-41f9-81b9-9d3eacf11984'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__mountain/20260928T172849Z-thuan-mac/reference/mountain_1990b78d-fa2b-41f9-81b9-9d3eacf11984.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='mountain'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('mountain',)

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
        poly('outline',(4,40),(16,20),(20,25),(30,8),(44,40),closed=True)
        line('ridge',(20,25),(25,31));join('outline','ridge')
