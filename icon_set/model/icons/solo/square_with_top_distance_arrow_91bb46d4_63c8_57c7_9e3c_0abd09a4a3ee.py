from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '91bb46d4-63c8-57c7-9e3c-0abd09a4a3ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/top distance_91bb46d4-63c8-57c7-9e3c-0abd09a4a3ee.svg'
AUTHOR = 'gpt-6'


class SquareWithTopDistanceArrow(Solo48):
    icon_id = 'square-with-top-distance-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/design'
    aliases = ()
    keywords = ('square', 'arrow', 'top', 'distance', 'boundary', 'spacing', 'layout', 'diagram')

    def build(self) -> None:
        # One attached distance diagram, centered on x=24 below the top boundary.
        axis=24
        self.add_line('boundary',(6,6),(42,6))
        self.add_polyline('square',(axis-6,30),(axis,30),(axis+6,30),(axis+6,42),(axis-6,42),closed=True)
        self.add_line('stem',(axis,30),(axis,14))
        self.add_polyline('head',(axis-6,20),(axis,14),(axis+6,20))
        self.relate('connect','stem','square');self.relate('connect','stem','head')
