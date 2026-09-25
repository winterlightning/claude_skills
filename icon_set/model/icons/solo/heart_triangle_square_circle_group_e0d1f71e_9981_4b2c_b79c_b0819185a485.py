from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0d1f71e-9981-4b2c-b79c-b0819185a485'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/photo shape_e0d1f71e-9981-4b2c-b79c-b0819185a485.svg'
AUTHOR = 'gpt-6'


class HeartTriangleSquareCircleGroup(Solo48):
    icon_id = 'heart-triangle-square-circle-group'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('shapes', 'heart', 'triangle', 'square', 'circle', 'geometry', 'forms', 'design')

    def build(self) -> None:
        # Four separate symbols occupy equal 14-unit cells, separated by eight.
        self.add_bezier('heart',(13,9),((14,7),(15,6),(17,6)),((19,6),(20,8),(20,10)),((20,14),(16,18),(13,20)),((10,18),(6,14),(6,10)),((6,8),(7,6),(9,6)),((11,6),(12,7),(13,9)))
        self.add_polyline('triangle',(35,6),(42,20),(28,20),closed=True)
        self.add_polyline('square',(6,28),(20,28),(20,42),(6,42),closed=True)
        self.add_arc('circle-top',(28,35),(42,35),radius_x=7)
        self.add_arc('circle-bottom',(42,35),(28,35),radius_x=7)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
