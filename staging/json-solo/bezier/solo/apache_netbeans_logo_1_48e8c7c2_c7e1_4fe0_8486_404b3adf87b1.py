"""Apache netbeans logo 1 (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48e8c7c2-c7e1-4fe0-8486-404b3adf87b1'
SOURCE_PATH = 'icons-json/_uncategorized_03/apache netbeans logo 1_48e8c7c2-c7e1-4fe0-8486-404b3adf87b1.json'
AUTHOR = 'json_to_solo'

class ApacheNetbeansLogo1Uncategorized03(Solo48):
    icon_id = 'apache-netbeans-logo-1-uncategorized-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('apache', 'netbeans', 'logo', '_uncategorized_03')

    def build(self):
        self.add_line('sym-e0', (24, 44), (24, 24))
        self.add_line('sym-e1', (24, 24), (40, 14))
        self.add_line('sym-e2', (40, 14), (40, 33))
        self.add_line('sym-e3', (40, 33), (24, 44))
        self.add_line('sym-e4', (24, 44), (8, 33))
        self.add_line('sym-e5', (8, 33), (8, 14))
        self.add_line('sym-e6', (8, 14), (24, 24))
        self.add_line('sym-e7', (24, 4), (24, 4))
        self.add_line('sym-e8', (24, 4), (40, 14))
        self.add_line('sym-e9', (8, 14), (24, 4))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6')
        self.add_contour('sym-c1', 'sym-e7', 'sym-e8')
        self.add_contour('sym-c2', 'sym-e9')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
