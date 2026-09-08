"""Pentagon badge with five-point star and one stripe. Centerline extremes (2,2)-(46,46). Second stripe removed to give star room."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '901869c8-bdce-553a-afb2-859aca2f3363'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/pentagon usa_901869c8-bdce-553a-afb2-859aca2f3363.svg'
AUTHOR = 'gpt-6'

class PentagonWithStar(Solo48):
    icon_id = 'pentagon-with-star'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('pentagon', 'usa', 'defence', 'military', 'star', 'badge', 'government', 'emblem')

    def build(self) -> None:
        self.add_polyline('badge', (24, 2), (46, 18), (38, 46), (10, 46), (2, 18), closed=True)
        self.add_polyline('star', (24, 12), (27, 20), (35, 20), (29, 26), (31, 34), (24, 29), (17, 34), (19, 26), (13, 20), (21, 20), closed=True)
        self.add_line('stripe', (15, 40), (33, 40))
