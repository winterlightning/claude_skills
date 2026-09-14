"""Settings on (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0392b574-2d42-4e72-8939-91f0c4b24d2f'
SOURCE_PATH = 'icons-json/interface-essential/settings on_0392b574-2d42-4e72-8939-91f0c4b24d2f.json'
AUTHOR = 'json_to_solo'

class SettingsOnInterfaceEssential(Solo48):
    icon_id = 'settings-on-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('settings', 'on', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (33, 30), (33, 18))
        self.add_arc('sym-e1', (44, 24), (44, 23), radius_x=28)
        self.add_line('sym-e2-1', (44, 23), (43, 16))
        self.add_arc('sym-e2-2', (43, 16), (39, 9), radius_x=13, sweep=False)
        self.add_line('sym-e3', (39, 9), (37, 8))
        self.add_line('sym-e5', (37, 8), (11, 8))
        self.add_line('sym-e7', (11, 8), (9, 9))
        self.add_arc('sym-e8-1', (9, 9), (5, 16), radius_x=14, sweep=False)
        self.add_arc('sym-e8-2', (5, 16), (4, 23), radius_x=25, sweep=False)
        self.add_line('sym-e10', (4, 23), (4, 24))
        self.add_line('sym-e11', (4, 24), (4, 25))
        self.add_arc('sym-e13-1', (4, 25), (5, 32), radius_x=25, sweep=False)
        self.add_arc('sym-e13-2', (5, 32), (9, 39), radius_x=14, sweep=False)
        self.add_line('sym-e14', (9, 39), (11, 40))
        self.add_line('sym-e16', (11, 40), (37, 40))
        self.add_line('sym-e18', (37, 40), (39, 39))
        self.add_arc('sym-e19-1', (39, 39), (43, 32), radius_x=13, sweep=False)
        self.add_line('sym-e19-2', (43, 32), (44, 25))
        self.add_line('sym-e20', (44, 25), (44, 24))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2-1', 'sym-e2-2', 'sym-e3', 'sym-e5', 'sym-e7', 'sym-e8-1', 'sym-e8-2', 'sym-e10', 'sym-e11', 'sym-e13-1', 'sym-e13-2', 'sym-e14', 'sym-e16', 'sym-e18', 'sym-e19-1', 'sym-e19-2', 'sym-e20', closed=True)
