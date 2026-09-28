"""Elastic load balance circle (programing), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5811619-4d2e-4d0e-bd82-0ceb97f8b687'
SOURCE_PATH = 'pictographic-primitives/programing/elastic load balance circle_b5811619-4d2e-4d0e-bd82-0ceb97f8b687.svg'
AUTHOR = 'gpt-6'

class ElasticLoadBalanceCircle(Solo48):
    icon_id = 'elastic-load-balance-circle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('elastic', 'load', 'balance', 'circle', 'programing')

    def build(self) -> None:
        # Circular root plus a repeated pair of circular branch nodes.
        # SQUARE extremes: root reaches x=6; branch circles reach x=42,y=6,42.
        def circle(name, x, y, radius):
            self.add_arc(name+'-a', (x-radius,y), (x+radius,y), radius_x=radius)
            self.add_arc(name+'-b', (x+radius,y), (x-radius,y), radius_x=radius)
            self.add_contour(name, name+'-a', name+'-b', closed=True)
        circle('root', 14, 24, 8)
        circle('middle', 38, 24, 3)
        self.add_line('middle-branch', (22,24), (35,24))
        self.relate('connect', 'root', 'middle-branch')
        self.relate('connect', 'middle', 'middle-branch')
        for name, y in [('upper',10), ('lower',38)]:
            circle(name, 38, y, 4)
            self.add_line(name+'-branch', (22,24), (34,y))
            self.relate('connect', 'root', name+'-branch')
            self.relate('connect', name, name+'-branch')
            self.relate('connect', 'middle-branch', name+'-branch')
        self.relate('connect', 'upper-branch', 'lower-branch')
