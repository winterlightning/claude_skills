"""Restore smooth curtain contours, clear radial clock hands and rounded seat backs; retain the cinema showtime composition.
Construction: Lucide theater: draped curtain contours and round-backed seats.
Omissions: Three seat backs reduced to two; small curtain tie folds omitted.
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '84c261a3-7abc-40bc-a142-dc7275ce0a7e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/entertainment/movie cinema clock_84c261a3-7abc-40bc-a142-dc7275ce0a7e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'cinema-showtime-with-audience-batch-007-15'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitives')
    aliases = ()
    keywords = ('cinema', 'showtime', 'with', 'audience', 'batch', '007', '15')
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

        poly('top',(6,6),(10,6),(38,6),(42,6))
        path('curtain-left',(10,6),[('C',(6,15),(10,11),(8,15)),('L',(6,26))])
        path('curtain-right',(38,6),[('C',(42,15),(38,11),(40,15)),('L',(42,26))])
        join('top','curtain-left');join('top','curtain-right')
        circle('clock',24,23,7)
        poly('hands',(24,16),(24,23),(27,23));join('hands','clock')
        for x in (13,35):
         path(f'seat-{x}',(x-6,42),[('A',(x+6,42),6,6,True)])
