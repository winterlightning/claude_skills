"""VRECT_XL (8,6)-(40,42) centerlines. Preserve attached cross, tall gabled nave, lower wings and arched entrance. Omit facade seams. Mirrored about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90fbedce-fc6d-53a4-9026-f769a2eefc2e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/church_90fbedce-fc6d-53a4-9026-f769a2eefc2e.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'gabled-church-with-cross'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'landmarks'
    aliases = ()
    keywords = ('church', 'chapel', 'cross', 'religion', 'worship', 'gable', 'building', 'christian')

    def build(self):
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('outline', (8, 44), (8, 32), (14, 28), (14, 24), (24, 16), (34, 24), (34, 28), (40, 32), (40, 44), (28, 44), (20, 44), closed=True)
        self.add_polyline('cross-stem', (24, 4), (24, 8), (24, 16))
        self.add_polyline('cross-bar', (20, 8), (24, 8), (28, 8))
        self.relate('connect', 'cross-stem', 'cross-bar')
        self.relate('connect', 'cross-stem', 'outline')
        self.add_line('door-left', (20, 44), (20, 36))
        self.add_arc('door-arch', (20, 36), (28, 36), radius_x=4)
        self.add_line('door-right', (28, 36), (28, 44))
        self.add_contour('door', 'door-left', 'door-arch', 'door-right')
        self.relate('connect', 'door', 'outline')
