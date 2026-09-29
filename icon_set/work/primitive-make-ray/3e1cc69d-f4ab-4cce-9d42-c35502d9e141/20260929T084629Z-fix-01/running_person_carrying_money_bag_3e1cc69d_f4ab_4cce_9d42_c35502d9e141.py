"""Human reference aligned detached circular head; carrying arm reaches left to tied money sack. Asymmetric arms and bent legs convey forward motion. Exact head-to-torso ink gap is 4."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '3e1cc69d-f4ab-4cce-9d42-c35502d9e141'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__running-person-carrying-money-bag/20260929T084629Z-thuan-mac/reference/robber_3e1cc69d-f4ab-4cce-9d42-c35502d9e141.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'running-person-carrying-money-bag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('robber',)

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
        ellipse('head',27,11,5)
        line('torso',(22,23),(17,35))
        poly('forward-arm',(22,23),(34,18),(42,22))
        poly('carrying-arm',(22,23),(15,27),(9,23))
        poly('back-leg',(17,35),(13,40),(19,42))
        poly('front-leg',(17,35),(29,31),(34,40),(42,40))
        path('bag',(6,30),[('L',(10,30)),('L',(12,36)),('A',(4,36),4,5),('L',(6,30))],True)
        poly('tie',(6,30),(5,26),(11,26),(10,30))
        line('money-stroke',(8,34),(8,39))
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
