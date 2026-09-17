"""Takeaway Drink Cup with Straw: independently authored container.

Construction plan: Tapered cup, broad rim band and centered straight straw; no invented liquid decoration.
Keyshape VRECT_XL; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/drinks/bubble tea_13dcc618-4810-41aa-a6d9-2196457533c6.svg. Lucide cup-soda original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (4, 0, 60, 64).
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = '13dcc618-4810-41aa-a6d9-2196457533c6'
SOURCE_PATH = 'pictographic-primitives/drinks/bubble tea_13dcc618-4810-41aa-a6d9-2196457533c6.svg'
AUTHOR = 'gpt-6'


class TakeawayCupWithStrawContainer(Container64):
    icon_id = 'takeaway-cup-with-straw-container'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ('takeaway', 'cup', 'with', 'straw', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        poly('cup',(10,18),(54,18),(48,62),(16,62),closed=True)
        line('rim',(6,10),(58,10));line('straw',(32,2),(32,10));join('rim','straw')
        line('lid-left',(10,10),(10,18));line('lid-right',(54,10),(54,18))
        for n in ('lid-left','lid-right'):join(n,'rim');join(n,'cup')
