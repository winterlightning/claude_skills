"""A square frame holds the letters IJ at its upper left and a short horizontal bar near its bottom left.

Plan: Square brand tile, IJ upper field and lower-left signature dash.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected file-text: sparse inner strokes within a frame.
Simplification: I serifs removed for clear letter spacing; fixed brand tile remains one subject.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '66cf9f40-4254-4619-ba1e-7b78e0914552'
SOURCE_PATH = 'pictographic-primitives/logos/intellij idea logo_66cf9f40-4254-4619-ba1e-7b78e0914552.svg'
AUTHOR = 'gpt-6'


class IntellijIdeaLogoSquare(Solo48):
    icon_id = 'intellij-idea-logo-square'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('intellij-idea', 'jetbrains', 'ide', 'logo', 'brand', 'developer', 'java')

    def build(self):
        self.add_polyline('frame',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_line('I',(16,15),(16,24))
        self.add_line('jt',(32,15),(32,20))
        self.add_arc('jb',(32,20),(24,20),radius_x=4)
        self.add_contour('J','jt','jb')
        self.add_line('dash',(16,34),(26,34))
