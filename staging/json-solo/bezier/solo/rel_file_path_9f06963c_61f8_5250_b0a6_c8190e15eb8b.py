"""Rel file path (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f06963c-61f8-5250-b0a6-c8190e15eb8b'
SOURCE_PATH = 'icons-json/programing/rel file path_9f06963c-61f8-5250-b0a6-c8190e15eb8b.json'
AUTHOR = 'json_to_solo'

class RelFilePathPrograming(Solo48):
    icon_id = 'rel-file-path-programing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('rel', 'file', 'path', 'programing')

    def build(self):
        self.add_line('e0', (24, 44), (40, 4))
        self.add_arc('e1-top', (8, 40), (14, 40), radius_x=3, radius_y=4)
        self.add_arc('e1-bottom', (14, 40), (8, 40), radius_x=3, radius_y=4)
        self.add_contour('c0', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
