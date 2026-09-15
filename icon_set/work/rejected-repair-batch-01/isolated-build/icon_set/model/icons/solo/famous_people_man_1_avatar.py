"""Man with a large swept quiff with open-collar stage jacket.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with open-collar stage jacket. SOLO48 VRECT_L visible ink (6,2)-(42,46);
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

SOURCE_ICON_ID = 'e17e1056-a4a0-4c20-a5ed-799d92f9a6f0'
SOURCE_PATH = 'pictographic-primitives/avatars/famous people man_e17e1056-a4a0-4c20-a5ed-799d92f9a6f0.svg'
SOURCE_HEAD_ICON_ID = 'famous-people-man-1'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 26


class FamousPeopleMan1Avatar(Solo48):
    icon_id = 'famous-people-man-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('famous', 'people', 'man', '1', 'portrait', 'bust')

    def build(self):
        # Head construction preserves the reference's identifying silhouette.
        self.add_bezier('hair-left',(14,16),((8,14),(10,4),(20,4)))
        self.add_bezier('quiff',(20,4),((28,4),(34,10),(40,6)))
        self.add_bezier('hair-right',(40,6),((40,12),(36,16),(34,16)))
        self.add_bezier('fringe',(34,16),((28,16),(20,12),(14,16)))
        self.add_contour('hair','hair-left','quiff','hair-right','fringe',closed=True)
        self.add_arc('face',(34,16),(14,16),radius_x=10,radius_y=10)
        self.relate('connect','hair','face')

        # Body cue: open-collar stage jacket; smooth shoulders remain primary.
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
