"""Arched speedometer with three ticks and diagonal needle.
HRECT_L (4,8)-(44,40) fits the broad dashboard dial. Shared shell nodes own
ticks; the hub owns the needle attachment. Lucide gauge informs minimal
needle/dial hierarchy. Source contributes closed base and hub. Reduce five
detached ticks to three attached ticks for native readability.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "951456f0-7a11-4ecc-b29c-400594778716"
SOURCE_PATH = "pictographic-primitives/_uncategorized_28/odometer_951456f0-7a11-4ecc-b29c-400594778716.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "arched-speedometer"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport"
    aliases = ("Dashboard Speedometer Gauge",)
    keywords = ("speedometer", "gauge", "dial", "needle", "speed", "dashboard")
    def build(self):
        self.add_arc("arch-left",(4,28),(24,8),radius_x=20)
        self.add_arc("arch-right",(24,8),(44,28),radius_x=20)
        self.add_line("wall-right",(44,28),(44,36))
        self.add_arc("corner-right",(44,36),(40,40),radius_x=4)
        self.add_line("base",(40,40),(8,40))
        self.add_arc("corner-left",(8,40),(4,36),radius_x=4)
        self.add_line("wall-left",(4,36),(4,28))
        self.add_contour("dial","arch-left","arch-right","wall-right","corner-right","base","corner-left","wall-left",closed=True)
        for name,a,b,parts in [
            ('tick-top',(24,8),(24,12),('arch-left','arch-right')),
            ('tick-left',(4,28),(8,28),('arch-left','wall-left')),
            ('tick-right',(44,28),(40,28),('arch-right','wall-right'))]:
            self.add_line(name,a,b)
            self.relate('connect',name,*parts)
        self.add_arc('hub-upper',(27,28),(21,28),radius_x=3,sweep=False)
        self.add_arc('hub-lower',(21,28),(27,28),radius_x=3,sweep=False)
        self.add_contour('hub','hub-upper','hub-lower',closed=True)
        self.add_line('needle',(27,28),(33,22))
        self.relate('connect','needle','hub-upper','hub-lower')
