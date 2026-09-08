"""A rectangular picture frame enclosing a second rectangular opening.

Keyshape VRECT_XL: (4, 0, 60, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide rectangle-horizontal informs the nested four-sided construction.
Square corners preserve the reference frame; an eight-unit centerline inset keeps the border open.
Hosting measured with compose.py: plus: does not clear; heart: does not clear; check: does not clear.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class RectangularPictureFrame(Container64):
    icon_id = 'rectangular-picture-frame'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('rectangular', 'picture', 'frame')

    def build(self) -> None:
        self.add_polyline('outer', (6, 2), (58, 2), (58, 62), (6, 62), closed=True)
        self.add_polyline('inner', (14, 10), (50, 10), (50, 54), (14, 54), closed=True)
