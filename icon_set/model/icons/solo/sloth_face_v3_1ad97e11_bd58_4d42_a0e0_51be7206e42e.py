from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1ad97e11-bd58-4d42-a0e0-51be7206e42e'
SOURCE_PATH = 'pictographic-primitives/animals/sloth_1ad97e11-bd58-4d42-a0e0-51be7206e42e.svg'
AUTHOR = 'gpt-6'

class SlothFaceVariant3(Solo48):
    icon_id = 'sloth-face-v3'
    variant_of = 'sloth-face'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('sloth', 'face', 'head', 'eyes', 'animal', 'slow', 'cute', 'wildlife')

    def build(self) -> None:
        self.add_arc('head0', (6, 24), (24, 6), radius_x=22, radius_y=19, sweep=True)
        self.add_arc('head1', (24, 6), (42, 24), radius_x=22, radius_y=19, sweep=True)
        self.add_arc('head2', (42, 24), (24, 42), radius_x=22, radius_y=19, sweep=True)
        self.add_arc('head3', (24, 42), (6, 24), radius_x=22, radius_y=19, sweep=True)
        self.add_contour('head', 'head0', 'head1', 'head2', 'head3', closed=True)
        self.add_arc('left-mask', (6, 24), (19, 17), radius_x=17, radius_y=10, sweep=False)
        self.add_dot('left-eye', (17, 30))
        self.add_arc('right-mask', (42, 24), (29, 17), radius_x=17, radius_y=10, sweep=True)
        self.add_dot('right-eye', (31, 30))
        self.relate('connect', 'head', 'left-mask')
        self.relate('connect', 'head', 'right-mask')
