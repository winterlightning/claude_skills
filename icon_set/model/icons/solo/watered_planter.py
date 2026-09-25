# Review candidate; original preserved.
"""A water droplet above leafy foliage in a shallow bowl; leaf veins omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '10782152-f13b-462f-8c54-0579748cb38a'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 1_10782152-f13b-462f-8c54-0579748cb38a.svg'
AUTHOR = 'gpt-6'

class WateredPlanter(Solo48):
    icon_id = 'watered-planter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('planter', 'water', 'droplet', 'leaves', 'plant', 'bowl', 'gardening')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('potrim', (6, 34), (42, 34))
        self.add_arc('potarc', (42, 34), (6, 34), radius_x=18, radius_y=8, large_arc=False, sweep=True)
        self.add_line('foliage-1', (6, 34), (6, 22))
        self.add_line('foliage-2', (6, 22), (16, 26))
        self.add_line('foliage-3', (16, 26), (16, 18))
        self.add_line('foliage-4', (16, 18), (24, 26))
        self.add_line('foliage-5', (24, 26), (32, 18))
        self.add_line('foliage-6', (32, 18), (32, 26))
        self.add_line('foliage-7', (32, 26), (42, 22))
        self.add_line('foliage-8', (42, 22), (42, 34))
        self.add_contour('pot', *('potrim', 'potarc'), closed=True)
        self.add_contour('foliage', *('foliage-1', 'foliage-2', 'foliage-3', 'foliage-4', 'foliage-5', 'foliage-6', 'foliage-7', 'foliage-8'), closed=False)
        self.relate('connect', *('foliage', 'pot'))
        self.add_line('drop',(24,6),(24,10))
