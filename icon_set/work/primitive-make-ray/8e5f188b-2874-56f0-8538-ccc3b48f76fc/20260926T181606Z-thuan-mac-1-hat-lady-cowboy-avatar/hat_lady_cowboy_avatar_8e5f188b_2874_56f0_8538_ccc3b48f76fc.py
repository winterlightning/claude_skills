"""hat-lady-cowboy-avatar: revised SOLO48 drawing from the claimed source.

Comparison: The rejected straight brim and sharp M crown lost the upturned cowboy hat and long hair.
Revision: Redrew a broad raised brim, dipped crown, face, and long side locks.
Human construction: icon_set/references/human_ref/user.svg; Lucide user-round supplies simple circular head and shoulder arcs.
The emitted primitives use a shared axis where the reference is symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '8e5f188b-2874-56f0-8538-ccc3b48f76fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hat-lady-cowboy-avatar/20260926T175531Z-thuan-mac-1/reference/hat lady cowboy_8e5f188b-2874-56f0-8538-ccc3b48f76fc.svg'
SOURCE_HEAD_ICON_ID = 'hat-lady-cowboy'
AUTHOR = "gpt-6"

class HatLadyCowboyAvatar(Solo48):
    icon_id = 'hat-lady-cowboy-avatar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('hat', 'lady', 'cowboy', 'portrait', 'bust')

    def build(self):
        # Wide upturned brim, dipped crown, open face, and long side hair.
        axis = 24
        self.add_polyline('crown',(12,22),(16,8),(axis,10),(32,8),(36,22))
        self.add_polyline('brim-left',(4,18),(8,22),(16,22))
        self.add_polyline('brim-right',(32,22),(40,22),(44,18))
        self.relate('connect','crown','brim-left')
        self.relate('connect','crown','brim-right')
        self.add_arc('face',(32,22),(16,22),radius_x=8)
        self.relate('connect','face','brim-left')
        self.relate('connect','face','brim-right')
        self.add_polyline('hair-left',(8,22),(8,36),(12,40))
        self.add_polyline('hair-right',(40,22),(40,36),(36,40))
        self.relate('connect','hair-left','brim-left')
        self.relate('connect','hair-right','brim-right')
