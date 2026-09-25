"""Interlocking Chain Link Symbol.

Symbol plan: Two diagonal open chain loops with balanced curved ends; breaks express interlocking.
Keyshape: SQUARE; authored at SOLO48, never scaled from the source.
Reference construction: Lucide link.
Reduction: Opened overlapping wire contours to keep the interlock legible.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '55bd9f6e-12a9-4d3a-9646-c1852d270efe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/attached file_55bd9f6e-12a9-4d3a-9646-c1852d270efe.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (4, 4, 44, 44); centerline (6, 6, 42, 42).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/attached file_55bd9f6e-12a9-4d3a-9646-c1852d270efe.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/13-interlocking-chain-link-symbol--55bd9f6e-12a9-4d3a-9646-c1852d270efe.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/references/attached file_55bd9f6e-12a9-4d3a-9646-c1852d270efe.svg'

class GeneratedIcon(Solo48):
    icon_id = 'interlocking-chain-links-solo-batch-025-13'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    keywords = ('interlocking', 'chain', 'links', 'solo')

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
        path('upper',(28,6),('L',(32,6)),('C',(38,6),(42,10),(42,16)),('C',(42,19),(41,21),(39,23)),('L',(31,31)),('C',(28,34),(24,33),(22,30)))
        path('lower',(20,42),('L',(16,42)),('C',(10,42),(6,38),(6,32)),('C',(6,29),(7,27),(9,25)),('L',(17,17)),('C',(20,14),(24,15),(26,18)))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
