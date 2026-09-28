"""A camera drone seen from the front: rotors on posts, a pill body, curved landing legs and a gimbal camera.

Symbol plan: symmetric about x=24. Each rotor is a horizontal blade line with a post down
to the body top (shared endpoints). The body is one closed pill (r4 end caps, 8 tall)
whose top rises in a smooth central bump. Each landing leg is one arc of a circle
(r15, centre (24,34)) leaving the body bottom, then a straight drop and a short outward
foot. The gimbal camera is a circle (r4) inside the legs, 9 below the body.
The reference's centre dot in the camera is dropped (a dot needs an r8 ring).
Lucide construction: 'drone' has no local match; 'camera'/'circle' construction for the
gimbal and a capsule for the body.
Keyshape SQUARE: centerline x 6..42 (body caps), y 6..42 (rotor blades, feet).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d66af9da-0871-557c-abb0-a240e310287a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__camera-drone-front/20260926T034135Z-thuan-mac/reference/drone camera_d66af9da-0871-557c-abb0-a240e310287a.svg"
AUTHOR = "claude-opus-5-5"


class CameraDroneFront(Solo48):
    icon_id = "camera-drone-front"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("drone", "quadcopter", "camera drone")
    keywords = ("drone", "quadcopter", "camera", "aerial", "uav", "rotor", "flying")

    def build(self) -> None:
        ax = 24
        blade_y, top, bot, cap = 6, 14, 22, 4
        post = 10  # left post x; right mirrored
        leg_c, leg_r = (24, 34), 15

        def m(x):
            return 2 * ax - x

        # rotors
        for side, sx in (("l", 1), ("r", -1)):
            px = post if sx == 1 else m(post)
            self.add_line(f"blade-{side}-out", (px - 4 * sx, blade_y), (px, blade_y))
            self.add_line(f"blade-{side}-in", (px, blade_y), (px + 4 * sx, blade_y))
            self.add_line(f"post-{side}", (px, blade_y), (px, top))
            self.relate("connect", f"blade-{side}-out", f"post-{side}")
            self.relate("connect", f"blade-{side}-in", f"post-{side}")
        # body pill with a central bump on top
        self.add_arc("cap-l", (post, bot), (post, top), radius_x=cap)
        self.add_line("top-l", (post, top), (17, top))
        self.add_bezier("bump", (17, top), ((20, top), (21, 11), (ax, 11)),
                        ((27, 11), (28, top), (m(17), top)))
        self.add_line("top-r", (m(17), top), (m(post), top))
        self.add_arc("cap-r", (m(post), top), (m(post), bot), radius_x=cap)
        self.add_line("bot-r", (m(post), bot), (m(15), bot))
        self.add_line("bot-m", (m(15), bot), (15, bot))
        self.add_line("bot-l", (15, bot), (post, bot))
        self.add_contour("body", "cap-l", "top-l", "bump", "top-r", "cap-r",
                         "bot-r", "bot-m", "bot-l", closed=True)
        for side in ("l", "r"):
            self.relate("connect", f"post-{side}", "body")
        # landing legs
        self.add_arc("leg-l-arc", (15, bot), (leg_c[0] - leg_r, leg_c[1]), radius_x=leg_r, sweep=False)
        self.add_line("leg-l-drop", (leg_c[0] - leg_r, leg_c[1]), (9, 42))
        self.add_line("leg-l-foot", (9, 42), (6, 42))
        self.add_contour("leg-l", "leg-l-arc", "leg-l-drop", "leg-l-foot")
        self.add_arc("leg-r-arc", (m(15), bot), (leg_c[0] + leg_r, leg_c[1]), radius_x=leg_r, sweep=True)
        self.add_line("leg-r-drop", (leg_c[0] + leg_r, leg_c[1]), (m(9), 42))
        self.add_line("leg-r-foot", (m(9), 42), (m(6), 42))
        self.add_contour("leg-r", "leg-r-arc", "leg-r-drop", "leg-r-foot")
        self.relate("connect", "body", "leg-l")
        self.relate("connect", "body", "leg-r")
        # gimbal camera
        cy, cr = 35, 4
        pts = [(ax - cr, cy), (ax, cy - cr), (ax + cr, cy), (ax, cy + cr)]
        names = ("cam-nw", "cam-ne", "cam-se", "cam-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=cr)
        self.add_contour("camera", *names, closed=True)
