'Variable font: paired T forms with consistent stems and a balanced slider.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de8c9243-bc9c-4c89-8720-203c0db986ff'
SOURCE_PATH = 'pictographic-primitives/interface-essential/variable font_de8c9243-bc9c-4c89-8720-203c0db986ff.svg'
AUTHOR = 'gpt-6'

class VariableFont(Solo48):
    icon_id = 'variable-font'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('variable', 'font', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('top-12-1', (4, 12), (4, 8))
        self.add_line('top-12-2', (4, 8), (20, 8))
        self.add_line('top-12-3', (20, 8), (20, 12))
        self.add_line('stem-12', (12, 8), (12, 24))
        self.add_line('foot-12', (8, 24), (16, 24))
        self.add_line('top-36-1', (28, 12), (28, 8))
        self.add_line('top-36-2', (28, 8), (44, 8))
        self.add_line('top-36-3', (44, 8), (44, 12))
        self.add_line('stem-36', (36, 8), (36, 24))
        self.add_line('foot-36', (32, 24), (40, 24))
        self.add_line('slider-left', (4, 35), (19, 35))
        self.add_line('slider-right', (29, 35), (44, 35))
        self.add_arc('knob-top', (19, 35), (29, 35), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_arc('knob-bottom', (29, 35), (19, 35), radius_x=5, radius_y=5, large_arc=False, sweep=True)
        self.add_contour('top-12', *('top-12-1', 'top-12-2', 'top-12-3'), closed=False)
        self.add_contour('top-36', *('top-36-1', 'top-36-2', 'top-36-3'), closed=False)
        self.add_contour('knob', *('knob-top', 'knob-bottom'), closed=True)
        self.relate('connect', *('top-12', 'stem-12'))
        self.relate('connect', *('stem-12', 'foot-12'))
        self.relate('connect', *('top-36', 'stem-36'))
        self.relate('connect', *('stem-36', 'foot-36'))
        self.relate('connect', *('knob', 'slider-left'))
        self.relate('connect', *('knob', 'slider-right'))
