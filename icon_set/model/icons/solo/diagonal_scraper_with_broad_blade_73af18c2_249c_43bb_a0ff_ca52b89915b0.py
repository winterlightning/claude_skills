"""Broad scraper blade with rounded shoulders and a diagonal rounded grip. Blade and grip share a real shoulder seam.
Keyshape SQUARE: exact SOLO48 contract envelope.
Construction: brush and pill: smooth diagonal grip; source governs broad blade
Omissions: Fine blade band omitted.
Feedback: Bad stroke drawn. Fresh reference-based revision."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '73af18c2-249c-43bb-a0ff-ca52b89915b0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/scraper_73af18c2-249c-43bb-a0ff-ca52b89915b0.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='diagonal-scraper-with-broad-blade'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('diagonal', 'scraper', 'with', 'broad', 'blade')
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

        path('blade',(6,28),[('L',(16,18)),('C',(22,18),(18,16),(20,16)),('L',(30,26)),('C',(30,32),(32,28),(32,30)),('L',(20,42)),('L',(6,28))],True)
        path('handle',(22,18),[('L',(30,8)),('C',(36,6),(32,6),(34,6)),('A',(42,12),6,6,True),('C',(40,18),(42,14),(42,16)),('L',(30,26))]);join('handle','blade')
