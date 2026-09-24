"""Symmetric broad downward chevron, with one coherent rounded join.
Keyshape HRECT_M: exact SOLO48 contract envelope.
Construction: chevron-down: mirrored two-segment contour
Omissions: None; shallowest available horizontal keyshape selected.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__arrow-bottom-symbol/20260924T142441Z-thuan-mac/reference/arrow bottom_0ae4f1cf-6b9f-48d8-bd6d-83d0f2255432.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='arrow-bottom-symbol'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('arrow', 'bottom', 'symbol')
    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; here=start
            for i,step in enumerate(steps):
                tag=f'{name}-{i}'; kind,end,*args=step
                if kind=='L': self.add_line(tag,here,end)
                elif kind=='A': self.add_arc(tag,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(tag,here,(args[0],args[1],end))
                here=end;members.append(tag)
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        axis=24; half_width=20
        poly('chevron',(axis-half_width,10),(axis,38),(axis+half_width,10))
