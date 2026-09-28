"""Farmer with a broad-brimmed hat and flowing hair with open apron over a blouse.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with open apron over a blouse. SOLO48 VRECT_L visible ink (6,2)-(42,46);
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

SOURCE_ICON_ID = '5206b2d8-df0f-5400-9894-ee72881cb0ae'
SOURCE_PATH = 'pictographic-primitives/avatars/farmer woman_5206b2d8-df0f-5400-9894-ee72881cb0ae.svg'
SOURCE_HEAD_ICON_ID = 'farmer-woman-1'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26


class FarmerWoman1Avatar(Solo48):
    icon_id = 'farmer-woman-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('farmer', 'woman', '1', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_arc('cap-left',(12,16),(24,4),radius_x=12)
        self.add_arc('cap-right',(24,4),(36,16),radius_x=12)
        self.add_contour('cap','cap-left','cap-right')
        self.add_polyline('brim',(8,16),(12,16),(14,16),(34,16),(36,16),(40,16))
        self.relate('connect','cap','brim')
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','face','brim')
        for side,sign in [('left',-1),('right',1)]:
            self.add_bezier('hair-'+side,(24+sign*10,16),((24+sign*10,22),(24+sign*13,26),(24+sign*16,26)))
            self.relate('connect','hair-'+side,'face')
            self.relate('connect','hair-'+side,'brim')

        # Body cue: open apron over a blouse; smooth shoulders remain primary.
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side',(8,44),(8,42))
        self.add_arc('body-left-shoulder',(8,42),(18,top),radius_x=10,radius_y=42-top)
        self.add_contour('body-left','body-left-side','body-left-shoulder')
        self.add_line('body-top',(18,top),(24,top))
        self.add_line('body-top-right',(24,top),(30,top))
        self.add_arc('body-right-shoulder',(30,top),(40,42),radius_x=10,radius_y=42-top)
        self.add_line('body-right-side',(40,42),(40,44))
        self.add_contour('body-right','body-right-shoulder','body-right-side')
        self.relate('connect','body-left','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.add_line('body-apron-left',(18,top),(18,44))
        self.add_line('body-apron-right',(30,top),(30,44))
        self.relate('connect','body-apron-left','body-top')
        self.relate('connect','body-apron-right','body-top-right')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
