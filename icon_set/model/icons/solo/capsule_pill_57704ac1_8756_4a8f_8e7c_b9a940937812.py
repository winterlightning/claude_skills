"""Replace flattened capsule shoulders with balanced rounded ends and tangent diagonal sidewalls; center the transverse seam.
Construction: Lucide pill: parallel diagonal walls, smoothly rounded ends and perpendicular midpoint seam.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57704ac1-8756-4a8f-8e7c-b9a940937812'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pill_57704ac1-8756-4a8f-8e7c-b9a940937812.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'capsule-pill-57704ac1'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('capsule', 'pill', '57704ac1')
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

        path('shell',(24,10),[('C',(31,6),(26,8),(28,6)),('C',(42,17),(37,6),(42,11)),('C',(38,24),(42,20),(40,22)),('L',(31,31)),('L',(24,38)),('C',(17,42),(22,40),(20,42)),('C',(6,31),(11,42),(6,37)),('C',(10,24),(6,28),(8,26)),('L',(17,17)),('L',(24,10))],True)
        line('seam',(17,17),(31,31));join('seam','shell')
