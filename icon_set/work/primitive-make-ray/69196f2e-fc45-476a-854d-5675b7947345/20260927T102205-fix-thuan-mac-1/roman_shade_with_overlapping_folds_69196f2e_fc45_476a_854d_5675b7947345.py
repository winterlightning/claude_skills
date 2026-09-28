from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '69196f2e-fc45-476a-854d-5675b7947345'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__roman-shade-with-overlapping-folds/20260927T101542Z-thuan-mac-1/reference/roman shade closed_69196f2e-fc45-476a-854d-5675b7947345.svg'
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
    icon_id = 'roman-shade-with-overlapping-folds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('roman', 'shade', 'with', 'overlapping', 'folds')

    def build(self) -> None:
        # Plan: r4 pill headrail across the top; pull cord hangs from the rail's left
        # end to an r3 ring; fabric hangs below the rail as two stacked folds, the
        # upper fold's hem flaring out past the fold below it (overlap).
        self.add_line("rail-top", (10, 6), (38, 6))
        self.add_arc("rail-right", (38, 6), (38, 14), radius_x=4, radius_y=4, sweep=True)
        self.add_line("rail-bottom-a", (38, 14), (21, 14))
        self.add_line("rail-bottom-b", (21, 14), (10, 14))
        self.add_arc("rail-left", (10, 14), (10, 6), radius_x=4, radius_y=4, sweep=True)
        self.add_contour("rail", "rail-top", "rail-right", "rail-bottom-a", "rail-bottom-b", "rail-left", closed=True)
        self.add_line("cord", (10, 14), (10, 36))
        _circle(self, "cord-ring", 10, 39, 3)
        self.relate("connect", "cord", "rail")
        self.relate("connect", "cord", "cord-ring")
        _path(self, "fold1", (21, 14), [(18, 28), (27, 28)], False)
        self.add_line("fold1-hem", (27, 28), (38, 28))
        _path(self, "fold2", (27, 28), [(24, 42), (38, 42)], False)
        self.add_line("shade-right-a", (38, 14), (38, 28))
        self.add_line("shade-right-b", (38, 28), (38, 42))
        for a, b in (("rail", "fold1"), ("rail", "shade-right-a"), ("fold1", "fold1-hem"), ("fold1", "fold2"),
                     ("fold1-hem", "fold2"), ("fold1-hem", "shade-right-a"), ("shade-right-a", "shade-right-b"),
                     ("fold2", "shade-right-b"), ("fold1-hem", "shade-right-b")):
            self.relate("connect", a, b)
