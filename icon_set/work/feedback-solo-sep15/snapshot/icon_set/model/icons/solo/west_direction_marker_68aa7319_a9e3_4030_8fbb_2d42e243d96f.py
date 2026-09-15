"""A west triangle sits beside a W. HRECT extremes (4,8)-(44,40); W uses a shared middle axis with mirrored legs.
Reduction: Removed circular letter frame and arrow notch to retain a legible W and leftward direction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '68aa7319-a9e3-4030-8fbb-2d42e243d96f'
SOURCE_PATH = 'pictographic-primitives/navigation/compass west_68aa7319-a9e3-4030-8fbb-2d42e243d96f.svg'
AUTHOR = 'gpt-6'


class WestDirectionMarker(Solo48):
    icon_id = 'west-direction-marker'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/navigation"
    aliases = ()
    keywords = ('west', 'direction', 'compass', 'navigation', 'arrow', 'orientation', 'marker')

    def build(self) -> None:
        self.add_polyline("west", (16,8), (4,24), (16,40), closed=True)
        axis, half = 34, 10
        self.add_polyline("letter-w", (axis-half,8), (axis-half,40), (axis,28), (axis+half,40), (axis+half,8))
