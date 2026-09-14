"""Deploy rules (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab4efcc8-0cf1-4f8d-a402-841966ada655'
SOURCE_PATH = 'icons-json/arrows/deploy rules_ab4efcc8-0cf1-4f8d-a402-841966ada655.json'
AUTHOR = 'json_to_solo'

class DeployRules(Solo48):
    icon_id = 'deploy-rules'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('deploy', 'rules', 'arrows')

    def build(self):
        self.add_line('e0', (17, 13), (23, 6))
        self.add_line('e1', (23, 25), (23, 6))
        self.add_line('e2', (30, 13), (23, 6))
        self.add_line('e3', (6, 32), (42, 32))
        self.add_line('e4', (6, 42), (42, 42))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
