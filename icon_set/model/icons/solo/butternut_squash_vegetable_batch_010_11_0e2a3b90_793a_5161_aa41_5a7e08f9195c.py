"""Restore the squash broad bulb, narrowed neck and a visible curved stem with smooth outline transitions.
Construction: No useful exact Lucide match; supplied reference controls the silhouette.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0e2a3b90-793a-5161-aa41-5a7e08f9195c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/butternutsquash_0e2a3b90-793a-5161-aa41-5a7e08f9195c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'butternut-squash-vegetable-batch-010-11'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('butternut', 'squash', 'vegetable', 'batch', '010', '11')
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

        path('fruit',(18,42),[('C',(6,29),(11,42),(6,37)),('C',(20,17),(6,22),(14,21)),('C',(31,10),(25,13),(26,10)),('C',(42,19),(38,10),(42,12)),('C',(32,32),(42,24),(36,27)),('C',(18,42),(28,38),(27,42))],True)
        path('stem',(31,10),[('C',(34,6),(34,10),(35,8))]);join('stem','fruit')
