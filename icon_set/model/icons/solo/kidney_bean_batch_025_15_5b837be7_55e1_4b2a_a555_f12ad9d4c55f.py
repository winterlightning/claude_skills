"""Kidney Bean Seed.

Symbol plan: Kidney bean with an inward notch and an inner seed crease; diagonal asymmetric organic form.
Keyshape: SQUARE; authored at SOLO48, never scaled from the source.
Reference construction: Lucide bean.
Reduction: No identity-bearing features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5b837be7-55e1-4b2a-a555-f12ad9d4c55f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/peanut_5b837be7-55e1-4b2a-a555-f12ad9d4c55f.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (4, 4, 44, 44); centerline (6, 6, 42, 42).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/peanut_5b837be7-55e1-4b2a-a555-f12ad9d4c55f.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/15-kidney-bean-seed--5b837be7-55e1-4b2a-a555-f12ad9d4c55f.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/references/peanut_5b837be7-55e1-4b2a-a555-f12ad9d4c55f.svg'

class GeneratedIcon(Solo48):
    icon_id = 'kidney-bean-batch-025-15'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('kidney', 'bean')

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
        path('bean',(24,12),('C',(27,8),(30,6),(34,6)),('C',(40,6),(42,11),(42,18)),('C',(42,33),(30,42),(18,42)),('C',(10,42),(6,38),(6,30)),('C',(6,20),(17,20),(24,12)),closed=True)
        path('crease',(18,31),('C',(25,29),(30,25),(32,20)))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
