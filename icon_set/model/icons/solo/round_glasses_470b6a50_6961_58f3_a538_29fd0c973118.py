"""Round glasses with matched lenses and arched bridge. Lucide glasses informs repeated circles; tiny temple stubs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '470b6a50-6961-58f3-a538-29fd0c973118'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/glasses_470b6a50-6961-58f3-a538-29fd0c973118.svg'
AUTHOR = 'astra-chatgpt'

class RoundGlasses(Solo48):
    icon_id = 'round-glasses'
    keyshape = Keyshape.HRECT_S
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('round', 'glasses')

    def build(self) -> None:
        self.add_arc("lens-left-top", (2,24), (22,24), radius_x=10)
        self.add_arc("lens-left-bottom", (22,24), (2,24), radius_x=10)
        self.add_contour("lens-left", "lens-left-top", "lens-left-bottom", closed=True)
        self.add_arc("lens-right-top", (26,24), (46,24), radius_x=10)
        self.add_arc("lens-right-bottom", (46,24), (26,24), radius_x=10)
        self.add_contour("lens-right", "lens-right-top", "lens-right-bottom", closed=True)
        # Centerline extremes (2,14)-(46,34).
        self.add_arc("bridge", (22,24), (26,24), radius_x=2)
        self.relate("connect", "lens-left", "bridge")
        self.relate("connect", "lens-right", "bridge")
