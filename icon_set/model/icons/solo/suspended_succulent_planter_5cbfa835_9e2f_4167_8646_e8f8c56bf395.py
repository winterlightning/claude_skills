"""Three pointed succulent leaves in a bowl suspended from a cord; leaf veins omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5cbfa835-9e2f-4167-8646-e8f8c56bf395'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/hanging plant 2_5cbfa835-9e2f-4167-8646-e8f8c56bf395.svg'
AUTHOR = 'gpt-6'

class SuspendedSucculentPlanter(Solo48):
    icon_id = 'suspended-succulent-planter'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('planter', 'hanging', 'succulent', 'leaves', 'cord', 'bowl', 'plant')

    def build(self) -> None:
        # VRECT_XL: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_line('cord', (24, 2), (24, 8))
        self.add_polyline('suspension', (5, 34), (5, 26), (24, 8), (43, 26), (43, 34), closed=False)
        self.relate('connect', 'cord', 'suspension')
        self.add_line('potrim', (5, 34), (43, 34))
        self.add_arc('potarc', (43, 34), (5, 34), radius_x=19, radius_y=12, sweep=True)
        self.add_contour('pot', 'potrim', 'potarc', closed=True)
        self.relate('connect', 'suspension', 'pot')
        self.add_polyline('leaves', (12, 34), (12, 25), (19, 28), (24, 19), (29, 28), (36, 25), (36, 34), closed=False)
        self.relate('connect', 'leaves', 'pot')
