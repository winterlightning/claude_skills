"""One rounded crown transitions into mirrored side curls; three hanging lower arms curl upward."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '64eee8f4-0acb-4945-bff4-e2c5283f21e0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-headed-octopus/20260929T084629Z-thuan-mac/reference/cephalopod_64eee8f4-0acb-4945-bff4-e2c5283f21e0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-headed-octopus'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('cephalopod',)

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
        path('crown-and-side-arms',(8,25),[('L',(8,28)),('A',(16,28),4,4,False),('A',(12,17),15,15,False),('A',(36,17),12,13),('A',(32,28),15,15,False),('A',(40,28),4,4,False),('L',(40,25))])
        path('left-arm',(10,36),[('L',(10,39)),('A',(20,39),5,5,False),('L',(20,32))])
        path('right-arm',(28,32),[('L',(28,39)),('A',(38,39),5,5,False),('L',(38,36))])
        line('central-arm',(24,34),(24,44))
        self.add_dot('eye-left',(20,24)); self.add_dot('eye-right',(28,24))
