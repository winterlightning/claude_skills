"""islamic-women-hijab-1: plain long garment beneath the reference hair/headwear.

Plan: SOLO48 VRECT_L ink bounds (6,2)-(42,46); centered circular face x24,
head bottom 24, shoulder top 28, zero visible head/body gap.
Primary reference preserves identifying silhouette; tiny trim/facial marks are
omitted for clear openings. Human reference user.svg supplies rounded shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg inform arcs.
Clothing cue: plain long garment. Hair asymmetry follows the reference, face remains centered.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '2da10a1c-94d1-53ec-a2db-86f6dd5377fd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__islamic-women-hijab-1-avatar/20260926T175531Z-thuan-mac-1/reference/islamic women hijab_2da10a1c-94d1-53ec-a2db-86f6dd5377fd.svg'
SOURCE_HEAD_ICON_ID = 'islamic-women-hijab-1'
AUTHOR = "gpt-6"
HEAD_BOTTOM = 24

class IslamicWomenHijab1Avatar(Solo48):
    icon_id = 'islamic-women-hijab-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('islamic', 'women', 'hijab', '1', 'portrait', 'bust')

    def build(self):
        # Outer hijab, inner face opening, and a broad drape across the chest.
        self.add_line('left-side',(8,44),(8,20))
        self.add_arc('hood-left',(8,20),(24,4),radius_x=16)
        self.add_arc('hood-right',(24,4),(40,20),radius_x=16)
        self.add_line('right-side',(40,20),(40,44))
        self.add_contour('hijab','left-side','hood-left','hood-right','right-side')
        self.add_arc('face-left',(24,13),(24,29),radius_x=7,radius_y=8)
        self.add_arc('face-right',(24,29),(24,13),radius_x=7,radius_y=8)
        self.add_contour('face-opening','face-left','face-right',closed=True)
        self.add_bezier('draped-hem',(8,38),((16,42),(32,42),(40,38)))
        self.relate('connect','hijab','draped-hem')
