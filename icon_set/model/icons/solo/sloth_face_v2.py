# Variant of sloth-face; parent file remains unchanged.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ad97e11-bd58-4d42-a0e0-51be7206e42e'
SOURCE_PATH = 'pictographic-primitives/animals/sloth_1ad97e11-bd58-4d42-a0e0-51be7206e42e.svg'
AUTHOR = 'gpt-6'

class SlothFaceVariant2(Solo48):
    icon_id = 'sloth-face-v2'
    variant_of = 'sloth-face'
    variant_label = 'Circular face'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('sloth', 'face', 'head', 'eyes', 'animal', 'slow', 'cute', 'wildlife')

    def build(self) -> None:
        # Circular face: radius 22 about (24, 24), extremes (2, 2)-(46, 46).
        self.add_arc('head0', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('head1', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('head2', (46, 24), (24, 46), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('head3', (24, 46), (2, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_contour('head', 'head0', 'head1', 'head2', 'head3', closed=True)
        self.add_arc('left-mask', (2, 24), (19, 17), radius_x=17, radius_y=10, sweep=False)
        self.add_dot('left-eye', (14, 30))
        self.add_arc('right-mask', (46, 24), (29, 17), radius_x=17, radius_y=10, sweep=True)
        self.add_dot('right-eye', (34, 30))
        self.relate('connect', 'head', 'left-mask')
        self.relate('connect', 'head', 'right-mask')
