"""Text strike through (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8a2022f-6ae0-41e6-966f-a2ea1e79a09b'
SOURCE_PATH = 'icons-json/interface-essential/text strike through_a8a2022f-6ae0-41e6-966f-a2ea1e79a09b.json'
AUTHOR = 'json_to_solo'

class TextStrikeThrough(Solo48):
    icon_id = 'text-strike-through'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'strike', 'through', 'interface-essential')

    def build(self):
        self.add_line('e0', (20, 22), (27, 24))
        self.add_line('e1', (6, 26), (31, 26))
        self.add_line('e2', (42, 26), (31, 26))
        self.add_bezier('e3', (32, 15), ((31.894, 13.83), (31.92, 12.701), (31.437, 11.621)), ((29.973, 8.381), (26.495, 6.008), (22.895, 6.008)), ((22.831, 6.008), (22.767, 6), (22.702, 6)), ((22.701, 6), (22.7, 6), (22.699, 6)), ((22.495, 6), (22.298, 6.008), (22.094, 6.008)), ((15.998, 6.008), (11.76, 12.447), (14.959, 17.864)), ((16.031, 19.672), (18.036, 21.345), (20, 22)))
        self.add_bezier('e4', (27, 24), ((28.154, 24.385), (29.912, 25.452), (31, 26)))
        self.add_bezier('e5', (13, 32), ((13.237, 35.968), (14.075, 39.284), (17.913, 40.985)), ((19.255, 41.583), (20.76, 41.992), (22.241, 41.992)), ((22.305, 41.992), (22.378, 42), (22.442, 42)), ((22.443, 42), (22.444, 42), (22.445, 42)), ((22.642, 42), (22.846, 41.992), (23.043, 41.992)), ((30.169, 41.992), (34.865, 35.103), (32.386, 28.484)), ((31.969, 27.379), (31.736, 26.933), (31, 26)))
        self.add_contour('c0', 'e3', 'e0', 'e4')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
