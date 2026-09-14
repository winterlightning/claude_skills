"""Virustotal logo (logos), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dfc6b464-8ac0-49cb-aee2-e4779e00be3a'
SOURCE_PATH = 'icons-json/logos/virustotal logo_dfc6b464-8ac0-49cb-aee2-e4779e00be3a.json'
AUTHOR = 'json_to_solo'

class VirustotalLogoLogos(Solo48):
    icon_id = 'virustotal-logo-logos'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('virustotal', 'logo', 'logos')

    def build(self):
        self.add_line('e0', (6, 6), (42, 6))
        self.add_line('e1', (42, 6), (42, 42))
        self.add_line('e2', (42, 42), (6, 42))
        self.add_line('e3', (6, 42), (23, 24))
        self.add_line('e4', (23, 24), (6, 6))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', closed=True)
