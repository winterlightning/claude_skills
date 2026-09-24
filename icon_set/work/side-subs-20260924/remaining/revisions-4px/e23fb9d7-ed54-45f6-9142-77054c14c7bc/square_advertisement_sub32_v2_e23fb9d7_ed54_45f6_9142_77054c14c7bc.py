"""Complete source composition; see the accompanying visual and validation evidence."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.sub._base import Sub32
from icon_set.model.primitives import Bezier, Point
SOURCE_ICON_ID = 'e23fb9d7-ed54-45f6-9142-77054c14c7bc'
SOURCE_PATH = 'pictographic-primitives/other/rectangle ad text_e23fb9d7-ed54-45f6-9142-77054c14c7bc.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('rounded square frame', 'uppercase A', 'uppercase D')

class Drawing(Sub32):
    variant_of = 'square-advertisement-sub32'
    variant_label = 'Uniform 4px readability repair'
    REPAIR_PLAN = {'concept': 'Square Advertisement Icon', 'core_parts': ['rounded square frame', 'uppercase A', 'uppercase D'], 'flexible_parts': 'Coordinates and proportions only; no parts removed.', 'repair': 'Make both reused letters taller and slightly wider, with a distinct inter-letter gap.'}
    icon_id = 'square-advertisement-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('square', 'advertisement', 'icon')
    TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-d-uppercase')

    def build(self):
        self.box('frame', 2, 2, 30, 30, 2)
        self.add_line('text-A-0-0-0-0', (9.0, 22.0), (11.232143, 10.48))
        self.primitives.append(Bezier('text-A-0-0-1-0', Point(*(11.232143, 10.48)), Point(*(11.767857, 10.48)), (((11.410714, 9.84), (11.589286, 9.84), (11.767857, 10.48)),)))
        self.add_line('text-A-0-0-1-1', (11.767857, 10.48), (14.0, 22.0))
        self.add_contour('glyph-A-0-0-1', *['text-A-0-0-1-0', 'text-A-0-0-1-1'], closed=False)
        self.add_line('text-A-0-1-0-0', (9.982143, 16.88), (13.017857, 16.88))
        self.add_line('text-D-1-0-0-0', (18.0, 10.0), (20.0, 10.0))
        self.primitives.append(Bezier('text-D-1-0-0-1', Point(*(20.0, 10.0)), Point(*(20.0, 22.0)), (((24.0, 10.0), (24.0, 22.0), (20.0, 22.0)),)))
        self.add_contour('glyph-D-1-0-0', *['text-D-1-0-0-0', 'text-D-1-0-0-1'], closed=False)
        self.add_line('text-D-1-0-1-0', (20.0, 22.0), (18.0, 22.0))
        self.add_line('text-D-1-0-1-1', (18.0, 22.0), (18.0, 10.0))
        self.add_contour('glyph-D-1-0-1', *['text-D-1-0-1-0', 'text-D-1-0-1-1'], closed=False)
        self._map_primitives(lambda name: name.startswith('text-A'), lambda x, y: (7 + (x - 9) * 6 / 5, 7 + (y - 10) * 18 / 12))
        self._map_primitives(lambda name: name.startswith('text-D'), lambda x, y: (19 + (x - 18) * 6 / 5, 7 + (y - 10) * 18 / 12))

    def box(self, name, left, top, right, bottom, r):
        points = [(left + r, top), (right - r, top), (right, top + r), (right, bottom - r), (right - r, bottom), (left + r, bottom), (left, bottom - r), (left, top + r)]
        for i, a in enumerate(points):
            b = points[(i + 1) % 8]
            if i % 2:
                self.add_arc(f'{name}-{i}', a, b, radius_x=r)
            else:
                self.add_line(f'{name}-{i}', a, b)
        self.add_contour(name, *[f'{name}-{i}' for i in range(8)], closed=True)

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
