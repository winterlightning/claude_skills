"""Young man with side-parted hair with soft open-neck casual shirt.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with soft open-neck casual shirt. SOLO48 VRECT_L visible ink (6,2)-(42,46);
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
SOURCE_PATH = 'work/head-solo/batch-02/references/boyfriend.svg'
SOURCE_HEAD_ICON_ID = 'boyfriend'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 24


class BoyfriendAvatar(Solo48):
    icon_id = 'boyfriend-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('boyfriend', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        radius, cy = 10, 14
        self.add_arc('crown',(14,cy),(34,cy),radius_x=radius)
        self.add_arc('jaw',(34,cy),(14,cy),radius_x=radius)
        self.add_contour('head','crown','jaw',closed=True)
        self.add_bezier('fringe',(14,14),((20,14),(24,13),(27,11)),((29,13),(32,14),(34,14)))
        self.relate('connect','head','fringe')

        # Body cue: soft open-neck casual shirt; smooth shoulders remain primary.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(20,top),radius_x=12,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(20,top),(24,top))
        self.add_line('body-top-right',(24,top),(28,top))
        self.add_arc('body-right-shoulder',(28,top),(40,42),radius_x=12,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_line('body-opening',(24,top),(24,top+6))
        self.relate('connect','body-opening','body-top')
        self.relate('connect','body-opening','body-top-right')

        self.relate('connect','head','body-top')
        self.relate('connect','head','body-top-right')
