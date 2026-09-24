"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '537f61ca-8ecd-4e15-bb46-ac683be40ccd'
SOURCE_PATH = 'pictographic-primitives/rating/ranking first_537f61ca-8ecd-4e15-bb46-ac683be40ccd.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('three podium blocks', 'taller central block', 'left block taller than right', 'numeral 1 on central block')

class Drawing(Sub32):
    icon_id = 'first-place-podium-sub32'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('first', 'place', 'winner', 'podium')
    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {name:4 for name in ('base','left-bottom','left-side','left-corner','left-top','center-left','center-tl','center-top','center-tr','center-right','right-top','right-corner','right-side','right-bottom')}
    COMPACT_EXCEPTION = 'User requested uniform 4px strokes on a 32px canvas. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    TYPEFACE_GLYPH_IDS = ('digit-1',)

    def build(self):
        # All three blocks share a baseline; center keeps its distinct tall silhouette.
        self.add_line('base',(4,28),(28,28))
        self.add_arc('left-bottom',(4,28),(2,26),radius_x=2)
        self.add_line('left-side',(2,26),(2,16))
        self.add_arc('left-corner',(2,16),(4,14),radius_x=2)
        self.add_line('left-top',(4,14),(11,14))
        self.add_line('center-left',(11,28),(11,6))
        self.add_arc('center-tl',(11,6),(13,4),radius_x=2)
        self.add_line('center-top',(13,4),(19,4))
        self.add_arc('center-tr',(19,4),(21,6),radius_x=2)
        self.add_line('center-right',(21,6),(21,28))
        self.add_line('right-top',(21,16),(28,16))
        self.add_arc('right-corner',(28,16),(30,18),radius_x=2)
        self.add_line('right-side',(30,18),(30,26))
        self.add_arc('right-bottom',(30,26),(28,28),radius_x=2)
        self.relate('connect','base','center-left','center-right')
        self.relate('connect','left-top','center-left')
        self.relate('connect','right-top','center-right')
        self.add_line('text-1-0-0-0-0',(16.005902, 23.90522),(16.005902, 12.354073))
        self.primitives.append(Bezier('text-1-0-0-1-0',Point(*(16.005902, 12.354073)),Point(*(15.756454, 12.0)),(((16.005902, 12.15852), (15.894223, 12.0), (15.756454, 12.0)),)))
        self.add_line('text-1-0-0-2-0',(15.756454, 12.0),(14.0, 12.0))
        self.add_line('text-1-0-1-0-0',(14.0, 24.0),(18.0, 24.0))

