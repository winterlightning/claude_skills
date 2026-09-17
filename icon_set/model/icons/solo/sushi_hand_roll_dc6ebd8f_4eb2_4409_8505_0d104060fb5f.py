"""Sushi Hand Roll."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc6ebd8f-4eb2-4409-8505-0d104060fb5f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/japanese assorted seafood in seaweed cone_dc6ebd8f-4eb2-4409-8505-0d104060fb5f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sushi-hand-roll'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('sushi', 'hand', 'roll')

    def build(self):
        # Plan: Sushi cone with a broad rounded filling and a projecting vegetable strip. Shared top-rim nodes and a rounded cone point; asymmetric vegetable topping retained. Multiple small fillings reduced to one large mound. No useful exact Lucide match.
        # Envelope: VRECT_L; visible ink (6, 2, 42, 46) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('fillings',(8,22),[('C',(14,12),(8,16),(8,12)),('L',(22,12)),('C',(32,8),(24,8),(28,8)),('C',(40,22),(40,8),(40,16))])
        poly('vegetable',(14,12),(10,4),(22,4),(22,12));join('vegetable','fillings')
        path('wrap',(8,22),[('C',(24,26),(12,25),(18,26)),('C',(40,22),(30,26),(36,25)),('L',(28,42)),('A',(20,42),4,2,True),('L',(8,22))],True);join('wrap','fillings')
