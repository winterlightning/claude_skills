"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32
from ...primitives import Bezier, Point
SOURCE_ICON_ID = '485f3232-8803-4b14-8a22-76cf5241c606'
SOURCE_PATH = 'pictographic-primitives/state/arrow distance 2m_485f3232-8803-4b14-8a22-76cf5241c606.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('digit 2', 'uppercase M', 'horizontal double-headed arrow below text')

class Drawing(Sub32):
    icon_id = 'distance-two-meters-uppercase-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('two', 'meter', 'distance', 'arrow')
    TYPEFACE_GLYPH_IDS = ('digit-2', 'letter-m-uppercase')

    def build(self):
        self.add_line('text-2-0-0-0-0',(5, 2),(10.741796, 2))
        self.primitives.append(Bezier('text-2-0-0-0-1',Point(*(10.741796, 2)),Point(*(12.016864, 6.982953)),(((12.939008, 2), (13.823722, 5.457447), (12.016864, 6.982953)),)))
        self.add_contour('glyph-2-0-0-0',*['text-2-0-0-0-0', 'text-2-0-0-0-1'],closed=False)
        self.add_line('text-2-0-0-1-0',(12.016864, 6.982953),(6.448755, 11.68409))
        self.primitives.append(Bezier('text-2-0-0-2-0',Point(*(6.448755, 11.68409)),Point(*(5, 15.056965)),(((5.54145, 12.450121), (5, 13.710694), (5, 15.056965)),)))
        self.add_line('text-2-0-0-3-0',(5, 15.056965),(5, 15.316409))
        self.primitives.append(Bezier('text-2-0-0-3-1',Point(*(5, 15.316409)),Point(*(5.560222, 16)),(((5, 15.693935), (5.250829, 16), (5.560222, 16)),)))
        self.add_line('text-2-0-0-3-2',(5.560222, 16),(13, 16))
        self.add_contour('glyph-2-0-0-3',*['text-2-0-0-3-0', 'text-2-0-0-3-1', 'text-2-0-0-3-2'],closed=False)
        self.add_line('text-M-1-0-0-0',(19, 16),(19, 2))
        self.add_line('text-M-1-0-0-1',(19, 2),(23, 10.944444))
        self.add_line('text-M-1-0-0-2',(23, 10.944444),(27, 2))
        self.add_contour('glyph-M-1-0-0',*['text-M-1-0-0-0', 'text-M-1-0-0-1', 'text-M-1-0-0-2'],closed=False)
        self.add_line('text-M-1-0-1-0',(27, 2),(27, 16))

        self.add_line('shaft',(2,26),(30,26))
        self.add_polyline('left-head',(6,22),(2,26),(6,30))
        self.add_polyline('right-head',(26,22),(30,26),(26,30))
        self.relate('connect','shaft','left-head-1','left-head-2')
        self.relate('connect','shaft','right-head-1','right-head-2')


# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'distance-two-meters-uppercase-sub32': {'status': 'fixed',
                                         'date': '2026-09-24',
                                         'author': 'gpt-6',
                                         'source_icon_id': '485f3232-8803-4b14-8a22-76cf5241c606',
                                         'failures_at_review': ['style/grid [text-2-0-0-0-0]: '
                                                                'end.x must be an integer on grid '
                                                                '1, got 10.741796',
                                                                'style/grid [text-2-0-0-0-1]: '
                                                                'start.x must be an integer on '
                                                                'grid 1, got 10.741796',
                                                                'style/grid [text-2-0-0-0-1]: '
                                                                'end.x must be an integer on grid '
                                                                '1, got 12.016864',
                                                                'style/grid [text-2-0-0-0-1]: '
                                                                'end.y must be an integer on grid '
                                                                '1, got 6.982953',
                                                                'style/grid [text-2-0-0-1-0]: '
                                                                'start.x must be an integer on '
                                                                'grid 1, got 12.016864',
                                                                'style/grid [text-2-0-0-1-0]: '
                                                                'start.y must be an integer on '
                                                                'grid 1, got 6.982953',
                                                                'style/grid [text-2-0-0-1-0]: '
                                                                'end.x must be an integer on grid '
                                                                '1, got 6.448755',
                                                                'style/grid [text-2-0-0-1-0]: '
                                                                'end.y must be an integer on grid '
                                                                '1, got 11.68409',
                                                                'style/grid [text-2-0-0-2-0]: '
                                                                'start.x must be an integer on '
                                                                'grid 1, got 6.448755',
                                                                'style/grid [text-2-0-0-2-0]: '
                                                                'start.y must be an integer on '
                                                                'grid 1, got 11.68409',
                                                                'style/grid [text-2-0-0-2-0]: '
                                                                'end.y must be an integer on grid '
                                                                '1, got 15.056965',
                                                                'style/grid [text-2-0-0-3-0]: '
                                                                'start.y must be an integer on '
                                                                'grid 1, got 15.056965',
                                                                'style/grid [text-2-0-0-3-0]: '
                                                                'end.y must be an integer on grid '
                                                                '1, got 15.316409',
                                                                'style/grid [text-2-0-0-3-1]: '
                                                                'start.y must be an integer on '
                                                                'grid 1, got 15.316409',
                                                                'style/grid [text-2-0-0-3-1]: '
                                                                'end.x must be an integer on grid '
                                                                '1, got 5.560222',
                                                                'style/grid [text-2-0-0-3-2]: '
                                                                'start.x must be an integer on '
                                                                'grid 1, got 5.560222',
                                                                'style/grid [text-M-1-0-0-1]: '
                                                                'end.y must be an integer on grid '
                                                                '1, got 10.944444',
                                                                'style/grid [text-M-1-0-0-2]: '
                                                                'start.y must be an integer on '
                                                                'grid 1, got 10.944444',
                                                                'mic: parallel straight geometry '
                                                                'could not be checked: '
                                                                'text-2-0-0-0-0: non-integer '
                                                                'authored line',
                                                                'internal-spacing [glyph-M-1-0-0]: '
                                                                'text-M-1-0-0-0 and text-M-1-0-0-2 '
                                                                'have 0.25 units of ink clearance '
                                                                'over 4.4092 units; requires 2; '
                                                                'review required'],
                                         'variant': 'distance-two-meters-uppercase-sub32-clean',
                                         'evidence': 'icon_set/work/side-subs-20260924/fix-25/485f3232-8803-4b14-8a22-76cf5241c606'}}
