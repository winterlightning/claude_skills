"""Wise logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce82081f-764d-46c5-b559-2b27f5182b14'
SOURCE_PATH = 'icons-json/logos/wise logo_ce82081f-764d-46c5-b559-2b27f5182b14.json'
AUTHOR = 'json_to_solo'

class WiseLogo(Solo48):
    icon_id = 'wise-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('wise', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (25, 26), (6, 26))
        self.add_line('e1', (6, 26), (17, 17))
        self.add_line('e2', (17, 17), (9, 6))
        self.add_line('e3', (9, 6), (42, 6))
        self.add_line('e4', (42, 6), (29, 42))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4')
