"""Coconut Drink with Straw.
Plan: Coconut shell, bent straw and one attached wavy upper band.
Construction reference: Lucide soup; independently solved SOLO48 geometry.
Source copy inspected: work/brief-exports/20260917-all-todo-batches-15/batches/batch-007/references/coconut_e56410b3-feae-47c6-986d-ad4b7fd0714d.svg
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e56410b3-feae-47c6-986d-ad4b7fd0714d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/drinks/coconut_e56410b3-feae-47c6-986d-ad4b7fd0714d.svg'
AUTHOR = 'gpt-6'


class GeneratedSolo(Solo48):
    icon_id = 'coconut-drink-with-straw-batch-007-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "drinks"
    aliases = ()
    keywords = ('coconut', 'drink', 'with', 'straw')

    def build(self):

        def line(name, start, end):
            self.add_line(name, start, end)
        def arc(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
        def curve(name, start, *segments):
            self.add_bezier(name, start, *segments)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def circle(name, x, y, r, ry=None):
            ry = r if ry is None else ry
            points = [(x-r,y),(x,y-ry),(x+r,y),(x,y+ry)]
            for j in range(4): arc(f'{name}-{j}',points[j],points[(j+1)%4],r,ry)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                path(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                 (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(f'{name}-{j}',pts[j],pts[(j+1)%8],r)
                else: line(f'{name}-{j}',pts[j],pts[(j+1)%8])
            self.add_contour(name,*(f'{name}-{j}' for j in range(8)),closed=True)

        line('rim',(6,20),(42,20))
        curve('shell',(42,20),((42,31),(36,42),(24,42)),((12,42),(6,31),(6,20)))
        path('straw',(30,20),(34,8),(42,6))
        curve('shell-band',(6,20),((10,31),(14,24),(20,28)),((29,34),(35,25),(42,20)))

        # Connect only actual shared endpoints, including contour junctions.
        # Split receiving straight runs at attachment nodes to preserve topology.
        from ...primitives import Line, Point
        endpoints = {p.start for p in self.primitives} | {p.end for p in self.primitives}
        replacements = {}
        rebuilt = []
        for primitive in self.primitives:
            if isinstance(primitive, Line) and primitive.start != primitive.end:
                a, b = primitive.start, primitive.end
                dx, dy = b.x-a.x, b.y-a.y
                cuts = [q for q in endpoints if q not in (a,b)
                        and (q.x-a.x)*dy == (q.y-a.y)*dx
                        and 0 < (q.x-a.x)*dx+(q.y-a.y)*dy < dx*dx+dy*dy]
                if cuts:
                    nodes = [a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        ident=f'{primitive.element_id}-join-{j}'
                        rebuilt.append(Line(ident,u,v)); ids.append(ident)
                    replacements[primitive.element_id]=ids
                    continue
            rebuilt.append(primitive)
        if replacements:
            from dataclasses import replace
            self.primitives[:] = rebuilt
            self.contours[:] = [replace(c, members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
        for i, a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
