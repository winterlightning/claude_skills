'video-e80765f4: independent smooth-curve repair.\n\nConstruction: Video camera with four equal body corners and a horizontally symmetric lens housing.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/video.svg and atomic-debug/video.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e80765f4-90c9-40bf-aed4-9fbc533d28fb'
SOURCE_PATH = 'pictographic-primitives/symbol/video_e80765f4-90c9-40bf-aed4-9fbc533d28fb.svg'
AUTHOR = 'gpt-6'


class VideoE80765f4(Solo48):
    icon_id = 'video-e80765f4'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('video', 'symbol')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'body',4,8,32,40,6,ys=(18,30))
        poly(self,'lens',(32,18),(44,12),(44,36),(32,30))
        contacts(self)
