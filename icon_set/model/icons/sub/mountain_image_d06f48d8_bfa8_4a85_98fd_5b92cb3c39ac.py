"""Mountain Image: A pointed mountain peak rises between two diagonal slopes, with a tiny sun dot positioned above and to its left. Generate this component alone; exclude Wavy Frame.

Construction: The source open peaked ridge and small upper-left sun remain unclosed.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd06f48d8-bfa8-4a85-98fd-5b92cb3c39ac'
SOURCE_PATH = 'pictographic-primitives/state/image 2_d06f48d8-bfa8-4a85-98fd-5b92cb3c39ac.svg'
AUTHOR = 'gpt-6'


class MountainImage(Sub32):
    icon_id = 'mountain-image'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('mountain', 'image', 'pointed', 'peak', 'rises', 'between', 'diagonal', 'slopes')

    def build(self):
        self.add_polyline('ridge',(2,28),(18,8),(30,22))
        self.add_dot('sun',(5,4))
