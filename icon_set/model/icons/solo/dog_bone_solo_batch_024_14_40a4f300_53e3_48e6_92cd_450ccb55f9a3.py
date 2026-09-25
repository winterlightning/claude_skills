"""Horizontal Dog Bone Shape.

Symbol plan: Horizontal bone with four rounded lobes and a straight narrow shaft.
Keyshape: HRECT_M; authored at SOLO48, never scaled from the source.
Reference construction: Lucide bone.
Reduction: No identity-bearing features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40a4f300-53e3-48e6-92cd-450ccb55f9a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bone_40a4f300-53e3-48e6-92cd-450ccb55f9a3.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (2, 8, 46, 40); centerline (4, 10, 44, 38).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/bone_40a4f300-53e3-48e6-92cd-450ccb55f9a3.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-024/14-horizontal-dog-bone-shape--40a4f300-53e3-48e6-92cd-450ccb55f9a3.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-024/references/bone_40a4f300-53e3-48e6-92cd-450ccb55f9a3.svg'

class GeneratedIcon(Solo48):
    icon_id = 'dog-bone-solo-batch-024-14'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('dog', 'bone', 'solo')

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
        path('bone',(16,18),('C',(16,13),(15,10),(11,10)),('C',(7,10),(4,12),(4,16)),('C',(4,20),(7,22),(9,24)),('C',(7,26),(4,28),(4,32)),('C',(4,36),(7,38),(11,38)),('C',(15,38),(16,35),(16,30)),('L',(32,30)),('C',(32,35),(33,38),(37,38)),('C',(41,38),(44,36),(44,32)),('C',(44,28),(41,26),(39,24)),('C',(41,22),(44,20),(44,16)),('C',(44,12),(41,10),(37,10)),('C',(33,10),(32,13),(32,18)),('L',(16,18)),closed=True)
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
