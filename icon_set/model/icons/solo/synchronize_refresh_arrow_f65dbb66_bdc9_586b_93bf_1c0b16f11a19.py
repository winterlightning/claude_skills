"""Synchronize refresh arrow (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f65dbb66-bdc9-586b-93bf-1c0b16f11a19'
SOURCE_PATH = 'icons-json/interface-essential/synchronize refresh arrow_f65dbb66-bdc9-586b-93bf-1c0b16f11a19.json'
AUTHOR = 'json_to_solo'

class SynchronizeRefreshArrowF65dbb66(Solo48):
    icon_id = 'synchronize-refresh-arrow-f65dbb66'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('synchronize', 'refresh', 'arrow', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 20), (9, 26))
        self.add_line('e1', (9, 26), (15, 20))
        self.add_bezier('e2', (11, 32), ((13.936, 36.834), (19.945, 39.992), (26.073, 39.992)), ((26.279, 39.992), (26.484, 40), (26.682, 40)), ((26.685, 40), (26.688, 40), (26.691, 40)), ((26.9, 40), (27.109, 39.992), (27.309, 39.992)), ((36, 39.992), (43.991, 32.632), (43.991, 24.573)), ((43.991, 24.382), (44, 24.199), (44, 24.009)), ((44, 24.006), (44, 24.003), (44, 24)), ((44, 23.806), (43.991, 23.613), (43.991, 23.419)), ((43.991, 15.36), (35.991, 8.008), (27.3, 8.008)), ((27.094, 8.008), (26.888, 8), (26.683, 8)), ((26.679, 8), (26.676, 8), (26.673, 8)), ((26.464, 8), (26.245, 8.008), (26.036, 8.008)), ((23.927, 8.008), (21.745, 8.531), (19.818, 9.297)), ((12.555, 12.168), (8.564, 18.884), (9, 26)))
        self.add_contour('c0', 'e2')
        self.add_contour('c1', 'e0', 'e1')
