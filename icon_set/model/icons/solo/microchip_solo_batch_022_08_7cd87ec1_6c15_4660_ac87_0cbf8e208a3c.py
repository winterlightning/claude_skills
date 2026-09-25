"""Electronic Computer Microchip.

Symbol plan: Square chip with two pins per side; repeated 12-unit pin spacing.
Keyshape: SQUARE; authored at SOLO48, never scaled from the source.
Reference construction: Lucide cpu.
Reduction: Kept empty center, as in the source.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7cd87ec1-6c15-4660-ac87-0cbf8e208a3c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/microchip_7cd87ec1-6c15-4660-ac87-0cbf8e208a3c.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (4, 4, 44, 44); centerline (6, 6, 42, 42).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/microchip_7cd87ec1-6c15-4660-ac87-0cbf8e208a3c.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/08-electronic-computer-microchip--7cd87ec1-6c15-4660-ac87-0cbf8e208a3c.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-022/references/microchip_7cd87ec1-6c15-4660-ac87-0cbf8e208a3c.svg'

class GeneratedIcon(Solo48):
    icon_id = 'microchip-solo-batch-022-08'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('microchip', 'solo')

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
        poly('chip',(12,12),(18,12),(30,12),(36,12),(36,18),(36,30),(36,36),(30,36),(18,36),(12,36),(12,30),(12,18),closed=True)
        for v in (18,30):
            line(f'top-{v}',(v,6),(v,12)); line(f'bottom-{v}',(v,36),(v,42)); line(f'left-{v}',(6,v),(12,v)); line(f'right-{v}',(36,v),(42,v))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
