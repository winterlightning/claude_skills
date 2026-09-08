"""Frontal lioness with rounded ears, broad skull and a central nose stem above a rounded chin. Tiny nostrils omitted. Lucide cat informs bilateral contour and sparse face; mirrored about x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c615acac-5746-5d49-a79c-eebad9a2ebc2'
SOURCE_PATH = 'pictographic-primitives/animals/lioness_c615acac-5746-5d49-a79c-eebad9a2ebc2.svg'
AUTHOR = 'gpt-6'


class LionessFace(Solo48):
    icon_id = 'lioness-face'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('lioness', 'face', 'animal')

    def build(self) -> None:
        # HRECT_XL: authored to its exact SOLO48 centerline bounds.
        self.add_arc('crown-left', (18, 13), (24, 11), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('crown-right', (24, 11), (30, 13), radius_x=10, radius_y=6, sweep=True)
        self.add_arc('cheek-right', (30, 13), (40, 25), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('jaw-right', (40, 25), (24, 43), radius_x=16, radius_y=18, sweep=True)
        self.add_arc('jaw-left', (24, 43), (8, 25), radius_x=16, radius_y=18, sweep=True)
        self.add_arc('cheek-left', (8, 25), (18, 13), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('head', 'crown-left', 'crown-right', 'cheek-right', 'jaw-right', 'jaw-left', 'cheek-left', closed=True)
        self.add_arc('ear-left-top', (18, 13), (2, 13), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('ear-left-low', (2, 13), (8, 25), radius_x=6, radius_y=12, sweep=False)
        self.add_contour('ear-left', 'ear-left-top', 'ear-left-low', closed=False)
        self.relate("connect", 'ear-left', 'head')
        self.add_arc('ear-right-top', (30, 13), (46, 13), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('ear-right-low', (46, 13), (40, 25), radius_x=6, radius_y=12, sweep=True)
        self.add_contour('ear-right', 'ear-right-top', 'ear-right-low', closed=False)
        self.relate("connect", 'ear-right', 'head')
        self.add_line('nose-1', (20, 26), (24, 30))
        self.add_line('nose-2', (24, 30), (28, 26))
        self.add_contour('nose', 'nose-1', 'nose-2', closed=False)
        self.add_line('philtrum', (24, 30), (24, 34))
        self.relate("connect", 'nose', 'philtrum')
