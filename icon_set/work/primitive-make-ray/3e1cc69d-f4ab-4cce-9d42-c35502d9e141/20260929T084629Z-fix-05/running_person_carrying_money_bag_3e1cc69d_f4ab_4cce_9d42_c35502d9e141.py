"""Tied sack with separated dollar glyph and a running figure; 4-unit detached head gap. Widened sack shoulders and shifted the rear leg to prevent unwanted joins."""
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
        ellipse('head',33,9,5)
        line('torso',(33,22),(33,27))
        line('lower-torso',(33,27),(29,32))
        poly('forward-arm',(33,22),(40,24),(44,18))
        poly('carrying-arm',(33,22),(25,22),(17,17),(13,17))
        poly('back-leg',(29,32),(28,39),(33,44))
        poly('front-leg',(29,32),(38,31),(41,40),(44,40))
        path('bag',(8,22),[('L',(3,26)),('L',(3,38)),('A',(23,38),10,6,False),('L',(23,26)),('L',(18,22))])
        poly('tie',(8,22),(7,17),(13,17),(19,17),(18,22))
        path('dollar',(17,28),[('L',(11,28)),('A',(11,32),3,2,False),('L',(15,34)),('A',(15,38),3,2),('L',(9,38))])
        line('dollar-stem',(13,24),(13,39))
        self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Retain the explicit dollar sack and running person in one 48 px composition. Bag lettering requires compact gaps; the head-to-torso ink gap remains exactly 4 px.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '2311cc37e938aa9cbeff83f0cb2ff20dc6b68a58bbc37a074654694691c6e40c'}
