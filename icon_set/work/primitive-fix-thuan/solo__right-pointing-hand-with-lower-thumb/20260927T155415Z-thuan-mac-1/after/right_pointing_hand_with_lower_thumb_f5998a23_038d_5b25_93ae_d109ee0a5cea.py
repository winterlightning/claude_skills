"""Right pointing hand with a low thumb, redrawn from the claimed reference."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f5998a23-038d-5b25-93ae-d109ee0a5cea"
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__right-pointing-hand-with-lower-thumb/20260927T155415Z-thuan-mac-1/reference/hand pointer right_f5998a23-038d-5b25-93ae-d109ee0a5cea.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = "right-pointing-hand-with-lower-thumb"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ("hand", "right", "point", "finger", "thumb", "gesture")

    def build(self):
        # One continuous gesture preserves the open spaces between fingers.
        steps = [
            ("C", (4, 12), (10, 8), (18, 8)),
            ("L", (25, 8)),
            ("C", (29, 8), (31, 12), (27, 15)),
            ("C", (33, 14), (35, 18), (30, 20)),
            ("C", (36, 20), (37, 24), (32, 26)),
            ("L", (40, 26)),
            ("C", (44, 26), (44, 28), (44, 30)),
            ("C", (44, 32), (42, 34), (40, 34)),
            ("L", (22, 34)),
            ("C", (28, 37), (27, 40), (22, 40)),
            ("L", (9, 32)),
            ("C", (5, 29), (4, 26), (4, 20)),
        ]
        p = (4, 20)
        members = []
        for i, step in enumerate(steps):
            name = f"outline-{i}"
            if step[0] == "L":
                self.add_line(name, p, step[1])
                p = step[1]
            else:
                self.add_bezier(name, p, (step[1], step[2], step[3]))
                p = step[3]
            members.append(name)
        self.add_contour("hand", *members, closed=True)
