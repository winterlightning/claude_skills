"""Two opposing arrows have curved return tails."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c6e7551b-5203-4efa-81e3-83c79d80e829'
SOURCE_PATH='pictographic-primitives/networks/data transfer_c6e7551b-5203-4efa-81e3-83c79d80e829.svg'
AUTHOR='gpt-6'

class ArrowsCurvedTransfer(Solo48):
    icon_id='arrows-curved-transfer'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/networks'
    aliases=()
    keywords=('arrows', 'curved', 'transfer', 'network')

    def build(self):
        # Plan: Two opposing arrows have curved return tails. Centerline extremes (6,6)-(42,42).
        # Reduction: Replace broad double outlines with single shafts to keep clear opposing arrows and curved tails.
        # Reference: Lucide repeat-2: paired arrows with tangent quarter-circle tails.
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

        # One arrow repeated by half-turn; radius 8 tails join horizontal shafts.
        for n,flip in [('upper',False),('lower',True)]:
            def p(x,y):return (48-x,48-y) if flip else (x,y)
            arc(n+'-tail',p(6,22),p(14,14),8)
            line(n+'-shaft',p(14,14),p(42,14))
            self.add_contour(n+'-flow',n+'-tail',n+'-shaft')
            path(n+'-head',p(34,6),p(42,14),p(34,22))
        join_contacts()
