"""Long rounded password field enclosing two crosses and a lower underscore. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Long rounded password field enclosing two crosses and a lower underscore. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Password Characters: Two X-shaped password marks appear beside a short low underscore, arranged horizontally from left to right. Generate this component alone; exclude Capsule Frame.\n\nConstruction: Two small X marks are followed by a lower underscore, preserving all three source characters.\nKeyshape: HRECT_S; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b9ace82f-9c93-4337-ac44-7380ce0657f4'
SOURCE_PATH = 'pictographic-primitives/state/password_b9ace82f-9c93-4337-ac44-7380ce0657f4.svg'
AUTHOR = 'gpt-6'

class PasswordCharactersVariant2(SourceFaithfulSideSub):
    icon_id = 'password-characters-v2'
    variant_of = 'password-characters'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('password', 'characters', 'x', 'shaped', 'marks', 'appear', 'beside', 'short')
    keyshape = Keyshape.SQUARE
    canvas_width = 64
    canvas_height = 32

    def build(self):
        """Long rounded password field enclosing two crosses and a lower underscore."""
        box(self, 'frame', 2, 2, 62, 30, 7)
        for i, x in enumerate([14, 32]):
            self.add_line('a' + str(i), (x - 4, 12), (x + 4, 20))
            self.add_line('b' + str(i), (x + 4, 12), (x - 4, 20))
            self.relate('connect', 'a' + str(i), 'b' + str(i))
        self.add_line('underscore', (46, 21), (54, 21))

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
