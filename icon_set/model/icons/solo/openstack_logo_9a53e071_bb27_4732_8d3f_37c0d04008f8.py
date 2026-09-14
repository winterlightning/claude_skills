"""Openstack logo (logos), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a53e071-bb27-4732-8d3f-37c0d04008f8'
SOURCE_PATH = 'icons-json/logos/openstack logo_9a53e071-bb27-4732-8d3f-37c0d04008f8.json'
AUTHOR = 'json_to_solo'

class OpenstackLogo(Solo48):
    icon_id = 'openstack-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('openstack', 'logo', 'logos')

    def build(self):
        self.add_line('sym-e0', (6, 30), (6, 18))
        self.add_line('sym-e1', (6, 18), (14, 18))
        self.add_line('sym-e2', (14, 18), (14, 30))
        self.add_line('sym-e3', (14, 30), (14, 34))
        self.add_line('sym-e4', (14, 34), (34, 34))
        self.add_line('sym-e5', (34, 34), (34, 30))
        self.add_line('sym-e6', (34, 30), (34, 18))
        self.add_line('sym-e7', (34, 18), (34, 14))
        self.add_line('sym-e8', (34, 14), (14, 14))
        self.add_line('sym-e9', (14, 14), (14, 18))
        self.add_line('sym-e10', (42, 30), (42, 18))
        self.add_line('sym-e11', (42, 18), (34, 18))
        self.add_line('sym-e12', (6, 30), (14, 30))
        self.add_line('sym-e13', (6, 30), (6, 37))
        self.add_arc('sym-e14', (6, 37), (11, 42), radius_x=6, sweep=False)
        self.add_line('sym-e15', (11, 42), (24, 42))
        self.add_line('sym-e16', (24, 42), (37, 42))
        self.add_arc('sym-e17', (37, 42), (42, 37), radius_x=6, sweep=False)
        self.add_line('sym-e18', (42, 37), (42, 30))
        self.add_line('sym-e19', (42, 30), (34, 30))
        self.add_line('sym-e20', (6, 18), (6, 11))
        self.add_arc('sym-e21', (6, 11), (11, 6), radius_x=6)
        self.add_line('sym-e22', (11, 6), (24, 6))
        self.add_line('sym-e23', (24, 6), (37, 6))
        self.add_arc('sym-e24', (37, 6), (42, 11), radius_x=6)
        self.add_line('sym-e25', (42, 11), (42, 18))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9')
        self.add_contour('sym-c1', 'sym-e10', 'sym-e11')
        self.add_contour('sym-c2', 'sym-e12')
        self.add_contour('sym-c3', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19')
        self.add_contour('sym-c4', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c4')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
