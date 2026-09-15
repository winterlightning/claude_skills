"""ice-cream-cone-food: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '89acf638-2184-527a-8681-8ad6b144260c'
SOURCE_PATH = 'pictographic-primitives/food/ice cream cone_89acf638-2184-527a-8681-8ad6b144260c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class IceCreamConeFood(Solo48):
    icon_id = 'ice-cream-cone-food'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('ice', 'cream', 'cone', 'food')

    def build(self):
        # Plan: VRECT_L; mirrored scoop and cone, smooth crown and three deliberate scallops.
        # Reference: Geometric paired curves; retain the scoop and cone.
        self.add_bezier('crown-left',(8,18),((8,10),(14,4),(24,4)))
        self.add_bezier('crown-right',(24,4),((34,4),(40,10),(40,18)))
        self.add_bezier('right-scallop',(40,18),((40,22),(35,24),(32,21)))
        self.add_bezier('center-scallop',(32,21),((28,25),(20,25),(16,21)))
        self.add_bezier('left-scallop',(16,21),((13,24),(8,22),(8,18)))
        self.add_contour('scoop','crown-left','crown-right','right-scallop','center-scallop','left-scallop',closed=True)
        self.add_polyline('cone',(16,21),(24,44),(32,21))
        self.relate('connect','cone','scoop')
