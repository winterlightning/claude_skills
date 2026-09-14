"""Inset the hook and shaft ends; smoothed the leaning shaft into a tangent hook.

Keyshape VRECT_L: visible bounds (6, 2, 42, 46).
Reference: No useful exact match.
"""
# Independent repair of shepherds-crook; parent preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7169d0df-e69e-5ecc-8180-aa3f755ddd80'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/astrology cane_7169d0df-e69e-5ecc-8180-aa3f755ddd80.svg'
AUTHOR = 'gpt-6'

class ShepherdsCrookVariant2(Solo48):
    icon_id = 'shepherds-crook-v2'
    variant_of = 'shepherds-crook'
    variant_label = 'Fit current SOLO48 bounds and spacing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('crook', 'cane', 'staff', 'shepherd', 'hook', 'stick', 'symbol', 'pastoral')

    # Symbol plan: retain the subject and shared attachment stations;
    # fit the current keyshape by adjusting the owning cap, base or repeat.
    def build(self) -> None:
        self.add_bezier('shaft', (8, 44), ((12, 34), (20, 24), (20, 14)))
        self.add_arc('hook', (20, 14), (40, 14), radius_x=10)
        self.add_line('tip', (40, 14), (40, 18))
        self.add_contour('crook', 'shaft', 'hook', 'tip')
