"""Shared human-reference circle head, torso and bent limbs. Upper torso vector (5,-12) points at the head; center-to-shoulder distance 13 minus head radius 5 leaves 8 centerline units, exactly 4 ink units."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '308599f6-0b87-5e57-8523-c30eb5dd4e7a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__running-athlete/20260929T084629Z-thuan-mac/reference/sport runner_308599f6-0b87-5e57-8523-c30eb5dd4e7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'running-athlete'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('sport runner',)

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
        ellipse('head',29,11,5)
        line('torso',(24,23),(19,35))
        poly('arm-back',(24,23),(15,21),(7,29))
        poly('arm-forward',(24,23),(36,28),(42,14))
        poly('leg-back',(19,35),(13,41),(6,42))
        poly('leg-forward',(19,35),(29,39),(29,42))
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
