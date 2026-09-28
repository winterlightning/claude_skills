"""Drooling Sleepy Face Emoji.

Symbol plan: Round sleepy face; paired closed eyes, drooping mouth with a hanging drool stroke.
Keyshape: CIRCLE; authored at SOLO48, never scaled from the source.
Reference construction: supplied reference; no useful exact Lucide match.
Reduction: Hanging drool simplified to an attached stroke; no tiny enclosed droplet.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '78d4dd51-e8ae-5a7d-8c02-d136d1e41511'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mouth drop_78d4dd51-e8ae-5a7d-8c02-d136d1e41511.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (2, 2, 46, 46); centerline (4, 4, 44, 44).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/mouth drop_78d4dd51-e8ae-5a7d-8c02-d136d1e41511.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/06-drooling-sleepy-face-emoji--78d4dd51-e8ae-5a7d-8c02-d136d1e41511.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/references/mouth drop_78d4dd51-e8ae-5a7d-8c02-d136d1e41511.svg'

class GeneratedIcon(Solo48):
    icon_id = 'drooling-sleepy-face-batch-022-06'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    keywords = ('drooling', 'sleepy', 'face')

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
        circle('face',24,24,20)
        for j,x in enumerate((15,29)): path(f'eye-{j}',(x,17),('A',(x+4,17),3,2,False))
        path('mouth',(17,30),('A',(31,30),7,4,True),('L',(25,30)),('L',(25,35)))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
