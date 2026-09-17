# Review revision; previous candidates preserved.
"""Paw print with enlarged circular toes and rounded mirrored central pad. Lucide paw-print informs coherent round lobes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1'
SOURCE_PATH = 'pictographic-primitives/animals/animal print paw_3a1bcec0-4f4d-5256-8275-cc56ec3fa7d1.svg'
AUTHOR = 'gpt-6'

class PawPrint(Solo48):
    icon_id = 'paw-print'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('paw', 'print', 'track', 'footprint', 'animal', 'pet', 'dog', 'cat', 'wildlife')

    def build(self):
        # Made all four toes equally large circles and replaced the angular pad with a rounded oval; Lucide paw-print informs the separated pads.

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
        for name,x,y in [('upper-left',16,8),('upper-right',32,8),('outer-left',12,24),('outer-right',36,24)]:ellipse(name,x,y,4,4)
        ellipse('pad',24,39,7,5)
