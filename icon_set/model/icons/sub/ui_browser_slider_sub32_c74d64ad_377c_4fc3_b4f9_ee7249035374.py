"""Independent 32px profile of ui-browser-slider.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'c74d64ad-377c-4fc3-b4f9-ee7249035374'
SOURCE_PATH = 'pictographic-primitives/websites/ui browser slider_c74d64ad-377c-4fc3-b4f9-ee7249035374.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c74d64ad-377c-4fc3-b4f9-ee7249035374', 'pictographic-primitives/websites/ui browser slider_c74d64ad-377c-4fc3-b4f9-ee7249035374.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ui-browser-slider',)
SOLO_SOURCE_ICON_IDS = ('ui-browser-slider',)
REFERENCE_EXPORT_SHA256 = 'bbe7abdff89bedf4b8c61d744d73c876ac3b916406f0ec2fb57f99bad9da4ebe'

class Drawing(Sub32):
    icon_id = 'ui-browser-slider-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'websites'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (30, 10), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (9, 17), (22, 17))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 2), (5, 2))
        self.add_arc('p3-r1-2', (5, 2), (2, 5), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_line('p3-r1-3', (2, 5), (2, 27))
        self.add_arc('p3-r1-4', (2, 27), (3, 29), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p3-r1-5', (3, 29), (4, 30))
        self.add_arc('p3-r1-6', (4, 30), (5, 30), radius_x=17, radius_y=17, large_arc=False, sweep=True)
        self.add_line('p3-r1-7', (5, 30), (27, 30))
        self.add_line('p3-r1-8', (27, 30), (29, 29))
        self.add_line('p3-r1-9', (29, 29), (30, 25))
        self.add_line('p3-r1-10', (30, 25), (30, 5))
        self.add_arc('p3-r1-11', (30, 5), (27, 2), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', 'p3-r1-8', 'p3-r1-9', 'p3-r1-10', 'p3-r1-11', closed=False)
