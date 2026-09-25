"""navigation-direction-left: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22ff4baa-e14e-4622-9ea4-d56766efca09'
SOURCE_PATH = 'pictographic-primitives/interface-essential/navigation direction left_22ff4baa-e14e-4622-9ea4-d56766efca09.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class NavigationDirectionLeft(Solo48):
    icon_id = 'navigation-direction-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('navigation', 'direction', 'left', 'interface-essential')

    def build(self):
        # HRECT_L (4,8)-(44,40); symmetric arrowhead and round turn.
        # Construction reference: Lucide undo-2: tangent quarter circle
        self.add_line('shaft',(4,20),(36,20))
        self.add_arc('bend',(36,20),(44,28),radius_x=8)
        self.add_line('tail',(44,28),(44,40))
        self.add_contour('run','shaft','bend','tail')
        self.add_polyline('head',(16,8),(4,20),(16,32))
        self.relate('connect','run','head')
