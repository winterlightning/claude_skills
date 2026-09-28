"""Gantt Chart with Progress Dividers.
Plan: Three staggered eight-unit-high task boxes with individual progress dividers; one timeline joins the lower two. Bounds (8,4)-(40,44).
References: Lucide chart-gantt for staggered rows; workflow for rounded task outlines.
Reduction: Top timeline extension omitted to avoid duplicating a task wall; three tasks, all dividers and the lower connector retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c6f9a1df-2dbc-4ed6-a75b-2dbdfa9e9de1'
SOURCE_PATH = 'pictographic-primitives/business/workflow gantt chart_c6f9a1df-2dbc-4ed6-a75b-2dbdfa9e9de1.svg'
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


def rectangle(icon,name,x1,y1,x2,y2,r=2,knots=()):
    """One box owns its radii and splits receiving walls at true attachment nodes."""
    xs=sorted({(x1+x2)//2,*knots})
    xs=[x for x in xs if x1+r<x<x2-r]
    ym=(y1+y2)//2
    steps=[('L',(x,y1)) for x in xs]
    steps += [('L',(x2-r,y1)),('A',(x2,y1+r),r,r,True)]
    if y1+r<ym<y2-r:steps += [('L',(x2,ym))]
    steps += [('L',(x2,y2-r)),('A',(x2-r,y2),r,r,True)]
    steps += [('L',(x,y2)) for x in reversed(xs)]
    steps += [('L',(x1+r,y2)),('A',(x1,y2-r),r,r,True)]
    if y1+r<ym<y2-r:steps += [('L',(x1,ym))]
    steps += [('L',(x1,y1+r)),('A',(x1+r,y1),r,r,True)]
    path(icon,name,(x1+r,y1),*steps,closed=True)

class GanttChartWithProgressDividers(Solo48):
    icon_id = 'gantt-chart-with-progress-dividers'
    keyshape = Keyshape.VRECT_L
    category = 'business'
    categories = ('primitives', 'business')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('gantt', 'chart', 'with', 'progress', 'dividers')
    def build(self):
        for n,x1,y1,x2,divider in ((0,8,4,32,24),(1,16,20,40,24),(2,24,36,40,32)):
         rectangle(self,f'task-{n}',x1,y1,x2,y1+8,knots=(divider,32))
         self.add_line(f'progress-{n}',(divider,y1),(divider,y1+8))
         self.relate('connect',f'task-{n}',f'progress-{n}')
        self.add_line('timeline-bottom',(32,28),(32,36))
        self.relate('connect','timeline-bottom','task-1')
        self.relate('connect','timeline-bottom','task-2')
