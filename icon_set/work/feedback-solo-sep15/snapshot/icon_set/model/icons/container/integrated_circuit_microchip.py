"""A square chip enclosure with two connector pins on each side.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide microchip informs rounded package corners and straight, attached pins; the reference supplies the square, eight-pin layout.
Hosting (compose.py): plus review, heart review, check review.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class IntegratedCircuitMicrochip(Container64):
    icon_id = 'integrated-circuit-microchip'
    keyshape = Keyshape.SQUARE
    aliases = ('processor-chip',)
    keywords = ('integrated', 'circuit', 'microchip')

    def build(self) -> None:
        # SQUARE centerline extremes: (2,2)-(62,62).
        self.add_line("package-0", (18, 12), (46, 12))
        self.add_arc("package-1", (46, 12), (52, 18), radius_x=6)
        self.add_line("package-2", (52, 18), (52, 46))
        self.add_arc("package-3", (52, 46), (46, 52), radius_x=6)
        self.add_line("package-4", (46, 52), (18, 52))
        self.add_arc("package-5", (18, 52), (12, 46), radius_x=6)
        self.add_line("package-6", (12, 46), (12, 18))
        self.add_arc("package-7", (12, 18), (18, 12), radius_x=6)
        self.add_contour("package", "package-0", "package-1", "package-2", "package-3", "package-4", "package-5", "package-6", "package-7", closed=True)
        for v in (22,42):
            for side,a,b in (("top",(v,2),(v,12)), ("bottom",(v,52),(v,62)), ("left",(2,v),(12,v)), ("right",(52,v),(62,v))):
                name=f"pin-{side}-{v}"
                self.add_line(name,a,b)
                self.relate("connect", "package", name)
