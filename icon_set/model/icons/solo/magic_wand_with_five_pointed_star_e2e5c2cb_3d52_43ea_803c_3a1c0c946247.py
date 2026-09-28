"""Rotate the five-pointed star toward the diagonal shaft; a longer 45-degree wand ends at a star valley.
Construction: Lucide wand: single diagonal shaft; source five-point star retained.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e2e5c2cb-3d52-43ea-803c-3a1c0c946247'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/magic wand 1_e2e5c2cb-3d52-43ea-803c-3a1c0c946247.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'magic-wand-with-five-pointed-star'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'entertainment'
    categories = ('entertainment', 'primitive', 'primitives')
    aliases = ()
    keywords = ('magic', 'wand', 'with', 'five', 'pointed', 'star')
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

        poly('star',(25,6),(32,12),(41,8),(37,18),(42,26),(32,25),(28,34),(25,25),(16,23),(24,17),closed=True)
        line('wand',(6,42),(25,25));join('wand','star')
