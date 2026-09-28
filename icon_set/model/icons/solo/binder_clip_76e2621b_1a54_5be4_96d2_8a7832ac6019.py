"""A binder clip has a raised looped wire handle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='76e2621b-1a54-5be4-96d2-8a7832ac6019'
SOURCE_PATH='pictographic-primitives/office/office clipper_76e2621b-1a54-5be4-96d2-8a7832ac6019.svg'
AUTHOR='gpt-6'

class BinderClip(Solo48):
    icon_id='binder-clip'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('binder clip', 'clip', 'paper', 'stationery', 'fastener', 'office')

    def build(self):
        # Plan: A binder clip has a raised looped wire handle. Centerline extremes (4,8)-(44,40).
        # Reduction: Keep the rounded wire loop, narrowed shoulder and wire ends spreading through the trapezoidal clamp; omit duplicate handle.
        # Reference: Lucide paperclip: coherent rounded wire loop.
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
        # The wire narrows at the shoulder then spreads through the clamp.
        arc('handle-top',(16,16),(32,16),8)
        path('wire-left',(16,16),(20,24),(16,40))
        path('wire-right',(32,16),(28,24),(32,40))
        path('clamp',(8,24),(20,24),(28,24),(40,24),(44,40),(32,40),(16,40),(4,40),closed=True)
        join_contacts()
