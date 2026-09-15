'Human construction repair. Remove the short gun-stock overhang trapping a pinch against the bent arm. Rebalance outlined shoulders: nearest shoulder point is 8u below the head outline.\nShared reference: icon_set/references/human_ref/full_body_ref.png; busts use human_ref/user.svg.\nLucide person-standing original and atomic-debug inform shared limb junctions. Preserve intentional action-pose asymmetry.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3025dd06-abf8-561c-a34e-645334e08f61'
SOURCE_PATH = 'pictographic-primitives/recreation/hunting_3025dd06-abf8-561c-a34e-645334e08f61.svg'
AUTHOR = 'gpt-6'
HUMAN_CONSTRUCTION = 'outlined-body'

class BirdHunterVariant2(Solo48):
    icon_id = 'bird-hunter-v2'
    variant_of = 'bird-hunter'
    variant_label = 'Correct human head and torso construction'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/recreation'
    aliases = ()
    keywords = ('bird', 'hunter')

    def build(self):
        self.add_arc('head-top', (32, 22), (38, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (38, 22), (32, 22), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('torso-1', (31, 42), (31, 34))
        self.add_line('torso-2', (31, 34), (35, 33))
        self.add_line('torso-3', (35, 33), (42, 37))
        self.add_line('torso-4', (42, 37), (42, 42))
        self.add_line('arms-1', (31, 34), (23, 37))
        self.add_line('arms-2', (23, 37), (17, 29))
        self.add_line('gun-1', (6, 23), (17, 29))
        self.add_line('bird-1', (6, 6), (13, 12))
        self.add_line('bird-2', (13, 12), (20, 6))
        self.add_contour('head', *('head-top', 'head-bottom'), closed=True)
        self.add_contour('torso', *('torso-1', 'torso-2', 'torso-3', 'torso-4'), closed=False)
        self.add_contour('arms', *('arms-1', 'arms-2'), closed=False)
        self.add_contour('gun', *('gun-1',), closed=False)
        self.add_contour('bird', *('bird-1', 'bird-2'), closed=False)
        self.relate('connect', *('arms', 'torso'))
        self.relate('connect', *('gun', 'arms'))
