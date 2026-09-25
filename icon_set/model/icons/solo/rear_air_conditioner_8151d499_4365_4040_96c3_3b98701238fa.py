"""Three upward wavy airflow arrows cross the lower edge of a wide rectangular rear-window outline."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8151d499-4365-4040-96c3-3b98701238fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air conditioner rear 1_8151d499-4365-4040-96c3-3b98701238fa.svg'
AUTHOR = 'gpt-6'
ADAPTED_FROM = 'rear-window-defrost'
DESIGN_NOTES = 'Smooth airflow simplified to three rising stems; preserve direction and rear-window enclosure.'
CONSTRUCTION_REFERENCE = 'Lucide presentation original and atomic-debug; coherent contours and shared attachment nodes.'

class Drawing(Solo48):
    icon_id = 'rear-air-conditioner'
    variant_of = 'rear-window-defrost'
    variant_label = 'Rear Air Conditioner'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('air', 'conditioner', 'upward', 'wavy', 'airflow', 'arrows', 'cross', 'wide')
    def build(self):
        # Plan: Three upward wavy airflow arrows cross the lower edge of a wide rectangular rear-window outline.
        # HRECT_L: exact SOLO48 envelope; repeated parts share coordinates.
        # Reduction: Smooth airflow simplified to three rising stems; preserve direction and rear-window enclosure.

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

        p('window',(4,32),(4,8),(44,8),(44,32),(4,32))
        for j,x in enumerate([12,24,36]):
         p(f'flow-{j}',(x,40),(x,32),(x,16));p(f'arrow-{j}',(x-4,20),(x,16),(x+4,20))

        # Only exact shared nodes declare physical contact; never proximity.
        names=list(nodes)
        for i,n in enumerate(names):
            for m in names[i+1:]:
                if nodes[n] & nodes[m]: self.relate('connect',n,m)
