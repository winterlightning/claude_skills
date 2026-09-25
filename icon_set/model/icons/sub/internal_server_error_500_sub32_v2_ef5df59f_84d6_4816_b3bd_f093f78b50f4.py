"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.primitives import Bezier, Point
SOURCE_ICON_ID = 'ef5df59f-84d6-4816-b3bd-f093f78b50f4'
SOURCE_PATH = 'pictographic-primitives/symbol/500 ERROR_ef5df59f-84d6-4816-b3bd-f093f78b50f4.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('500 on upper row', 'ERROR on lower row', 'all eight source characters retained')

class Drawing(Sub32):
    variant_of = 'internal-server-error-500-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Five Hundred Internal Server Error', 'core_parts': ['500 on upper row', 'ERROR on lower row', 'all eight source characters retained'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Try a wider 500 row; the five-letter ERROR row remains constrained by the 32px width.'}
    icon_id = 'internal-server-error-500-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    keywords = ('five', 'hundred', 'internal', 'server', 'error')
    TYPEFACE_GLYPH_IDS = ('digit-5', 'digit-0', 'digit-0', 'letter-e-uppercase', 'letter-r-uppercase', 'letter-r-uppercase', 'letter-o-uppercase', 'letter-r-uppercase')

    def build(self):
        self.add_line('text-5-0-0-0-0', (11.576334, 2.0), (8.168258, 2.0))
        self.primitives.append(Bezier('text-5-0-0-1-0', Point(*(8.168258, 2.0)), Point(*(8.0, 2.291739)), (((8.075332, 2.0), (8.0, 2.130617), (8.0, 2.291739)),)))
        self.add_line('text-5-0-0-1-1', (8.0, 2.291739), (8.0, 5.878247))
        self.add_contour('glyph-5-0-0-1', *['text-5-0-0-1-0', 'text-5-0-0-1-1'], closed=False)
        self.primitives.append(Bezier('text-5-0-0-2-0', Point(*(8.0, 5.878247)), Point(*(8.168258, 6.169986)), (((8.0, 6.039369), (8.075332, 6.169986), (8.168258, 6.169986)),)))
        self.add_line('text-5-0-0-3-0', (8.168258, 6.169986), (10.315437, 6.169986))
        self.primitives.append(Bezier('text-5-0-0-4-0', Point(*(10.315437, 6.169986)), Point(*(11.526028, 11.107728)), (((11.798278, 6.169986), (12.554975, 9.256367), (11.526028, 11.107728)),)))
        self.primitives.append(Bezier('text-5-0-0-5-0', Point(*(11.526028, 11.107728)), Point(*(10.315437, 12.0)), (((11.209136, 11.677882), (10.772114, 12.0), (10.315437, 12.0)),)))
        self.add_line('text-5-0-0-6-0', (10.315437, 12.0), (8.186855, 12.0))
        self.primitives.append(Bezier('text-0-1-0-0-0', Point(*(14.0, 4.855153)), Point(*(18.0, 4.855153)), (((14.0, 4.09821), (14.210858, 3.371495), (14.585786, 2.836255)), ((14.960715, 2.301015), (15.46977, 2.0), (16.0, 2.0)), ((16.53023, 2.0), (17.039285, 2.301015), (17.414214, 2.836255)), ((17.789142, 3.371495), (18.0, 4.09821), (18.0, 4.855153)))))
        self.add_line('text-0-1-0-0-1', (18.0, 4.855153), (18.0, 9.144847))
        self.primitives.append(Bezier('text-0-1-0-0-2', Point(*(18.0, 9.144847)), Point(*(14.0, 9.144847)), (((18.0, 9.90179), (17.789142, 10.628505), (17.414214, 11.163745)), ((17.039285, 11.698985), (16.53023, 12.0), (16.0, 12.0)), ((15.46977, 12.0), (14.960715, 11.698985), (14.585786, 11.163745)), ((14.210858, 10.628505), (14.0, 9.90179), (14.0, 9.144847)))))
        self.add_line('text-0-1-0-0-3', (14.0, 9.144847), (14.0, 4.855153))
        self.add_contour('glyph-0-1-0-0', *['text-0-1-0-0-0', 'text-0-1-0-0-1', 'text-0-1-0-0-2', 'text-0-1-0-0-3'], closed=True)
        self.primitives.append(Bezier('text-0-2-0-0-0', Point(*(20.0, 4.855153)), Point(*(24.0, 4.855153)), (((20.0, 4.09821), (20.210858, 3.371495), (20.585786, 2.836255)), ((20.960715, 2.301015), (21.46977, 2.0), (22.0, 2.0)), ((22.53023, 2.0), (23.039285, 2.301015), (23.414214, 2.836255)), ((23.789142, 3.371495), (24.0, 4.09821), (24.0, 4.855153)))))
        self.add_line('text-0-2-0-0-1', (24.0, 4.855153), (24.0, 9.144847))
        self.primitives.append(Bezier('text-0-2-0-0-2', Point(*(24.0, 9.144847)), Point(*(20.0, 9.144847)), (((24.0, 9.90179), (23.789142, 10.628505), (23.414214, 11.163745)), ((23.039285, 11.698985), (22.53023, 12.0), (22.0, 12.0)), ((21.46977, 12.0), (20.960715, 11.698985), (20.585786, 11.163745)), ((20.210858, 10.628505), (20.0, 9.90179), (20.0, 9.144847)))))
        self.add_line('text-0-2-0-0-3', (20.0, 9.144847), (20.0, 4.855153))
        self.add_contour('glyph-0-2-0-0', *['text-0-2-0-0-0', 'text-0-2-0-0-1', 'text-0-2-0-0-2', 'text-0-2-0-0-3'], closed=True)
        self.add_line('text-E-0-0-0-0', (6.0, 20.0), (2.0, 20.0))
        self.add_line('text-E-0-0-0-1', (2.0, 20.0), (2.0, 30.0))
        self.add_line('text-E-0-0-0-2', (2.0, 30.0), (6.0, 30.0))
        self.add_contour('glyph-E-0-0-0', *['text-E-0-0-0-0', 'text-E-0-0-0-1', 'text-E-0-0-0-2'], closed=False)
        self.add_line('text-E-0-1-0-0', (2.0, 25.0), (5.272727, 25.0))
        self.add_line('text-R-1-0-0-0', (8.0, 30.0), (8.0, 20.0))
        self.add_line('text-R-1-0-0-1', (8.0, 20.0), (10.0, 20.0))
        self.primitives.append(Bezier('text-R-1-0-0-2', Point(*(10.0, 20.0)), Point(*(10.0, 25.277778)), (((12.461538, 20.0), (12.461538, 25.277778), (10.0, 25.277778)),)))
        self.add_contour('glyph-R-1-0-0', *['text-R-1-0-0-0', 'text-R-1-0-0-1', 'text-R-1-0-0-2'], closed=False)
        self.add_line('text-R-1-0-1-0', (10.0, 25.277778), (8.0, 25.277778))
        self.add_line('text-R-1-1-0-0', (10.0, 25.277778), (12.0, 30.0))
        self.add_line('text-R-2-0-0-0', (14.0, 30.0), (14.0, 20.0))
        self.add_line('text-R-2-0-0-1', (14.0, 20.0), (16.0, 20.0))
        self.primitives.append(Bezier('text-R-2-0-0-2', Point(*(16.0, 20.0)), Point(*(16.0, 25.277778)), (((18.461538, 20.0), (18.461538, 25.277778), (16.0, 25.277778)),)))
        self.add_contour('glyph-R-2-0-0', *['text-R-2-0-0-0', 'text-R-2-0-0-1', 'text-R-2-0-0-2'], closed=False)
        self.add_line('text-R-2-0-1-0', (16.0, 25.277778), (14.0, 25.277778))
        self.add_line('text-R-2-1-0-0', (16.0, 25.277778), (18.0, 30.0))
        self.primitives.append(Bezier('text-O-3-0-0-0', Point(*(20.0, 25.0)), Point(*(24.0, 25.0)), (((20.0, 23.674426), (20.210858, 22.401788), (20.585786, 21.464466)), ((20.960715, 20.527144), (21.46977, 20.0), (22.0, 20.0)), ((22.53023, 20.0), (23.039285, 20.527144), (23.414214, 21.464466)), ((23.789142, 22.401788), (24.0, 23.674426), (24.0, 25.0)))))
        self.primitives.append(Bezier('text-O-3-0-0-1', Point(*(24.0, 25.0)), Point(*(20.0, 25.0)), (((24.0, 26.325574), (23.789142, 27.598212), (23.414214, 28.535534)), ((23.039285, 29.472856), (22.53023, 30.0), (22.0, 30.0)), ((21.46977, 30.0), (20.960715, 29.472856), (20.585786, 28.535534)), ((20.210858, 27.598212), (20.0, 26.325574), (20.0, 25.0)))))
        self.add_contour('glyph-O-3-0-0', *['text-O-3-0-0-0', 'text-O-3-0-0-1'], closed=True)
        self.add_line('text-R-4-0-0-0', (26.0, 30.0), (26.0, 20.0))
        self.add_line('text-R-4-0-0-1', (26.0, 20.0), (28.0, 20.0))
        self.primitives.append(Bezier('text-R-4-0-0-2', Point(*(28.0, 20.0)), Point(*(28.0, 25.277778)), (((30.461538, 20.0), (30.461538, 25.277778), (28.0, 25.277778)),)))
        self.add_contour('glyph-R-4-0-0', *['text-R-4-0-0-0', 'text-R-4-0-0-1', 'text-R-4-0-0-2'], closed=False)
        self.add_line('text-R-4-0-1-0', (28.0, 25.277778), (26.0, 25.277778))
        self.add_line('text-R-4-1-0-0', (28.0, 25.277778), (30.0, 30.0))
        self._map_primitives(lambda name: name.startswith(('text-5', 'text-0')), lambda x, y: (2 + (x - 8) * 28 / 16, y))

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
