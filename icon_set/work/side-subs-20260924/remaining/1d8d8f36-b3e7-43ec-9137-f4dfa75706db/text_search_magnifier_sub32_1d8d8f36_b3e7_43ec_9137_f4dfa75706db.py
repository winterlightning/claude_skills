"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '1d8d8f36-b3e7-43ec-9137-f4dfa75706db'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass t_1d8d8f36-b3e7-43ec-9137-f4dfa75706db.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular magnifier lens', 'lower-right handle', 'uppercase T with source-style horizontal caps')

class Drawing(Sub32):
    icon_id = 'text-search-magnifier-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('text', 'search', 'magnifying', 'glass')
    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'frame': 4, 'handle': 4}
    COMPACT_EXCEPTION = 'User requested uniform 4px strokes on a 32px canvas. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    TYPEFACE_GLYPH_IDS = ('letter-t-uppercase',)

    def build(self):
        self.circle('frame',14,14,12)
        # Preserve the reference's three serif caps around the reused T glyph.
        self.add_line('serif-left',(9,7),(9,9))
        self.add_line('serif-right',(19,7),(19,9))
        self.add_line('serif-foot',(12,21),(16,21))
        join=14+12/(2**0.5)
        self.add_line('handle',(join,join),(30,30))
        self.relate('connect','handle','frame-bottom')
        self.add_line('text-T-0-0-0-0',(9.0, 7.0),(19.0, 7.0))
        self.add_line('text-T-0-1-0-0',(14.0, 7.0),(14.0, 21.0))

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

