"""Side-parted man in evening wear with wide dinner-jacket lapels.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with wide dinner-jacket lapels. SOLO48 VRECT_L visible ink (6,2)-(42,46);
centerline extremes (8,4)-(40,44). Head and body ink touch on the shoulder plateau.
Primary source supplies the hair/headwear silhouette; fine facial marks,
hat stitching and microdetails are omitted to preserve openings at 48.
Human reference: icon_set/references/human_ref/user.svg for proportions,
curved shoulders and open bottom. Lucide original/user-round.svg and its
atomic-debug counterpart inform cardinal arcs and tangent joins; original/shirt.svg
and atomic-debug/shirt.svg inform the clothing cue. Intentional source hairstyle
or hat asymmetry is retained, with mirrored shoulders where appropriate.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = None
SOURCE_PATH = 'work/head-solo/batch-02/references/casino-player-man.svg'
SOURCE_HEAD_ICON_ID = 'casino-player-man'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24


class CasinoPlayerManAvatar(Solo48):
    icon_id = 'casino-player-man-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('casino', 'player', 'man', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        radius, cy = 10, 14
        self.add_arc('crown',(14,cy),(34,cy),radius_x=radius)
        self.add_arc('jaw',(34,cy),(14,cy),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('fringe',(14,14),((20,14),(24,13),(27,11)),((29,13),(32,14),(34,14)))
        self.relate('connect','head','fringe')

        # Body cue: wide dinner-jacket lapels; smooth shoulders remain primary.
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
        self.add_polyline('body-collar',(16,top),(24,40),(32,top))
        self.relate('connect','body-collar','body-top')
        self.relate('connect','body-collar','body-top-right')
        self.add_line('body-jacket-opening',(24,40),(24,44))
        self.relate('connect','body-jacket-opening','body-collar')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
