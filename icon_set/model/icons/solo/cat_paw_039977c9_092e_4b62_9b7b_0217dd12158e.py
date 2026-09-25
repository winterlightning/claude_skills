"""Make the toe pads read as a paw instead of a two-eyed face.
Plan: three rounded toes and a broad paw pad; preserve the open leg sides.
VRECT_L centerline extremes (8,4)-(40,44).
Lucide: paw-print; geometric contour construction adapted to SOLO48.
Independent variant; original preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '039977c9-092e-4b62-9b7b-0217dd12158e'
SOURCE_PATH = 'pictographic-primitives/animals/cat pawn_039977c9-092e-4b62-9b7b-0217dd12158e.svg'
AUTHOR = 'gpt-6'

class CatPaw(Solo48):
    icon_id = 'cat-paw'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('cat', 'paw', 'print', 'pad', 'toe', 'pet', 'animal', 'foot')

    def build(self):
        # Three rounded toe circles above one simple pad, following the Lucide paw-print vocabulary.

        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        for name,x,y in [('left',10,20),('middle',24,10),('right',38,20)]:ellipse(name,x,y,4,4)
        ellipse('pad',24,35,10,7)
