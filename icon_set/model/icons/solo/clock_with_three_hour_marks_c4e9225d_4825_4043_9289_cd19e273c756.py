"""Clock with Three Hour Marks.

Plan: One radius-20 clock, three attached cardinal hour marks and a joined pair of hands. Center (24,24).
Construction references: Lucide clock: circular face and one joined hand stroke.
Simplification: Hour marks shortened and attached to rim to preserve clear space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c4e9225d-4825-4043-9289-cd19e273c756'
SOURCE_PATH = 'pictographic-primitives/business/time clock_c4e9225d-4825-4043-9289-cd19e273c756.svg'
AUTHOR = 'gpt-6'

def path(icon, name, start, *steps, closed=False):
    """Emit one coherent stroke; each knot belongs to its owning shape."""
    members = []
    point = start
    for index, step in enumerate(steps):
        member = f"{name}-{index + 1}"
        kind, end, *args = step
        if kind == "L":
            icon.add_line(member, point, end)
        elif kind == "A":
            rx, ry, sweep = args
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
        elif kind == "B":
            icon.add_bezier(member, point, (args[0], args[1], end))
        members.append(member)
        point = end
    icon.add_contour(name, *members, closed=closed)


def circle(icon, name, cx, cy, radius):
    path(icon, name, (cx-radius, cy),
         ("A", (cx, cy-radius), radius, radius, True),
         ("A", (cx+radius, cy), radius, radius, True),
         ("A", (cx, cy+radius), radius, radius, True),
         ("A", (cx-radius, cy), radius, radius, True), closed=True)


class ClockWithThreeHourMarks(Solo48):
    icon_id = 'clock-with-three-hour-marks'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('clock', 'with', 'three', 'hour', 'marks')

    def build(self):
        circle(self,'face',24,24,20)
        self.add_polyline('hands',(24,13),(24,24),(17,31))
        for name,start,end in [('left',(4,24),(7,24)),('right',(44,24),(41,24)),('bottom',(24,44),(24,41))]:
            self.add_line('hour-'+name,start,end)
            self.relate('connect','face','hour-'+name)
