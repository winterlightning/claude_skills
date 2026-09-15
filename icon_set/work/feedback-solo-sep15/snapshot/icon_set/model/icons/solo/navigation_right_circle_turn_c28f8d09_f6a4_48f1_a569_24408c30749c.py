"""navigation-right-circle-turn: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c28f8d09-f6a4-48f1-a569-24408c30749c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation right circle turn_c28f8d09-f6a4-48f1-a569-24408c30749c.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class NavigationRightCircleTurn(Solo48):
    icon_id = 'navigation-right-circle-turn'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('navigation', 'right', 'circle', 'turn', 'interface-essential')

    def build(self):
        # HRECT_L (4,8)-(44,40); one circular turn and matching arrowhead arms.
        # Construction reference: Lucide undo-2: tangent semicircular turn
        turn_x, turn_y, radius = 16,28,12
        self.add_line('tail',(24,40),(turn_x,40))
        self.add_arc('bend',(turn_x,40),(turn_x,16),radius_x=radius)
        self.add_line('shaft',(turn_x,16),(44,16))
        self.add_contour('run','tail','bend','shaft')
        self.add_polyline('head',(36,8),(44,16),(36,24))
        self.relate('connect','run','head')
