"""A bride and groom standing side by side: groom in a V-collared jacket, bride in veil and gown.

Human construction: icon_set/references/human_ref/full_body_ref.png (restroom-style
figures: circular outlined head, simple torso shapes, straight legs, flared dress) and
user.svg (rounded shoulders, head-to-body proportions).
Groom (axis x=13): circular head r5 at (13,11). The jacket's V collar starts at (8,23)
and (18,23), both exactly 13 from the head centre, so the detached head sits exactly 8
from its body on centerlines (4 visible) and those collar corners are the body points
nearest the head. Rounded cubic shoulders fall to the sides x 6 and 20; the hem at y=36
leaves 8 below the collar point; legs 8 apart run to y=42.
Bride (axis x=35): the veil is a hood - an r5 arch over the head falling straight to the
shoulders at y=23 - so her head is framed by the veil and attached to the body (no
detached-head flag). A V neckline joins the veil ends; the gown flares from the shoulders
(30..40) to the hem (28..42).
Lucide construction: 'users' - circular heads, simple rounded shoulders, figures spaced
8 apart.
Keyshape SQUARE: centerline x 6..42 (jacket side, hem), y 6..42 (heads, feet/hem).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ba426bfa-e027-4bc0-9121-dc4823da6704"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bride-and-groom/20260926T030905Z-thuan-mac/reference/wedding bride groom_ba426bfa-e027-4bc0-9121-dc4823da6704.svg"
AUTHOR = "claude-opus-5-5"

HEAD_R, HEAD_Y, SHOULDER_Y = 5, 11, 23


class BrideAndGroom(Solo48):
    icon_id = "bride-and-groom"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/events"
    aliases = ("wedding-bride-groom", "wedding-couple", "newlyweds")
    keywords = ("wedding", "bride", "groom", "couple", "marriage", "veil", "gown", "suit", "people")

    def build(self) -> None:
        # groom
        g, hem = 13, 36
        top, bottom = (g - HEAD_R, HEAD_Y), (g + HEAD_R, HEAD_Y)
        self.add_arc("groom-head-top", top, bottom, radius_x=HEAD_R, sweep=True)
        self.add_arc("groom-head-bottom", bottom, top, radius_x=HEAD_R, sweep=True)
        self.add_contour("groom-head", "groom-head-top", "groom-head-bottom", closed=True)
        cl, cr, v = (g - 5, SHOULDER_Y), (g + 5, SHOULDER_Y), (g, SHOULDER_Y + 5)
        self.add_line("collar-left", cl, v)
        self.add_line("collar-right", v, cr)
        self.add_bezier("shoulder-right", cr, ((19.5, 23), (20, 25), (20, 28)))
        self.add_line("jacket-side-right", (20, 28), (20, hem))
        self.add_line("jacket-hem", (20, hem), (6, hem))
        self.add_line("jacket-side-left", (6, hem), (6, 28))
        self.add_bezier("shoulder-left", (6, 28), ((6, 25), (6.5, 23), cl))
        self.add_contour("jacket", "collar-left", "collar-right", "shoulder-right", "jacket-side-right",
                         "jacket-hem", "jacket-side-left", "shoulder-left", closed=True)
        self.add_line("groom-leg-left", (g - 4, hem), (g - 4, 42))
        self.add_line("groom-leg-right", (g + 4, hem), (g + 4, 42))
        self.relate("connect", "jacket", "groom-leg-left")
        self.relate("connect", "jacket", "groom-leg-right")
        self.mark_human_figure("groom", head="groom-head", torso="collar-left", torso_junction="start")
        # bride: veil hood over the head, V neckline, flared gown
        b = 35
        vl, vr = (b - HEAD_R, SHOULDER_Y), (b + HEAD_R, SHOULDER_Y)
        self.add_line("veil-left", vl, (b - HEAD_R, HEAD_Y))
        self.add_arc("veil-top", (b - HEAD_R, HEAD_Y), (b + HEAD_R, HEAD_Y), radius_x=HEAD_R, sweep=True)
        self.add_line("veil-right", (b + HEAD_R, HEAD_Y), vr)
        self.add_line("neckline-right", vr, (b, SHOULDER_Y + 4))
        self.add_line("neckline-left", (b, SHOULDER_Y + 4), vl)
        self.add_contour("veil", "veil-left", "veil-top", "veil-right", "neckline-right", "neckline-left",
                         closed=True)
        self.add_line("gown-side-left", vl, (b - 7, 42))
        self.add_line("gown-hem", (b - 7, 42), (b + 7, 42))
        self.add_line("gown-side-right", (b + 7, 42), vr)
        self.add_contour("gown", "gown-side-left", "gown-hem", "gown-side-right")
        self.relate("connect", "veil", "gown")
