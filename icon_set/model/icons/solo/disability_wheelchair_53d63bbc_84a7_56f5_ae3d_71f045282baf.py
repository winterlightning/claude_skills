'Wheelchair user: round detached head with exact 4-unit head/body clearance, continuous seated posture, and a round wheel. Nonessential arm detail omitted for clarity.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '53d63bbc-84a7-56f5-ae3d-71f045282baf'
SOURCE_PATH = 'icons-json/wayfinding/disability wheelchair_53d63bbc-84a7-56f5-ae3d-71f045282baf.json'
AUTHOR = 'gpt-6'

class DisabilityWheelchair(Solo48):
    icon_id = 'disability-wheelchair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('disability', 'wheelchair', 'wayfinding')

    def build(self) -> None:
        self.add_arc('head-top', (12,8), (20,8), radius_x=4, radius_y=4)
        self.add_arc('head-bottom', (20,8), (12,8), radius_x=4, radius_y=4)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)

        # Shared human reference: full_body_ref.png. Head bottom=12, body starts=20: exact 4u ink gap.
        # The seated body meets the wheel at its actual (26,28) circular point.
        self.add_polyline('body',(16,20),(18,28),(26,28),(32,28),(36,42),(40,42))
        self.add_arc('wheel-top',(18,24),(26,28),radius_x=10)
        self.add_arc('wheel-right',(26,28),(18,44),radius_x=10)
        self.add_arc('wheel-lower-left',(18,44),(8,34),radius_x=10)
        self.add_arc('wheel-upper-left',(8,34),(18,24),radius_x=10)
        self.add_contour('wheel','wheel-top','wheel-right','wheel-lower-left','wheel-upper-left',closed=True)
        self.relate('connect','body','wheel')
