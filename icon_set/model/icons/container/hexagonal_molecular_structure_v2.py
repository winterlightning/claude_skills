# Variant of hexagonal-molecular-structure; parent file remains unchanged.
"""A hexagonal molecular enclosure with ring nodes at three alternating vertices.

VRECT_XL: visible bounds (4, 0, 60, 64); chosen for the source proportions.
Construction reference: Lucide hexagon: paired vertical sides and mirrored diagonal bonds. Independently authored on CONTAINER64.
Source silhouette and defining details retained; no decorative detail added.
Hosting measured with compose.py: plus invalid, heart invalid, check invalid.
"""
from ...keyshapes import Keyshape
from ._base import Container64
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = None
SOURCE_PATH = None

class HexagonalMolecularStructureVariant2(Container64):
    icon_id = 'hexagonal-molecular-structure-v2'
    variant_of = 'hexagonal-molecular-structure'
    variant_label = 'Larger molecular rings'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('hexagonal', 'molecular', 'structure')

    def build(self) -> None:
        # VRECT_XL centerline extremes (6,2)-(58,62); equal radius-7 rings.
        for name, x, y in (("top", 32, 9), ("left", 13, 45), ("right", 51, 45)):
            points = ((x-7,y), (x,y-7), (x+7,y), (x,y+7), (x-7,y))
            for i in range(4):
                self.add_arc(f"{name}-{i}", points[i], points[i+1], radius_x=7, sweep=True)
            self.add_contour(name, *(f"{name}-{i}" for i in range(4)), closed=True)
        self.add_polyline("upper-left", (25,9), (13,20), (13,38))
        self.add_polyline("upper-right", (39,9), (51,20), (51,38))
        self.add_polyline("bottom", (13,52), (32,62), (51,52))
        for a,b in (("top","upper-left"),("top","upper-right"),("left","upper-left"),("left","bottom"),("right","upper-right"),("right","bottom")):
            self.relate("connect", a, b)
