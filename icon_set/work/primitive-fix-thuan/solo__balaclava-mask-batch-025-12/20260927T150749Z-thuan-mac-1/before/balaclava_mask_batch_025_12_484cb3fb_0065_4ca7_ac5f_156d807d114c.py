"""Infinity Symbol Balaclava.

Symbol plan: Rounded balaclava with flared lower neck and a paired eye opening.
Keyshape: VRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: supplied reference; no useful exact Lucide match.
Reduction: Merged the small crossing eye loops into one binocular eye opening to preserve negative space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '484cb3fb-0065-4ca7-ac5f-156d807d114c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (6, 2, 42, 46); centerline (8, 4, 40, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/12-infinity-symbol-balaclava--484cb3fb-0065-4ca7-ac5f-156d807d114c.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/references/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'

class GeneratedIcon(Solo48):
    icon_id = 'balaclava-mask-batch-025-12'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    keywords = ('balaclava', 'mask')

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
        path('hood',(14,34),('C',(9,30),(8,26),(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('C',(40,26),(39,30),(34,34)),('L',(38,42)),('C',(34,44),(30,44),(24,44)),('C',(18,44),(14,44),(10,42)),('L',(14,34)),closed=True)
        path('eyes',(24,18),('C',(19,14),(17,16),(17,21)),('C',(17,26),(20,28),(24,24)),('C',(28,28),(31,26),(31,21)),('C',(31,16),(29,14),(24,18)),closed=True)
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
