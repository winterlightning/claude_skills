"""bird-life — re-authored in place for smooth SOLO48 geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dee6f213-07ab-4305-8dd4-d656ac7937ec'
SOURCE_PATH = 'pictographic-primitives/transportation/bird life_dee6f213-07ab-4305-8dd4-d656ac7937ec.svg'
AUTHOR = 'gpt-6'

class BirdLife(Solo48):
    icon_id = 'bird-life'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    aliases = ()
    keywords = ('bird', 'life', 'transportation')

    def build(self):
        # One symmetric hanging curve; ellipse halves remove the converted spikes.
        # HRECT_L centerline extremes: (4,8)-(44,40). No useful subject match in Lucide.
        axis = 24
        self.add_line('left-flange', (4, 8), (axis-8, 8))
        self.add_arc('left-bend', (axis-8, 8), (axis, 40), radius_x=8, radius_y=32, sweep=False)
        self.add_arc('right-bend', (axis, 40), (axis+8, 8), radius_x=8, radius_y=32, sweep=False)
        self.add_line('right-flange', (axis+8, 8), (44, 8))
        self.add_contour('outline', 'left-flange', 'left-bend', 'right-bend', 'right-flange')
