"""Spiral Helical Protein Ribbon."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b1ca9299-f064-4596-bd7a-279b553da82b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/protein strand_b1ca9299-f064-4596-bd7a-279b553da82b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiral-protein-ribbon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('spiral', 'protein', 'ribbon')

    def build(self):
        # Plan: Broad protein ribbon with one open helical turn, two curved folds and slanted free ends. Lucide dna informs the diagonal flow; the supplied broad ribbon remains distinct from a double helix. Fewer turns and larger fold faces preserve open interiors at 48 pixels.
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

        path('ribbon',(42,16),[('L',(42,34)),('C',(34,42),(42,42),(38,42)),('L',(16,22)),('L',(16,42)),('L',(6,36)),('L',(6,14)),('C',(14,6),(6,6),(10,6)),('L',(32,26)),('L',(32,10)),('L',(42,16))],True)
        line('fold-top',(32,26),(34,42));join('fold-top','ribbon')
        line('fold-bottom',(14,6),(16,22));join('fold-bottom','ribbon')
