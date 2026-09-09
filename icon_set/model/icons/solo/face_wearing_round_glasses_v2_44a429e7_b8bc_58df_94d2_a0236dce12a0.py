# Variant of face-wearing-round-glasses; parent file remains unchanged.
'Larger round lenses. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '44a429e7-b8bc-58df-94d2-a0236dce12a0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/glasses_44a429e7-b8bc-58df-94d2-a0236dce12a0.svg'
AUTHOR = 'gpt-6'

class FaceWearingRoundGlassesVariant2(Solo48):
    icon_id = 'face-wearing-round-glasses-v2'
    variant_of = 'face-wearing-round-glasses'
    variant_label = 'Larger round lenses'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('face', 'glasses', 'spectacles', 'smile', 'avatar', 'person', 'eyewear', 'portrait')

    def build(self) -> None:
        self.add_arc('face-0', (46, 24), (24, 46), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('face-1', (24, 46), (2, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('face-2', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('face-3', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_contour('face', 'face-0', 'face-1', 'face-2', 'face-3', closed=True)
        for name, cx in [('left',15),('right',33)]:
            self.add_arc(f'lens-{name}-top',(cx-6,22),(cx+6,22),radius_x=6)
            self.add_arc(f'lens-{name}-bottom',(cx+6,22),(cx-6,22),radius_x=6)
            self.add_contour(f'lens-{name}',f'lens-{name}-top',f'lens-{name}-bottom',closed=True)
        self.add_line('bridge',(21,22),(27,22))
        self.relate('connect','bridge','lens-left')
        self.relate('connect','bridge','lens-right')
        self.add_arc('smile', (18, 34), (30, 34), radius_x=10, radius_y=10, sweep=False)
