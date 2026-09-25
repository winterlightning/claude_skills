"""Human User Profile Icon.

Symbol plan: Front portrait with a circular face and broad shoulders; ears represented by outward arcs.
Keyshape: VRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: Lucide user.
Reduction: Kept ears and open shoulders; simplified face shape.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '07e1bb79-331c-4f70-8f6d-2c162b0b2d9a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/person 1_07e1bb79-331c-4f70-8f6d-2c162b0b2d9a.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (6, 2, 42, 46); centerline (8, 4, 40, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/person 1_07e1bb79-331c-4f70-8f6d-2c162b0b2d9a.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/08-human-user-profile-icon--07e1bb79-331c-4f70-8f6d-2c162b0b2d9a.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-025/references/person 1_07e1bb79-331c-4f70-8f6d-2c162b0b2d9a.svg'

class GeneratedIcon(Solo48):
    icon_id = 'human-profile-bust-batch-025-08'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    human_construction = 'bust'
    keywords = ('human', 'profile', 'bust')

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
        path('head',(14,14),('A',(34,14),10,10,True),('L',(34,18)),('A',(34,26),4,4,True),('A',(24,36),10,10,True),('A',(14,26),10,10,True),('A',(14,18),4,4,True),('L',(14,14)),closed=True)
        path('shoulders',(8,44),('A',(24,40),16,4,True),('A',(40,44),16,4,True))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
        self.relate('connect','head','shoulders')
