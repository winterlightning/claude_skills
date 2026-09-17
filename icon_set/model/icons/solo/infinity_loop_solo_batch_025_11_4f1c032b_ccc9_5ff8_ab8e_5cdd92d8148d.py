"""Infinity Loop Symbol.

Symbol plan: Continuous infinity loop with balanced lobes and a true central crossing.
Keyshape: HRECT_M; authored at SOLO48, never scaled from the source.
Reference construction: Lucide infinity.
Reduction: No identity-bearing features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4f1c032b-ccc9-5ff8-ab8e-5cdd92d8148d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hyperloop symbol_4f1c032b-ccc9-5ff8-ab8e-5cdd92d8148d.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (2, 8, 46, 40); centerline (4, 10, 44, 38).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/hyperloop symbol_4f1c032b-ccc9-5ff8-ab8e-5cdd92d8148d.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/11-infinity-loop-symbol--4f1c032b-ccc9-5ff8-ab8e-5cdd92d8148d.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/references/hyperloop symbol_4f1c032b-ccc9-5ff8-ab8e-5cdd92d8148d.svg'

class GeneratedIcon(Solo48):
    icon_id = 'infinity-loop-solo-batch-025-11'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    keywords = ('infinity', 'loop', 'solo')

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
        path('infinity',(24,24),('C',(18,18),(17,10),(12,10)),('C',(7,10),(4,16),(4,24)),('C',(4,32),(7,38),(12,38)),('C',(17,38),(18,30),(24,24)),('C',(30,18),(31,10),(36,10)),('C',(41,10),(44,16),(44,24)),('C',(44,32),(41,38),(36,38)),('C',(31,38),(30,30),(24,24)),closed=True)
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
