"""A wider hexagonal molecular enclosure with three alternating ring nodes.

SQUARE: centerline (2,2)-(62,62), visible (0,0)-(64,64). The wider keyshape
increases the bond-side separation from 38 to 46 while preserving the height
and all three radius-7 nodes. Lucide hexagon informs vertical sides and
mirrored diagonal bonds. No defining detail is removed; no asymmetry added.
The brief's archived v2 SVG matches revision 91e996c033918f6c36c1044a8bd8198910aaccdd7fc4bf36d82c7fc976ea82ef;
The accepted wider drawing now replaces the original registered icon.
Hosting measured with compose.py: check valid; plus and heart invalid because the top ring crowds the child.
"""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'
FEEDBACK_PATHS = ('/Users/jakesdev/Downloads/feedback-briefs 2/container/155-container-hexagonal-molecular-structure-v2.md',)


class HexagonalMolecularStructure(Container64):
    icon_id = 'hexagonal-molecular-structure'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    aliases = ()
    keywords = ('hexagonal', 'molecular', 'structure', 'wide')

    def build(self) -> None:
        # Plan: repeated radius-7 circles, paired sides mirrored about x=32;
        # all bonds share exact cardinal attachment nodes with their circles.
        axis, half_width, radius = 32, 23, 7
        top_y, side_y, shoulder_y, bottom_y = 9, 45, 20, 62
        for name, x, y in (('top', axis, top_y),
                           ('left', axis-half_width, side_y),
                           ('right', axis+half_width, side_y)):
            points = ((x-radius,y), (x,y-radius), (x+radius,y), (x,y+radius), (x-radius,y))
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[i+1], radius_x=radius)
            self.add_contour(name, *(f'{name}-{i}' for i in range(4)), closed=True)
        for name, sign in (('left', -1), ('right', 1)):
            x = axis+sign*half_width
            self.add_polyline(f'upper-{name}', (axis+sign*radius, top_y),
                              (x, shoulder_y), (x, side_y-radius))
            self.relate('connect', 'top', f'upper-{name}')
            self.relate('connect', name, f'upper-{name}')
        self.add_polyline('bottom', (axis-half_width, side_y+radius),
                          (axis,bottom_y), (axis+half_width, side_y+radius))
        for name in ('left','right'):
            self.relate('connect', name, 'bottom')
