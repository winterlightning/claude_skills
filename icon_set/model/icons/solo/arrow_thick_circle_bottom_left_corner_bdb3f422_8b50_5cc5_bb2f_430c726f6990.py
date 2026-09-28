'Directional arrow: equal-angle head with an explicit shared shaft endpoint and comfortable inset from its frame.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bdb3f422-8b50-5cc5-bb2f-430c726f6990'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick circle bottom left corner_bdb3f422-8b50-5cc5-bb2f-430c726f6990.svg'
AUTHOR = 'gpt-6'

class ArrowThickCircleBottomLeftCorner(Solo48):
    icon_id = 'arrow-thick-circle-bottom-left-corner'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'thick', 'circle', 'bottom', 'left', 'corner', 'arrows')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)

        self.add_polyline('head',(17,18),(17,31),(30,31))
        self.add_line('shaft',(17,31),(31,17))
        self.relate('connect','head','shaft')
