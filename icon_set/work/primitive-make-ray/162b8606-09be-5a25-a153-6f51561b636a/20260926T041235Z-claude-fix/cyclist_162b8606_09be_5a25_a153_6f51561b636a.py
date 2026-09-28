"""A cyclist riding a bicycle: rider leaning forward over two wheels, hands on the bars.

Human construction: icon_set/references/human_ref/full_body_ref.png (stick figure:
circular outlined head, single-stroke torso and limbs). The torso rises from the hip
(18,26) through the shoulder A=(23,18) to the neck N=(24,16); the head (r2, the approved
4x4 small circle, a solid dot at 48px as in common cyclist glyphs) is centred (30,8), continuing the forward lean (N + (6,-8)), so its
outline is exactly 10 - 2 = 8 from the neck on centerlines (4 visible) and N is the
nearest body point. The arm runs from the shoulder to the handlebar; the leg bends at
the knee down to the pedal. The fork drops from the bar to the top of the front wheel.
Wheels are r5 circles at the bottom corners; the hip sits 8 clear of the rear wheel and the
handlebar 10 above the front wheel.
Lucide construction: 'bike' - two circles with straight frame strokes.
Keyshape SQUARE: centerline x 6..42 (wheels), y 6..42 (head top, wheel bottoms).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "162b8606-09be-5a25-a153-6f51561b636a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__cyclist/20260926T035939Z-thuan-mac/reference/fitness bicycle_162b8606-09be-5a25-a153-6f51561b636a.svg"
AUTHOR = "claude-opus-5-5"


class Cyclist(Solo48):
    icon_id = "cyclist"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/cycling"
    aliases = ("fitness-bicycle", "bicycle-rider", "biker")
    keywords = ("cyclist", "bicycle", "bike", "cycling", "ride", "fitness", "sport", "exercise", "rider")

    def _circle(self, name, c, r):
        self.add_arc(f"{name}-top", (c[0] - r, c[1]), (c[0] + r, c[1]), radius_x=r, sweep=True)
        self.add_arc(f"{name}-bottom", (c[0] + r, c[1]), (c[0] - r, c[1]), radius_x=r, sweep=True)
        self.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)

    def build(self) -> None:
        self._circle("head", (30, 8), 2)
        self._circle("wheel-rear", (11, 37), 5)
        # front wheel split at its top so the fork can end there
        self.add_arc("wheel-front-1", (32, 37), (37, 32), radius_x=5, sweep=True)
        self.add_arc("wheel-front-2", (37, 32), (42, 37), radius_x=5, sweep=True)
        self.add_arc("wheel-front-3", (42, 37), (32, 37), radius_x=5, sweep=True)
        self.add_contour("wheel-front", "wheel-front-1", "wheel-front-2", "wheel-front-3", closed=True)
        Hp, A, N = (18, 26), (23, 18), (24, 16)
        self.add_line("torso-upper", N, A)
        self.add_line("torso-lower", A, Hp)
        self.add_contour("torso", "torso-upper", "torso-lower")
        self.add_line("arm", A, (32, 22))
        self.add_line("handlebar", (32, 22), (37, 22))
        self.add_line("fork", (35, 22), (37, 32))
        self.add_polyline("leg", Hp, (24, 30), (24, 38))
        for a, b in (("torso", "arm"), ("torso", "leg"), ("arm", "handlebar"), ("handlebar", "fork"),
                     ("fork", "wheel-front")):
            self.relate("connect", a, b)
        self.mark_human_figure("rider", head="head", torso="torso-upper", torso_junction="start")
