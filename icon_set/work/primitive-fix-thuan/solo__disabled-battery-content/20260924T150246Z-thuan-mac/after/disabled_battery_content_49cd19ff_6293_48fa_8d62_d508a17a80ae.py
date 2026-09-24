"""Complete battery outline with a right terminal and one diagonal disabling slash, without arrow-like corners.
Keyshape HRECT_M: exact SOLO48 contract envelope.
Construction: battery: continuous outline and right terminal
Omissions: None.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='49cd19ff-6293-48fa-8d62-d508a17a80ae'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__disabled-battery-content/20260924T150246Z-thuan-mac/reference/slash battery_49cd19ff-6293-48fa-8d62-d508a17a80ae.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='disabled-battery-content'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('disabled', 'battery', 'content')
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

        path('battery',(4,38),[('L',(4,14)),('A',(8,10),4,4,True),('L',(36,10)),('L',(36,34)),('A',(32,38),4,4,True),('L',(4,38))],True)
        line('slash',(4,38),(36,10));join('slash','battery')
        poly('terminal',(36,22),(44,22),(44,30),(36,30));join('terminal','battery')
