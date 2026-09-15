'video-e80765f4: distinct review variant.\n\nConstruction: Video camera with a compact body and a tall tapered lens hood; keep a clear horizontal viewing direction.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: video from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e80765f4-90c9-40bf-aed4-9fbc533d28fb'
SOURCE_PATH = 'pictographic-primitives/symbol/video_e80765f4-90c9-40bf-aed4-9fbc533d28fb.svg'
AUTHOR = 'gpt-6'


class VideoE80765f4Variant2(Solo48):
    icon_id = 'video-e80765f4-v2'
    variant_of = 'video-e80765f4'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('video', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'body',4,14,30,34,4,ys=(20,28))
        poly(self,'lens',(30,20),(44,8),(44,40),(30,28))
        contacts(self)
