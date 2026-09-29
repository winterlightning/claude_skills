"""Lucide gamepad construction informs a rounded top with tapered grips. Reference four-button diamond and cross are retained."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '540e6c7f-d9cf-5188-9e6f-b558f13e37e5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rounded-gamepad-with-cross-control-and-four-buttons/20260929T084629Z-thuan-mac/reference/console_540e6c7f-d9cf-5188-9e6f-b558f13e37e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-gamepad-with-cross-control-and-four-buttons'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('console',)

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
        path('shell',(12,10),[('L',(36,10)),('A',(42,16),6),('L',(44,33)),('A',(37,38),5,5),('L',(30,30)),('L',(18,30)),('L',(11,38)),('A',(4,33),5,5),('L',(6,16)),('A',(12,10),6)],True)
        poly('dpad-h',(10,21),(14,21),(18,21))
        poly('dpad-v',(14,17),(14,21),(14,25))
        for i,p in enumerate(((33,16),(28,21),(38,21),(33,26))):self.add_dot(f'button-{i}',p)

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Preserve four face buttons, a clear cross D-pad and sloping grips. Compact button spacing is essential; natural grip arcs slightly depart from the rectangle envelope.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '7c1ae29efab1137560393929241c98b8adaa4f1121f710f71769187ff6ce8195'}
