"""Concentric marker rings above a south triangle, all mirrored about x=24. VRECT extremes (8,4)-(40,44); shared circle center and radii.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd93cab24-2bd3-457b-ad02-6d5bc4af9f2d'
SOURCE_PATH = 'pictographic-primitives/navigation/compass south_d93cab24-2bd3-457b-ad02-6d5bc4af9f2d.svg'
AUTHOR = 'gpt-6'


class SouthDirectionMarker(Solo48):
    icon_id = 'south-direction-marker'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/navigation"
    aliases = ()
    keywords = ('south', 'direction', 'compass', 'navigation', 'triangle', 'orientation', 'marker')

    def build(self) -> None:
        cx,cy = 24,15
        for name,r in (("outer",11),("inner",2)):
            self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name, name+"-top", name+"-bottom", closed=True)
        self.add_polyline("south", (8,35), (40,35), (24,44), closed=True)
