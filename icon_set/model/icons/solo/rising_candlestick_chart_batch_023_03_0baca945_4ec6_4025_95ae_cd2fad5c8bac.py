"""Financial Candlestick Chart.

Symbol plan: Three rising candlesticks with shared 8-unit width and 8-unit gaps; wicks meet split top/bottom edges.
Keyshape: HRECT_L; authored at SOLO48, never scaled from the source.
Reference construction: supplied reference; no useful exact Lucide match.
Reduction: No identity-bearing features omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0baca945-4ec6-4025-95ae-cd2fad5c8bac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'
AUTHOR = 'gpt-6'
# Keyshape design bounds: visible (2, 6, 46, 42); centerline (4, 8, 44, 40).
SAVED_SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/other/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-023/03-financial-candlestick-chart--0baca945-4ec6-4025-95ae-cd2fad5c8bac.md'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-023/references/trading_0baca945-4ec6-4025-95ae-cd2fad5c8bac.svg'

class GeneratedIcon(Solo48):
    icon_id = 'rising-candlestick-chart-batch-023-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    keywords = ('rising', 'candlestick', 'chart')

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
        for j,(x,t,b,hi,lo) in enumerate(((4,24,36,18,40),(20,18,30,12,36),(36,12,24,8,30))):
            poly(f'body-{j}',(x,t),(x+4,t),(x+8,t),(x+8,b),(x+4,b),(x,b),closed=True)
            line(f'wick-top-{j}',(x+4,hi),(x+4,t)); line(f'wick-bottom-{j}',(x+4,b),(x+4,lo))
        primitives = list(self.primitives)
        for i, first in enumerate(primitives):
            for second in primitives[i+1:]:
                if {first.start, first.end} & {second.start, second.end}:
                    self.relate("connect", first.element_id, second.element_id)
