"""Wavy image border, detached dot and original asymmetric mountain. Complete-source repair; previous variant preserved."""
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Wavy image border, detached dot and original asymmetric mountain. Complete-source repair; previous variant preserved.'
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
from icon_set.model.icons.sub._tall_base import SourceFaithfulSideSub
'Mountain Image: A pointed mountain peak rises between two diagonal slopes, with a tiny sun dot positioned above and to its left. Generate this component alone; exclude Wavy Frame.\n\nConstruction: The source open peaked ridge and small upper-left sun remain unclosed.\nKeyshape: HRECT_XL; authored to the SUB32 envelope.\n'
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd06f48d8-bfa8-4a85-98fd-5b92cb3c39ac'
SOURCE_PATH = 'pictographic-primitives/state/image 2_d06f48d8-bfa8-4a85-98fd-5b92cb3c39ac.svg'
AUTHOR = 'gpt-6'

class MountainImageVariant2(SourceFaithfulSideSub):
    icon_id = 'mountain-image-v2'
    variant_of = 'mountain-image'
    variant_label = 'Complete original restored on a proportionate canvas'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('mountain', 'image', 'pointed', 'peak', 'rises', 'between', 'diagonal', 'slopes')
    keyshape = Keyshape.SQUARE
    canvas_width = 32
    canvas_height = 32

    def build(self):
        """Wavy image border, detached dot and original asymmetric mountain."""
        self.add_bezier('corner-tr', (26, 2), ((29, 2), (30, 3), (30, 6)))
        self.add_bezier('corner-br', (30, 26), ((30, 29), (29, 30), (26, 30)))
        self.add_bezier('corner-bl', (6, 30), ((3, 30), (2, 29), (2, 26)))
        self.add_bezier('corner-tl', (2, 6), ((2, 3), (3, 2), (6, 2)))
        self.add_bezier('s0-0', (6, 2), ((8, 2), (9, 4), (11, 4)))
        self.add_bezier('s0-1', (11, 4), ((13, 4), (14, 2), (16, 2)))
        self.add_bezier('s0-2', (16, 2), ((18, 2), (19, 4), (21, 4)))
        self.add_bezier('s0-3', (21, 4), ((23, 4), (24, 2), (26, 2)))
        self.add_bezier('s1-0', (30, 6), ((30, 8), (28, 9), (28, 11)))
        self.add_bezier('s1-1', (28, 11), ((28, 13), (30, 14), (30, 16)))
        self.add_bezier('s1-2', (30, 16), ((30, 18), (28, 19), (28, 21)))
        self.add_bezier('s1-3', (28, 21), ((28, 23), (30, 24), (30, 26)))
        self.add_bezier('s2-0', (26, 30), ((24, 30), (23, 28), (21, 28)))
        self.add_bezier('s2-1', (21, 28), ((19, 28), (18, 30), (16, 30)))
        self.add_bezier('s2-2', (16, 30), ((14, 30), (13, 28), (11, 28)))
        self.add_bezier('s2-3', (11, 28), ((9, 28), (8, 30), (6, 30)))
        self.add_bezier('s3-0', (2, 26), ((2, 24), (4, 23), (4, 21)))
        self.add_bezier('s3-1', (4, 21), ((4, 19), (2, 18), (2, 16)))
        self.add_bezier('s3-2', (2, 16), ((2, 14), (4, 13), (4, 11)))
        self.add_bezier('s3-3', (4, 11), ((4, 9), (2, 8), (2, 6)))
        self.add_contour('frame', 's0-0', 's0-1', 's0-2', 's0-3', 'corner-tr', 's1-0', 's1-1', 's1-2', 's1-3', 'corner-br', 's2-0', 's2-1', 's2-2', 's2-3', 'corner-bl', 's3-0', 's3-1', 's3-2', 's3-3', 'corner-tl', closed=True)
        self.add_dot('sun', (11, 11))
        self.add_polyline('mountain', (12, 22), (19, 12), (22, 18))

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
