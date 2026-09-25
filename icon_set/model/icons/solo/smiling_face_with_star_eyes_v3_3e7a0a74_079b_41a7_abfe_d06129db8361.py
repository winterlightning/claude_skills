"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e7a0a74-079b-41a7-abfe-d06129db8361'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_17/face grin stars_3e7a0a74-079b-41a7-abfe-d06129db8361.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'smiling-face-with-star-eyes-v3'
    variant_of = 'smiling-face-with-star-eyes'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'face', 'with', 'star', 'eyes')

    def build(self):
        # Plan: concentric face; mirrored five-point eye definition; centered smile.
        # CIRCLE centerline radius 20. Lucide face-slightly-smiling + star.
        self.add_arc('face-top', (4,24), (44,24), radius_x=20)
        self.add_arc('face-bottom', (44,24), (4,24), radius_x=20)
        self.add_contour('face', 'face-top', 'face-bottom', closed=True)
        for i, cx in enumerate((15,33)):
            points = [(0,-6),(2,-2),(6,-2),(3,1),(4,5),(0,3),(-4,5),(-3,1),(-6,-2),(-2,-2)]
            self.add_polyline(f'eye-{i}', *((cx+x,19+y) for x,y in points), closed=True)
        self.add_bezier('smile', (16,31), ((20,36),(28,36),(32,31)))
