"""Mountain road; independently authored for SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9de0bb08-aa64-47f3-8ea6-b9ac7d3cb14e'
SOURCE_PATH = 'pictographic-primitives/transportation/off road mode_9de0bb08-aa64-47f3-8ea6-b9ac7d3cb14e.svg'
AUTHOR = 'gpt-6'

class MountainRoad(Solo48):
    icon_id = 'mountain-road'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('mountain', 'road', 'off-road', 'terrain', 'trail')

    def build(self) -> None:
        # SQUARE centerline bounds (6,6)-(42,42); asymmetry preserves the landscape.
        self.add_polyline('main-peak',(6,22),(16,6),(22,14),(28,22))
        self.add_polyline('rear-peak',(22,14),(30,8),(42,22))
        self.relate('connect','main-peak','rear-peak')
        self.add_arc('road-left-turn',(16,30),(16,38),radius_x=6,radius_y=4,sweep=False)
        self.add_arc('road-left-exit',(16,38),(22,42),radius_x=6,radius_y=4)
        self.add_contour('road-left','road-left-turn','road-left-exit')
        self.add_arc('road-right-turn',(30,31),(30,35),radius_x=3,radius_y=2,sweep=False)
        self.add_arc('road-right-exit',(30,35),(42,42),radius_x=12,radius_y=7)
        self.add_contour('road-right','road-right-turn','road-right-exit')
