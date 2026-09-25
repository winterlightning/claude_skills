"""Independent 32px profile of graph.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'a8abb591-1282-4a97-be3e-9a18708db726'
SOURCE_PATH = 'pictographic-primitives/arrows/graph_a8abb591-1282-4a97-be3e-9a18708db726.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a8abb591-1282-4a97-be3e-9a18708db726', 'pictographic-primitives/arrows/graph_a8abb591-1282-4a97-be3e-9a18708db726.svg'),)
PROFILE_SOURCE_KEYS = ('solo/graph',)
SOLO_SOURCE_ICON_IDS = ('graph',)
REFERENCE_EXPORT_SHA256 = '2d11a302432b15321d1b87775c61466d1c0076bdfebd72a93cca0392c5198a3b'

class Drawing(Sub32):
    icon_id = 'graph-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (24, 5), (30, 5))
        self.add_line('p1-r1-2', (30, 5), (17, 21))
        self.add_line('p1-r1-3', (17, 21), (12, 15))
        self.add_line('p1-r1-4', (12, 15), (2, 27))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (30, 5), (30, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.relate("connect", 'p1-r1-1', 'p2-r1-1')
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
