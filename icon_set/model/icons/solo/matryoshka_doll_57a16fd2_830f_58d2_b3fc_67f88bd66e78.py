"""Rebalanced the dome, circular face and rounded base; retained the scarf.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match; face is an inset doll feature, not a detached human head.
"""
# Independent repair of matryoshka-doll; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57a16fd2-830f-58d2-b3fc-67f88bd66e78'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/babushka_57a16fd2-830f-58d2-b3fc-67f88bd66e78.svg'
AUTHOR = 'gpt-6'

class MatryoshkaDoll(Solo48):
    icon_id = 'matryoshka-doll'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('matryoshka', 'babushka', 'nesting doll', 'russian', 'doll', 'toy', 'folk', 'souvenir')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_arc('dome-right', (24, 4), (40, 32), radius_x=16, radius_y=28)
        self.add_arc('base-right', (40, 32), (32, 44), radius_x=8, radius_y=12)
        self.add_line('base', (32, 44), (16, 44))
        self.add_arc('base-left', (16, 44), (8, 32), radius_x=8, radius_y=12)
        self.add_arc('dome-left', (8, 32), (24, 4), radius_x=16, radius_y=28)
        self.add_contour('body', 'dome-right', 'base-right', 'base', 'base-left', 'dome-left', closed=True)
        self.add_arc('face-right', (24, 12), (24, 26), radius_x=7)
        self.add_arc('face-left', (24, 26), (24, 12), radius_x=7)
        self.add_contour('face', 'face-right', 'face-left', closed=True)
        self.add_arc('scarf-left', (8, 32), (24, 26), radius_x=16, radius_y=7, sweep=False)
        self.add_arc('scarf-right', (24, 26), (40, 32), radius_x=16, radius_y=7, sweep=False)
        self.add_contour('scarf', 'scarf-left', 'scarf-right')
        self.relate('connect', 'body', 'scarf')
        self.relate('connect', 'face', 'scarf')
