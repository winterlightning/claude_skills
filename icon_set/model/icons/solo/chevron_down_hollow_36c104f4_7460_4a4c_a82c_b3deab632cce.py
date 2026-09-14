"""Hollow Down Chevron. Retains all identifying parts, reconstructed on the integer grid.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide rotate-cw and undo-2: coherent arcs, open arrowheads and explicit shaft joins.
Mirrored subjects use paired coordinates; directional parts preserve their
intentional asymmetry. Geometry is authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '36c104f4-7460-4a4c-a82c-b3deab632cce'
SOURCE_PATH = 'pictographic-primitives/symbol/arrow down button_36c104f4-7460-4a4c-a82c-b3deab632cce.svg'
AUTHOR = 'gpt-6'


class ChevronDownHollow(Solo48):
    icon_id = 'chevron-down-hollow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('chevron', 'down', 'arrow', 'expand', 'hollow', 'dropdown', 'direction', 'button')

    def build(self) -> None:
        self.add_polyline('chevron', (4, 8), (24, 28), (44, 8), (44, 20), (24, 40), (4, 20), closed=True)
