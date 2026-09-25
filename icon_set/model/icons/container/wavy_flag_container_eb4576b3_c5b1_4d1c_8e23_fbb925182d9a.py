"""Simple Wavy Flag: independently authored container.

Construction plan: Two matching smooth wave edges joined by upright sides; no pole beyond the source flag.
Keyshape HRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/social/flag 1_eb4576b3-c5b1-4d1c-8e23-fbb925182d9a.svg. Lucide flag original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 4, 64, 60).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'eb4576b3-c5b1-4d1c-8e23-fbb925182d9a'
SOURCE_PATH = 'pictographic-primitives/social/flag 1_eb4576b3-c5b1-4d1c-8e23-fbb925182d9a.svg'
AUTHOR = 'gpt-6'


class WavyFlagContainer(Container64):
    icon_id = 'wavy-flag-container'
    category = 'social'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ('wavy', 'flag', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'flag',(2,10),[('A',(32,10),15,4,True),('A',(62,10),15,4,False),('L',(62,54)),('A',(32,54),15,4,True),('A',(2,54),15,4,False),('L',(2,10))],True)
