"""A reversed S-shaped hryvnia sign crosses two horizontal bars. VRECT_L extremes (8,6)-(40,42). Lucide russian-ruble informs clear parallel currency bars; source sets the reversed curve. Preserve both bars and the currency’s direction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5afaf6ee-841d-4918-940a-7de550ac7754'
SOURCE_PATH = 'pictographic-primitives/symbol/hryvnia sign_5afaf6ee-841d-4918-940a-7de550ac7754.svg'
AUTHOR = 'gpt-6'

class HryvniaSign(Solo48):
    icon_id = 'hryvnia-sign'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('hryvnia', 'currency', 'ukraine', 'money', 'sign', 'uah', 'finance', 'symbol')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('top', (14, 4), (26, 4))
        self.add_arc('upper', (26, 4), (26, 20), radius_x=8)
        self.add_line('diagonal', (26, 20), (22, 28))
        self.add_arc('lower', (22, 28), (22, 44), radius_x=8, sweep=False)
        self.add_line('bottom', (22, 44), (34, 44))
        self.add_contour('currency', 'top', 'upper', 'diagonal', 'lower', 'bottom')
        self.add_polyline('bar-upper', (8, 20), (26, 20), (40, 20))
        self.add_polyline('bar-lower', (8, 28), (22, 28), (40, 28))
        self.relate('connect', 'currency', 'bar-upper')
        self.relate('connect', 'currency', 'bar-lower')
