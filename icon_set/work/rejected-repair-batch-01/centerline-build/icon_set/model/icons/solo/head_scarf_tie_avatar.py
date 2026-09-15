"""head-scarf-tie: diagonally tied scarf beneath the reference hair/headwear.

Plan: SOLO48 VRECT_L ink bounds (6,2)-(42,46); centered circular face x24,
head bottom 24, shoulder top 28, zero visible head/body gap.
Primary reference preserves identifying silhouette; tiny trim/facial marks are
omitted for clear openings. Human reference user.svg supplies rounded shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg inform arcs.
Clothing cue: diagonally tied scarf. Hair asymmetry follows the reference, face remains centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'd91b104f-4bd1-4359-bf72-c9162bc1c67b'
SOURCE_PATH = 'pictographic-primitives/avatars/head scarf tie_d91b104f-4bd1-4359-bf72-c9162bc1c67b.svg'
SOURCE_HEAD_ICON_ID = 'head-scarf-tie'
AUTHOR = 'gpt-6'
HEAD_BOTTOM = 24

class HeadScarfTieAvatar(Solo48):
    icon_id = 'head-scarf-tie-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('head', 'scarf', 'tie', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_arc('hood',(8,16),(40,16),radius_x=16,radius_y=12)
        self.add_polyline('brim',(8,16),(16,16),(32,16),(40,16))
        self.relate('connect','hood','brim')
        self.add_arc('face',(32,16),(16,16),radius_x=8,radius_y=8)
        self.relate('connect','face','brim')
        for side,sign in [('left',-1),('right',1)]:
            self.add_line('flap-'+side,(24+sign*16,16),(24+sign*16,24))
            self.relate('connect','flap-'+side,'hood')
            self.relate('connect','flap-'+side,'brim')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(16,top),radius_x=8,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(16,top),(24,top))
        self.add_line('body-top-right',(24,top),(32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_polyline('body-collar',(16,top),(24,42),(32,top))
        self.relate('connect','body-collar','body-top')
        self.relate('connect','body-collar','body-top-right')
        self.add_line('body-scarf-tail',(24,42),(30,44))
        self.relate('connect','body-scarf-tail','body-collar')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
