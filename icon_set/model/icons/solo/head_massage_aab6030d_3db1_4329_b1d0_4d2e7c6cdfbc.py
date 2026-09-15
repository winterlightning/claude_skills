"""Head Massage.

Plan: Therapist head radius 5 at (24,9); its rounded upper torso starts at (24,22), giving exactly 8 centerline units / 4 ink units below the head. Mirrored hands meet a larger client head. Bounds (8,4)-(40,44).
Construction references: human_ref/user.svg and full_body_ref.png: circular heads and smooth shoulders.
Simplification: Client shoulders and lower body omitted to let the head and two massaging hands read clearly.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aab6030d-3db1-4329-b1d0-4d2e7c6cdfbc'
SOURCE_PATH = 'pictographic-primitives/beauty/thai massage head_aab6030d-3db1-4329-b1d0-4d2e7c6cdfbc.svg'
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


class HeadMassage(Solo48):
    icon_id = 'head-massage'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('head', 'massage')

    def build(self):
        axis = 24
        circle(self,'therapist-head',axis,9,5)
        circle(self,'client-head',axis,37,7)
        for side in (-1,1):
            x=lambda value: axis+side*value
            name='left' if side == -1 else 'right'
            path(self,'therapist-body-'+name,(axis,22),('B',(x(16),30),(x(10),22),(x(16),22)),('B',(x(7),37),(x(16),37),(x(12),37)))
            self.relate('connect','client-head','therapist-body-'+name)
        self.relate('connect','therapist-body-left','therapist-body-right')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-body-left-1',torso_junction='start')
