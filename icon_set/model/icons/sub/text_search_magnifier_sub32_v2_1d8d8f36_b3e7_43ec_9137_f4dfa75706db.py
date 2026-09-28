"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.primitives import Bezier, Point
SOURCE_ICON_ID = '1d8d8f36-b3e7-43ec-9137-f4dfa75706db'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass t_1d8d8f36-b3e7-43ec-9137-f4dfa75706db.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circular magnifier lens', 'lower-right handle', 'uppercase T with source-style horizontal caps')

class Drawing(Sub32):
    variant_of = 'text-search-magnifier-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Text Search Magnifying Glass', 'core_parts': ['circular magnifier lens', 'lower-right handle', 'uppercase T with source-style horizontal caps'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Move the complete serif T inward to separate all caps from the magnifier circle.'}
    icon_id = 'text-search-magnifier-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('other', 'state', 'primitives-generate')
    keywords = ('text', 'search', 'magnifying', 'glass')
    TYPEFACE_GLYPH_IDS = ('letter-t-uppercase',)

    def build(self):
        self.circle('frame', 14, 14, 12)
        join = 14 + 12 / 2 ** 0.5
        self.add_line('handle', (join, join), (30, 30))
        self.relate('connect', 'handle', 'frame-bottom')
        self.add_line('glyph-T-bar', (8, 10), (20, 10))
        self.add_line('glyph-T-stem', (14, 10), (14, 20))
        self.add_line('serif-left', (8, 10), (8, 13))
        self.add_line('serif-right', (20, 10), (20, 13))
        self.add_line('serif-foot', (12, 20), (16, 20))
        self.relate('connect', 'glyph-T-bar', 'serif-left', 'serif-right', 'glyph-T-stem')
        self.relate('connect', 'glyph-T-stem', 'serif-foot')

    def circle(self, name, cx, cy, r):
        self.add_arc(name + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
        self.add_arc(name + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
        self.add_contour(name, name + '-top', name + '-bottom', closed=True)

    def _map_primitives(self, selector, point_map):
        from dataclasses import replace
        from icon_set.model.primitives import Point, Line, Bezier

        def point(p):
            x, y = point_map(p.x, p.y)
            return Point(int(x) if abs(x - round(x)) < 1e-06 else x, int(y) if abs(y - round(y)) < 1e-06 else y)
        result = []
        for p in self.primitives:
            if not selector(p.element_id):
                result.append(p)
                continue
            fields = dict(start=point(p.start), end=point(p.end))
            if isinstance(p, Bezier):
                fields['segments'] = tuple((tuple((point_map(*q) for q in segment)) for segment in p.segments))
            result.append(replace(p, **fields))
        self.primitives = result

# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'text-search-magnifier-sub32-v2': {'status': 'fixed',
                                    'date': '2026-09-24',
                                    'author': 'gpt-6',
                                    'source_icon_id': '1d8d8f36-b3e7-43ec-9137-f4dfa75706db',
                                    'failures_at_review': ['style/grid [handle]: start.x must be '
                                                           'an integer on grid 1, got '
                                                           '22.485281374238568',
                                                           'style/grid [handle]: start.y must be '
                                                           'an integer on grid 1, got '
                                                           '22.485281374238568',
                                                           'mic: parallel straight geometry could '
                                                           'not be checked: handle: non-integer '
                                                           'authored line',
                                                           'mic [frame]: frame and glyph-T-bar are '
                                                           '4.78845 apart on centerlines nearest '
                                                           '(24.0138, 7.38874)<->(20, 10); SUB32 '
                                                           'requires at least 6 (ink clearance 2) '
                                                           'unless the contact is declared with a '
                                                           'scoped `connect` relationship',
                                                           'mic [frame]: frame and handle are 0 '
                                                           'apart on centerlines nearest (22.4853, '
                                                           '22.4853)<->(22.4853, 22.4853); SUB32 '
                                                           'requires at least 6 (ink clearance 2) '
                                                           'unless the contact is declared with a '
                                                           'scoped `connect` relationship'],
                                    'variant': 'text-search-magnifier-sub32-v2-clean',
                                    'evidence': 'icon_set/work/side-subs-20260924/fix-25/1d8d8f36-b3e7-43ec-9137-f4dfa75706db'}}
