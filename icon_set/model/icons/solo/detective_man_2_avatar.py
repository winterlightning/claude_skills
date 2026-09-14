"""Detective in a notched fedora with trench coat with a diagonal lapel.

Plan: separate head/hair or headwear symbol, exact detached gap, curved torso
with trench coat with a diagonal lapel. SOLO48 VRECT_L visible ink (6,2)-(42,46);
centerline extremes (8,4)-(40,44). Head bottom 26, body top 34;
nearest painted head/body gap is 4 on the shared x24 shoulder plateau.
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
SOURCE_PATH = 'work/head-solo/batch-02/references/detective-man-2.svg'
SOURCE_HEAD_ICON_ID = 'detective-man-2'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26


class DetectiveMan2Avatar(Solo48):
    icon_id = 'detective-man-2-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('detective', 'man', '2', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_polyline('hat',(12,16),(15,4),(24,8),(33,4),(36,16),(12,16))
        self.add_polyline('brim',(8,16),(12,16),(14,16),(34,16),(36,16),(40,16))
        self.relate('connect','hat','brim')
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','face','brim')

        # Body cue: trench coat with a diagonal lapel; smooth shoulders remain primary.
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
        self.add_line('body-lapel',(18,top),(32,44))
        self.relate('connect','body-lapel','body-top')
