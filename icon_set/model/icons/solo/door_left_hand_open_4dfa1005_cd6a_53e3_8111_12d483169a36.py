'Open door: straight perspective edges, a balanced leaf and a clear handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4dfa1005-cd6a-53e3-8111-12d483169a36'
SOURCE_PATH = 'pictographic-primitives/building/door left hand open_4dfa1005-cd6a-53e3-8111-12d483169a36.svg'
AUTHOR = 'gpt-6'

class DoorLeftHandOpen(Solo48):
    icon_id = 'door-left-hand-open'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('door', 'left', 'hand', 'open', 'building')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('frame-1', (8, 44), (8, 4))
        self.add_line('frame-2', (8, 4), (40, 4))
        self.add_line('frame-3', (40, 4), (40, 44))
        self.add_line('leaf-1', (40, 4), (20, 12))
        self.add_line('leaf-2', (20, 12), (20, 36))
        self.add_line('leaf-3', (20, 36), (40, 44))
        self.add_line('knob', (30, 25), (30, 25))
        self.add_contour('frame', *('frame-1', 'frame-2', 'frame-3'), closed=False)
        self.add_contour('leaf', *('leaf-1', 'leaf-2', 'leaf-3'), closed=False)
        self.relate('connect', *('frame', 'leaf'))
