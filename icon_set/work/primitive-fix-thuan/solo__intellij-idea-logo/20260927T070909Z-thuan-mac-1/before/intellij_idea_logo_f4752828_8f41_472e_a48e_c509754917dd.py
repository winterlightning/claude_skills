"""A J-shaped curl hooks around a small ring at the left, beside a tall rounded vertical bar at the right.

Plan: Left J curl around a circular inset; independent right vertical bar.
Keyshape: SQUARE; exact SOLO48 envelope from the contract.
Construction reference: Previously inspected corner-down-right and at-sign: tangent curl and nested ring.
Simplification: Outlined J and vertical capsule reduce to monoline strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4752828-8f41-472e-a48e-c509754917dd'
SOURCE_PATH = 'pictographic-primitives/logos/intellijidea logo_f4752828-8f41-472e-a48e-c509754917dd.svg'
AUTHOR = 'gpt-6'


class IntellijIdeaLogo(Solo48):
    icon_id = 'intellij-idea-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('intellij-idea', 'jetbrains', 'ide', 'logo', 'brand', 'developer', 'java')

    def build(self):
        self.add_line('top',(6,6),(20,6))
        self.add_arc('shoulder',(20,6),(28,14),radius_x=8)
        self.add_line('side',(28,14),(28,26))
        self.add_arc('curl',(28,26),(12,42),radius_x=16)
        self.add_line('end',(12,42),(6,42))
        self.add_contour('J','top','shoulder','side','curl','end')
        self.add_arc('r1',(15,23),(9,23),radius_x=3)
        self.add_arc('r2',(9,23),(15,23),radius_x=3)
        self.add_contour('ring','r1','r2',closed=True)
        self.add_line('bar',(42,6),(42,42))
