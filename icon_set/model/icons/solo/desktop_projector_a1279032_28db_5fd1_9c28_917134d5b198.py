"""A desktop projector has a large lens on the right and a left ventilation mark."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='a1279032-28db-5fd1-9c28-917134d5b198'
SOURCE_PATH='pictographic-primitives/office/presentation projector_a1279032-28db-5fd1-9c28-917134d5b198.svg'
AUTHOR='gpt-6'

class DesktopProjector(Solo48):
    icon_id='desktop-projector'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('projector', 'lens', 'presentation', 'projection', 'equipment', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Three ventilation slots become one; retain lens and both feet.
        # Reference: Lucide projector: circular lens interrupting the housing outline.
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
        # Plan: lens circle, housing wrapped around its sides, vent and repeated feet.
        circle('lens',34,18,10)
        line('top-left',(24,18),(8,18))
        arc('corner-tl',(8,18),(4,22),4,sweep=False)
        line('left',(4,22),(4,32))
        arc('corner-bl',(4,32),(8,36),4,sweep=False)
        path('base',(8,36),(12,36),(36,36),(40,36))
        arc('corner-br',(40,36),(44,32),4,sweep=False)
        line('right',(44,32),(44,18))
        line('vent',(12,26),(12,28))
        for i,x in enumerate([12,36]):line(f'foot-{i}',(x,36),(x,40))
        join_contacts()
