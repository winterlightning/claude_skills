# Variant of face-wearing-round-glasses; parent file remains unchanged.
'Circular face with mirrored round glasses and raised smile. Human reference icon_set/references/human_ref/user.svg supplies the round head vocabulary; no body or head-to-body gap applies. Lucide glasses informs paired lenses and bridge. Pupils and temple arms remain omitted. CIRCLE visible radius 22; SOLO48 stroke 4.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '44a429e7-b8bc-58df-94d2-a0236dce12a0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/glasses_44a429e7-b8bc-58df-94d2-a0236dce12a0.svg'
AUTHOR = 'gpt-6'

class FaceWearingRoundGlassesVariant4(Solo48):
    icon_id = 'face-wearing-round-glasses-v4'
    variant_of = 'face-wearing-round-glasses'
    variant_label = 'Circle envelope and full spacing repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('face', 'glasses', 'spectacles', 'smile', 'avatar', 'person', 'eyewear', 'portrait')

    def build(self) -> None:
        # CIRCLE envelope: center (24,24), centerline radius 20, visible radius 22.
        # Shared cardinal nodes keep concentric geometry and attachments exact.
        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        circle('face', 24, 24, 20)
        for side in (-1, 1):
            circle('lens-left' if side < 0 else 'lens-right', 24 + side * 8, 21, 3)
        self.add_line('bridge', (19, 21), (29, 21))
        self.relate('connect', 'bridge', 'lens-left')
        self.relate('connect', 'bridge', 'lens-right')
        self.add_arc('smile', (18, 33), (30, 33), radius_x=10, sweep=False)
