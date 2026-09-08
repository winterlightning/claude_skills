"""Potala palace: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b03a227-7fcd-4b0d-8f9b-301b2e6d6f80'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/potala palace tibet_5b03a227-7fcd-4b0d-8f9b-301b2e6d6f80.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'potala-palace'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('potala', 'palace', 'tibet', 'lhasa', 'fortress', 'monastery', 'landmark', 'heritage')

    def build(self):
        # Centerline extremes: (2,5)-(46,43); open, asymmetric stepped hillside.
        self.add_polyline("outline", (2,31), (5,17), (11,17), (12,11), (18,11), (20,5), (30,5), (32,11), (35,11), (37,22), (41,22), (44,22), (46,36))
        self.add_line("central-roof", (18,11), (32,11))
        self.relate("connect", "central-roof", "outline")
        self.add_polyline("terraces", (2,31), (14,31), (16,38), (24,38), (24,43), (36,43))
        self.relate("connect", "terraces", "outline")
        self.add_line("central-wall", (37,22), (35,35))
        self.relate("connect", "central-wall", "outline")
        self.add_line("flagpole", (41,14), (41,22))
        self.relate("connect", "flagpole", "outline")
