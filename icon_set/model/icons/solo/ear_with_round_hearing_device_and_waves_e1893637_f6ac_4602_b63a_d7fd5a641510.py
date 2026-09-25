"""Smooth outer ear with a round hearing device and two evenly separated sound waves.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction: ear: continuous helix and lower lobe; human reference checked for consistent rounded anatomy
Omissions: Interior canal curl omitted to keep the hearing device and waves clear.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1893637-f6ac-4602-b63a-d7fd5a641510'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_15/disability hearing aid t_e1893637-f6ac-4602-b63a-d7fd5a641510.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='ear-with-round-hearing-device-and-waves'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('ear', 'with', 'round', 'hearing', 'device', 'and', 'waves')
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

        path('ear',(4,12),[('C',(14,8),(5,9),(8,8)),('C',(24,18),(21,8),(24,11)),('C',(18,31),(24,25),(20,27)),('C',(14,40),(17,36),(18,40)),('C',(4,37),(8,40),(4,39))])
        ellipse('device',8,24,4,4)
        path('wave-inner',(33,18),[('C',(35,24),(34,20),(35,22)),('C',(33,30),(35,26),(34,28))])
        path('wave-outer',(40,8),[('C',(44,24),(43,13),(44,18)),('C',(40,40),(44,30),(43,35))])
