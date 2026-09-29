"""Elliptical lid, a shallow repeated front band, cylindrical body, centered semicircular handle."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'cd694669-154a-40d8-b638-21a45768cc05'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-hatbox-with-loop-handle/20260929T084629Z-thuan-mac/reference/hatbox_cd694669-154a-40d8-b638-21a45768cc05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-hatbox-with-loop-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('hatbox',)

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
        ellipse('lid',24,17,16,5)
        path('body',(8,17),[('L',(8,38)),('A',(40,38),16,6,False),('L',(40,17))])
        arc('lid-band',(8,24),(40,24),16,5,False)
        path('handle',(18,13),[('L',(18,10)),('A',(30,10),6,6),('L',(30,13))])

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Preserve elliptical lid band and genuine handle-to-lid and wall-to-band contacts; they identify the cylindrical hatbox rather than a purse.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '951ff1d67a2cb5367f3260f344f34aff84413c62cd9261860390a2c4d175a6d6'}
