from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'feb54050-e1d1-5584-98e2-cf2b2667eb4c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-reaching-toward-airflow-at-open-window/20260927T072841Z-thuan-mac-1/reference/air quality window open_feb54050-e1d1-5584-98e2-cf2b2667eb4c.svg'
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
    icon_id = 'person-reaching-toward-airflow-at-open-window'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'ecology'
    categories = ('primitives', 'ecology')
    aliases = ()
    keywords = ('window', 'person', 'airflow', 'air', 'fresh', 'ventilation', 'home', 'ecology')

    def build(self) -> None:
        # open window: frame with the left jamb open where the arm reaches through
        self.add_polyline("frame", (20, 12), (20, 6), (42, 6), (42, 42), (20, 42), (20, 36))
        # person inside (human ref full_body_ref.png): r3 head 8 above the torso, arm reaching out
        _circle(self, "head", 30, 18, 3)
        self.add_line("torso", (30, 29), (30, 34))
        self.mark_human_figure("person", head="head", torso="torso", torso_junction="start")
        self.add_line("arm", (30, 30), (12, 25))
        self.relate("connect", "torso", "arm")
        # airflow outside the window
        self.add_bezier("air-top", (6, 11), ((8, 7), (10, 15), (12, 11)))
        self.add_bezier("air-bottom", (6, 37), ((8, 33), (10, 41), (12, 37)))
