"""Stegosaurus facing right, with three broad dorsal plates. Centerlines (2,8)-(46,40). Plate silhouette replaces fine separated plates; two visible legs replace four."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4fef4df-3a16-50f0-b013-b0ef9ef619e3'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur stegosaurus_a4fef4df-3a16-50f0-b013-b0ef9ef619e3.svg'
AUTHOR = 'gpt-6'


class Stegosaurus(Solo48):
    icon_id = 'stegosaurus'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('stegosaurus', 'dinosaur', 'plates', 'spikes', 'prehistoric', 'jurassic', 'reptile', 'extinct')

    def build(self) -> None:
        self.add_polyline('upper', (2,33), (10,27), (12,16), (18,21), (20,8), (26,18), (32,11), (34,24), (39,23))
        self.add_arc('brow', (39,23), (46,30), radius_x=7)
        self.add_arc('nose', (46,30), (42,34), radius_x=4)
        self.add_line('chin', (42,34), (36,34))
        self.add_polyline('legs-belly', (36,34), (36,40), (29,40), (27,33), (19,33), (17,40), (10,40), (11,33), (2,33))
        self.add_contour('head', 'brow', 'nose', 'chin')
        self.relate('connect','upper','head')
        self.relate('connect','head','legs-belly')
        self.relate('connect','legs-belly','upper')
