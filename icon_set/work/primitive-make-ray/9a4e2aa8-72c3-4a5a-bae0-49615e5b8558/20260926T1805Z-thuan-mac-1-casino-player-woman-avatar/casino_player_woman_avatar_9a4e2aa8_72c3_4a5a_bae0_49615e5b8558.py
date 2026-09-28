"""Woman with a flared bob with rounded evening neckline.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with rounded evening neckline. SOLO48 VRECT_L visible ink (6,2)-(42,46);
centerline extremes (8,4)-(40,44). Head and body ink touch on the shoulder plateau.
Primary source supplies the hair/headwear silhouette; fine facial marks,
hat stitching and microdetails are omitted to preserve openings at 48.
Human reference: icon_set/references/human_ref/user.svg for proportions,
curved shoulders and open bottom. Lucide original/user-round.svg and its
atomic-debug counterpart inform cardinal arcs and tangent joins; original/shirt.svg
and atomic-debug/shirt.svg inform the clothing cue. Intentional source hairstyle
or hat asymmetry is retained, with mirrored shoulders where appropriate.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '9a4e2aa8-72c3-4a5a-bae0-49615e5b8558'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__casino-player-woman-avatar/20260926T175531Z-thuan-mac-1/reference/casino player woman_9a4e2aa8-72c3-4a5a-bae0-49615e5b8558.svg'
SOURCE_HEAD_ICON_ID = 'casino-player-woman'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 32


class CasinoPlayerWomanAvatar(Solo48):
    icon_id = 'casino-player-woman-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('casino', 'player', 'woman', 'portrait', 'bust')

    def build(self):
        self.add_arc('bun-left',(24,12),(24,4),radius_x=4)
        self.add_arc('bun-right',(24,4),(24,12),radius_x=4)
        self.add_contour('bun','bun-left','bun-right',closed=True)
        self.add_arc('crown-left',(14,22),(24,12),radius_x=10)
        self.add_arc('crown-right',(24,12),(34,22),radius_x=10)
        self.add_arc('jaw',(34,22),(14,22),radius_x=10)
        self.add_contour('head','crown-left','crown-right','jaw',closed=True)
        self.relate('connect','bun','head')
        self.add_bezier('fringe',(14,22),((20,24),(24,20),(27,17)),((29,20),(32,22),(34,22)))
        self.relate('connect','head','fringe')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top', (16,top), (24, top))
        self.add_line('body-top-right', (24, top), (32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
