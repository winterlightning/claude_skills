"""Doctor with Medical Cap.

Symbol plan: Medical cap above a circular jaw and broad shoulders. Cross is intrinsic to the cap.
Keyshape: VRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: Lucide user.
Reduction: Removed ears and collar; enlarged the medical cap to accommodate the cross.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '709ecaa2-14b1-430d-9254-115ba73f6c42'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/doctor_709ecaa2-14b1-430d-9254-115ba73f6c42.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (6, 2, 42, 46); centerline (8, 4, 40, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/doctor_709ecaa2-14b1-430d-9254-115ba73f6c42.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-021/15-doctor-with-medical-cap--709ecaa2-14b1-430d-9254-115ba73f6c42.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-021/references/doctor_709ecaa2-14b1-430d-9254-115ba73f6c42.svg'

class GeneratedIcon(Solo48):
    icon_id = 'doctor-wearing-medical-cap-batch-021-15'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    human_construction = 'bust'
    keywords = ('doctor', 'wearing', 'medical', 'cap')

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
        poly('cap',(12,24),(12,4),(36,4),(36,24),(32,24),(16,24),closed=True)
        cross('medical',24,14,2)
        path('jaw',(16,24),('A',(24,32),8,8,False),('A',(32,24),8,8,False))
        path('shoulders',(8,44),('A',(24,36),16,8,True),('A',(40,44),16,8,True))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
        self.relate('connect','jaw','shoulders')
