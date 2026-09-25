from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d59d637-c7fc-571d-b339-c3ee94ed0915'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/artboard expand_3d59d637-c7fc-571d-b339-c3ee94ed0915.svg'
AUTHOR = 'gpt-6'


class ArtboardWithDiagonalGuide(Solo48):
    icon_id = 'artboard-with-diagonal-guide'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('artboard', 'guide', 'diagonal', 'crop', 'corner', 'layout', 'design', 'geometry')

    def build(self) -> None:
        # Extended orthogonal crop guides and their rising diagonal share one corner.
        self.add_polyline('corner',(12,6),(12,12),(12,36),(36,36),(42,36))
        self.add_polyline('top',(6,12),(12,12),(24,12))
        self.add_polyline('right',(36,24),(36,36),(36,42))
        self.add_line('diagonal',(12,36),(42,6))
        for name in ('top','right','diagonal'):self.relate('connect',name,'corner')
