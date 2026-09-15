"""Two separate arrows point outward along a rising diagonal."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='2d56f258-b529-5945-bceb-ffb22b676c73'
SOURCE_PATH='pictographic-primitives/networks/data transfer diagonal_2d56f258-b529-5945-bceb-ffb22b676c73.svg'
AUTHOR='gpt-6'

class ArrowsDiagonalOpposing(Solo48):
    icon_id='arrows-diagonal-opposing'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/networks'
    aliases=()
    keywords=('arrows', 'diagonal', 'opposing', 'network')

    def build(self):
        # Plan: Two separate arrows point outward along a rising diagonal. Centerline extremes (6,6)-(42,42).
        # Reduction: Keep two open arrowheads and separate diagonal shafts.
        # Reference: Lucide move-up-right: equal orthogonal arrowhead arms.
        # All contacts below are physical joints sharing exact endpoints.
        endpoints = {}
        def line(name, a, b):
            self.add_line(name, a, b)
            endpoints[name] = (a, b)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
            endpoints[name] = tuple(points)
        def arc(name, a, b, r, ry=None, sweep=True):
            self.add_arc(name, a, b, radius_x=r, radius_y=ry or r, sweep=sweep)
            endpoints[name] = (a, b)
        def join_contacts():
            names = list(endpoints)
            for i, a in enumerate(names):
                for b in names[i+1:]:
                    if set(endpoints[a]) & set(endpoints[b]):
                        self.relate("connect", a, b)
        def circle(name,cx,cy,r):
            arc(name+'-top',(cx-r,cy),(cx,cy-r),r)
            arc(name+'-right',(cx,cy-r),(cx+r,cy),r)
            arc(name+'-bottom',(cx+r,cy),(cx,cy+r),r)
            arc(name+'-left',(cx,cy+r),(cx-r,cy),r)
            self.add_contour(name,*(name+s for s in ['-top','-right','-bottom','-left']),closed=True)

        # Both arrows are the same symbol, rotated 180 degrees about (24,24).
        for n,flip in [('upper',False),('lower',True)]:
            def p(x,y):return (48-x,48-y) if flip else (x,y)
            path(n+'-head',p(26,6),p(42,6),p(42,22))
            line(n+'-shaft',p(28,20),p(42,6))
        join_contacts()
