"""Deepen the front message while preserving both speech tails and the rear bubble.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class DoubleSpeechBubblesVariant2(Container64):
    icon_id = 'double-speech-bubbles-v2'
    variant_of = 'double-speech-bubbles'
    variant_label = "Room for native 32-unit sub-icons"
    keyshape = Keyshape.SQUARE
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'front',(6,2),[('L',(46,2)),('A',(50,6),4,4,True),('L',(50,42)),('A',(46,46),4,4,True),('L',(22,46)),('L',(10,54)),('L',(10,46)),('L',(6,46)),('A',(2,42),4,4,True),('L',(2,6)),('A',(6,2),4,4,True)],True)
        path(self,'rear',(50,30),[('L',(58,30)),('A',(62,34),4,4,True),('L',(62,52)),('L',(58,52)),('L',(58,62)),('L',(44,54)),('L',(34,54)),('A',(30,50),4,4,True),('L',(30,46))]);join('front','rear')
