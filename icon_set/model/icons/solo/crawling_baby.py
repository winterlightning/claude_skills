# Review revision; previous candidates preserved.
"""A left-facing baby on hands and knees; deliberate side-view asymmetry preserves the crawling pose."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d74887d-18df-5bd5-97d7-55b28bd0ed99'
SOURCE_PATH = 'pictographic-primitives/babies/crawling kid_1d74887d-18df-5bd5-97d7-55b28bd0ed99.svg'
AUTHOR = 'gpt-6'

class CrawlingBaby(Solo48):
    icon_id = 'crawling-baby'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'primitives')
    aliases = ()
    keywords = ('crawling', 'baby', 'infant', 'nursery')

    def build(self) -> None:
        self.add_arc('head-top', (7, 11), (17, 11), radius_x=5)
        self.add_arc('head-bottom', (17, 11), (7, 11), radius_x=5)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('back', (20, 24), (32, 24))
        self.add_arc('hip', (32, 24), (42, 34), radius_x=10)
        self.add_line('leg-outer', (42, 34), (42, 38))
        self.add_arc('foot-round', (42, 38), (38, 42), radius_x=4)
        self.add_line('sole', (38, 42), (30, 42))
        self.add_line('leg-inner', (30, 42), (30, 34))
        self.add_line('belly', (30, 34), (22, 34))
        self.add_line('arm-inner', (22, 34), (14, 42))
        self.add_arc('hand', (14, 42), (6, 36), radius_x=8, radius_y=6)
        self.add_line('arm-outer', (6, 36), (14, 26))
        self.add_arc('shoulder', (14, 26), (20, 24), radius_x=6)
        self.add_contour('body', 'back', 'hip', 'leg-outer', 'foot-round', 'sole', 'leg-inner', 'belly', 'arm-inner', 'hand', 'arm-outer', 'shoulder', closed=True)
