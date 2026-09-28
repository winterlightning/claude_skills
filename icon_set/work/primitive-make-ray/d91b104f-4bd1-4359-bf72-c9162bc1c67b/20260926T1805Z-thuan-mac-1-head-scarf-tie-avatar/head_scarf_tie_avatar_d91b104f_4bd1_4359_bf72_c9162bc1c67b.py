"""head-scarf-tie: diagonally tied scarf beneath the reference hair/headwear.

Plan: SOLO48 VRECT_L ink bounds (6,2)-(42,46); centered circular face x24,
head bottom 24, shoulder top 28, zero visible head/body gap.
Primary reference preserves identifying silhouette; tiny trim/facial marks are
omitted for clear openings. Human reference user.svg supplies rounded shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg inform arcs.
Clothing cue: diagonally tied scarf. Hair asymmetry follows the reference, face remains centered.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'd91b104f-4bd1-4359-bf72-c9162bc1c67b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__head-scarf-tie-avatar/20260926T175531Z-thuan-mac-1/reference/head scarf tie_d91b104f-4bd1-4359-bf72-c9162bc1c67b.svg'
SOURCE_HEAD_ICON_ID = 'head-scarf-tie'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24

class HeadScarfTieAvatar(Solo48):
    icon_id = 'head-scarf-tie-avatar'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('head', 'scarf', 'tie', 'portrait', 'bust')

    def build(self):
        # Tied scarf: a band across the round head and two leaves on its right.
        self.add_arc('head-top',(8,20),(32,20),radius_x=12)
        self.add_arc('head-bottom',(32,20),(8,20),radius_x=12)
        self.add_contour('head','head-top','head-bottom',closed=True)
        self.add_line('scarf-band',(8,20),(32,20))
        self.relate('connect','scarf-band','head')
        self.add_polyline('bow-upper',(32,20),(38,14),(44,14))
        self.add_polyline('bow-lower',(32,20),(38,26),(44,26))
        self.relate('connect','bow-upper','bow-lower')
        self.relate('connect','bow-upper','head')
        self.relate('connect','bow-lower','head')
        self.add_arc('body',(4,40),(36,40),radius_x=16,radius_y=4,sweep=True)
        self.relate('connect','head','body')
