"""Rounded card containing horizontal key with two downward teeth. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Rounded card containing horizontal key with two downward teeth. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Key: A round key bow sits on the right of a horizontal shaft, with two short teeth hanging downward near its left end. Generate this component alone; exclude Rounded Rectangle Frame.\n\nConstruction: A horizontal shaft joins the round right bow, with the two short downward teeth shown in the source.\nKeyshape: HRECT_S; final SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '8b4fe16b-01b4-4124-995d-f69a0724af25'
SOURCE_PATH = 'pictographic-primitives/state/key horizontal rectangle_8b4fe16b-01b4-4124-995d-f69a0724af25.svg'
AUTHOR = 'gpt-6'

class KeyState143Variant2(SourceFaithfulSideSub):
    icon_id = 'key-state-143-v2'
    variant_of = 'key-state-143'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives/shape'
    aliases = ()
    keywords = ('key', 'round', 'bow', 'sits', 'right', 'horizontal', 'shaft', 'short')
    keyshape = Keyshape.SQUARE
    canvas_width = 48
    canvas_height = 32

    def build(self):
        """Rounded card containing horizontal key with two downward teeth."""
        box(self, 'frame', 2, 2, 46, 30, 3)
        circle(self, 'bow', 33, 16, 6)
        self.add_line('shaft', (10, 16), (27, 16))
        self.relate('connect', 'shaft', 'bow')
        for i, x in enumerate([10, 18]):
            self.add_line('tooth' + str(i), (x, 16), (x, 20))
            self.relate('connect', 'tooth' + str(i), 'shaft')

def box(s, n, l, t, r, b, k=3):
    points = [(l + k, t), (r - k, t), (r, t + k), (r, b - k), (r - k, b), (l + k, b), (l, b - k), (l, t + k)]
    members = []
    for i, p in enumerate(points):
        q = points[(i + 1) % 8]
        name = f'{n}-{i}'
        if i % 2:
            s.add_arc(name, p, q, radius_x=k)
        else:
            s.add_line(name, p, q)
        members.append(name)
    s.add_contour(n, *members, closed=True)

def circle(s, n, cx, cy, r):
    s.add_arc(n + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
    s.add_arc(n + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
    s.add_contour(n, n + '-top', n + '-bottom', closed=True)
