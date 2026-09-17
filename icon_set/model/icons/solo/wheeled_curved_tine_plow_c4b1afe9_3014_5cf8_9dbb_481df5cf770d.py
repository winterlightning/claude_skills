"""Agricultural Disk Plow.
Plan: Two repeated sweeping tines on beam, triangular hitch and right support wheel. Extrema (4,8)-(44,40).
Reference: Original source silhouette; Lucide geometric construction with shared joints and coherent curves.
Reduction: Fine interior detail omitted to preserve negative space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4b1afe9-3014-5cf8-9dbb-481df5cf770d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/farming/disk plow_c4b1afe9-3014-5cf8-9dbb-481df5cf770d.svg'
AUTHOR = 'gpt-6'

class Batch27Icon(Solo48):
    icon_id = 'wheeled-curved-tine-plow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/agriculture"
    aliases = ()
    keywords = ('agricultural', 'disk', 'plow')

    def build(self):

        self.add_polyline('beam',(4,20),(8,20),(20,20),(24,20),(38,20),(44,20))
        self.add_polyline('hitch',(8,20),(8,8),(20,20));self.relate('connect','beam','hitch')
        for i,x in enumerate((8,24)):
            self.add_bezier(f'tine-{i}',(x,20),((x,30),(x,35),(x-4,40)))
            self.relate('connect','beam',f'tine-{i}')
        self.add_line('fork',(38,20),(38,28));self.relate('connect','beam','fork')
        self.add_arc('wheel-a',(38,28),(38,40),radius_x=6)
        self.add_arc('wheel-b',(38,40),(38,28),radius_x=6)
        self.add_contour('wheel','wheel-a','wheel-b',closed=True);self.relate('connect','fork','wheel')
