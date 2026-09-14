"""Ar Letters Underlined. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide type: continuous letter strokes; supplied source determines the case and underline.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a642d559-a61c-4224-b0ae-b1681b0be69e'
SOURCE_PATH = 'pictographic-primitives/symbol/ar (text u)_a642d559-a61c-4224-b0ae-b1681b0be69e.svg'
AUTHOR = 'gpt-6'


class ArLettersUnderlined(Solo48):
    icon_id = 'ar-letters-underlined'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('ar', 'letters', 'text', 'underline', 'language', 'arabic', 'typography', 'abbreviation')

    def build(self) -> None:
        self.add_polyline('a-arch', (6, 32), (6, 24), (10, 8), (14, 8), (18, 24), (20, 32))
        self.add_line('a-bar', (6, 24), (18, 24))
        self.relate("connect", 'a-arch', 'a-bar')
        self.add_line('underline', (6, 40), (42, 40))
        self.add_polyline('r-stem', (32, 32), (32, 24), (32, 18))
        self.add_arc('r-arch', (32, 24), (42, 24), radius_x=6, radius_y=6, sweep=True)
        self.relate("connect", 'r-stem', 'r-arch')
