'Two office blocks: clean shared roof and baseline, a centered window replacing an off-center short fragment.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '929733e7-35b6-4e6e-bcee-05768cc7b7d3'
SOURCE_PATH = 'icons-json/building/building_929733e7-35b6-4e6e-bcee-05768cc7b7d3.json'
AUTHOR = 'gpt-6'

class Building929733e7(Solo48):
    icon_id = 'building-929733e7'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('building',)

    def build(self) -> None:
        # Both blocks use shared ground and an exact joint at the front roof.
        self.add_polyline('ground',(8,44),(12,44),(23,44),(40,44))
        self.add_polyline('rear',(12,44),(12,4),(30,4),(30,16))
        self.add_polyline('front',(23,44),(23,16),(30,16),(40,16),(40,44))
        self.relate('connect','ground','rear')
        self.relate('connect','ground','front')
        self.relate('connect','rear','front')
        self.add_dot('window',(31,26))
