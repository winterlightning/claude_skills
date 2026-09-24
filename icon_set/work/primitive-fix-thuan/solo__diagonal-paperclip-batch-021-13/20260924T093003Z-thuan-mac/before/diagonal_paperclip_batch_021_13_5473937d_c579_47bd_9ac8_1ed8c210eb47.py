"""Diagonal Paperclip Attachment.

Symbol plan: One wire run with nested rounded turns on a diagonal; preserves two open ends.
Keyshape: SQUARE; authored at SOLO48, never scaled from the source.
Reference construction: Lucide paperclip.
Reduction: No identity-bearing features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5473937d-c579-47bd-9ac8-1ed8c210eb47'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/attached file_5473937d-c579-47bd-9ac8-1ed8c210eb47.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (4, 4, 44, 44); centerline (6, 6, 42, 42).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/attached file_5473937d-c579-47bd-9ac8-1ed8c210eb47.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-021/13-diagonal-paperclip-attachment--5473937d-c579-47bd-9ac8-1ed8c210eb47.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-021/references/attached file_5473937d-c579-47bd-9ac8-1ed8c210eb47.svg'

class GeneratedIcon(Solo48):
    icon_id = 'diagonal-paperclip-batch-021-13'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    keywords = ('diagonal', 'paperclip')

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
        path('wire',(42,30),('L',(34,38)),('C',(31,41),(28,42),(24,42)),('C',(14,42),(6,36),(6,28)),('C',(6,26),(8,24),(10,22)),('L',(24,8)),('C',(26,6),(28,6),(30,6)),('C',(37,6),(42,11),(42,18)),('C',(42,20),(40,20),(38,22)),('L',(29,31)),('C',(25,35),(19,29),(23,25)),('L',(30,18)))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
