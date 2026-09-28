from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "bf69141f-78b0-4910-b341-912076827fbd"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__torch-relay-runner/20260927T155443Z-thuan-mac-1/reference/olympics torch_bf69141f-78b0-4910-b341-912076827fbd.svg"
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
PLAN = "Running stick figure (round head, upright torso, back arm, striding legs) holding an upright torch on the right; the torch is a stick under a pointed flame drop."
CONSTRUCTION_REFERENCES = "icon_set/references/human_ref/full_body_ref.png: circular head, round-ended limbs, minimal anatomy; head r4 at (16,10), torso (16,22)-(16,32), outline-to-torso gap 8 centerline / 4 ink. Flame from Lucide droplet inverted."
OMISSIONS = "Flame inner tongue and doubled body outlines dropped."


class Drawing(Solo48):
    icon_id = "torch-relay-runner"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports"
    aliases = ("olympic-torch-bearer", "torchbearer")
    keywords = ("torch", "relay", "runner", "flame", "athletics", "olympics", "sport")

    def build(self):
        path(self, "head", (12, 10), [("A", (20, 10), 4, 4, True), ("A", (12, 10), 4, 4, True)], closed=True)
        self.add_line("torso", (16, 22), (16, 32))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm-back", (16, 22), (7, 26)); join(self, "arm-back", "torso")
        path(self, "arm-front", (16, 22), [("L", (27, 26)), ("L", (37, 26))]); join(self, "arm-front", "torso")
        path(self, "leg-front", (16, 32), [("L", (24, 38)), ("L", (32, 42))]); join(self, "leg-front", "torso")
        path(self, "leg-back", (16, 32), [("L", (10, 36)), ("L", (6, 42))]); join(self, "leg-back", "torso")
        join(self, "leg-front", "leg-back")
        path(self, "stick", (37, 18), [("L", (37, 26)), ("L", (37, 30))]); join(self, "stick", "arm-front")
        path(self, "flame", (37, 6), [("A", (32, 13), 8, 8, False), ("A", (37, 18), 5, 5, False), ("A", (42, 13), 5, 5, False), ("A", (37, 6), 8, 8, False)], closed=True)
        join(self, "flame", "stick")
