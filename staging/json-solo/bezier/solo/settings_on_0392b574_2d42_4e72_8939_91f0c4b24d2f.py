"""Settings on (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('sym-e1', (44, 24), ((44, 23.764), (44, 23.231), (44, 23)))
        self.add_bezier('sym-e2', (44, 23), ((44, 17.048), (42.127, 11.24), (39, 9)))
        self.add_bezier('sym-e3', (39, 9), ((38.491, 8.632), (37.564, 8), (37, 8)))
        self.add_bezier('sym-e4', (37, 8), ((36.964, 8), (37.036, 8), (37, 8)))
        self.add_line('sym-e5', (37, 8), (11, 8))
        self.add_bezier('sym-e6', (11, 8), ((10.955, 8), (11.045, 8), (11, 8)))
        self.add_bezier('sym-e7', (11, 8), ((10.382, 8), (9.564, 8.584), (9, 9)))
        self.add_bezier('sym-e8', (9, 9), ((5.973, 11.24), (4, 17.192), (4, 23)))
        self.add_bezier('sym-e9', (4, 23), ((4, 23.112), (4, 22.888), (4, 23)))
        self.add_bezier('sym-e10', (4, 23), ((4, 23.195), (4, 23.801), (4, 24)))
        self.add_bezier('sym-e11', (4, 24), ((4, 24.199), (4, 24.805), (4, 25)))
        self.add_bezier('sym-e12', (4, 25), ((4, 25.112), (4, 24.888), (4, 25)))
        self.add_bezier('sym-e13', (4, 25), ((4, 30.808), (5.973, 36.76), (9, 39)))
        self.add_bezier('sym-e14', (9, 39), ((9.564, 39.416), (10.382, 40), (11, 40)))
        self.add_bezier('sym-e15', (11, 40), ((11.045, 40), (10.955, 40), (11, 40)))
        self.add_line('sym-e16', (11, 40), (37, 40))
        self.add_bezier('sym-e17', (37, 40), ((37.036, 40), (36.964, 40), (37, 40)))
        self.add_bezier('sym-e18', (37, 40), ((37.564, 40), (38.491, 39.368), (39, 39)))
        self.add_bezier('sym-e19', (39, 39), ((42.127, 36.76), (44, 30.952), (44, 25)))
        self.add_bezier('sym-e20', (44, 25), ((44, 24.769), (44, 24.236), (44, 24)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', closed=True)
