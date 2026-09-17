"""Small Group of Amaranth Seeds."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f225537d-d635-4009-ae09-1c789051cbc5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/amaranth_f225537d-d635-4009-ae09-1c789051cbc5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-amaranth-seed-group'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('small', 'amaranth', 'seed', 'group')

    def build(self):
        # Plan: Three elongated amaranth seeds arranged as a loose cluster. Shared tapered seed definition; overlaps and interior creases removed to keep all three forms readable. No useful exact Lucide match.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

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

        for j,(x,y) in enumerate(((12,14),(36,14),(24,34))):
         path('seed-'+str(j),(x,y-8),[('C',(x+6,y+1),(x+2,y-6),(x+6,y-4)),('C',(x,y+8),(x+6,y+6),(x+3,y+8)),('C',(x-6,y+1),(x-3,y+8),(x-6,y+6)),('C',(x,y-8),(x-6,y-4),(x-2,y-6))],True)
