"""Two closed umbrellas stand upright inside a tapered open-topped holder with a rounded base. Their hooked handles face outward, while the narrow folded canopies protrude above the holder.

Reduced folded canopies to straight stems; retained opposed hooks and broad umbrella holder.
Construction reference: No useful exact local match; matched handle arcs and symmetric holder.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '86dfb48d-ca2a-48b0-a33d-7a0d24a14ec8'
SOURCE_PATH = 'pictographic-primitives/weather/rain umbrella case_86dfb48d-ca2a-48b0-a33d-7a0d24a14ec8.svg'
AUTHOR = 'gpt-6'

class UmbrellaStand(Solo48):
    icon_id = 'umbrella-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('umbrella', 'stand', 'holder', 'rain', 'storage', 'entrance')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('holder', (8, 27), (13, 44), (35, 44), (40, 27), closed=True)
        self.add_line('left-shaft', (17, 8), (17, 27))
        self.add_arc('left-hook', (17, 8), (9, 8), radius_x=4, radius_y=4, sweep=False, large_arc=False)
        self.relate('connect', 'left-shaft', 'left-hook')
        self.relate('connect', 'holder', 'left-shaft')
        self.add_line('right-shaft', (31, 8), (31, 27))
        self.add_arc('right-hook', (31, 8), (39, 8), radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.relate('connect', 'right-shaft', 'right-hook')
        self.relate('connect', 'holder', 'right-shaft')
