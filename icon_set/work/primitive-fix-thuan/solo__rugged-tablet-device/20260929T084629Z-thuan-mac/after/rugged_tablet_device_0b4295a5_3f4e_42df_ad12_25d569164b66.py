"""Lucide rounded tablet body with a large rectangular display and centered short home indicator."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '0b4295a5-3f4e-42df-ad12-25d569164b66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rugged-tablet-device/20260929T084629Z-thuan-mac/reference/tablet rugged_0b4295a5-3f4e-42df-ad12-25d569164b66.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rugged-tablet-device'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('tablet rugged',)

    def build(self):

        def line(n, a, b): self.add_line(n, a, b)
        def poly(n, *p, closed=False): self.add_polyline(n, *p, closed=closed)
        def arc(n, a, b, rx, ry=None, sweep=True, large=False):
            self.add_arc(n, a, b, radius_x=rx, radius_y=ry or rx, sweep=sweep, large_arc=large)
        def ellipse(n, x, y, rx, ry=None):
            ry = ry or rx
            arc(n+'-top', (x-rx,y), (x+rx,y), rx, ry)
            arc(n+'-bottom', (x+rx,y), (x-rx,y), rx, ry)
            self.add_contour(n, n+'-top', n+'-bottom', closed=True)
        def path(n, start, segments, closed=False):
            p = start; members = []
            for i, seg in enumerate(segments):
                name = f'{n}-{i}'; q = seg[1]
                if seg[0] == 'L': line(name,p,q)
                else: arc(name,p,q,*seg[2:])
                members.append(name); p=q
            self.add_contour(n,*members,closed=closed)
        def rounded(n, x1,y1,x2,y2,r):
            path(n,(x1+r,y1), [('L',(x2-r,y1)),('A',(x2,y1+r),r),
                ('L',(x2,y2-r)),('A',(x2-r,y2),r),('L',(x1+r,y2)),
                ('A',(x1,y2-r),r),('L',(x1,y1+r)),('A',(x1+r,y1),r)],True)
        rounded('case',8,4,40,44,4)
        poly('screen',(14,10),(34,10),(34,34),(14,34),closed=True)
        line('home',(22,39),(26,39))

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Preserve the large display and home indicator of a tablet. The slim bezel needs 2 px ink gaps to avoid recreating the rejected tiny-screen design.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '97f46f075b4909e09255913ca684446ce4130cda1c880294720d3be282efa3ed'}
