"""Shallow rounded rectangle with evenly stepped diagonal lines; deliberate short height preserves the strip concept."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '537ef89a-3255-4de5-963f-3e20a738be5d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-horizontal-strip-with-diagonal-bands/20260929T084629Z-thuan-mac/reference/strip_537ef89a-3255-4de5-963f-3e20a738be5d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-horizontal-strip-with-diagonal-bands'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('strip',)

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
        rounded('strip',4,16,44,32,3)
        for i,(a,b) in enumerate((((4,29),(17,16)),((17,32),(33,16)),((33,32),(44,21)))):line(f'diagonal-{i}',a,b)

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Preserve the reference shallow strip aspect ratio instead of stretching it into a thick capsule. All geometry and spacing checks pass apart from the intended keyshape height.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '7406b471c6989d099e0d849ae5155f6e545894487d6f8b5007d7e270cf2394db'}
