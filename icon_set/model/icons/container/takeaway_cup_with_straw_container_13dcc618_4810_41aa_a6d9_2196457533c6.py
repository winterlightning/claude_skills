"""Broaden the tapered cup body, retaining the lid and straw.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = '13dcc618-4810-41aa-a6d9-2196457533c6'
SOURCE_PATH = 'pictographic-primitives/drinks/bubble tea_13dcc618-4810-41aa-a6d9-2196457533c6.svg'
AUTHOR = 'gpt-6'

class TakeawayCupWithStrawContainer(Container64):
    icon_id = 'takeaway-cup-with-straw-container'
    category = 'drinks'
    keyshape = Keyshape.VRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        poly('cup',(6,18),(58,18),(52,62),(12,62),closed=True)
        line('rim',(6,10),(58,10));line('straw',(32,2),(32,10));join('rim','straw')
        for x in (6,58):line(f'lid-{x}',(x,10),(x,18));join(f'lid-{x}','rim');join(f'lid-{x}','cup')
