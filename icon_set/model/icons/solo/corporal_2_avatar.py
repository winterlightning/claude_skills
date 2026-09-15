"""Soldier wearing a tilted beret with asymmetric uniform lapel.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with asymmetric uniform lapel. SOLO48 VRECT_L visible ink (6,2)-(42,46);
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

SOURCE_ICON_ID = '2f3a6dc9-7f3d-4326-868e-3002693d3414'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_13/corporal_2f3a6dc9-7f3d-4326-868e-3002693d3414.svg'
SOURCE_HEAD_ICON_ID = 'corporal-2'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26


class Corporal2Avatar(Solo48):
    icon_id = 'corporal-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('corporal', '2', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_bezier('beret-left',(14,16),((8,16),(8,12),(12,10)))
        self.add_bezier('beret-crown',(12,10),((18,6),(30,4),(36,4)))
        self.add_bezier('beret-right',(36,4),((42,4),(40,12),(34,16)))
        self.add_line('beret-band',(34,16),(14,16))
        self.add_contour('beret','beret-left','beret-crown','beret-right','beret-band',closed=True)
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','face','beret')

        # Body cue: asymmetric uniform lapel; smooth shoulders remain primary.
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
        self.add_line('body-lapel',(18,top),(28,44))
        self.relate('connect','body-lapel','body-top')

        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
