"""A north triangle sits above an N. VRECT extremes (8,4)-(40,44); arrow mirrors about x=24 and letter shares its horizontal span.
Reduction: Removed circular letter frame and arrow notch to retain a legible N and upward direction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcf71cda-12ba-4a46-903e-1a90ca9095ae'
SOURCE_PATH = 'pictographic-primitives/navigation/compass north_fcf71cda-12ba-4a46-903e-1a90ca9095ae.svg'
AUTHOR = 'gpt-6'


class NorthDirectionMarker(Solo48):
    icon_id = 'north-direction-marker'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/navigation"
    aliases = ()
    keywords = ('north', 'direction', 'compass', 'navigation', 'arrow', 'orientation', 'marker')

    def build(self) -> None:
        left, right, center = 8, 40, 24
        self.add_polyline("north", (left,16), (center,4), (right,16), closed=True)
        self.add_polyline("letter-n", (left,44), (left,24), (right,44), (right,24))
