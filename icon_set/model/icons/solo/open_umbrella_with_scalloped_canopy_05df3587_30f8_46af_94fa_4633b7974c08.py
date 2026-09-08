"""Scalloped umbrella with a left J handle. Lucide umbrella informs the dome and shaft; source scallops preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '05df3587-30f8-46af-94fa-4633b7974c08'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/umbrella_05df3587-30f8-46af-94fa-4633b7974c08.svg'
AUTHOR = 'astra-chatgpt'

class OpenUmbrellaWithScallopedCanopy(Solo48):
    icon_id = 'open-umbrella-with-scalloped-canopy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('open', 'umbrella', 'with', 'scalloped', 'canopy')

    def build(self) -> None:
        # Centerline extremes (2,2)-(46,46).
        self.add_arc("dome-left", (2,26), (24,6), radius_x=22, radius_y=20)
        self.add_arc("dome-right", (24,6), (46,26), radius_x=22, radius_y=20)
        self.add_arc("scallop-right", (46,26), (32,26), radius_x=7, radius_y=4, sweep=False)
        self.add_arc("scallop-middle-right", (32,26), (24,22), radius_x=8, radius_y=4, sweep=False)
        self.add_arc("scallop-middle-left", (24,22), (16,26), radius_x=8, radius_y=4, sweep=False)
        self.add_arc("scallop-left", (16,26), (2,26), radius_x=7, radius_y=4, sweep=False)
        self.add_contour("canopy", "dome-left", "dome-right", "scallop-right", "scallop-middle-right", "scallop-middle-left", "scallop-left", closed=True)
        self.add_line("finial", (24,2), (24,6))
        self.add_line("shaft", (24,22), (24,40))
        self.add_arc("hook", (24,40), (12,40), radius_x=6)
        self.add_line("hook-tip", (12,40), (12,38))
        self.add_contour("handle", "shaft", "hook", "hook-tip")
        self.relate("connect", "canopy", "finial")
        self.relate("connect", "canopy", "handle")
