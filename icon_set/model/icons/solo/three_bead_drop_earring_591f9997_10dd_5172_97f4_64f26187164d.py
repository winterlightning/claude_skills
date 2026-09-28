"""Re-authored the three-bead chain diagonally to preserve circular beads and avoid an oversized middle bead.

SQUARE: visible ink (4, 4, 44, 44). Diagonal square construction preserves a narrow subject without stretching it sideways.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '591f9997-10dd-5172-97f4-64f26187164d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/earring_591f9997-10dd-5172-97f4-64f26187164d.svg'
AUTHOR = 'gpt-6'

class ThreeBeadDropEarring(Solo48):
    icon_id = 'three-bead-drop-earring'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('earring', 'bead', 'drop', 'pearl', 'jewellery', 'jewelry', 'circle', 'accessory')

    def build(self):
        # Increased the top and bottom beads and rebalanced the middle bead for clear diagonal spacing.

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
        ellipse('stud',10,10,4,4);ellipse('middle',24,24,7,7);ellipse('drop',38,38,4,4)
        line('upper-link',(14,10),(24,17));line('lower-link',(24,31),(34,38))
        for a,b in [('stud','upper-link'),('middle','upper-link'),('middle','lower-link'),('drop','lower-link')]:join(a,b)
