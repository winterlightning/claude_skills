"""Flared console rises behind a broad gamepad with rounded grips and its source horizontal control mark.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: gamepad-2: rounded grips and centered controls
Omissions: Small console inset ridge omitted; defining flared silhouette retained.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '07cbf38f-e8b3-4015-94f4-e67984c4bd1d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/32-07cbf38f-e8b3-4015-94f4-e67984c4bd1d.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='flared-console-and-gamepad'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('flared', 'console', 'and', 'gamepad')
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

        path('console',(20,22),[('L',(18,8)),('C',(32,6),(24,6),(28,6)),('L',(42,6)),('C',(42,42),(37,21),(37,33)),('L',(28,42))])
        path('pad',(12,22),[('L',(26,22)),('C',(30,28),(29,22),(30,24)),('L',(32,39)),('C',(28,42),(32,42),(30,42)),('L',(24,40)),('L',(14,40)),('L',(10,42)),('C',(6,39),(8,42),(6,42)),('L',(8,28)),('C',(12,22),(8,24),(9,22))],True);join('console','pad')
        line('control',(17,31),(21,31))
