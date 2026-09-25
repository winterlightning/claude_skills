"""Square envelope; opened the narrow wing/neck junction while preserving the directional silhouette.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
Lucide bird: reduction to a coherent wing silhouette; no exact subject match.
"""
# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur pteranodon_af2670c9-c3b2-595d-aceb-a0d1c1eeeb7c.svg'
AUTHOR = 'gpt-6'

class Pteranodon(Solo48):
    icon_id = 'pteranodon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('pteranodon', 'pterodactyl', 'dinosaur', 'flying', 'wings', 'prehistoric', 'reptile', 'jurassic')

    def build(self) -> None:
        self.add_polyline('silhouette', (6, 14), (25, 6), (21, 16), (25, 25), (33, 13), (42, 6), (39, 25), (39, 34), (30, 37), (20, 33), (6, 34), (15, 25), (11, 18), (6, 14), closed=True)
        self.add_polyline('head', (39, 25), (42, 24))
        self.relate('connect', 'silhouette', 'head')
        self.add_line('trailing-leg', (30, 37), (34, 42))
        self.relate('connect', 'silhouette', 'trailing-leg')
