"""Rounded Mechanical Gear Wheel: independently authored container.

Construction plan: Eight repeated rounded teeth around a circular enclosure; one continuous outline, no hub absent from source.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/interface-essential/cog 1_3c5d9e7b-b736-46fd-9cd0-c46678889d84.svg. Lucide cog original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '3c5d9e7b-b736-46fd-9cd0-c46678889d84'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog 1_3c5d9e7b-b736-46fd-9cd0-c46678889d84.svg'
AUTHOR = 'gpt-6'


class RoundedGearContainer(Container64):
    icon_id = 'rounded-gear-container'
    category = 'interface-essential'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('rounded', 'gear', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        # One quarter owns its rounded tooth and recessed shoulder; rotate it.
        start=(26,8)
        quarter=[('A',(38,8),6,6,True),('A',(42,12),4,4,False),('L',(48,12)),('A',(52,16),4,4,True),('L',(52,22)),('A',(56,26),4,4,False)]
        commands=[]
        for k in range(4):
            for kind,(x,y),*args in quarter:
                for _ in range(k):x,y=64-y,x
                commands.append((kind,(x,y),*args))
        path(self,'gear',start,commands,True)
