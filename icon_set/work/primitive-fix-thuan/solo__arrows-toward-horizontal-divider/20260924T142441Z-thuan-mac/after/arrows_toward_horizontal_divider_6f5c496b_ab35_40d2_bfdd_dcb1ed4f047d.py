"""Two vertically mirrored arrows point toward a detached horizontal guide. Longer shafts preserve reference proportions.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: arrow-down-right and chevron-down: common arrow vertices; align-vertical-justify-center: central guide spacing
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6f5c496b-ab35-40d2-bfdd-dcb1ed4f047d'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__arrows-toward-horizontal-divider/20260924T142441Z-thuan-mac/reference/shrink vertical_6f5c496b-ab35-40d2-bfdd-dcb1ed4f047d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='arrows-toward-horizontal-divider'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('arrows', 'toward', 'horizontal', 'divider')
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

        line('guide',(6,24),(42,24))
        for side in (-1,1):
         y=lambda d:24+side*d
         name=f'arrow-{side}'
         poly(name,(17,y(15)),(24,y(8)),(31,y(15)))
         line(name+'-shaft',(24,y(18)),(24,y(8)));join(name,name+'-shaft')
