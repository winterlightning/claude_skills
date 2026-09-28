"""A dog standing in its lean-to kennel.

SOLO48 SQUARE: visible (4, 4)-(44, 44), centerline (6, 6)-(42, 42).

Symbol plan: the kennel is a back wall at x=6 under a roof sloping from
(6,16) up to (42,6), over a floor at y=42. The dog stands on the floor in
side view, facing right: a level back from (16,28) to (32,28), a hind and a
front leg dropping to the floor (split floor nodes), a tail cocked up from
the rump, a neck rising to the head at (35,20), a long snout forward to the
right edge and a floppy ear hanging behind the head.
Revision: the rejected drawing's dog was a zigzag outline that did not read
(feedback: "dog"); the dog is now a simple side-view figure with legs,
tail, snout and ear.
Construction reference: no useful Lucide match (`dog` is a frontal face).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '176149f5-709e-4aea-827c-9e372966aa1a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__outdoors-dog-house/20260926T160211Z-thuan-mac-1/reference/outdoors dog house_176149f5-709e-4aea-827c-9e372966aa1a.svg'
AUTHOR = 'claude-opus-5-5'

FLOOR, WALL_X, ROOF_L, ROOF_R = 42, 6, (6, 16), (42, 6)
RUMP, SHOULDER = (16, 28), (32, 28)
TAIL, HEAD, SNOUT, EAR = (14, 22), (35, 20), (42, 23), (31, 24)


class Drawing(Solo48):
    icon_id = 'outdoors-dog-house'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('outdoors dog house', 'kennel')
    keywords = ('dog', 'kennel', 'dog house', 'pet', 'shelter', 'outdoors', 'animal')

    def build(self):
        self.add_line('roof', ROOF_L, ROOF_R)
        self.add_line('wall', (WALL_X, FLOOR), ROOF_L)
        self.add_contour('kennel', 'wall', 'roof')
        self.add_line('floor-a', (WALL_X, FLOOR), (RUMP[0], FLOOR))
        self.add_line('floor-b', (RUMP[0], FLOOR), (SHOULDER[0], FLOOR))
        self.add_line('floor-c', (SHOULDER[0], FLOOR), (42, FLOOR))
        self.add_contour('floor', 'floor-a', 'floor-b', 'floor-c')
        self.relate('connect', 'floor', 'kennel')
        self.add_line('tail', TAIL, RUMP)
        self.add_line('back', RUMP, SHOULDER)
        self.add_line('neck', SHOULDER, HEAD)
        self.add_line('snout', HEAD, SNOUT)
        self.add_contour('dog', 'tail', 'back', 'neck', 'snout')
        self.add_line('ear', HEAD, EAR)
        self.add_line('hind-leg', RUMP, (RUMP[0], FLOOR))
        self.add_line('front-leg', SHOULDER, (SHOULDER[0], FLOOR))
        for part in ('ear', 'hind-leg', 'front-leg'):
            self.relate('connect', part, 'dog')
        self.relate('connect', 'hind-leg', 'floor')
        self.relate('connect', 'front-leg', 'floor')
