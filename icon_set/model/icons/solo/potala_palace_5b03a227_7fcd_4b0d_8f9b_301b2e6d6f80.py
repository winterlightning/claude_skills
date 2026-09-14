"""Potala palace: reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b03a227-7fcd-4b0d-8f9b-301b2e6d6f80'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-03/potala palace tibet_5b03a227-7fcd-4b0d-8f9b-301b2e6d6f80.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'potala-palace'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('potala', 'palace', 'tibet', 'lhasa', 'fortress', 'monastery', 'landmark', 'heritage')

    def build(self):
        # HRECT_L centerline extremes (6,8)-(42,40).
        # Building owns silhouette and attached architecture; repeat pairs share axes.
        # Asymmetric terraced hillside; shared roof and wall junctions.
        self.add_polyline("outline", (6,30), (7,16), (14,16), (16,8), (28,8), (30,16), (34,16), (36,24), (40,24), (42,24), (42,36))
        self.add_line("central-roof", (14,16), (30,16))
        self.relate("connect", "central-roof", "outline")
        self.add_polyline("terraces", (6,30), (14,30), (16,36), (24,36), (24,40), (34,40))
        self.relate("connect", "terraces", "outline")
        self.add_line("central-wall", (36,24), (34,34))
        self.relate("connect", "central-wall", "outline")
        self.add_line("finial", (40,18), (40,24))
        self.relate("connect", "finial", "outline")
