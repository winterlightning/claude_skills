"""Undo (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca81781a-87b1-5f68-8c21-db6549eefdae'
SOURCE_PATH = 'icons-json/interface-essential/undo_ca81781a-87b1-5f68-8c21-db6549eefdae.json'
AUTHOR = 'json_to_solo'

class Undo(Solo48):
    icon_id = 'undo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('undo', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 4), (8, 16))
        self.add_line('e1', (17, 16), (8, 16))
        self.add_line('e2', (8, 16), (11, 13))
        self.add_bezier('e3', (11, 13), ((11.404, 12.673), (12.227, 12.509), (12.615, 12.155)), ((13.305, 11.527), (13.903, 10.836), (14.661, 10.309)), ((16.775, 8.845), (19.284, 7.982), (21.777, 7.773)), ((31.697, 6.955), (39.992, 16.118), (39.992, 26.636)), ((39.992, 26.762), (40, 26.896), (40, 27.021)), ((40, 27.023), (40, 27.025), (40, 27.027)), ((40, 27.091), (39.992, 27.155), (39.992, 27.227)), ((39.992, 34.473), (35.718, 40.718), (30, 44)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3')
