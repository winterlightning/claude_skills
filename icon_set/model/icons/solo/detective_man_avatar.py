"""Detective in a rounded deerstalker with coat with broad lapels.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with coat with broad lapels. SOLO48 VRECT_L visible ink (6,2)-(42,46);
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

SOURCE_ICON_ID = '2d7dfb6a-9827-48bc-89a3-9b86d474dcb7'
SOURCE_PATH = 'pictographic-primitives/avatars/detective man_2d7dfb6a-9827-48bc-89a3-9b86d474dcb7.svg'
SOURCE_HEAD_ICON_ID = 'detective-man'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26


class DetectiveManAvatar(Solo48):
    icon_id = 'detective-man-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('detective', 'man', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_arc('cap-left',(12,16),(24,4),radius_x=12)
        self.add_arc('cap-right',(24,4),(36,16),radius_x=12)
        self.add_contour('cap','cap-left','cap-right')
        self.add_polyline('brim',(8,16),(12,16),(14,16),(34,16),(36,16),(40,16))
        self.relate('connect','cap','brim')
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','face','brim')
        self.add_line('crown-seam',(24,4),(24,8))
        self.relate('connect','cap','crown-seam')

        # Body cue: coat with broad lapels; smooth shoulders remain primary.
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

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
