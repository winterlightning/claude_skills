"""A smiling face with round glasses. CIRCLE radius 22. Lucide glasses informs paired circular lenses and bridge. Tiny pupils and temple arms are omitted to keep lenses open; face and smile remain symmetric."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44a429e7-b8bc-58df-94d2-a0236dce12a0'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/glasses_44a429e7-b8bc-58df-94d2-a0236dce12a0.svg'
AUTHOR = 'astra-chatgpt'


class FaceWearingRoundGlasses(Solo48):
    icon_id = 'face-wearing-round-glasses'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('face', 'glasses', 'spectacles', 'smile', 'avatar', 'person', 'eyewear', 'portrait')

    def build(self) -> None:
        self.add_arc('face-0', (46, 24), (24, 46), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('face-1', (24, 46), (2, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('face-2', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('face-3', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_contour('face', 'face-0', 'face-1', 'face-2', 'face-3', closed=True)
        self.add_arc('lens-left-0', (20, 21), (15, 26), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('lens-left-1', (15, 26), (10, 21), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('lens-left-2', (10, 21), (15, 16), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('lens-left-3', (15, 16), (20, 21), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('lens-left', 'lens-left-0', 'lens-left-1', 'lens-left-2', 'lens-left-3', closed=True)
        self.add_arc('lens-right-0', (38, 21), (33, 26), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('lens-right-1', (33, 26), (28, 21), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('lens-right-2', (28, 21), (33, 16), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('lens-right-3', (33, 16), (38, 21), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('lens-right', 'lens-right-0', 'lens-right-1', 'lens-right-2', 'lens-right-3', closed=True)
        self.add_line('bridge', (20, 21), (28, 21))
        self.relate("connect", 'bridge', 'lens-left')
        self.relate("connect", 'bridge', 'lens-right')
        self.add_arc('smile', (18, 34), (30, 34), radius_x=10, radius_y=10, sweep=False)
