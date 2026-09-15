"""An elliptical speech enclosure with a lower-left tail.
Centerline extremes (2,10)-(62,54); landscape fit keeps the oval readable.
Lucide message-circle informs the integrated tail; elliptical arcs replace its
round body. Tail is deliberately asymmetric. No semantic features dropped.

Keyshape HRECT_L; authored directly on CONTAINER64. Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class OvalSpeechBubble(Container64):
    icon_id = 'oval-speech-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('oval', 'speech', 'bubble')

    def build(self) -> None:
        self.add_arc('upper-left',(2,30),(32,10),radius_x=30,radius_y=20)
        self.add_arc('upper-right',(32,10),(62,30),radius_x=30,radius_y=20)
        self.add_arc('lower-right',(62,30),(32,50),radius_x=30,radius_y=20)
        self.add_arc('shoulder',(32,50),(14,46),radius_x=30,radius_y=20)
        self.add_line('tail-out',(14,46),(6,54))
        self.add_line('tail-in',(6,54),(8,42))
        self.add_arc('lower-left',(8,42),(2,30),radius_x=30,radius_y=20)
        self.add_contour('outline','upper-left','upper-right','lower-right','shoulder','tail-out','tail-in','lower-left',closed=True)
