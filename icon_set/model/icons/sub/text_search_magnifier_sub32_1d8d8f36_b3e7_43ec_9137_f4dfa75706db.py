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
    category = 'primitives-generate'
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


# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'text-search-magnifier-sub32': {'status': 'fixed',
                                 'date': '2026-09-24',
                                 'author': 'gpt-6',
                                 'source_icon_id': '1d8d8f36-b3e7-43ec-9137-f4dfa75706db',
                                 'failures_at_review': ['style/grid [handle]: start.x must be an '
                                                        'integer on grid 1, got 22.485281374238568',
                                                        'style/grid [handle]: start.y must be an '
                                                        'integer on grid 1, got 22.485281374238568',
                                                        'style/grid [text-T-0-0-0-0]: start.x must '
                                                        'be an integer on grid 1, got 9.0',
                                                        'style/grid [text-T-0-0-0-0]: start.y must '
                                                        'be an integer on grid 1, got 7.0',
                                                        'style/grid [text-T-0-0-0-0]: end.x must '
                                                        'be an integer on grid 1, got 19.0',
                                                        'style/grid [text-T-0-0-0-0]: end.y must '
                                                        'be an integer on grid 1, got 7.0',
                                                        'style/grid [text-T-0-1-0-0]: start.x must '
                                                        'be an integer on grid 1, got 14.0',
                                                        'style/grid [text-T-0-1-0-0]: start.y must '
                                                        'be an integer on grid 1, got 7.0',
                                                        'style/grid [text-T-0-1-0-0]: end.x must '
                                                        'be an integer on grid 1, got 14.0',
                                                        'style/grid [text-T-0-1-0-0]: end.y must '
                                                        'be an integer on grid 1, got 21.0',
                                                        'mic: parallel straight geometry could not '
                                                        'be checked: handle: non-integer authored '
                                                        'line',
                                                        'mic [frame]: frame and serif-right are '
                                                        '3.39691 apart on centerlines nearest '
                                                        '(20.9899, 4.24695)<->(19, 7); SUB32 '
                                                        'requires at least 6 (ink clearance 2) '
                                                        'unless the contact is declared with a '
                                                        'scoped `connect` relationship',
                                                        'holes/pinches: 1 undersized holes; 0 '
                                                        'pinches',
                                                        'mic [frame]: frame and handle are 0 apart '
                                                        'on centerlines nearest (22.4853, '
                                                        '22.4853)<->(22.4853, 22.4853); SUB32 '
                                                        'requires at least 6 (ink clearance 2) '
                                                        'unless the contact is declared with a '
                                                        'scoped `connect` relationship'],
                                 'variant': 'text-search-magnifier-sub32-v2-clean',
                                 'evidence': 'icon_set/work/side-subs-20260924/fix-25/1d8d8f36-b3e7-43ec-9137-f4dfa75706db'}}
