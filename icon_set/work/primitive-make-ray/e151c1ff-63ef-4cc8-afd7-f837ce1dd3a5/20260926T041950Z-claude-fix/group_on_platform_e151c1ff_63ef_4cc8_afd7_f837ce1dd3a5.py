"""A group of three people standing on a round platform, the middle one taller.

Human construction: icon_set/references/human_ref/full_body_ref.png and user.svg
(circular outlined heads over rounded torsos). Shared parameters: head radius 4, torso a
half-round crown 8 wide (r4); each head's
lowest point is exactly 8 above its torso crown on centerlines (4 visible) and the crown
is its nearest body point. The middle person (axis x=24) stands higher; the side people
(axes x=8 and x=40) stand 3 lower, their heads 8.3 from the middle head.
The platform is its front edge: a straight rim across the full width at y=40, 9 below
the side people and 12 below the middle one.
Lucide construction: 'users' - heads over rounded shoulders; an elliptical rim below.
Keyshape HRECT_L: centerline x 4..44 (side torsos, rim ends), y 8..40 (middle head, rim).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e151c1ff-63ef-4cc8-afd7-f837ce1dd3a5"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__group-on-platform/20260926T035939Z-thuan-mac/reference/multiple circle_e151c1ff-63ef-4cc8-afd7-f837ce1dd3a5.svg"
AUTHOR = "claude-opus-5-5"


class GroupOnPlatform(Solo48):
    icon_id = "group-on-platform"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ("multiple-circle", "group", "team-on-stage")
    keywords = ("group", "team", "people", "users", "community", "platform", "stage", "crowd", "members")

    def build(self) -> None:
        for name, x, crown_y in (("left", 8, 27), ("middle", 24, 24), ("right", 40, 27)):
            hy = crown_y - 8 - 4
            base = crown_y + 4
            self.add_arc(f"{name}-head-top", (x - 4, hy), (x + 4, hy), radius_x=4, sweep=True)
            self.add_arc(f"{name}-head-bottom", (x + 4, hy), (x - 4, hy), radius_x=4, sweep=True)
            self.add_contour(f"{name}-head", f"{name}-head-top", f"{name}-head-bottom", closed=True)
            self.add_arc(f"{name}-crown-left", (x - 4, base), (x, crown_y), radius_x=4, sweep=True)
            self.add_arc(f"{name}-crown-right", (x, crown_y), (x + 4, base), radius_x=4, sweep=True)
            self.add_contour(f"{name}-torso", f"{name}-crown-left", f"{name}-crown-right")
            self.mark_human_figure(name, head=f"{name}-head", torso=f"{name}-crown-right", torso_junction="start")
        self.add_line("platform-rim", (4, 40), (44, 40))
