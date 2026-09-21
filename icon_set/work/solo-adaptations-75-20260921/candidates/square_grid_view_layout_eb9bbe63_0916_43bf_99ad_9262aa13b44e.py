"""Four separate small squares form a two-by-two grid inside a rounded square frame."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb9bbe63-0916-43bf-99ad-9262aa13b44e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/images/picture polaroid album_eb9bbe63-0916-43bf-99ad-9262aa13b44e.svg'
AUTHOR = 'gpt-6'
ADAPTED_FROM = 'four-square-grid'
DESIGN_NOTES = 'No defining feature omitted.'
CONSTRUCTION_REFERENCE = 'Lucide panels-top-left original and atomic-debug; coherent contours and shared attachment nodes.'

class Drawing(Solo48):
    icon_id = 'square-grid-view-layout'
    variant_of = 'four-square-grid'
    variant_label = 'Square Grid View Layout'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'images'
    aliases = ()
    keywords = ('square', 'grid', 'view', 'layout', 'squares', 'form', 'frame')
    def build(self):
        # Plan: Four separate small squares form a two-by-two grid inside a rounded square frame.
        # SQUARE: exact SOLO48 envelope; repeated parts share coordinates.
        # Reduction: No defining feature omitted.

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

        rr('frame',6,6,42,42)
        for row in range(2):
         for col in range(2):
          x=14+col*12;y=14+row*12;p(f'cell-{row}-{col}',(x,y),(x+8,y),(x+8,y+8),(x,y+8),closed=True)

        # Only exact shared nodes declare physical contact; never proximity.
        names=list(nodes)
        for i,n in enumerate(names):
            for m in names[i+1:]:
                if nodes[n] & nodes[m]: self.relate('connect',n,m)
