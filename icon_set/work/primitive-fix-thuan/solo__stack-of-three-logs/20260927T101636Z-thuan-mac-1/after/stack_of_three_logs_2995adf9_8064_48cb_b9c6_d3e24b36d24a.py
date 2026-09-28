"""Stack of Three Logs.
Plan: Three log ends share radius7: lower centers (13,35),(35,35), top end (13,13) with cylinder extending to35. Bounds (6,6)-(42,42).
References: Supplied stack for cylinder construction; Lucide logs offered no useful physical-log match.
Reduction: Growth rings and bark slashes omitted; lower logs shown end-on, top log in side view.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '2995adf9-8064-48cb-b9c6-d3e24b36d24a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__stack-of-three-logs/20260927T101636Z-thuan-mac-1/reference/wood material_2995adf9-8064-48cb-b9c6-d3e24b36d24a.svg'
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


def symmetric(icon, name, start, left_steps, axis=24):
    """One half owns the whole outline; reflect and reverse its traversal."""
    flip = lambda p: (2*axis-p[0], p[1])
    prior = start
    reverse = []
    for kind, end, *args in left_steps:
        if kind == 'B':
            reverse.append((kind, flip(prior), flip(args[1]), flip(args[0])))
        else:
            reverse.append((kind, flip(prior), *args))
        prior = end
    path(icon, name, start, *left_steps, *reversed(reverse), closed=True)

class StackOfThreeLogs(Solo48):
    icon_id = 'stack-of-three-logs'
    keyshape = Keyshape.SQUARE
    category = 'construction'
    categories = ('construction', 'primitives')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('stack', 'of', 'three', 'logs')
    def build(self):
        # Three stacked cut ends; the top log shows its length and growth center.
        circle(self,'end-top',15,15,9)
        circle(self,'end-bottom-left',11,37,5)
        circle(self,'end-bottom-right',37,37,5)
        path(self,'log-top',(15,6),('L',(33,6)),('A',(42,15),9,9,True),('A',(33,24),9,9,True),('L',(15,24)))
        self.relate('connect','end-top','log-top')
        self.add_dot('growth-center',(15,15))

