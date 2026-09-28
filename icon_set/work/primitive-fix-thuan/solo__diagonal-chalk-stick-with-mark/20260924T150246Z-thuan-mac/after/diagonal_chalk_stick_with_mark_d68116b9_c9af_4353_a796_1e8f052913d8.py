"""Diagonal chalk stick with rounded upper end, beveled lower end and a detached horizontal chalk mark.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: pencil and pill: coherent diagonal body and round terminal
Omissions: None; missing chalk mark restored.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='d68116b9-c9af-4353-a796-1e8f052913d8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__diagonal-chalk-stick-with-mark/20260924T150246Z-thuan-mac/reference/chalk_d68116b9-c9af-4353-a796-1e8f052913d8.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-chalk-stick-with-mark'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('diagonal', 'chalk', 'stick', 'with', 'mark')
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

        path('chalk',(6,34),[('C',(10,26),(6,31),(7,28)),('L',(32,6)),('L',(36,6)),('C',(42,12),(39,6),(42,9)),('L',(18,32)),('L',(6,34))],True)
        line('bevel',(10,26),(18,32));join('bevel','chalk')
        line('mark',(18,42),(36,42))
