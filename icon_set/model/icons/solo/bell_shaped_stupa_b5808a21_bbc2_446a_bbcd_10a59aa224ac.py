"""Bell dome, needle finial and broad plinth. Lucide bell informs the coherent dome; stepped bands reduced to one base."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5808a21-bbc2-446a-bbcd-10a59aa224ac'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/wat phra kaew_b5808a21-bbc2-446a-bbcd-10a59aa224ac.svg'
AUTHOR = 'gpt-6'

class BellShapedStupa(Solo48):
    icon_id = 'bell-shaped-stupa'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('wat phra kaew', 'stupa', 'chedi', 'thailand', 'temple', 'buddhist', 'landmark', 'religion')

    def build(self) -> None:
        # Centerline extremes (5, 2, 43, 46).
        self.add_line("spire", (24,2), (24,14))
        self.add_arc("dome-left", (24,14), (7,36), radius_x=17, radius_y=22, sweep=False)
        self.add_line("base-left", (7,36), (24,36))
        self.add_line("base-right", (24,36), (41,36))
        self.add_arc("dome-right", (41,36), (24,14), radius_x=17, radius_y=22, sweep=False)
        self.add_contour("dome", "dome-left", "base-left", "base-right", "dome-right", closed=True)
        self.relate("connect", "spire", "dome")
        self.add_line("plinth", (5,46), (43,46))
