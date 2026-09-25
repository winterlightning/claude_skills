"""Next Playback: An outlined right-pointing triangle is followed by a detached right chevron of similar height. Generate this component alone; exclude Circle Frame.

Construction: A right triangle precedes a detached right chevron.
Keyshape: HRECT_XL; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '97e55857-e9a6-4c5f-83bf-abfd96b372ad'
SOURCE_PATH = 'pictographic-primitives/state/circle play forward_97e55857-e9a6-4c5f-83bf-abfd96b372ad.svg'
AUTHOR = 'gpt-6'


class NextPlayback(Sub32):
    icon_id = 'next-playback'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    aliases = ()
    keywords = ('next', 'playback', 'outlined', 'right', 'pointing', 'triangle', 'followed', 'detached')

    def build(self):
        self.add_polyline('triangle',(2,4),(16,16),(2,28),closed=True)
        self.add_polyline('chevron',(22,4),(30,16),(22,28))
