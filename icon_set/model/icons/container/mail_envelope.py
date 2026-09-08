"""An envelope enclosure with four short corner folds.

HRECT_L: exact centerline extremes recorded in build.
Construction: Lucide mail, rectangular enclosure and diagonal folds. Source identity retained without extra decoration.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""

from ...keyshapes import Keyshape
from ._base import Container64


class MailEnvelope(Container64):
    icon_id = 'mail-envelope'
    keyshape = Keyshape.HRECT_L
    aliases = ('mail-envelope-icon',)
    keywords = ('mail', 'envelope')

    def build(self) -> None:
        # Centerline (2,10)-(62,54); crisp corners preserve the source.
        self.add_polyline('outline',(2,10),(62,10),(62,54),(2,54),closed=True)
        for name,a,b in [('nw',(2,10),(15,19)),('ne',(62,10),(49,19)),('sw',(2,54),(15,45)),('se',(62,54),(49,45))]:
            self.add_line(name,a,b)
            self.relate('connect','outline',name)
