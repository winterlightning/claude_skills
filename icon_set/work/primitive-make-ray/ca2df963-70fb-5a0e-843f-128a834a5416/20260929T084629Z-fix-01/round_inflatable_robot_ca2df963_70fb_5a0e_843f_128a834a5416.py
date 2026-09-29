"""Horizontal oval face, mirrored hanging arms and a single soft body with two feet. Eyes connected by one horizontal face line."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'ca2df963-70fb-5a0e-843f-128a834a5416'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-inflatable-robot/20260929T084629Z-thuan-mac/reference/robot baymax_ca2df963-70fb-5a0e-843f-128a834a5416.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-inflatable-robot'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('robot baymax',)

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
        ellipse('head',24,11,9,7)
        line('face-link',(21,11),(27,11))
        path('body',(15,22),[('A',(12,34),20,20,False),('A',(15,40),6,6,False),('L',(15,44)),('L',(21,44)),('L',(21,40)),('L',(27,40)),('L',(27,44)),('L',(33,44)),('L',(33,40)),('A',(36,34),6,6,False),('A',(33,22),20,20,False)])
        path('left-arm',(15,19),[('A',(8,32),18,18,False),('A',(12,35),4,4,False)])
        path('right-arm',(33,19),[('A',(40,32),18,18),('A',(36,35),4,4)])
