"""An open locket with a round bail and portrait. Lucide user-round informs the head and shoulders; back half is shown behind the front."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '57afb5e4-7b86-4ac6-adf1-571db810e527'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/locket_57afb5e4-7b86-4ac6-adf1-571db810e527.svg'
AUTHOR = 'astra-chatgpt'

class OpenLocketWithPortrait(Solo48):
    icon_id = 'open-locket-with-portrait'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('open', 'locket', 'with', 'portrait')

    def build(self) -> None:
        # SQUARE extremes (2,2)-(46,46). Shared circle points use 9-12-15 triangles.
        self.add_arc("front-ne", (31,16), (46,31), radius_x=15)
        self.add_arc("front-se", (46,31), (31,46), radius_x=15)
        self.add_arc("front-sw-tip", (31,46), (22,43), radius_x=15)
        self.add_arc("front-sw", (22,43), (16,31), radius_x=15)
        self.add_arc("front-nw", (16,31), (22,19), radius_x=15)
        self.add_arc("front-nw-tip", (22,19), (31,16), radius_x=15)
        self.add_contour("front", "front-ne", "front-se", "front-sw-tip", "front-sw", "front-nw", "front-nw-tip", closed=True)
        self.add_arc("back-top", (22,19), (12,14), radius_x=10, radius_y=5, sweep=False)
        self.add_arc("back-upper", (12,14), (2,30), radius_x=10, radius_y=16, sweep=False)
        self.add_arc("back-lower", (2,30), (12,46), radius_x=10, radius_y=16, sweep=False)
        self.add_arc("back-bottom", (12,46), (22,43), radius_x=10, radius_y=3, sweep=False)
        self.add_contour("back", "back-top", "back-upper", "back-lower", "back-bottom")
        self.relate("connect", "front", "back")
        self.add_arc("bail-top", (20,5), (26,5), radius_x=3)
        self.add_arc("bail-bottom", (26,5), (20,5), radius_x=3)
        self.add_contour("bail", "bail-top", "bail-bottom", closed=True)
        self.add_dot("portrait-head", (31,25))
        self.add_arc("portrait-shoulders", (25,37), (37,37), radius_x=6, radius_y=5)
