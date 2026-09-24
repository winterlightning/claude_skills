"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '15fc1905-26f1-420c-9167-f58df5f29604'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass pill_15fc1905-26f1-420c-9167-f58df5f29604.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular magnifier lens', 'lower-right handle', 'diagonal capsule outline', 'one transverse divider')

class Drawing(Sub32):
    icon_id = 'medicine-search-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('medicine', 'search', 'magnifying', 'glass')


    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {'lens': 4, 'handle': 4}
    COMPACT_EXCEPTION = 'Complete source composition with uniform 4px strokes. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    def build(self):
        self.circle('lens',14,14,12)
        join=14+12/(2**0.5)
        self.add_line('handle',(join,join),(30,30))
        self.relate('connect','lens-bottom','handle')
        # Capsule is defined by parallel sides and two smooth semicircular ends.
        self.add_line('pill-left',(8,13),(13,8))
        self.add_bezier('pill-top',(13,8),((17,4),(23,10),(19,14)))
        self.add_line('pill-right',(19,14),(14,19))
        self.add_bezier('pill-bottom',(14,19),((10,23),(4,17),(8,13)))
        self.add_contour('capsule','pill-left','pill-top','pill-right','pill-bottom',closed=True)
        self.add_line('divider',(10,11),(16,17))
        self.relate('connect','divider','pill-left')
        self.relate('connect','divider','pill-right')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

