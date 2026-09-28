"""Rounded L-shaped inhaler with a cap seam and separate mouthpiece seam.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: cooking-pot: tangent rounded body corners
Omissions: Tilt normalized upright to preserve grid and clear openings.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4517e685-6537-5c40-aa8e-73894c87d03b'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__asthma-inhaler/20260924T142441Z-thuan-mac/reference/inhaler_4517e685-6537-5c40-aa8e-73894c87d03b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='asthma-inhaler'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('asthma', 'inhaler')
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

        path('body',(8,4),[('L',(24,4)),('L',(24,28)),('L',(36,28)),('A',(40,32),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(16,44)),('A',(8,36),8,8,True),('L',(8,4))],True)
        line('cap',(8,12),(24,12));join('cap','body')
        line('mouthpiece',(32,28),(32,44));join('mouthpiece','body')
