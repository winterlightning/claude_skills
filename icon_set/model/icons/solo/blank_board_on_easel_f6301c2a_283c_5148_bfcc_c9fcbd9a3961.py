"""A blank board rests on a splayed easel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='f6301c2a-283c-5148-bfcc-c9fcbd9a3961'
SOURCE_PATH='pictographic-primitives/office/office drawing board_f6301c2a-283c-5148-bfcc-c9fcbd9a3961.svg'
AUTHOR='gpt-6'

class BlankBoardOnEasel(Solo48):
    icon_id='blank-board-on-easel'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('easel', 'board', 'drawing', 'canvas', 'stand', 'office')

    def build(self):
        # Plan: A blank board rests on a splayed easel. Centerline extremes (8,4)-(40,44).
        # Reduction: Omit rear brace; retain upper mast and two splayed legs.
        # Reference: Lucide presentation: blank board and stand geometry.
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
        path('board',(8,12),(24,12),(40,12),(40,32),(32,32),(16,32),(8,32),closed=True)
        line('mast',(24,4),(24,12))
        for i,(x,foot) in enumerate([(16,12),(32,36)]):line(f'leg-{i}',(x,32),(foot,44))
        join_contacts()
