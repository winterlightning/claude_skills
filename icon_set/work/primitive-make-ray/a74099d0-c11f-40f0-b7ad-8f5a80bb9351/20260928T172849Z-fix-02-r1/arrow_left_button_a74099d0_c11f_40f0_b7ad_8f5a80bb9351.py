"""One symmetric outlined chevron with a constant diagonal band.
Reference comparison: Current outlined chevron has a cramped kink at the inner turn and irregular outer tip. Rebuild a symmetric continuous chevron with equal band widths.
Construction reference: Lucide mountain: coherent line joins.
SOLO48 keyshape VRECT_L; uniform 4-unit strokes; explicit coherent symbol ownership.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a74099d0-c11f-40f0-b7ad-8f5a80bb9351'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__arrow-left-button/20260928T172849Z-thuan-mac/reference/arrow left button_a74099d0-c11f-40f0-b7ad-8f5a80bb9351.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='arrow-left-button'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('arrow', 'left', 'button')

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
        poly('chevron',(8,24),(28,4),(40,4),(20,24),(40,44),(28,44),closed=True)
