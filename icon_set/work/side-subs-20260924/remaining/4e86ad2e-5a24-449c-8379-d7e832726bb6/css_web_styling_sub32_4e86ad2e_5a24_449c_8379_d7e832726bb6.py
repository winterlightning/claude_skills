"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '4e86ad2e-5a24-449c-8379-d7e832726bb6'
SOURCE_PATH = 'pictographic-primitives/symbol/CSS (text)_4e86ad2e-5a24-449c-8379-d7e832726bb6.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('uppercase C', 'two uppercase S characters in one row')

class Drawing(Sub32):
    icon_id = 'css-web-styling-sub32'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('css', 'web', 'styling', 'symbol')
    STROKE_WIDTH = 4
    PATH_STROKE_WIDTHS = {}
    COMPACT_EXCEPTION = 'User requested uniform 4px strokes on a 32px canvas. Spacing and grid findings are retained for review.'
    def to_record(self):
        record=super().to_record()
        record['style']['path_stroke_widths']=dict(self.PATH_STROKE_WIDTHS)
        record['compact_exception']=self.COMPACT_EXCEPTION
        return record

    TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-s-uppercase', 'letter-s-uppercase')

    def build(self):
        self.primitives.append(Bezier('text-C-0-0-0-0',Point(*(8.0, 11.757359)),Point(*(8.0, 20.242641)),(((6.996825, 10.044832), (5.480406, 9.52991), (4.169694, 10.456723)), ((2.858982, 11.383536), (2.0, 13.578121), (2.0, 16.0)), ((2.0, 18.421879), (2.858982, 20.616464), (4.169694, 21.543277)), ((5.480406, 22.47009), (6.996825, 21.955168), (8.0, 20.242641)))))
        self.primitives.append(Bezier('text-S-1-0-0-0',Point(*(18.752051, 11.629415)),Point(*(13.239669, 12.890121)),(((18.033044, 9.423179), (13.719006, 9.108002), (13.239669, 12.890121)),)))
        self.primitives.append(Bezier('text-S-1-0-1-0',Point(*(13.239669, 12.890121)),Point(*(18.991719, 18.563299)),(((12.760331, 16.67224), (18.752051, 14.781181), (18.991719, 18.563299)),)))
        self.primitives.append(Bezier('text-S-1-0-2-0',Point(*(18.991719, 18.563299)),Point(*(13.0, 20.139182)),(((19.231388, 22.660595), (14.198344, 22.975771), (13.0, 20.139182)),)))
        self.primitives.append(Bezier('text-S-2-0-0-0',Point(*(29.752051, 11.629415)),Point(*(24.239669, 12.890121)),(((29.033044, 9.423179), (24.719006, 9.108002), (24.239669, 12.890121)),)))
        self.primitives.append(Bezier('text-S-2-0-1-0',Point(*(24.239669, 12.890121)),Point(*(29.991719, 18.563299)),(((23.760331, 16.67224), (29.752051, 14.781181), (29.991719, 18.563299)),)))
        self.primitives.append(Bezier('text-S-2-0-2-0',Point(*(29.991719, 18.563299)),Point(*(24.0, 20.139182)),(((30.231388, 22.660595), (25.198344, 22.975771), (24.0, 20.139182)),)))

