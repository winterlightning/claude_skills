from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "fc615adc-97ee-5f84-9531-39dc64ae388f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__touring-bicycle/20260927T155443Z-thuan-mac-1/reference/touring bike_fc615adc-97ee-5f84-9531-39dc64ae388f.svg"
AUTHOR = "claude-fable-5-1"


def path(s, name, start, commands, closed=False):
    """Chain of L/A/C commands into one contour. A: (end, rx, ry, sweep[, large])."""
    here = start
    members = []
    for i, (kind, end, *args) in enumerate(commands):
        k = f"{name}-{i}"
        if kind == "L":
            s.add_line(k, here, end)
        elif kind == "A":
            s.add_arc(k, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2],
                      large_arc=args[3] if len(args) > 3 else False)
        elif kind == "C":
            s.add_bezier(k, here, (args[0], args[1], end))
        members.append(k)
        here = end
    s.add_contour(name, *members, closed=closed)
    return name


def join(s, a, b):
    s.relate("connect", a, b)
PLAN = "Two r7 wheels, a frame triangle above them (saddle tube, top tube, head tube) with stays and fork dropping to lattice points on the rims, a saddle extension and a raised handlebar."
CONSTRUCTION_REFERENCES = "Lucide bike: two equal wheels, a diamond-style frame, saddle left and handlebar right; frame members end on rim cardinal points instead of crossing the rims."
OMISSIONS = "Pedal crank, rack and second down tube dropped."


class Drawing(Solo48):
    icon_id = "touring-bicycle"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("bicycle", "bike", "touring-bike")
    keywords = ("touring bike", "bicycle", "bike", "cycling", "travel", "road bike", "pedal", "transport")

    def build(self):
        for side, cx in (("rear", 11), ("front", 37)):
            path(self, f"{side}-wheel", (cx, 26), [("A", (cx + 7, 33), 7, 7, True), ("A", (cx, 40), 7, 7, True), ("A", (cx - 7, 33), 7, 7, True), ("A", (cx, 26), 7, 7, True)], closed=True)
        path(self, "top-tube", (10, 12), [("L", (14, 12)), ("L", (34, 12))])
        path(self, "down-tubes", (14, 12), [("L", (24, 24)), ("L", (34, 12))]); join(self, "top-tube", "down-tubes")
        self.add_line("seat-stay", (14, 12), (11, 26)); join(self, "seat-stay", "top-tube"); join(self, "seat-stay", "rear-wheel"); join(self, "seat-stay", "down-tubes")
        self.add_line("fork", (34, 12), (37, 26)); join(self, "fork", "top-tube"); join(self, "fork", "front-wheel"); join(self, "fork", "down-tubes")
        self.add_line("chain-stay", (24, 24), (18, 33)); join(self, "chain-stay", "down-tubes"); join(self, "chain-stay", "rear-wheel")
        self.add_line("front-stay", (24, 24), (30, 33)); join(self, "front-stay", "down-tubes"); join(self, "front-stay", "front-wheel"); join(self, "chain-stay", "front-stay")
        self.add_line("handlebar", (34, 12), (38, 8)); join(self, "handlebar", "top-tube"); join(self, "handlebar", "fork")
