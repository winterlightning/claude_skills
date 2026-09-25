"""Tank wagon; authored directly on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bb5a229c-a87a-4aa2-a696-d97a47004bfa'
SOURCE_PATH = 'pictographic-primitives/transportation/railroad wagon_bb5a229c-a87a-4aa2-a696-d97a47004bfa.svg'
AUTHOR = 'gpt-6'

class TankWagon(Solo48):
    icon_id = 'tank-wagon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('tank wagon', 'tanker', 'rail car', 'railway', 'freight', 'fuel', 'wagon', 'train')

    def build(self):
        # Capsule tank with matched radius-11 ends, integral hatch and equally sized wheels. Preserve attached ladder. No useful Lucide tank-wagon match.
        self.add_line('top-1', (15, 12), (20, 12))
        self.add_line('top-2', (20, 12), (20, 8))
        self.add_line('top-3', (20, 8), (28, 8))
        self.add_line('top-4', (28, 8), (28, 12))
        self.add_line('top-5', (28, 12), (33, 12))
        self.add_arc('right', (33, 12), (33, 34), radius_x=11, radius_y=11, sweep=True)
        self.add_line('bottom', (33, 34), (15, 34))
        self.add_arc('left-bottom', (15, 34), (4, 23), radius_x=11, radius_y=11, sweep=True)
        self.add_arc('left-top', (4, 23), (15, 12), radius_x=11, radius_y=11, sweep=True)
        self.add_contour('tank', 'top-1', 'top-2', 'top-3', 'top-4', 'top-5', 'right', 'bottom', 'left-bottom', 'left-top', closed=True)
        self.add_polyline('ladder', (15, 12), (15, 23), (15, 34), closed=False)
        self.add_line('rung', (4, 23), (15, 23))
        self.relate("connect", 'ladder', 'tank')
        self.relate("connect", 'rung', 'tank')
        self.relate("connect", 'ladder', 'rung')
        self.add_arc('rear-a', (12, 37), (18, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('rear-b', (18, 37), (12, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('rear', 'rear-a', 'rear-b', closed=True)
        self.relate("connect", 'rear', 'tank')
        self.relate("connect", 'rear', 'ladder')
        self.add_arc('front-a', (30, 37), (36, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_arc('front-b', (36, 37), (30, 37), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('front', 'front-a', 'front-b', closed=True)
        self.relate("connect", 'front', 'tank')
