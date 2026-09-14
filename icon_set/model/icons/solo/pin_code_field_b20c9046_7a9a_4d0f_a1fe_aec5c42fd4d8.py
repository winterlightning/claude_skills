"""A code entry field with two dashes and a cursor. HRECT_L extremes (6,8)-(42,40). Lucide rectangle-ellipsis informs the rounded outline and spaced contents; retain the source dashes and tall cursor."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b20c9046-7a9a-4d0f-a1fe-aec5c42fd4d8'
SOURCE_PATH = 'pictographic-primitives/symbol/keycode_b20c9046-7a9a-4d0f-a1fe-aec5c42fd4d8.svg'
AUTHOR = 'gpt-6'


class PinCodeField(Solo48):
    icon_id = 'pin-code-field'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('pin', 'code', 'password', 'input', 'field', 'keycode', 'passcode', 'security')

    def build(self) -> None:
        self.add_line('field-top',(8,8),(40,8))
        self.add_arc('field-tr',(40,8),(42,12),radius_x=4)
        self.add_line('field-right',(42,12),(42,36))
        self.add_arc('field-br',(42,36),(40,40),radius_x=4)
        self.add_line('field-bottom',(40,40),(8,40))
        self.add_arc('field-bl',(8,40),(6,36),radius_x=4)
        self.add_line('field-left',(6,36),(6,12))
        self.add_arc('field-tl',(6,12),(8,8),radius_x=4)
        self.add_contour('field',*('field-'+p for p in ['top','tr','right','br','bottom','bl','left','tl']),closed=True)
        self.add_line('dash-left',(13,27),(15,27))
        self.add_line('dash-right',(23,27),(25,27))
        self.add_line('cursor',(35,20),(35,29))
