"""Protective Security Shield: independently authored container.

Construction plan: Crown-like upper edge joins one broad pointed shield bowl; keep the interior blank as in source.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/protection/shield_c3034182-8272-438e-bd25-32ee58c63442.svg. Lucide cross original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'c3034182-8272-438e-bd25-32ee58c63442'
SOURCE_PATH = 'pictographic-primitives/protection/shield_c3034182-8272-438e-bd25-32ee58c63442.svg'
AUTHOR = 'gpt-6'


class CrownTopShieldContainer(Container64):
    icon_id = 'crown-top-shield-container'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('crown', 'top', 'shield', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        path(self,'shield',(6,2),[('L',(18,10)),('L',(32,2)),('L',(46,10)),('L',(58,2)),('L',(58,30)),('A',(32,62),30,34,True),('A',(6,30),30,34,True),('L',(6,2))],True)
