"""A tall office tower stands behind a low entrance annex on its right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='c7498ea9-7caf-4e21-80b4-bb56905862bf'
SOURCE_PATH='pictographic-primitives/office/small office double building_c7498ea9-7caf-4e21-80b4-bb56905862bf.svg'
AUTHOR='gpt-6'

class OfficeTowerWithLowAnnex(Solo48):
    icon_id='office-tower-with-low-annex'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('office', 'building', 'tower', 'annex', 'architecture', 'workplace')

    def build(self):
        # Centerline extremes (6,6)-(42,42).
        # Reduction: Five windows become two; omit roof thickness but retain arched entrance and stepped massing.
        # Reference: Lucide building-2: grouped building masses and arched doorway.
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
        # Plan: tall left tower, low right annex, paired windows and inset doorway.
        path('tower',(18,42),(6,42),(6,6),(30,6),(30,22))
        path('roof',(18,22),(30,22),(42,22))
        path('annex-left',(18,22),(18,42),(26,42))
        path('annex-right',(34,42),(42,42),(42,22))
        for i,x in enumerate([14,22]):self.add_dot(f'window-{i}',(x,14))
        line('door-left',(26,42),(26,34))
        arc('door-arch',(26,34),(34,34),4)
        line('door-right',(34,34),(34,42))
        line('threshold',(26,42),(34,42))
        join_contacts()
