"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.primitives import Bezier, Point
SOURCE_ICON_ID = '537f61ca-8ecd-4e15-bb46-ac683be40ccd'
SOURCE_PATH = 'pictographic-primitives/rating/ranking first_537f61ca-8ecd-4e15-bb46-ac683be40ccd.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('three podium blocks', 'taller central block', 'left block taller than right', 'numeral 1 on central block')

class Drawing(Sub32):
    variant_of = 'first-place-podium-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'First Place Winner Podium', 'core_parts': ['three podium blocks', 'taller central block', 'left block taller than right', 'numeral 1 on central block'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Widen the central podium and shorten the reused numeral so it separates from all podium edges.'}
    icon_id = 'first-place-podium-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'rating'
    categories = ('rating', 'state', 'other', 'primitives-generate')
    keywords = ('first', 'place', 'winner', 'podium')
    TYPEFACE_GLYPH_IDS = ('digit-1',)

    def build(self):
        self.add_line('base', (4, 28), (28, 28))
        self.add_arc('left-bottom', (4, 28), (2, 26), radius_x=2)
        self.add_line('left-side', (2, 26), (2, 16))
        self.add_arc('left-corner', (2, 16), (4, 14), radius_x=2)
        self.add_line('left-top', (4, 14), (11, 14))
        self.add_line('center-left', (11, 28), (11, 6))
        self.add_arc('center-tl', (11, 6), (13, 4), radius_x=2)
        self.add_line('center-top', (13, 4), (19, 4))
        self.add_arc('center-tr', (19, 4), (21, 6), radius_x=2)
        self.add_line('center-right', (21, 6), (21, 28))
        self.add_line('right-top', (21, 16), (28, 16))
        self.add_arc('right-corner', (28, 16), (30, 18), radius_x=2)
        self.add_line('right-side', (30, 18), (30, 26))
        self.add_arc('right-bottom', (30, 26), (28, 28), radius_x=2)
        self.relate('connect', 'base', 'center-left', 'center-right')
        self.relate('connect', 'left-top', 'center-left')
        self.relate('connect', 'right-top', 'center-right')
        self.add_line('text-1-0-0-0-0', (16.005902, 23.90522), (16.005902, 12.354073))
        self.primitives.append(Bezier('text-1-0-0-1-0', Point(*(16.005902, 12.354073)), Point(*(15.756454, 12.0)), (((16.005902, 12.15852), (15.894223, 12.0), (15.756454, 12.0)),)))
        self.add_line('text-1-0-0-2-0', (15.756454, 12.0), (14.0, 12.0))
        self.add_line('text-1-0-1-0-0', (14.0, 24.0), (18.0, 24.0))
        self._map_primitives(lambda name: not name.startswith('text-'), lambda x, y: (x - 2 if x in (11, 13) else x + 2 if x in (19, 21) else x, y))
        self._map_primitives(lambda name: name.startswith('text-'), lambda x, y: (x, 11 + (y - 12) * 10 / 12))

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
SUB32_FIX_RECORDS = {'first-place-podium-sub32-v2': {'status': 'fixed',
                                 'date': '2026-09-24',
                                 'author': 'gpt-6',
                                 'source_icon_id': '537f61ca-8ecd-4e15-bb46-ac683be40ccd',
                                 'failures_at_review': ['style/grid [text-1-0-0-0-0]: start.x must '
                                                        'be an integer on grid 1, got 16.005902',
                                                        'style/grid [text-1-0-0-0-0]: start.y must '
                                                        'be an integer on grid 1, got '
                                                        '20.921016666666667',
                                                        'style/grid [text-1-0-0-0-0]: end.x must '
                                                        'be an integer on grid 1, got 16.005902',
                                                        'style/grid [text-1-0-0-0-0]: end.y must '
                                                        'be an integer on grid 1, got '
                                                        '11.295060833333332',
                                                        'style/grid [text-1-0-0-1-0]: start.x must '
                                                        'be an integer on grid 1, got 16.005902',
                                                        'style/grid [text-1-0-0-1-0]: start.y must '
                                                        'be an integer on grid 1, got '
                                                        '11.295060833333332',
                                                        'style/grid [text-1-0-0-1-0]: end.x must '
                                                        'be an integer on grid 1, got 15.756454',
                                                        'style/grid [text-1-0-0-2-0]: start.x must '
                                                        'be an integer on grid 1, got 15.756454',
                                                        'mic: parallel straight geometry could not '
                                                        'be checked: text-1-0-0-0-0: non-integer '
                                                        'authored line',
                                                        'mic [center-left]: center-left and '
                                                        'text-1-0-0-2-0 are 5 apart on centerlines '
                                                        'nearest (9, 11)<->(14, 11); SUB32 '
                                                        'requires at least 6 (ink clearance 2) '
                                                        'unless the contact is declared with a '
                                                        'scoped `connect` relationship',
                                                        'mic [center-left]: center-left and '
                                                        'text-1-0-1-0-0 are 5 apart on centerlines '
                                                        'nearest (9, 21)<->(14, 21); SUB32 '
                                                        'requires at least 6 (ink clearance 2) '
                                                        'unless the contact is declared with a '
                                                        'scoped `connect` relationship',
                                                        'mic [text-1-0-0-0-0]: text-1-0-0-0-0 and '
                                                        'text-1-0-1-0-0 are 0.0789833 apart on '
                                                        'centerlines nearest (16.0059, '
                                                        '20.921)<->(16.0059, 21); SUB32 requires '
                                                        'at least 6 (ink clearance 2) unless the '
                                                        'contact is declared with a scoped '
                                                        '`connect` relationship'],
                                 'variant': 'first-place-podium-sub32-v2-clean',
                                 'evidence': 'icon_set/work/side-subs-20260924/fix-25/537f61ca-8ecd-4e15-bb46-ac683be40ccd'}}
