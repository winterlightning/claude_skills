"""Automotive Car Battery Unit: independently authored container.

Construction plan: Rectangular battery housing and two matching terminal tabs; no charge glyph.
Keyshape SQUARE; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/transportation/car battery_51dcd939-bf74-4e07-8d2a-7009bab5f793.svg. Lucide battery-charging original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 0, 64, 64).
Hosting measured with compose.py: plus passes, heart passes, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '51dcd939-bf74-4e07-8d2a-7009bab5f793'
SOURCE_PATH = 'pictographic-primitives/transportation/car battery_51dcd939-bf74-4e07-8d2a-7009bab5f793.svg'
AUTHOR = 'gpt-6'


class CarBatteryContainer(Container64):
    icon_id = 'car-battery-container'
    category = 'transportation'
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ('car', 'battery', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'body',2,10,62,62,4)
        for x in (10,42):
         poly(f'terminal-{x}',(x,10),(x,2),(x+12,2),(x+12,10));join('body',f'terminal-{x}')
