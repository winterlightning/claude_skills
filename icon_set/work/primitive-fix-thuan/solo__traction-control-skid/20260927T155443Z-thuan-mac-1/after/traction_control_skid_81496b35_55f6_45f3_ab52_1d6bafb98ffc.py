from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "81496b35-55f6-45f3-ab52-1d6bafb98ffc"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__traction-control-skid/20260927T155443Z-thuan-mac-1/reference/traction control_81496b35-55f6-45f3-ab52-1d6bafb98ffc.svg"
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
PLAN = "Car seen from behind (cabin trapezoid over a body box) above two S-shaped skid marks, all mirrored about x=24."
CONSTRUCTION_REFERENCES = "Lucide car: cabin over a body band; skid marks as single cubic S curves whose control hulls stay 9 below the body."
OMISSIONS = "Tail lights and wheel stubs dropped: no 8-unit room inside a 10-unit body band or between body and skids."


class Drawing(Solo48):
    icon_id = "traction-control-skid"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ("esp-warning", "stability-control")
    keywords = ("traction control", "skid", "slippery", "esp", "stability", "dashboard", "car", "warning")

    def build(self):
        path(self, "body", (6, 16), [("L", (13, 16)), ("L", (35, 16)), ("L", (42, 16)), ("L", (42, 26)), ("L", (6, 26)), ("L", (6, 16))], closed=True)
        path(self, "cabin", (13, 16), [("L", (16, 6)), ("L", (32, 6)), ("L", (35, 16))]); join(self, "cabin", "body")
        self.add_bezier("skid-left", (6, 35), ((18, 35), (6, 42), (18, 42)))
        self.add_bezier("skid-right", (30, 35), ((42, 35), (30, 42), (42, 42)))
