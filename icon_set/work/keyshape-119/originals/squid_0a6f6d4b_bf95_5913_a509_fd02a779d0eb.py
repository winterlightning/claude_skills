"""Diagonal squid with pointed mantle and two streaming tentacles. Bounds (6,6)-(42,42). No useful local squid match; coherent sweeping arcs, intentional diagonal asymmetry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a6f6d4b-bf95-5913-a509-fd02a779d0eb'
SOURCE_PATH = 'pictographic-primitives/animals/squid_0a6f6d4b-bf95-5913-a509-fd02a779d0eb.svg'
AUTHOR = 'gpt-6'


class SwimmingSquid(Solo48):
    icon_id = 'swimming-squid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('squid', 'sea', 'ocean', 'marine', 'cephalopod', 'tentacles', 'swim', 'calamari')

    def build(self) -> None:
        self.add_arc('left-hook',(6,28),(8,34),radius_x=6,sweep=False)
        self.add_arc('left-arm',(8,34),(22,26),radius_x=18,sweep=False)
        self.add_line('left-fin-notch',(22,26),(20,24))
        self.add_arc('mantle-left',(20,24),(42,6),radius_x=32,sweep=True)
        self.add_arc('mantle-right',(42,6),(30,32),radius_x=38,sweep=True)
        self.add_line('right-fin-notch',(30,32),(28,30))
        self.add_arc('right-arm',(28,30),(22,40),radius_x=14,sweep=False)
        self.add_arc('right-hook',(22,40),(28,42),radius_x=6,sweep=False)
        self.add_contour('squid','left-hook','left-arm','left-fin-notch','mantle-left','mantle-right','right-fin-notch','right-arm','right-hook')
