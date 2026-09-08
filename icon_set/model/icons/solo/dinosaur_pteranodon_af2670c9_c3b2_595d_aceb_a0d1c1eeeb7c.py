"""Flying pteranodon: angular wings and backswept crest; intentionally directional. Centerlines (2,5)-(46,43). Lucide bird informs a single wing contour; omit tiny toes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur pteranodon_af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c.svg'
AUTHOR = 'gpt-6'


class Pteranodon(Solo48):
    icon_id = 'pteranodon'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('pteranodon', 'pterodactyl', 'dinosaur', 'flying', 'wings', 'prehistoric', 'reptile', 'jurassic')

    def build(self) -> None:
        self.add_polyline('silhouette', (2,14), (25,5), (19,17), (25,25), (33,13), (46,5), (39,25), (39,34), (30,37), (20,33), (2,34), (15,25), (11,18), (2,14), closed=True)
        self.add_polyline('head', (39,25), (46,24))
        self.relate('connect', 'silhouette', 'head')
        self.add_line('trailing-leg', (30,37), (34,43))
        self.relate('connect', 'silhouette', 'trailing-leg')
