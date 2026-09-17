"""Rosemary Herb Sprig."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '70f0d699-5cb0-50e4-aa94-97d2c3ed517b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/rosemary_70f0d699-5cb0-50e4-aa94-97d2c3ed517b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rosemary-herb-sprig'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('rosemary', 'herb', 'sprig')

    def build(self):
        # Plan: Supplied rosemary: evenly spaced opposing needle leaves, shared stem nodes and bilateral symmetry. Three leaf pairs replace the dense source series; no useful exact Lucide match.
        # Envelope: VRECT_M; visible ink (8, 2, 40, 46) on SOLO48.

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

        ys=(16,28,40)
        for i,(a,b) in enumerate(zip((4,)+ys,ys+(44,))):line('stem'+str(i),(24,a),(24,b))
        for i,y in enumerate(ys):
         for side in (-1,1):
          n=f'leaf-{i}-{side}';line(n,(24,y),(24+side*14,y-12));join(n,'stem'+str(i));join(n,'stem'+str(i+1))
         join(f'leaf-{i}--1',f'leaf-{i}-1')
