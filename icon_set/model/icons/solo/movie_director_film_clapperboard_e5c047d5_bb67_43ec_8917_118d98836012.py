"""Round lower board corners and restore stripes to raised clap rail. Shared rail attachment points prevent overshooting ends.
Construction: Lucide clapperboard: curved board corners, striped tilted upper rail.
Omissions: Lower duplicate striped band omitted to preserve board opening.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e5c047d5-bb67-43ec-8917-118d98836012'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clapperboard_e5c047d5-bb67-43ec-8917-118d98836012.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'movie-director-film-clapperboard'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('movie', 'director', 'film', 'clapperboard')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*pts,closed=False):self.add_polyline(name,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)

        poly('raised',(6,16),(22,11),(36,6),(40,14),(26,19),(10,24),closed=True)
        line('stripe-a',(22,11),(26,19));join('stripe-a','raised')
        path('board',(10,24),[('L',(42,24)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,24)),('L',(10,24))],True)
        join('raised','board')
