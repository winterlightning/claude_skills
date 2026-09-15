"""playstation-vr: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7ccf92a-afad-5337-b90a-b52d403c4d46'
SOURCE_PATH = 'pictographic-primitives/technology/playstation vr_e7ccf92a-afad-5337-b90a-b52d403c4d46.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class PlaystationVr(Solo48):
    icon_id = 'playstation-vr'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('playstation', 'vr', 'technology')

    def build(self):
        # Plan: HRECT_L; symmetric visor, smooth top and bottom rails and a circular headband.
        # Reference: Geometric paired visor curves.
        self.add_arc('headband',(5,27),(43,27),radius_x=19,radius_y=19)
        self.add_bezier('visor-top-left',(4,32),((4,23),(15,21),(24,21)))
        self.add_bezier('visor-top-right',(24,21),((33,21),(44,23),(44,32)))
        self.add_bezier('visor-right',(44,32),((44,36),(43,40),(39,40)),((34,40),(30,38),(24,38)))
        self.add_bezier('visor-left',(24,38),((18,38),(14,40),(9,40)),((5,40),(4,36),(4,32)))
        self.add_contour('visor','visor-top-left','visor-top-right','visor-right','visor-left',closed=True)
        self.relate('connect','headband','visor')
