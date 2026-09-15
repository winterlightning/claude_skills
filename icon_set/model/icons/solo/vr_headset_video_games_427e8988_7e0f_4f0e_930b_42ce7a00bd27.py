'vr-headset-video-games: independent smooth-curve repair.\n\nConstruction: Smooth goggles with one continuous outer contour; shared brow, paired temples and a rounded nose saddle.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/gamepad-2.svg and atomic-debug/gamepad-2.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '427e8988-7e0f-4f0e-930b-42ce7a00bd27'
SOURCE_PATH = 'pictographic-primitives/video-games/vr headset_427e8988-7e0f-4f0e-930b-42ce7a00bd27.svg'
AUTHOR = 'gpt-6'


class VrHeadsetVideoGames(Solo48):
    icon_id = 'vr-headset-video-games'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('vr', 'headset', 'video-games')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'goggles',(16,8),('L',(32,8)),('C',(41,8),(44,14),(44,22)),('C',(44,32),(40,40),(35,40)),('C',(30,40),(30,31),(24,31)),('C',(18,31),(18,40),(13,40)),('C',(8,40),(4,32),(4,22)),('C',(4,14),(7,8),(16,8)),closed=True)
        contacts(self)
