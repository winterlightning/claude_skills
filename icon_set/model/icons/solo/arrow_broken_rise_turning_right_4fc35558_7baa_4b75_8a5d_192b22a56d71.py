"""Restore an upright broken rising path with tangent quarter-circle turns and a longer horizontal arrow shaft.
Construction: Lucide undo-2: tangent circular bends and 45-degree open arrowhead.
Omissions: None
Keyshape SQUARE: authored to exact SOLO48 extremes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4fc35558-7baa-4b75-8a5d-192b22a56d71'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_14/diagram dash up steady large head_4fc35558-7baa-4b75-8a5d-192b22a56d71.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'arrow-broken-rise-turning-right'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('arrow', 'broken', 'rise', 'turning', 'right')
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

        path('lower',(6,42),[('L',(8,42)),('A',(16,34),8,8,False),('L',(16,31))])
        path('upper',(16,22),[('L',(16,20)),('A',(24,12),8,8,True),('L',(25,12))])
        line('terminal',(34,12),(42,12));poly('head',(36,6),(42,12),(36,18));join('terminal','head')
