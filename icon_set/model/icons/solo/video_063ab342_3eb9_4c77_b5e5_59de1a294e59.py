'video: independent smooth-curve repair.\n\nConstruction: Video camera with four equal body corners and a horizontally symmetric lens housing.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/video.svg and atomic-debug/video.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '063ab342-3eb9-4c77-b5e5-59de1a294e59'
SOURCE_PATH = 'pictographic-primitives/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'
AUTHOR = 'gpt-6'


class Video(Solo48):
    icon_id = 'video'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('video', 'state')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'body',4,8,32,40,6,ys=(18,30))
        poly(self,'lens',(32,18),(44,12),(44,36),(32,30))
        contacts(self)
