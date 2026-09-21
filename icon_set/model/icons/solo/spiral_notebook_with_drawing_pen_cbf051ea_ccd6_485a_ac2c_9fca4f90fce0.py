"""A spiral-bound sketchbook contains a curling line, a mountain sketch and a wavy stroke, with a large diagonal pencil crossing its lower-right area."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cbf051ea-ccd6-485a-ac2c-9fca4f90fce0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/design draw_cbf051ea-ccd6-485a-ac2c-9fca4f90fce0.svg'
AUTHOR = 'gpt-6'
ADAPTED_FROM = 'spiral-bound-notebook'
DESIGN_NOTES = 'Retain one mountain sketch, three binding marks and diagonal pencil; omit the tiny curl and wave.'
CONSTRUCTION_REFERENCE = 'Lucide notebook-pen original and atomic-debug; coherent contours and shared attachment nodes.'

class Drawing(Solo48):
    icon_id = 'spiral-notebook-with-drawing-pen'
    variant_of = 'spiral-bound-notebook'
    variant_label = 'Spiral Notebook with Drawing Pen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('spiral', 'notebook', 'drawing', 'pen', 'bound', 'sketchbook', 'curling', 'line')
    def build(self):
        # Plan: A spiral-bound sketchbook contains a curling line, a mountain sketch and a wavy stroke, with a large diagonal pencil crossing its lower-right area.
        # SQUARE: exact SOLO48 envelope; repeated parts share coordinates.
        # Reduction: Retain one mountain sketch, three binding marks and diagonal pencil; omit the tiny curl and wave.

        # Shared shape definitions: equal corner radii and exact attachment nodes.
        nodes = {}
        def l(n, a, b):
            self.add_line(n, a, b); nodes[n] = {a, b}
        def p(n, *pts, closed=False):
            self.add_polyline(n, *pts, closed=closed); nodes[n] = set(pts)
        def a(n, start, end, r, sweep=True, ry=None):
            self.add_arc(n, start, end, radius_x=r, radius_y=ry or r, sweep=sweep)
            nodes[n] = {start, end}
        def c(n, x, y, r):
            pts = [(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4):
                self.add_arc(f'{n}-{j}', pts[j], pts[(j+1)%4], radius_x=r)
            self.add_contour(n, *[f'{n}-{j}' for j in range(4)], closed=True)
            nodes[n] = set(pts)
        def rr(n, x1,y1,x2,y2,r=2, top=(),right=(),bottom=(),left=()):
            # Clockwise edges are split at real branch attachments.
            if r == 0:
                pts=[(x1,y1)]+[(x,y1) for x in sorted(top)]+[(x2,y1)]+[(x2,y) for y in sorted(right)]+[(x2,y2)]+[(x,y2) for x in sorted(bottom,reverse=True)]+[(x1,y2)]+[(x1,y) for y in sorted(left,reverse=True)]
                p(n,*pts,closed=True)
                return
            corners=[((x1+r,y1),(x2-r,y1),(x2,y1+r)),
                     ((x2,y1+r),(x2,y2-r),(x2-r,y2)),
                     ((x2-r,y2),(x1+r,y2),(x1,y2-r)),
                     ((x1,y2-r),(x1,y1+r),(x1+r,y1))]
            cuts=[[(x,y1) for x in sorted(top)],[(x2,y) for y in sorted(right)],
                  [(x,y2) for x in sorted(bottom,reverse=True)],[(x1,y) for y in sorted(left,reverse=True)]]
            members=[]; allpts=set()
            for j,(start,end,nxt) in enumerate(corners):
                pts=[start]+[q for q in cuts[j] if q not in (start,end)]+[end]
                allpts.update(pts)
                for k,(v,w) in enumerate(zip(pts,pts[1:])):
                    if v==w: continue
                    part=f'{n}-e{j}-{k}'; self.add_line(part,v,w);members.append(part)
                part=f'{n}-c{j}'; self.add_arc(part,end,nxt,radius_x=r);members.append(part)
            self.add_contour(n,*members,closed=True);nodes[n]=allpts
        def dot(n,x,y):
            self.add_dot(n,(x,y));nodes[n]={(x,y)}

        p('book',(30,6),(6,6),(6,14),(6,26),(6,34),(6,42),(14,42))
        for j,y in enumerate([14,26,34]):l(f'binding-{j}',(6,y),(10,y))
        p('pen',(22,40),(26,30),(36,20),(42,26),(32,36),closed=True)
        p('sketch',(18,18),(22,14),(26,18))

        # Only exact shared nodes declare physical contact; never proximity.
        names=list(nodes)
        for i,n in enumerate(names):
            for m in names[i+1:]:
                if nodes[n] & nodes[m]: self.relate('connect',n,m)
