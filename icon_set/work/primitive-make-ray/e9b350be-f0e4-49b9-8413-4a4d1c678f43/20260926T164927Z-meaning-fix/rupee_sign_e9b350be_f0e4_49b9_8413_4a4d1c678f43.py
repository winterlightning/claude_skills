from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "e9b350be-f0e4-49b9-8413-4a4d1c678f43"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__rupee-sign/20260926T163748Z-thuan-mac/reference/rupee sign_e9b350be-f0e4-49b9-8413-4a4d1c678f43.svg"
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = "rupee-sign"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "currency"
    aliases = ()
    keywords = ("rupee", "Indian rupee", "currency symbol")

    def build(self):
        # Reconstruct the reference glyph: twin rules, open bowl, and diagonal leg.
        self.add_line("upper-rule", (10, 4), (38, 4))
        self.add_line("lower-rule", (10, 12), (20, 12))
        self.add_arc("bowl-upper", (20, 12), (28, 20), radius_x=8, radius_y=8, sweep=True)
        self.add_arc("bowl-lower", (28, 20), (20, 28), radius_x=8, radius_y=8, sweep=True)
        self.add_polyline("diagonal-leg", (20, 28), (36, 44))
        self.relate("connect", "lower-rule", "bowl-upper")
        self.relate("connect", "bowl-lower", "diagonal-leg")
