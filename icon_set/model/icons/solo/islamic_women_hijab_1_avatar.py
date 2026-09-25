"""islamic-women-hijab-1: plain long garment beneath the reference hair/headwear.

Plan: SOLO48 VRECT_L ink bounds (6,2)-(42,46); centered circular face x24,
head bottom 24, shoulder top 28, zero visible head/body gap.
Primary reference preserves identifying silhouette; tiny trim/facial marks are
omitted for clear openings. Human reference user.svg supplies rounded shoulders;
Lucide original/user-round.svg and atomic-debug/user-round.svg inform arcs.
Clothing cue: plain long garment. Hair asymmetry follows the reference, face remains centered.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '2da10a1c-94d1-53ec-a2db-86f6dd5377fd'
SOURCE_PATH = 'pictographic-primitives/avatars/islamic women hijab_2da10a1c-94d1-53ec-a2db-86f6dd5377fd.svg'
SOURCE_HEAD_ICON_ID = 'islamic-women-hijab-1'
AUTHOR = 'gpt-6'
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
        self.add_line('body-top', (16,top), (24, top))
        self.add_line('body-top-right', (24, top), (32,top))
        self.add_arc('body-right-shoulder',(32,top),(40,42),radius_x=8,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
