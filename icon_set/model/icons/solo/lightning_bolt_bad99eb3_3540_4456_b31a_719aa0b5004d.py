"""A tall lightning bolt bends through two sharp zigzags, with a broad upper section and a long tapering lower point. Its outline encloses an otherwise empty interior.

Preserved angular silhouette and open interior.
Construction reference: No useful exact local match inspected; straight coherent polygon.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bad99eb3-3540-4456-b31a-719aa0b5004d'
SOURCE_PATH = 'pictographic-primitives/weather/bolt_bad99eb3-3540-4456-b31a-719aa0b5004d.svg'
AUTHOR = 'gpt-6'

class LightningBolt(Solo48):
    icon_id = 'lightning-bolt'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    categories = ('weather', 'primitives')
    aliases = ()
    keywords = ('lightning', 'bolt', 'electricity', 'storm', 'thunder', 'energy')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('bolt', (24, 4), (40, 4), (26, 20), (40, 20), (8, 44), (19, 27), (8, 27), closed=True)
