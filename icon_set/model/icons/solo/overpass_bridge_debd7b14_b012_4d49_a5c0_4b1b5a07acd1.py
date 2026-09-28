from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'debd7b14-b012-4d49-a5c0-4b1b5a07acd1'
SOURCE_PATH = 'pictographic-primitives/transportation/road sign_debd7b14-b012-4d49-a5c0-4b1b5a07acd1.svg'
AUTHOR = 'gpt-6'

class OverpassBridge(Solo48):
    icon_id = 'overpass-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('overpass', 'bridge', 'highway', 'road', 'flyover', 'motorway', 'junction', 'infrastructure')

    def build(self):
        self.add_polyline('deck',(6,24),(6,16),(14,16),(34,16),(42,16),(42,24))
        self.add_line('road-upper-left',(16,6),(14,16))
        self.add_line('road-upper-right',(32,6),(34,16))
        self.relate('connect','road-upper-left','deck')
        self.relate('connect','road-upper-right','deck')
        self.add_line('road-lower-left',(14,26),(10,42))
        self.add_line('road-lower-right',(34,26),(38,42))
        self.add_line('centre-upper',(24,6),(24,8))
        self.add_line('centre-lower',(24,26),(24,30))
        self.add_line('centre-bottom',(24,40),(24,42))
