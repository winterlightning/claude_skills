"""The Indian rupee currency sign.
Plan: VRECT_M fits the tall currency glyph. Visible ink bounds: (8, 2, 40, 46).
Reduction: No defining part omitted. Bowl now leaves the right end of the top rule vertically, avoiding a grazing upper curve.
Construction: Lucide indian-rupee: two horizontal bars, rounded bowl and descending diagonal leg."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e9b350be-f0e4-49b9-8413-4a4d1c678f43'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_33/rupee sign_e9b350be-f0e4-49b9-8413-4a4d1c678f43.svg'
AUTHOR = 'gpt-6'
PLAN = 'The Indian rupee currency sign.'
OMISSIONS = 'No defining part omitted. Bowl now leaves the right end of the top rule vertically, avoiding a grazing upper curve.'
CONSTRUCTION_REFERENCES = 'Lucide indian-rupee: two horizontal bars, rounded bowl and descending diagonal leg.'
KEYSHAPE_INK_BOUNDS = (8, 2, 40, 46)

class AuthoredIcon(Solo48):
    icon_id = 'rupee-sign'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('rupee', 'sign')

    def build(self):
        self.add_polyline('top', (10, 4), (38, 4), (38, 12))
        self.add_arc('bowl', (38, 12), (24, 26), radius_x=14)
        self.add_polyline('return-leg', (24, 26), (10, 26), (30, 44))
        self.add_line('bar', (10, 12), (38, 12))
        self.relate('connect', 'top', 'bowl')
        self.relate('connect', 'top', 'bar')
        self.relate('connect', 'bowl', 'bar')
        self.relate('connect', 'bowl', 'return-leg')
