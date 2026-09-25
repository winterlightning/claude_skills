"""Nanobot: A hexagonal robot body has a tiny central dot and two curved claw-like legs extending from its lower sides. Generate this component alone; exclude Circle Frame.

Construction: A hexagonal body with one dot has two open curved appendages attached low on its sides.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'e98db6d6-6f1e-4606-83b7-893ae0481377'
SOURCE_PATH = 'pictographic-primitives/state/circle nanobot_e98db6d6-6f1e-4606-83b7-893ae0481377.svg'
AUTHOR = 'gpt-6'


class NanobotSub(Sub32):
    icon_id = 'nanobot-sub'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('nanobot', 'hexagonal', 'robot', 'body', 'tiny', 'central', 'dot', 'curved')

    def build(self):
        self.add_polyline('body',(16,2),(26,8),(26,20),(16,26),(6,20),(6,8),closed=True)
        self.add_dot('centre',(16,14))
        self.add_arc('left-claw',(6,20),(6,30),radius_x=4,radius_y=5,sweep=False)
        self.add_arc('right-claw',(26,20),(26,30),radius_x=4,radius_y=5)
        self.relate('connect','body','left-claw')
        self.relate('connect','body','right-claw')
