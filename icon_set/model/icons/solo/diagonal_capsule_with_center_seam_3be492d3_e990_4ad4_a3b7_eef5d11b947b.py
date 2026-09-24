"""Upright diagonal capsule with matching rounded ends, parallel sides and a centered transverse seam.
Keyshape VRECT_L: exact SOLO48 contract envelope.
Construction: pill: paired rounded ends and perpendicular seam
Omissions: None; steeper source tilt restored.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3be492d3-e990-4ad4-a3b7-eef5d11b947b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/emery_3be492d3-e990-4ad4-a3b7-eef5d11b947b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-capsule-with-center-seam'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/reference'
    aliases=()
    keywords=('diagonal', 'capsule', 'with', 'center', 'seam')
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

        path('capsule',(21,9),[('C',(30,4),(23,5),(26,4)),('A',(40,14),10,10,True),('C',(39,19),(40,16),(40,17)),('L',(27,39)),('C',(18,44),(25,43),(22,44)),('A',(8,34),10,10,True),('C',(9,29),(8,32),(8,31)),('L',(21,9))],True)
        line('seam',(15,19),(33,29));join('seam','capsule')
