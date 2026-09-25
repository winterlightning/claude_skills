"""Hand Facing Down.

Symbol plan: Hand reaches from a left wrist toward a down-sloping index finger; thumb notch remains open.
Keyshape: HRECT_M; authored at SOLO48, never scaled from the source.
Reference construction: Lucide hand.
Reduction: Removed the small folded-thumb crease; retained the down-sloping finger, thumb notch and open wrist.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acc6f9a7-f1e5-46cf-961e-ce00f3dd0639'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand down_acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (2, 8, 46, 40); centerline (4, 10, 44, 38).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/hand down_acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-024/02-hand-facing-down--acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-024/references/hand down_acc6f9a7-f1e5-46cf-961e-ce00f3dd0639.svg'

class GeneratedIcon(Solo48):
    icon_id = 'hand-facing-down-batch-024-02'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    keywords = ('hand', 'facing', 'down')

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
        path('hand',(4,16),('C',(14,18),(17,10),(24,10)),('C',(30,10),(36,17),(42,23)),('C',(43,24),(44,25),(44,27)),('C',(44,32),(40,34),(36,31)),('L',(27,24)),('C',(24,33),(20,38),(14,38)),('L',(4,35)))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
