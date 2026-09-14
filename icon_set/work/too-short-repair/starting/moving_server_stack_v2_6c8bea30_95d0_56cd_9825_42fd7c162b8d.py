# Variant of moving-server-stack; parent file remains unchanged.
"""Moving Server Stack; re-authored from the supplied visual reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6c8bea30-95d0-56cd-9825-42fd7c162b8d'
SOURCE_PATH = 'pictographic-primitives/websites/server migration_6c8bea30-95d0-56cd-9825-42fd7c162b8d.svg'
SOURCE_REFERENCES = ({'source_icon_id': '6c8bea30-95d0-56cd-9825-42fd7c162b8d', 'source_path': 'pictographic-primitives/websites/server migration_6c8bea30-95d0-56cd-9825-42fd7c162b8d.svg'},)
AUTHOR = 'gpt-6'

class MovingServerStackVariant2(Solo48):
    icon_id = 'moving-server-stack-v2'
    variant_of = 'moving-server-stack'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/technology'
    aliases = ()
    keywords = ('server', 'stack', 'migration', 'motion', 'hardware', 'data', 'hosting')

    def build(self) -> None:
        for n, y in enumerate((6, 23)):
            self.box(f'server-{n}', 8, y, 40, y + 10, r=5)
        for n, x in enumerate((14, 24, 34)):
            self.add_line(f'motion-{n}', (x, 42), (x, 44))

    def box(self, name, x0, y0, x1, y1, r=2, joins=()):
        points = [(x0 + r, y0), (x1 - r, y0), (x1, y0 + r), (x1, y1 - r), (x1 - r, y1), (x0 + r, y1), (x0, y1 - r), (x0, y0 + r)]
        members = []
        for i, p in enumerate(points):
            q = points[(i + 1) % 8]
            if i % 2:
                name_i = f'{name}-{i}'
                self.add_arc(name_i, p, q, radius_x=r)
                members.append(name_i)
            else:
                mid = [v for v in joins if v != p and v != q and (p[0] == q[0] == v[0] and min(p[1], q[1]) < v[1] < max(p[1], q[1]) or (p[1] == q[1] == v[1] and min(p[0], q[0]) < v[0] < max(p[0], q[0])))]
                run = [p] + sorted(mid, key=lambda v: (v[0] - p[0]) ** 2 + (v[1] - p[1]) ** 2) + [q]
                for j, (a, b) in enumerate(zip(run, run[1:])):
                    name_i = f'{name}-{i}-{j}'
                    self.add_line(name_i, a, b)
                    members.append(name_i)
        self.add_contour(name, *members, closed=True)
