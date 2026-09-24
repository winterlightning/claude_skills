"""Balloon dog built from elongated oval lobes at shared twist junctions; rounded muzzle, ear, body, two legs and rising tail.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: bone: smooth rounded lobes; source governs balloon arrangement
Omissions: Far-side legs omitted as in source.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '20ee5dd9-0486-5c78-98b3-c068d4af7b7f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/entertainment/amusement park balloon_20ee5dd9-0486-5c78-98b3-c068d4af7b7f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='balloon-dog-with-oval-twisted-segments'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/recreation'
    aliases=()
    keywords=('balloon', 'dog', 'with', 'oval', 'twisted', 'segments')
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

        # Each balloon lobe meets a true twist node; shared nodes own all attachments.
        path('muzzle',(16,18),[('C',(6,14),(13,13),(6,10)),('C',(16,18),(6,20),(12,20))],True)
        path('ear',(16,18),[('C',(16,6),(10,14),(10,6)),('C',(16,18),(22,6),(22,14))],True)
        path('neck',(16,18),[('C',(22,29),(22,18),(25,23)),('C',(16,18),(16,27),(13,22))],True)
        path('body',(22,29),[('C',(36,29),(25,23),(33,23)),('C',(22,29),(33,35),(25,35))],True)
        path('front-leg',(22,29),[('C',(15,42),(23,36),(20,42)),('C',(22,29),(10,42),(15,32))],True)
        path('rear-leg',(36,29),[('C',(39,42),(42,32),(44,42)),('C',(36,29),(34,42),(32,35))],True)
        path('tail',(36,29),[('C',(42,16),(35,22),(38,16)),('C',(36,29),(42,23),(40,27))],True)
        for a,b in [('muzzle','ear'),('muzzle','neck'),('ear','neck'),('neck','body'),('neck','front-leg'),('body','front-leg'),('body','rear-leg'),('body','tail'),('rear-leg','tail')]:join(a,b)
