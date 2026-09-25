"""Isometric Textured Sugar Cube.

Symbol plan: Perspective sugar cube with shared top/front/right face edges and two texture dots.
Keyshape: SQUARE; authored at SOLO48, never scaled from the source.
Reference construction: supplied reference; no useful exact Lucide match.
Reduction: Three texture marks reduced to two.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8243788-9244-4cb8-90cd-09b9a3faa348'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sugar cube_b8243788-9244-4cb8-90cd-09b9a3faa348.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (4, 4, 44, 44); centerline (6, 6, 42, 42).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/sugar cube_b8243788-9244-4cb8-90cd-09b9a3faa348.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/14-isometric-textured-sugar-cube--b8243788-9244-4cb8-90cd-09b9a3faa348.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/references/sugar cube_b8243788-9244-4cb8-90cd-09b9a3faa348.svg'

class GeneratedIcon(Solo48):
    icon_id = 'sugar-cube-batch-025-14'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('sugar', 'cube')

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
        poly('cube',(6,18),(22,6),(42,6),(42,30),(26,42),(6,42),closed=True)
        poly('seam',(6,18),(26,18),(42,6))
        line('front-edge',(26,18),(26,42))
        dot('grain-a',(16,26))
        dot('grain-b',(16,34))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
