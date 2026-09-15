'Search with circular arrows: smooth open circular sweeps, clear arrowhead separation and a handle sharing the lower-right arc endpoint.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78eadcd2-270f-4356-8302-06a17f33acbd'
SOURCE_PATH = 'pictographic-primitives/apps/seo search_78eadcd2-270f-4356-8302-06a17f33acbd.svg'
AUTHOR = 'gpt-6'

class SeoSearch(Solo48):
    icon_id = 'seo-search'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    aliases = ()
    keywords = ('seo', 'search', 'apps')

    def build(self) -> None:
        # Two coherent circular sweeps and tangent arrowheads; handle attaches on the lower-right arc.
        self.add_bezier('left',(24,6),((14,6),(6,14),(6,24)),((6,29),(8,33),(12,36)))
        self.add_polyline('left-head',(6,36),(12,36),(12,28))
        self.relate('connect','left','left-head')
        self.add_bezier('right',(33,10),((38,14),(40,19),(40,24)),((40,29),(38,32),(34,35)),((31,38),(27,40),(21,40)))
        self.add_polyline('right-head',(40,10),(33,10),(33,18))
        self.add_line('handle',(34,35),(42,42))
        self.relate('connect','right','right-head');self.relate('connect','right','handle')
