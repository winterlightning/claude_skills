"""Increase oval height, preserving the wide elliptical bubble and lower-left tail.
Construction: shared body/attachment coordinates, integer grid, 4-unit stroke.
Lucide originals and atomic-debug references inspected for enclosure, handle and rounded-join construction.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse
SOURCE_ICON_ID = None
SOURCE_PATH = None
AUTHOR = 'gpt-6'

class OvalSpeechBubble(Container64):
    icon_id = 'oval-speech-bubble'
    keyshape = Keyshape.HRECT_XL
    aliases = ()
    keywords = ()

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate("connect",a,b)
        path(self,'outline',(2,30),[('A',(32,6),30,24,True),('A',(62,30),30,24,True),('A',(32,54),30,24,True),('A',(14,49),30,24,True),('L',(6,58)),('L',(8,44)),('A',(2,30),30,24,True)],True)
