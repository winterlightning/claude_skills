'Opera house: preserve the rising sail silhouettes above a smooth separate water line, with a clear gap beneath the base.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3eff9550-c341-4d47-a50c-db9b48c3be68'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/sydney opera house_3eff9550-c341-4d47-a50c-db9b48c3be68.svg'
AUTHOR = 'gpt-6'

class OperaHouseShellsOnWater(Solo48):
    icon_id = 'opera-house-shells-on-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('sydney opera house', 'australia', 'shells', 'sails', 'harbour', 'water', 'landmark', 'cloud')

    def build(self) -> None:
        self.add_polyline('base',(4,30),(44,30))
        self.add_bezier('sail-a',(4,30),((5,27),(5,23),(4,20)))
        self.add_line('sail-a-edge',(4,20),(17,26))
        self.add_bezier('sail-b',(17,26),((16,19),(14,12),(13,8)))
        self.add_bezier('sail-c',(13,8),((24,10),(29,18),(31,26)))
        self.add_bezier('sail-d',(31,26),((35,22),(39,21),(44,20)))
        self.add_line('sail-end',(44,20),(44,30))
        self.add_contour('shells','sail-a','sail-a-edge','sail-b','sail-c','sail-d','sail-end')
        self.relate('connect','shells','base')
        self.add_bezier('water',(4,40),((10,40),(12,39),(16,39)),((20,39),(22,40),(24,40)),((28,40),(30,39),(34,39)),((38,39),(40,40),(44,40)))
