from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5fc3beee-fe11-4737-8f05-c292e2c4f15d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-cannabis-leaves-on-stems/20260927T080808Z-thuan-mac-1/reference/cannabis tree_5fc3beee-fe11-4737-8f05-c292e2c4f15d.svg'
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
    icon_id = 'two-cannabis-leaves-on-stems'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'cannabis'
    categories = ('primitives', 'cannabis')
    aliases = ()
    keywords = ('two', 'cannabis', 'leaves', 'on', 'stems')

    def build(self) -> None:
        # Plan: two palmate cannabis leaves on stems as in the reference - a large 5-leaflet leaf
        # upper right and a small 5-leaflet leaf lower left. Leaflets are single strokes fanned
        # upward from each leaf's base, longest in the middle and shortening outward (the
        # palmate cannabis pattern); each leaf has its own stem to the ground at y42.
        import math

        def fan(name, base, rays):
            names = []
            for i, (a, length) in enumerate(rays):
                t = math.radians(a)
                tip = (round(base[0] + length * math.sin(t)), round(base[1] - length * math.cos(t)))
                self.add_line(f"{name}-{i}", base, tip); names.append(f"{name}-{i}")
            return names

        big = fan("leaflet-big", (29, 21), [(-66, 14), (-33, 13), (0, 15), (33, 13), (66, 14)])
        small = fan("leaflet-small", (13, 33), [(-80, 7), (-40, 9), (0, 10), (40, 9), (80, 7)])
        self.add_line("stem-big", (29, 21), (29, 42))
        self.add_line("stem-small", (13, 33), (15, 42))
        self.relate("connect", "stem-big", *big)
        self.relate("connect", "stem-small", *small)
