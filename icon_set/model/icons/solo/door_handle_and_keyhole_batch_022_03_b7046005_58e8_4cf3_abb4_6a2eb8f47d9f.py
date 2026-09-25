"""Door Handle with Keyhole.

Symbol plan: Tall backplate, keyhole and right-extending lever; plate opens around the lever.
Keyshape: VRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: supplied reference; no useful exact Lucide match.
Reduction: Keyhole simplified to a short slot; circular hub merged into the lever.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7046005-58e8-4cf3-abb4-6a2eb8f47d9f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/door knob_b7046005-58e8-4cf3-abb4-6a2eb8f47d9f.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (6, 2, 42, 46); centerline (8, 4, 40, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/door knob_b7046005-58e8-4cf3-abb4-6a2eb8f47d9f.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/03-door-handle-with-keyhole--b7046005-58e8-4cf3-abb4-6a2eb8f47d9f.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/references/door knob_b7046005-58e8-4cf3-abb4-6a2eb8f47d9f.svg'

class GeneratedIcon(Solo48):
    icon_id = 'door-handle-and-keyhole-batch-022-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('door', 'handle', 'and', 'keyhole')

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
        path('plate',(28,27),('L',(28,8)),('A',(24,4),4,4,False),('L',(12,4)),('A',(8,8),4,4,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(24,44)),('A',(28,40),4,4,False),('L',(28,35)))
        line('keyhole',(18,14),(18,19))
        path('lever',(20,27),('L',(40,27)),('L',(40,35)),('L',(20,35)),('A',(20,27),4,4,True),closed=True)
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
