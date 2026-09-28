"""Iterative Workflow Arrows.
Plan: Two unequal curled iteration paths meet tangentially at (20,22). Lower path lands at (20,40) on an arrowed baseline. Three actual arrowhead joins; bounds (8,4)-(40,44).
References: Lucide repeat for curved arrows; route for smooth turn sequences.
Reduction: Fine arrow tips simplified into open round-ended chevrons.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2d6aea0f-956f-475c-983c-4883f1ff0ac5'
SOURCE_PATH = 'pictographic-primitives/business/workflow scrum_2d6aea0f-956f-475c-983c-4883f1ff0ac5.svg'
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

class IterativeWorkflowArrows(Solo48):
    icon_id = 'iterative-workflow-arrows'
    keyshape = Keyshape.VRECT_L
    category = 'business'
    categories = ('primitives', 'business')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('iterative', 'workflow', 'arrows')
    def build(self):

        path(self,'upper',(20,22),('B',(12,13),(12,22),(12,18)),('B',(24,4),(12,8),(18,4)),('B',(36,13),(30,4),(36,8)),('L',(36,20)))
        self.add_polyline('upper-arrow',(32,16),(36,20),(40,16))
        path(self,'lower',(12,32),('B',(20,22),(12,26),(16,22)),('B',(28,31),(24,22),(28,26)),('B',(20,40),(28,36),(24,40)))
        self.add_polyline('lower-arrow',(12,26),(12,32),(18,30))
        self.add_polyline('baseline',(8,40),(20,40),(40,40))
        self.add_polyline('baseline-arrow',(36,36),(40,40),(36,44))
        self.relate('connect','upper','lower')
        self.relate('connect','upper','upper-arrow')
        self.relate('connect','lower','lower-arrow')
        self.relate('connect','lower','baseline')
        self.relate('connect','baseline','baseline-arrow')

