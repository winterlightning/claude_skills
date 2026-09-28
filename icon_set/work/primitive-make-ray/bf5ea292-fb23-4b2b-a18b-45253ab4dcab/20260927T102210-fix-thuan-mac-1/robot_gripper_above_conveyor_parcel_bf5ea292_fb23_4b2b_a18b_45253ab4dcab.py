from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'bf5ea292-fb23-4b2b-a18b-45253ab4dcab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__robot-gripper-above-conveyor-parcel/20260927T101542Z-thuan-mac-1/reference/factory assembly line belt arm box_bf5ea292-fb23-4b2b-a18b-45253ab4dcab.svg'
AUTHOR = "claude-opus-5-5"


def _path(icon, name, start, steps, closed=False):
    """steps: (x, y) line | ((x, y), rx, ry, sweep[, large]) arc | ('c', c1, c2, end) cubic."""
    members, point = [], start
    for i, step in enumerate(steps):
        member = f"{name}-{i + 1}"
        if step[0] == 'c':
            icon.add_bezier(member, point, (step[1], step[2], step[3])); point = step[3]
        elif isinstance(step[0], (int, float)):
            icon.add_line(member, point, step); point = step
        else:
            end, rx, ry, sweep = step[:4]
            large = step[4] if len(step) > 4 else False
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep, large_arc=large); point = end
        members.append(member)
    icon.add_contour(name, *members, closed=closed)
    return members


def _circle(icon, name, cx, cy, r):
    """Full circle from four cardinal quarter arcs (certifiable spacing)."""
    return _path(icon, name, (cx, cy - r), [((cx + r, cy), r, r, True), ((cx, cy + r), r, r, True),
                                            ((cx - r, cy), r, r, True), ((cx, cy - r), r, r, True)], True)


class Drawing(Solo48):
    icon_id = 'robot-gripper-above-conveyor-parcel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('factory', 'automation', 'industry', 'manufacturing', 'production', 'machine', 'robot', 'process')

    def build(self) -> None:
        # Plan: conveyor belt = r4 pill across the bottom; taped parcel box standing on
        # the belt's top run (shared nodes); open two-finger gripper on an r3 wrist hub
        # hangs above the parcel, jaws spread wider than the box.
        self.add_line("belt-top-left", (12, 36), (16, 36))
        self.add_line("belt-top-mid", (16, 36), (32, 36))
        self.add_line("belt-top-right", (32, 36), (36, 36))
        self.add_arc("belt-right", (36, 36), (36, 44), radius_x=4, radius_y=4, sweep=True)
        self.add_line("belt-bottom", (36, 44), (12, 44))
        self.add_arc("belt-left", (12, 44), (12, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_contour("belt", "belt-top-left", "belt-top-mid", "belt-top-right", "belt-right",
                         "belt-bottom", "belt-left", closed=True)
        _path(self, "box", (16, 36), [(16, 20), (32, 20), (32, 36)], False)
        self.add_line("tape", (24, 20), (24, 26))
        self.relate("connect", "box", "belt")
        self.relate("connect", "tape", "box")
        _circle(self, "wrist", 24, 7, 3)
        _path(self, "jaw-left", (21, 7), [(10, 10), (10, 14)], False)
        _path(self, "jaw-right", (27, 7), [(38, 10), (38, 14)], False)
        self.relate("connect", "jaw-left", "wrist")
        self.relate("connect", "jaw-right", "wrist")
