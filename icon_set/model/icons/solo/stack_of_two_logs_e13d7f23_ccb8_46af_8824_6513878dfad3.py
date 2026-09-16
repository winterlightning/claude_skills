"""Stack of Two Logs.
Plan: Two stacked cylindrical logs with equal circular ends and capsule-shaped bodies; common radius and width. Bounds (4,8)-(44,40).
References: Supplied stack for round log ends; Lucide logs offers no physical-log shape.
Reduction: Growth rings and bark slashes omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'e13d7f23-ccb8-46af-8824-6513878dfad3'
SOURCE_PATH = 'pictographic-primitives/construction/wood material_e13d7f23-ccb8-46af-8824-6513878dfad3.svg'
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

class StackOfTwoLogs(Solo48):
    icon_id = 'stack-of-two-logs'
    keyshape = Keyshape.HRECT_L
    category = 'construction'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('stack', 'of', 'two', 'logs')
    def build(self):
        for i,cy in enumerate((16,32)):
         path(self,f'log-{i}',(12,cy-8),('L',(36,cy-8)),('A',(44,cy),8,8,True),('A',(36,cy+8),8,8,True),('L',(12,cy+8)),('A',(4,cy),8,8,True),('A',(12,cy-8),8,8,True),closed=True)
         path(self,f'end-{i}',(12,cy-8),('A',(20,cy),8,8,True),('A',(12,cy+8),8,8,True))
         self.relate('connect',f'log-{i}',f'end-{i}')
