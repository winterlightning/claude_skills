"""An industrial barrel with projecting rims and two pairs of short reinforcing ribs.

Keyshape SQUARE: centerline extremes recorded in build below.
The supplied front-view barrel sets the construction. Lucide cylinder was inspected but its perspective ellipses are inappropriate here.
Hosting (compose.py): plus valid, heart valid, check valid.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class IndustrialStorageBarrel(Container64):
    icon_id = 'industrial-storage-barrel'
    keyshape = Keyshape.SQUARE
    aliases = ('storage-drum',)
    keywords = ('industrial', 'storage', 'barrel')

    def build(self) -> None:
        # SQUARE centerline extremes: (2,2)-(62,62).
        self.add_polyline("body", (8,2), (56,2), (56,62), (8,62), closed=True)
        for y, name in ((2,"rim-top"), (22,"rib-upper"), (42,"rib-lower"), (62,"rim-bottom")):
            self.add_line(name+"-left", (2,y), (8,y))
            self.add_line(name+"-right", (56,y), (62,y))
            self.relate("connect", "body", name+"-left")
            self.relate("connect", "body", name+"-right")
