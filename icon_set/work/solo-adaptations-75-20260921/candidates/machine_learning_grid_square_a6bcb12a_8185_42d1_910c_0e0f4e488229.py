"""A rounded square contains two separated rows of three rectangular cells, with a clipped internal corner in the lower row."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a6bcb12a-8185-42d1-910c-0e0f4e488229'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon machine learning square_a6bcb12a-8185-42d1-910c-0e0f4e488229.svg'
AUTHOR = 'gpt-6'
ADAPTED_FROM = 'two-rows-of-three-cells'
DESIGN_NOTES = 'Keep the six cells and enclosing frame; the tiny clipped internal corner is omitted.'
CONSTRUCTION_REFERENCE = 'Lucide panels-top-left original and atomic-debug; coherent contours and shared attachment nodes.'

class Drawing(Solo48):
    icon_id = 'machine-learning-grid-square'
    variant_of = 'two-rows-of-three-cells'
    variant_label = 'Machine Learning Grid Square'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('machine', 'learning', 'grid', 'square', 'separated', 'rows', 'cells', 'clipped')
    def build(self):
        # Plan: A rounded square contains two separated rows of three rectangular cells, with a clipped internal corner in the lower row.
        # SQUARE: exact SOLO48 envelope; repeated parts share coordinates.
        # Reduction: Keep the six cells and enclosing frame; the tiny clipped internal corner is omitted.

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

        rr('frame',6,6,42,42,2)
        for j,y in enumerate([12,28]):
         rr(f'row-{j}',12,y,36,y+8,0,top=(20,28),bottom=(20,28))
         for k,x in enumerate([20,28]):l(f'cell-{j}-{k}',(x,y),(x,y+8))

        # Only exact shared nodes declare physical contact; never proximity.
        names=list(nodes)
        for i,n in enumerate(names):
            for m in names[i+1:]:
                if nodes[n] & nodes[m]: self.relate('connect',n,m)
