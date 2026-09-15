"""Am Letters Underlined. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide type: continuous letter strokes; supplied source determines the case and underline.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e38cbfee-45cd-445c-978d-e64790667fa5'
SOURCE_PATH = 'pictographic-primitives/symbol/am (text u)_e38cbfee-45cd-445c-978d-e64790667fa5.svg'
AUTHOR = 'gpt-6'

class AmLettersUnderlinedVariant2(Solo48):
    icon_id = 'am-letters-underlined-v2'
    variant_of = 'am-letters-underlined'
    variant_label = 'Shared ink reconstruction'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbols/standalone'
    aliases = ()
    keywords = ('am', 'letters', 'text', 'underline', 'language', 'typography', 'abbreviation')

    def build(self) -> None:
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""
        self.add_polyline('a-arch', (4, 32), (4, 24), (10, 8), (14, 8), (18, 24), (20, 32))
        self.add_line('a-bar', (4, 24), (18, 24))
        self.relate('connect', 'a-arch', 'a-bar')
        self.add_line('underline', (4, 40), (44, 40))
        self.add_polyline('m-leg-0', (28, 31), (28, 24), (28, 20))
        self.add_arc('m-arch-0', (28, 24), (36, 24), radius_x=4, radius_y=4, sweep=True)
        self.add_line('m-down-0', (36, 24), (36, 31))
        self.add_contour('m-shoulder-0', 'm-arch-0', 'm-down-0')
        self.relate('connect', 'm-leg-0', 'm-shoulder-0')
        self.add_line('m-leg-1', (36, 24), (36, 20))
        self.add_arc('m-arch-1', (36, 24), (44, 24), radius_x=4, radius_y=4, sweep=True)
        self.add_line('m-down-1', (44, 24), (44, 31))
        self.add_contour('m-shoulder-1', 'm-arch-1', 'm-down-1')
        self.relate('connect', 'm-leg-1', 'm-shoulder-1')
        self.relate('connect', 'm-shoulder-0', 'm-leg-1')
        self.relate('connect', 'm-shoulder-0', 'm-shoulder-1')
