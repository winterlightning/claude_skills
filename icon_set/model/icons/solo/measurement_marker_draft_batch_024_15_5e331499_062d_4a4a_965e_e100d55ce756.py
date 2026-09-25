"""Horizontal Measurement Markers.

Symbol plan: Two rounded marker ends with horizontal extensions, a central dash and lower vertical tick.
Keyshape: HRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: supplied reference; no useful exact Lucide match.
Reduction: Small inward tick omitted; source remains an ambiguous marker draft.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5e331499-062d-4a4a-965e-e100d55ce756'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (2, 6, 46, 42); centerline (4, 8, 44, 40).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-024/15-horizontal-measurement-markers--5e331499-062d-4a4a-965e-e100d55ce756.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-024/references/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'

class GeneratedIcon(Solo48):
    icon_id = 'measurement-marker-draft-batch-024-15'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    keywords = ('measurement', 'marker', 'draft')

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
        path('upper',(44,8),('L',(20,8)),('L',(9,8)),('A',(9,18),5,5,False),('L',(15,18)),('L',(20,8)))
        path('lower',(20,30),('L',(9,30)),('A',(9,40),5,5,False),('L',(15,40)),('L',(20,30)),('L',(44,30)),('L',(44,40)))
        line('middle',(30,20),(44,20))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
