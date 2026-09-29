"""Larger tied sack with an explicit dollar; bent opposing strides and carrying arm. Circular head bottom is 14; upper torso starts at 22, exactly 4 units of visible gap."""
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
        # The torso is vertical at its upper junction, aligning the circular head.
        ellipse('head',33,9,5)
        line('torso',(33,22),(33,27))
        line('lower-torso',(33,27),(28,32))
        poly('forward-arm',(33,22),(40,24),(44,18))
        poly('carrying-arm',(33,22),(25,18),(13,18))
        poly('back-leg',(28,32),(26,38),(31,44))
        poly('front-leg',(28,32),(37,31),(41,40),(44,40))
        path('bag',(8,23),[('L',(4,29)),('A',(4,39),10,10,False),('A',(20,39),8,5,False),('A',(20,29),10,10,False),('L',(16,23)),('L',(8,23))],True)
        poly('tie',(8,23),(7,18),(17,18),(16,23))
        path('dollar',(15,28),[('L',(10,28)),('A',(10,33),2,3,False),('L',(14,34)),('A',(14,39),2,3),('L',(9,39))])
        line('dollar-stem',(12,26),(12,41))
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
