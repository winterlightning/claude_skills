"""Gantt Chart with Linked Tasks.
Plan: Open chart axes and three task bars with one dependency link. Bounds (6,6)-(42,42).
References: Lucide chart-gantt for open axes and staggered runs; source for dependency.
Reduction: Four outlined blocks reduced to three stout bars to leave clear dependency routing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '012ac09f-44c3-417b-a7cd-1dcaf5b7540e'
SOURCE_PATH = 'pictographic-primitives/business/workflow gantt chart_012ac09f-44c3-417b-a7cd-1dcaf5b7540e.svg'
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

class GanttChartWithLinkedTasks(Solo48):
    icon_id = 'gantt-chart-with-linked-tasks'
    keyshape = Keyshape.SQUARE
    category = 'business'
    categories = ('primitives', 'business')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('gantt', 'chart', 'with', 'linked', 'tasks')
    def build(self):
        path(self,'axes',(6,6),('L',(6,38)),('A',(10,42),4,4,False),('L',(42,42)))
        self.add_polyline('task-1',(16,10),(30,10))
        self.add_polyline('task-2',(30,24),(42,24))
        self.add_line('task-3',(16,32),(24,32))
        path(self,'dependency',(30,10),('L',(36,10)),('A',(40,14),4,4,True),('L',(40,24)))
        self.relate('connect','task-1','dependency')
        self.relate('connect','task-2','dependency')
