"""Human reference circular head and coherent stick limbs, with raised arms and angled running legs; finish tape crosses the waist. Detached head outline ends at 15, torso begins at 23: 4 ink units."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '16b9f2ab-9387-51cc-9d12-6908f0e5c10e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__runner-finish-ribbon/20260929T084629Z-thuan-mac/reference/marathon running finished goal_16b9f2ab-9387-51cc-9d12-6908f0e5c10e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'runner-finish-ribbon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('marathon running finished goal',)

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
        ellipse('head',24,10,5)
        line('torso',(24,23),(24,29))
        poly('left-arm',(24,23),(15,21),(10,15),(8,6))
        poly('right-arm',(24,23),(33,21),(38,15),(40,6))
        poly('left-leg',(24,35),(19,42),(11,42))
        poly('right-leg',(24,35),(31,39),(31,42))
        poly('tape',(6,29),(42,29),(40,32),(42,35),(6,35),(8,32),closed=True)
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Retain raised arms, bent running legs and a narrow finish tape with concave ends. The head-to-torso ink gap is exactly 4 px; compact arm and tape spacing is intentional.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': 'f545e0d82e8c98ef512526e5eb40d1faf8f6ce847211f5631189d2536ddbecd6'}
