"""Hang Glider, independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '46124d39-e8cc-47e1-a905-ab2eb126c524'
SOURCE_PATH = 'pictographic-primitives/sports/sport paragliding_46124d39-e8cc-47e1-a905-ab2eb126c524.svg'
AUTHOR = 'gpt-6'

class TriangularHangGliderVariant2(Solo48):
    icon_id = 'triangular-hang-glider-v2'
    variant_of = 'triangular-hang-glider'
    variant_label = 'Hole and centerline reconstruction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/sports'
    aliases = ()
    keywords = ('hang', 'glider', 'pilot', 'flight', 'wing', 'sport')

    def build(self) -> None:
        """Open the pilot head; nearest body point (38,38) sits exactly 4 ink units below its radius-3 ring."""

        def circle(n, x, y, r):
            self.add_arc(n + '-a', (x, y - r), (x, y + r), radius_x=r)
            self.add_arc(n + '-b', (x, y + r), (x, y - r), radius_x=r)
            self.add_contour(n, n + '-a', n + '-b', closed=True)

        def arc(n, a, b, r, ry=None, sweep=True):
            self.add_arc(n, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)

        def poly(n, *pts):
            for i, (a, b) in enumerate(zip(pts, pts[1:]), 1):
                self.add_line(f'{n}-{i}', a, b)
        axis = 24

        def mirror(p):
            return (2 * axis - p[0], p[1])
        self.add_polyline('wing', (4, 8), (44, 14), (27, 18), (10, 22), closed=True)
        self.add_line('support', (27, 18), (26, 34))
        circle('head', 38, 27, 3)
        self.add_polyline('pilot',(8,40),(17,33),(26,34),(35,38))
        self.add_polyline('pilot-upper',(35,38),(38,38),(42,40))
        self.relate('connect','pilot','pilot-upper')
        self.relate('connect', 'wing', 'support')
        self.relate('connect', 'support', 'pilot')
