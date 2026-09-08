"""An eight-pointed badge alternates cardinal tips and square shoulders.

Keyshape SQUARE: visible bounds (0, 0, 64, 64).
Lucide badge informs the balanced closed perimeter; the source determines the
geometric eight-point silhouette instead of Lucide scallops. Centerline
extremes (2,2)-(62,62). Tips retain deliberate corners softened by round joins.
Equivalent square shoulders use radius 3 quarter circles.
Hosting measured with compose.py: plus passes, heart passes, check does not pass.
"""
from ...keyshapes import Keyshape
from ._base import Container64


class EightPointedStarBadge(Container64):
    icon_id = 'eight-pointed-star-badge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('eight-point-badge',)
    keywords = ('badge', 'star', 'emblem', 'outline')

    def build(self) -> None:
        self.add_line('n-rise', (22, 12), (32, 2))
        self.add_line('n-fall', (32, 2), (42, 12))
        self.add_line('ne-top', (42, 12), (49, 12))
        self.add_arc('ne-corner', (49, 12), (52, 15), radius_x=3, radius_y=3, sweep=True)
        self.add_line('ne-side', (52, 15), (52, 22))
        self.add_line('e-rise', (52, 22), (62, 32))
        self.add_line('e-fall', (62, 32), (52, 42))
        self.add_line('se-side', (52, 42), (52, 49))
        self.add_arc('se-corner', (52, 49), (49, 52), radius_x=3, radius_y=3, sweep=True)
        self.add_line('se-bottom', (49, 52), (42, 52))
        self.add_line('s-rise', (42, 52), (32, 62))
        self.add_line('s-fall', (32, 62), (22, 52))
        self.add_line('sw-bottom', (22, 52), (15, 52))
        self.add_arc('sw-corner', (15, 52), (12, 49), radius_x=3, radius_y=3, sweep=True)
        self.add_line('sw-side', (12, 49), (12, 42))
        self.add_line('w-rise', (12, 42), (2, 32))
        self.add_line('w-fall', (2, 32), (12, 22))
        self.add_line('nw-side', (12, 22), (12, 15))
        self.add_arc('nw-corner', (12, 15), (15, 12), radius_x=3, radius_y=3, sweep=True)
        self.add_line('nw-top', (15, 12), (22, 12))
        self.add_contour('outline', 'n-rise', 'n-fall', 'ne-top', 'ne-corner', 'ne-side', 'e-rise', 'e-fall', 'se-side', 'se-corner', 'se-bottom', 's-rise', 's-fall', 'sw-bottom', 'sw-corner', 'sw-side', 'w-rise', 'w-fall', 'nw-side', 'nw-corner', 'nw-top', closed=True)
