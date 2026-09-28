"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '4ad3b70a-dda9-4459-9ffe-2c5fe51ff206'
SOURCE_PATH = 'pictographic-primitives/state/arrow distance 2m_4ad3b70a-dda9-4459-9ffe-2c5fe51ff206.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('digit 2', 'lowercase m', 'horizontal double-headed arrow below text')

class Drawing(Sub32):
    icon_id = 'distance-two-meters-lowercase-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('two', 'meters', 'distance', 'arrow')
    TYPEFACE_GLYPH_IDS = ('digit-2', 'letter-m')

    def build(self):
        self.add_line('text-2-0-0-0-0',(3, 2),(8.741796, 2))
        self.primitives.append(Bezier('text-2-0-0-0-1',Point(*(8.741796, 2)),Point(*(10.016864, 6.982953)),(((10.939008, 2), (11.823722, 5.457447), (10.016864, 6.982953)),)))
        self.add_contour('glyph-2-0-0-0',*['text-2-0-0-0-0', 'text-2-0-0-0-1'],closed=False)
        self.add_line('text-2-0-0-1-0',(10.016864, 6.982953),(4.448755, 11.68409))
        self.primitives.append(Bezier('text-2-0-0-2-0',Point(*(4.448755, 11.68409)),Point(*(3, 15.056965)),(((3.54145, 12.450121), (3, 13.710694), (3, 15.056965)),)))
        self.add_line('text-2-0-0-3-0',(3, 15.056965),(3, 15.316409))
        self.primitives.append(Bezier('text-2-0-0-3-1',Point(*(3, 15.316409)),Point(*(3.560222, 16)),(((3, 15.693935), (3.250829, 16), (3.560222, 16)),)))
        self.add_line('text-2-0-0-3-2',(3.560222, 16),(11, 16))
        self.add_contour('glyph-2-0-0-3',*['text-2-0-0-3-0', 'text-2-0-0-3-1', 'text-2-0-0-3-2'],closed=False)
        self.add_line('text-m-0-0-0-0',(23, 9.595497),(23, 16))
        self.add_line('text-m-0-1-0-0',(17, 16),(17, 9.595497))
        self.primitives.append(Bezier('text-m-0-1-1-0',Point(*(17, 9.595497)),Point(*(19.999991, 6)),(((17, 7.609768), (18.34315, 6), (19.999991, 6)),)))
        self.primitives.append(Bezier('text-m-0-1-2-0',Point(*(19.999991, 6)),Point(*(23, 9.595497)),(((21.65685, 6), (23, 7.609768), (23, 9.595497)),)))
        self.primitives.append(Bezier('text-m-0-1-3-0',Point(*(23, 9.595497)),Point(*(25.999991, 6)),(((23, 7.609768), (24.34315, 6), (25.999991, 6)),)))
        self.primitives.append(Bezier('text-m-0-1-4-0',Point(*(25.999991, 6)),Point(*(29, 9.595497)),(((27.65685, 6), (29, 7.609768), (29, 9.595497)),)))
        self.add_line('text-m-0-1-4-1',(29, 9.595497),(29, 16))
        self.add_contour('glyph-m-0-1-4',*['text-m-0-1-4-0', 'text-m-0-1-4-1'],closed=False)

        self.add_line('shaft',(2,26),(30,26))
        self.add_polyline('left-head',(6,22),(2,26),(6,30))
        self.add_polyline('right-head',(26,22),(30,26),(26,30))
        self.relate('connect','shaft','left-head-1','left-head-2')
        self.relate('connect','shaft','right-head-1','right-head-2')

