"""Diagonal shovel with a softly rounded digging blade, long shaft and broad open D grip.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: shovel: diagonal shaft, distinct blade and D-grip
Omissions: Blade ridge omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '571135a9-8294-425e-b2d7-526d9f1ec44f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dig_571135a9-8294-425e-b2d7-526d9f1ec44f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-shovel-with-broad-d-grip'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('diagonal', 'shovel', 'with', 'broad', 'd', 'grip')
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

        path('blade',(6,42),[('L',(6,31)),('C',(10,24),(6,28),(8,26)),('L',(14,20)),('L',(28,34)),('L',(24,38)),('C',(17,42),(22,40),(20,42)),('L',(6,42))],True)
        line('shaft',(18,30),(33,15));join('shaft','blade')
        path('grip',(26,10),[('C',(32,6),(28,7),(30,6)),('C',(42,16),(38,6),(42,10)),('L',(40,22)),('L',(26,10))],True);join('shaft','grip')
