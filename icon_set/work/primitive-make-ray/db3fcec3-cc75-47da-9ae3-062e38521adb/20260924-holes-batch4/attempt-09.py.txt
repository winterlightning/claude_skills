"""smartwatch circle: repaired SOLO48 composition.
Plan: Paired strap attachments and dominant round face.
Keyshape: VRECT_M keeps the near-circular face broad while reserving strap clearance.
Reduction: No defining parts omitted; face is mildly flattened to make room for the strap openings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'db3fcec3-cc75-47da-9ae3-062e38521adb'
SOURCE_PATH = 'pictographic-primitives/other/smartwatch circle_db3fcec3-cc75-47da-9ae3-062e38521adb.svg'
AUTHOR = "gpt-6"
CONSTRUCTION_REFERENCES = 'watch'

class AuthoredIcon(Solo48):
    icon_id = 'smartwatch-circle'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('smartwatch', 'circle')

    def build(self):
        self.add_bezier('face-top', (10, 24), ((10, 20), (12, 16), (16, 14)), ((20, 12), (28, 12), (32, 14)), ((36, 16), (38, 20), (38, 24)))
        self.add_bezier('face-bottom', (38, 24), ((38, 28), (36, 32), (32, 34)), ((28, 36), (20, 36), (16, 34)), ((12, 32), (10, 28), (10, 24)))
        self.add_contour('face', 'face-top', 'face-bottom', closed=True)
        for (n, pts) in [('upper', ((16, 14), (16, 4), (32, 4), (32, 14))), ('lower', ((16, 34), (16, 44), (32, 44), (32, 34)))]:
            self.add_polyline(n, *pts)
            self.relate('connect', n, 'face')
