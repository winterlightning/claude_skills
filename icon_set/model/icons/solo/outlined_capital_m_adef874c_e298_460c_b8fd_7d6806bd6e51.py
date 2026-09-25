"""maya logo: standalone repair of supplied reference.

Plan: Full-height outlined capital M. Keyshape SQUARE.
Reduction: Opened diagonal bands and flattened lower valley while retaining outlined letter.
Construction references: local Lucide originals and atomic-debug: none.

All geometry is authored for SOLO48; earlier runs remain unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "adef874c-e298-460c-b8fd-7d6806bd6e51"
SOURCE_PATH = "pictographic-primitives/_uncategorized_27/maya logo_adef874c-e298-460c-b8fd-7d6806bd6e51.svg"
AUTHOR = "gpt-6"


class OutlinedCapitalM(Solo48):
    icon_id = 'outlined-capital-m'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("capital m", "maya logo")
    keywords = ("letter", "alphabet", "uppercase", "outlined")

    def build(self) -> None:
        axis = 24
        outer_left, inner_left = 6, 14
        outer_right, inner_right = 2 * axis - outer_left, 2 * axis - inner_left
        self.add_polyline(
            "letter-outline",
            (outer_left, 6), (15, 6), (axis, 21), (33, 6),
            (outer_right, 6), (outer_right, 42), (inner_right, 42),
            (inner_right, 29), (27, 38), (21, 38), (inner_left, 29),
            (inner_left, 42), (outer_left, 42), closed=True,
        )
