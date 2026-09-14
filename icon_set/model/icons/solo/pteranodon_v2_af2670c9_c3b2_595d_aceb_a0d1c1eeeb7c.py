# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur pteranodon_af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c.svg'
AUTHOR = 'gpt-6'

class PteranodonVariant2(Solo48):
    icon_id = 'pteranodon-v2'
    variant_of = 'pteranodon'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/prehistoric'
    aliases = ()
    keywords = ('pteranodon', 'pterodactyl', 'dinosaur', 'flying', 'wings', 'prehistoric', 'reptile', 'jurassic')

    def build(self) -> None:
        self.add_polyline('silhouette', (6, 14), (25, 6), (19, 17), (25, 25), (33, 13), (42, 6), (39, 25), (39, 34), (30, 37), (20, 33), (6, 34), (15, 25), (11, 18), (6, 14), closed=True)
        self.add_polyline('head', (39, 25), (42, 24))
        self.relate('connect', 'silhouette', 'head')
        self.add_line('trailing-leg', (30, 37), (34, 42))
        self.relate('connect', 'silhouette', 'trailing-leg')
