"""A child playing with a toy car: a kneeling child pushing a small pickup truck along the floor.

Symbol plan: the toy pickup (left) is one open outline - front wall, low hood, slanted
windscreen, cab roof, cab back, bed, rear wall - whose feet are the two wheels: each wheel
is a ring (r3, the approved 6-diameter circle) whose left/right points are shared with the
walls and the short bottom line between the wheels, so the wheels overlap the body line as
in the reference. The child (right) follows the shared full-body reference with a child's
large head: ring head (r4) straight above the neck, exactly 8 on centerlines (4 units of
ink); a straight torso and thigh down to the knee; the shin along the floor behind; one
arm reaching down to the truck's rear wall (shared endpoint: the child pushes the car).
The reference's crawling pose is stood up to kneeling: a crawl needs a diagonal head gap
the checker cannot certify and more width than the canvas leaves beside the truck.
Lucide construction: 'truck'/'car' profile with wheels on the body line; figure from
icon_set/references/human_ref/full_body_ref.png.
Keyshape HRECT_L: centerline x 4..44 (truck front, foot), y 8..40 (head top, wheels / shin).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d2b08eed-cd59-4667-ba85-d70a3d670bef"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__child-playing-with-toy-car/20260926T034135Z-thuan-mac/reference/family child play car_d2b08eed-cd59-4667-ba85-d70a3d670bef.svg"
AUTHOR = "claude-opus-5-5"


class ChildPlayingWithToyCar(Solo48):
    icon_id = "child-playing-with-toy-car"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/activity"
    aliases = ("child play car", "kid with toy car")
    keywords = ("child", "kid", "toy", "car", "truck", "play", "family", "toddler", "playtime")

    def build(self) -> None:
        # truck
        front, rear, deck, roof, axle, wr = 4, 24, 25, 19, 37, 3
        w1, w2 = front + wr, rear - wr
        self.add_line("front-wall", (front, axle), (front, deck))
        self.add_line("hood", (front, deck), (8, deck))
        self.add_line("windscreen", (8, deck), (10, roof))
        self.add_line("roof", (10, roof), (18, roof))
        self.add_line("cab-back", (18, roof), (18, deck))
        self.add_line("bed", (18, deck), (rear, deck))
        push = (rear, 31)
        self.add_line("rear-wall-high", (rear, deck), push)
        self.add_line("rear-wall-low", push, (rear, axle))
        self.add_contour("truck", "front-wall", "hood", "windscreen", "roof", "cab-back", "bed",
                         "rear-wall-high", "rear-wall-low")
        self.add_line("underside", (w1 + wr, axle), (w2 - wr, axle))
        for name, cx in (("wheel-front", w1), ("wheel-rear", w2)):
            pts = [(cx - wr, axle), (cx, axle - wr), (cx + wr, axle), (cx, axle + wr)]
            names = [f"{name}-{q}" for q in ("nw", "ne", "se", "sw")]
            for i, n in enumerate(names):
                self.add_arc(n, pts[i], pts[(i + 1) % 4], radius_x=wr)
            self.add_contour(name, *names, closed=True)
            self.relate("connect", "truck", name)
            self.relate("connect", "underside", name)
        # child
        hx, hy, hr = 33, 12, 4
        neck = (hx, hy + hr + 8)
        knee = (hx, 40)
        pts = [(hx - hr, hy), (hx, hy - hr), (hx + hr, hy), (hx, hy + hr)]
        names = ("head-nw", "head-ne", "head-se", "head-sw")
        for i, name in enumerate(names):
            self.add_arc(name, pts[i], pts[(i + 1) % 4], radius_x=hr)
        self.add_contour("head", *names, closed=True)
        self.add_line("torso", neck, (hx, 32))
        self.add_line("thigh", (hx, 32), knee)
        self.add_line("shin", knee, (44, 40))
        self.add_contour("body", "torso", "thigh", "shin")
        self.mark_human_figure("child", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", neck, push)
        self.relate("connect", "body", "arm")
        self.relate("connect", "arm", "truck")
