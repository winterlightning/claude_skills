"""Circular badge contains mirrored eyes and triangular ear/brow marks; centered downward beak."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '09b24008-2fd9-4994-8d56-f0448e51ee39'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-owl-face-with-pointed-ear-marks/20260929T084629Z-thuan-mac/reference/askfm logo_09b24008-2fd9-4994-8d56-f0448e51ee39.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-owl-face-with-pointed-ear-marks'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('askfm logo',)

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
        ellipse('badge',24,24,20)
        for side,x in enumerate((17,31)):
            ellipse(f'eye-{side}',x,25,5)
            self.add_dot(f'pupil-{side}',(x,25))
        poly('left-brow',(12,16),(14,10),(20,15))
        poly('right-brow',(28,15),(34,10),(36,16))
        poly('beak',(20,33),(24,38),(28,33))

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Retain round owl badge, paired eye rings with pupils, brows and beak. These identifying nested facial details need compact spacing at 48 px.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': 'a0eb5908042db547ca46a8e8b674f6b1c8441de9d76d4ec6f557def9ae4a3a8e'}
