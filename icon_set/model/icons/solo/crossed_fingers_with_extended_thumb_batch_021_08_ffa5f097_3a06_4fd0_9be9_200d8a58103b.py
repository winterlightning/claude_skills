"""Crossed Fingers Hand Gesture.

Symbol plan: Crossing raised fingers above a rounded palm; one folded thumb line and one broad curled-finger contour.
Keyshape: VRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: Lucide hand.
Reduction: Reduced the two small curled fingertips to one rounded group.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffa5f097-3a06-4fd0-9be9-200d8a58103b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (6, 2, 42, 46); centerline (8, 4, 40, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-021/08-crossed-fingers-hand-gesture--ffa5f097-3a06-4fd0-9be9-200d8a58103b.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-021/references/finger crossed_ffa5f097-3a06-4fd0-9be9-200d8a58103b.svg'

class GeneratedIcon(Solo48):
    icon_id = 'crossed-fingers-with-extended-thumb-batch-021-08'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    keywords = ('crossed', 'fingers', 'with', 'extended', 'thumb')

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
        path('hand',(12,28),('L',(18,20)),('L',(24,12)),('L',(26,6)),('C',(27,4),(29,4),(30,4)),('C',(35,4),(37,8),(34,12)),('L',(24,28)),('C',(32,22),(40,22),(40,30)),('C',(40,40),(34,44),(24,44)),('C',(15,44),(8,36),(8,30)),('C',(8,25),(10,26),(12,28)),closed=True)
        path('rear-finger',(18,20),('L',(10,10)),('C',(6,6),(10,4),(14,4)),('C',(20,4),(22,8),(24,12)))
        line('thumb',(12,28),(25,28))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
