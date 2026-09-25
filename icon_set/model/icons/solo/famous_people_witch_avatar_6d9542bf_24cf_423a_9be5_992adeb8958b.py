"""Witch in a bent pointed hat with curved cape with a central opening.

Plan: separate head/hair or headwear symbol, painted head/body contact, curved torso
with curved cape with a central opening. SOLO48 VRECT_L visible ink (6,2)-(42,46);
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
SOURCE_ICON_ID = '6d9542bf-24cf-423a-9be5-992adeb8958b'
SOURCE_PATH = 'pictographic-primitives/avatars/famous people witch_6d9542bf-24cf-423a-9be5-992adeb8958b.svg'
SOURCE_HEAD_ICON_ID = 'famous-people-witch'
AUTHOR = 'gpt-6'
HUMAN_REFERENCE = 'icon_set/references/human_ref/user.svg'
HEAD_BOTTOM = 30

class FamousPeopleWitchAvatar(Solo48):
    icon_id = 'famous-people-witch-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('famous', 'people', 'witch', 'portrait', 'bust')

    def build(self):
        """Centerline review: preserve the silhouette; remove duplicated ink and split real attachments into shared nodes."""
        self.add_polyline('hat', (10, 20), (22, 4), (38, 4), (30, 12), (36, 20))
        self.add_polyline('brim', (8, 20), (10, 20), (14, 20), (34, 20), (36, 20), (40, 20))
        self.relate('connect', 'hat', 'brim')
        self.add_arc('face', (34, 20), (14, 20), radius_x=10, radius_y=10)
        self.relate('connect', 'face', 'brim')
        top = HEAD_BOTTOM + HEAD_BODY_CENTERLINE_GAP
        self.add_line('body-left-side', (8, 44), (8, 42))
        self.add_arc('body-left-shoulder', (8, 42), (18, top), radius_x=10, radius_y=42 - top)
        self.add_contour('body-left', 'body-left-side', 'body-left-shoulder')
        self.add_line('body-top', (18, top), (24, top))
        self.add_line('body-top-right', (24, top), (30, top))
        self.add_arc('body-right-shoulder', (30, top), (40, 42), radius_x=10, radius_y=42 - top)
        self.add_line('body-right-side', (40, 42), (40, 44))
        self.add_contour('body-right', 'body-right-shoulder', 'body-right-side')
        self.relate('connect', 'body-left', 'body-top')
        self.relate('connect', 'body-top', 'body-top-right')
        self.relate('connect', 'body-top-right', 'body-right')
        self.add_line('body-fastening', (24, top), (24, 44))
        self.relate('connect', 'body-fastening', 'body-top')
        self.relate('connect', 'body-fastening', 'body-top-right')
        self.relate('connect', 'face', 'body-top')
        self.relate('connect', 'face', 'body-top-right')
