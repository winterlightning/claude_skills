"""Avatar family: standalone head and body, without container hosting anchors."""
from ... import contracts
from ...keyshapes import Keyshape
from ...profiles import Profile, STROKE_WIDTH
from ..family import FamilyIcon

PROFILE = Profile.for_family("avatar")
CANVAS = PROFILE.spec.canvas_size
CENTER = PROFILE.spec.center
HEAD_BODY_INK_GAP = contracts.icon_profile()["profiles"][PROFILE.name]["head_body_ink_gap"]
HEAD_BODY_CENTERLINE_GAP = HEAD_BODY_INK_GAP + STROKE_WIDTH


class Avatar48(FamilyIcon):
    family = "avatar"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/avatars"
