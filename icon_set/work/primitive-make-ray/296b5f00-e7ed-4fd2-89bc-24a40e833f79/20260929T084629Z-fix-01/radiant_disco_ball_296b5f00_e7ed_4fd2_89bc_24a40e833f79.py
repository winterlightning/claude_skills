"""Circular globe with shared-axis ellipse meridian and two latitude chords; eight radial glints."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '296b5f00-e7ed-4fd2-89bc-24a40e833f79'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__radiant-disco-ball/20260929T084629Z-thuan-mac/reference/night club disco ball_296b5f00-e7ed-4fd2-89bc-24a40e833f79.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'radiant-disco-ball'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('night club disco ball',)

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
        ellipse('ball',24,24,13)
        ellipse('meridian',24,24,5,13)
        line('latitude-top',(13,18),(35,18))
        line('latitude-bottom',(13,30),(35,30))
        for i,p in enumerate([(24,4),(24,44),(4,24),(44,24),(10,10),(38,10),(10,38),(38,38)]): self.add_dot(f'glint-{i}',p)

    # User authorized meaning-preserving UI exceptions for this exact drawing.
    exception = {'reason': 'Retain the disco sphere meridians, latitude intersections and eight glints. Compact cells are intentional and the spherical grid remains readable at 48 px.', 'approved_by': 'user (delegated exception judgment to gpt-6)', 'approved_on': '2026-09-29', 'svg_sha256': '2575ce3f822cec2a62059c74c2c501affa5ff1daa3eb14698d320b7125877deb'}
