"""An E and east-pointing triangle form one directional marker. HRECT extremes (4,8)-(44,40); letter owns three equally spaced bars. Purposeful rightward asymmetry.
Reduction: Removed circular letter frame and arrow notch to prioritize the E and rightward direction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e91a4b42-5376-4b1a-ab2d-8d86c029fcca'
SOURCE_PATH = 'pictographic-primitives/navigation/compass east_e91a4b42-5376-4b1a-ab2d-8d86c029fcca.svg'
AUTHOR = 'gpt-6'


class EastDirectionMarker(Solo48):
    icon_id = 'east-direction-marker'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/navigation"
    aliases = ()
    keywords = ('east', 'direction', 'compass', 'navigation', 'arrow', 'orientation', 'marker')

    def build(self) -> None:
        left, end = 4, 16
        for i,y in enumerate((8,24,40)):
            self.add_line(f"bar-{i}", (left,y), (end,y))
        for i,(a,b) in enumerate(((8,24),(24,40))):
            self.add_line(f"stem-{i}", (left,a), (left,b))
            self.relate("connect", f"stem-{i}", f"bar-{i}")
            self.relate("connect", f"stem-{i}", f"bar-{i+1}")
        self.add_polyline("east", (28,12), (44,24), (28,36), closed=True)
