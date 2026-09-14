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
    category = 'objects/decoration'
    aliases = ()
    keywords = ('planter', 'water', 'droplet', 'leaves', 'plant', 'bowl', 'gardening')

    def build(self) -> None:
        """Opening repair: Deepened the bowl using a true half-ellipse; retained the foliage and droplet."""
        self.add_line('potrim', (6, 34), (42, 34))
        self.add_arc('potarc', (42, 34), (6, 34), sweep=True, radius_x=18, radius_y=8)
        self.add_contour('pot', 'potrim', 'potarc', closed=True)
        self.add_polyline('foliage', (6, 34), (6, 22), (16, 26), (16, 18), (24, 26), (32, 18), (32, 26), (42, 22), (42, 34), closed=False)
        self.relate('connect', 'foliage', 'pot')
        self.add_arc('drop-a', (24, 6), (28, 10), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('drop-b', (28, 10), (20, 10), radius_x=4, radius_y=4, sweep=True)
        self.add_arc('drop-c', (20, 10), (24, 6), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('drop', 'drop-a', 'drop-b', 'drop-c', closed=True)
