"""Left-facing crawling baby with circular head, open arm and back, rounded hip and bent leg. Remove narrow outlined hand and foot returns. SQUARE centerline bounds (6,6)-(42,42). Lucide person-standing informed open limbs; side-view asymmetry preserves the pose."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1d74887d-18df-5bd5-97d7-55b28bd0ed99'
SOURCE_PATH = 'pictographic-primitives/babies/crawling kid_1d74887d-18df-5bd5-97d7-55b28bd0ed99.svg'
AUTHOR = 'gpt-6'

class CrawlingBabyVariant2(Solo48):
    icon_id = 'crawling-baby-v2'
    variant_of = 'crawling-baby'
    variant_label = 'Roomier spacing — review 03'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'people/babies'
    aliases = ()
    keywords = ('crawling', 'baby', 'infant', 'nursery')

    def build(self):
        self.add_arc('head-a', (12, 6), (12, 18), radius_x=6)
        self.add_arc('head-b', (12, 18), (12, 6), radius_x=6)
        self.add_contour('head', 'head-a', 'head-b', closed=True)
        self.add_line('arm', (8, 42), (16, 27))
        self.add_line('back', (16, 27), (32, 27))
        self.add_arc('hip', (32, 27), (42, 37), radius_x=10)
        self.add_line('leg-1', (42, 37), (42, 42))
        self.add_line('leg-2', (42, 42), (32, 42))
        self.add_contour('pose', 'arm', 'back', 'hip', 'leg-1', 'leg-2')
