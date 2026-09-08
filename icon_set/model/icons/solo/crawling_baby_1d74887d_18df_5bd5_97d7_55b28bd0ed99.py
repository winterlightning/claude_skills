"""A left-facing baby on hands and knees; deliberate side-view asymmetry preserves the crawling pose."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d74887d-18df-5bd5-97d7-55b28bd0ed99'
SOURCE_PATH = 'pictographic-primitives/babies/crawling kid_1d74887d-18df-5bd5-97d7-55b28bd0ed99.svg'
AUTHOR = 'gpt-6'


class CrawlingBaby(Solo48):
    icon_id = 'crawling-baby'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/babies"
    aliases = ()
    keywords = ('crawling', 'baby', 'infant', 'nursery')

    def build(self) -> None:
        # Centerline extremes: (2,2)-(46,46).
        self.add_arc('head-top', (2, 10), (18, 10), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('head-bottom', (18, 10), (2, 10), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_line('back', (19, 24), (33, 24))
        self.add_arc('hip', (33, 24), (41, 32), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('thigh', (41, 32), (39, 40))
        self.add_line('foot-top', (39, 40), (43, 40))
        self.add_arc('foot-end', (43, 40), (43, 46), radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_line('sole', (43, 46), (33, 46))
        self.add_arc('knee', (33, 46), (29, 42), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('thigh-inner', (29, 42), (29, 34))
        self.add_line('belly', (29, 34), (19, 34))
        self.add_line('arm-inner', (19, 34), (12, 44))
        self.add_arc('hand', (12, 44), (4, 38), radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('arm-outer', (4, 38), (13, 27))
        self.add_arc('shoulder', (13, 27), (19, 24), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('body', 'back', 'hip', 'thigh', 'foot-top', 'foot-end', 'sole', 'knee', 'thigh-inner', 'belly', 'arm-inner', 'hand', 'arm-outer', 'shoulder', closed=True)
