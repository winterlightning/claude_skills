"""An upright parchment scroll has opposite curled ends and two short horizontal text lines."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6618a5da-4477-5f3d-a34d-6c989e22cf2b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-10/scroll_6618a5da-4477-5f3d-a34d-6c989e22cf2b.svg'
AUTHOR = 'gpt-6'
ADAPTED_FROM = 'scroll-with-text-lines'
DESIGN_NOTES = 'Mirror the existing scroll construction and explicitly split the lower roll at its seam attachment; retain both text lines.'
CONSTRUCTION_REFERENCE = 'Lucide scroll-text original and atomic-debug; coherent contours and shared attachment nodes.'

class Drawing(Solo48):
    icon_id = 'vertical-ancient-paper-scroll'
    variant_of = 'scroll-with-text-lines'
    variant_label = 'Vertical Ancient Paper Scroll'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('ancient', 'paper', 'scroll', 'parchment', 'opposite', 'curled', 'ends', 'text')
    def build(self):
        # Plan: An upright parchment scroll has opposite curled ends and two short horizontal text lines.
        # SQUARE: exact SOLO48 envelope; repeated parts share coordinates.
        # Reduction: Mirror the existing scroll construction and explicitly split the lower roll at its seam attachment; retain both text lines.

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

        l('top',(36,6),(10,6));a('top-curl',(10,6),(6,10),4,sweep=False);p('tab',(6,10),(6,16),(14,16));l('left',(14,16),(14,36));a('foot',(14,36),(20,42),6,sweep=False);p('base',(20,42),(26,42),(37,42));a('bottom-curl',(37,42),(37,32),5,sweep=False);l('bottom-top',(37,32),(26,32))
        a('upper-inner',(10,6),(14,10),4);l('upper-wall',(14,10),(14,16));a('lower-inner',(26,32),(26,42),5);l('right',(36,6),(36,32));l('text-one',(23,15),(27,15));l('text-two',(23,23),(27,23))

        # Only exact shared nodes declare physical contact; never proximity.
        names=list(nodes)
        for i,n in enumerate(names):
            for m in names[i+1:]:
                if nodes[n] & nodes[m]: self.relate('connect',n,m)
