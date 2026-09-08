"""Gabled Church with Cross. Rebuilt from the supplied silhouette."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '90fbedce-fc6d-53a4-9026-f769a2eefc2e'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/church_90fbedce-fc6d-53a4-9026-f769a2eefc2e.svg'
AUTHOR = 'gpt-6'


class Landmark(Solo48):
    icon_id = 'gabled-church-with-cross'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('church', 'chapel', 'cross', 'religion', 'worship', 'gable', 'building', 'christian')

    def build(self):
        self.add_polyline('outline', (5, 46), (5, 32), (13, 27), (13, 22), (24, 14), (35, 22), (35, 27), (43, 32), (43, 46), (28, 46), (20, 46), closed=True)
        self.add_polyline('cross-stem', (24, 2), (24, 6), (24, 14), closed=False)
        self.add_polyline('cross-bar', (20, 6), (24, 6), (28, 6), closed=False)
        self.relate("connect", "cross-stem", "cross-bar")
        self.relate("connect", "cross-stem", 'outline')
        self.add_line("door-left", (20, 46), (20, 35))
        self.add_arc("door-arch", (20, 35), (28, 35), radius_x=4)
        self.add_line("door-right", (28, 35), (28, 46))
        self.add_contour("door", "door-left", "door-arch", "door-right")
        self.relate("connect", "door", "outline")
