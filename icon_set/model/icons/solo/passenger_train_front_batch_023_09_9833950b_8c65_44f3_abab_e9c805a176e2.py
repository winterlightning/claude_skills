"""Front View Passenger Train.

Symbol plan: Rounded train front divided by its windshield seam; rails diverge from shared lower corners.
Keyshape: VRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: Lucide train-front.
Reduction: No identity-bearing features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9833950b-8c65-44f3-abab-e9c805a176e2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/train_9833950b-8c65-44f3-abab-e9c805a176e2.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (6, 2, 42, 46); centerline (8, 4, 40, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/train_9833950b-8c65-44f3-abab-e9c805a176e2.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-023/09-front-view-passenger-train--9833950b-8c65-44f3-abab-e9c805a176e2.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-023/references/train_9833950b-8c65-44f3-abab-e9c805a176e2.svg'

class GeneratedIcon(Solo48):
    icon_id = 'passenger-train-front-batch-023-09'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('passenger', 'train', 'front')

    def build(self):
        def path(name, start, *steps, closed=False):
            point = start
            members = []
            for j, step in enumerate(steps):
                eid = f"{name}-{j}"
                if step[0] == 'L':
                    self.add_line(eid, point, step[1])
                    point = step[1]
                elif step[0] == 'A':
                    self.add_arc(eid, point, step[1], radius_x=step[2], radius_y=step[3], sweep=step[4], large_arc=step[5] if len(step)>5 else False)
                    point = step[1]
                else:
                    self.add_bezier(eid, point, (step[1], step[2], step[3]))
                    point = step[3]
                members.append(eid)
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), ('A',(x+r,y),r,r,True), ('A',(x-r,y),r,r,True), closed=True)
        def rect(name, l,t,r,b, radius=0):
            if not radius:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
            else:
                q=radius
                path(name,(l+q,t),('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True),closed=True)
        def line(name,a,b):
            self.add_line(name,a,b)
        def poly(name,*pts,closed=False):
            self.add_polyline(name,*pts,closed=closed)
        def dot(name,p):
            self.add_dot(name,p)
        def cross(name,x,y,r):
            for j,p in enumerate(((x-r,y),(x+r,y),(x,y-r),(x,y+r))):
                line(f'{name}-{j}',(x,y),p)
        path('body',(12,16),('A',(16,12),4,4,True),('L',(32,12)),('A',(36,16),4,4,True),('L',(36,24)),('L',(36,36)),('L',(12,36)),('L',(12,24)),('L',(12,16)),closed=True)
        line('window',(12,24),(36,24))
        line('rail-left',(12,36),(8,44))
        line('rail-right',(36,36),(40,44))
        line('roof-mark',(19,4),(29,4))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
