"""Exclamation Mark Warning Symbol.

Symbol plan: Broad tapered warning mark and detached circular dot.
Keyshape: VRECT_M; authored at SOLO48, never scaled from the source.
Reference construction: supplied reference; no useful exact Lucide match.
Reduction: No identity-bearing features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd8e53a33-32ee-4c7d-85e0-ac0f71bcdb94'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/exclamation_d8e53a33-32ee-4c7d-85e0-ac0f71bcdb94.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (8, 2, 40, 46); centerline (10, 4, 38, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/exclamation_d8e53a33-32ee-4c7d-85e0-ac0f71bcdb94.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/11-exclamation-mark-warning-symbol--d8e53a33-32ee-4c7d-85e0-ac0f71bcdb94.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/references/exclamation_d8e53a33-32ee-4c7d-85e0-ac0f71bcdb94.svg'

class GeneratedIcon(Solo48):
    icon_id = 'exclamation-mark-solo-batch-022-11'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('exclamation', 'mark', 'solo')

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
        path('stem',(10,10),('A',(16,4),6,6,True),('L',(32,4)),('A',(38,10),6,6,True),('L',(29,28)),('L',(19,28)),('L',(10,10)),closed=True)
        circle('dot',24,40,4)
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
