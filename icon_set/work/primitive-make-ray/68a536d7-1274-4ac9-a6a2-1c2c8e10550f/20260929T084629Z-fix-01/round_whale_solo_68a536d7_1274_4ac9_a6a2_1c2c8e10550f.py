"""Round whale body with broad smile and two lower belly seams; a mirrored two-arc fountain springs from its crown."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '68a536d7-1274-4ac9-a6a2-1c2c8e10550f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-whale-solo/20260929T084629Z-thuan-mac/reference/whale_68a536d7-1274-4ac9-a6a2-1c2c8e10550f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-whale-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('whale',)

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
        ellipse('body',24,28,16)
        arc('smile',(8,28),(40,28),24,11,False)
        path('fountain-left',(24,12),[('A',(14,4),10,8,False)])
        path('fountain-right',(24,12),[('A',(34,4),10,8,True)])
        arc('belly-left',(18,34),(20,43),18,18,False)
        arc('belly-right',(30,34),(28,43),18,18,True)

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Retain round whale body, curved fountain, shallow smile and belly seams. Seams intentionally meet the body and smile, preserving the supplied stylized whale.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '38aa0ac869896ff75f29c7b8796032f68d6c38b562a45ada17d5e13a2dd51c63'}
