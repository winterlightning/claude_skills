"""Arrow Down Left with Open Shaft.

Plan: SQUARE centerlines (6,6)-(42,42); broad L-shaped head with radius-4 caps; an open diagonal shaft attaches to its inner corner.
Construction references: Lucide move-down-left: diagonal shaft meets the L head at one shared node.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3a6332e-410a-53b4-9730-c7959df16019'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick corner bottom left_f3a6332e-410a-53b4-9730-c7959df16019.svg'
SOURCE_ICON_IDS = ('f3a6332e-410a-53b4-9730-c7959df16019',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow thick corner bottom left_f3a6332e-410a-53b4-9730-c7959df16019.svg',)
AUTHOR = 'gpt-6'


class ArrowDownLeftWithOpenShaft(Solo48):
    icon_id = 'arrow-down-left-with-open-shaft'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'down', 'left', 'with', 'open', 'shaft')

    def build(self) -> None:
        self.add_line("arm-outer",(6,10),(6,38))
        self.add_arc("corner",(6,38),(10,42),radius_x=4,sweep=False)
        self.add_line("base",(10,42),(38,42))
        self.add_arc("end-right",(38,42),(38,34),radius_x=4,sweep=False)
        self.add_line("arm-inner",(38,34),(14,34))
        self.add_line("upright-inner",(14,34),(14,10))
        self.add_arc("end-top",(14,10),(6,10),radius_x=4,sweep=False)
        self.add_contour("bent-head","arm-outer","corner","base","end-right","arm-inner","upright-inner","end-top",closed=True)
        self.add_line("shaft",(14,34),(42,6))
        self.relate("connect","bent-head","shaft")
