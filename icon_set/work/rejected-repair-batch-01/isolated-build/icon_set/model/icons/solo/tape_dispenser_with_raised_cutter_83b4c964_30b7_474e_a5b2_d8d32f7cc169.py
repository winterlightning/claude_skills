"""A tape dispenser has a raised left cutter and a deeply recessed roll housing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='83b4c964-30b7-474e-a5b2-d8d32f7cc169'
SOURCE_PATH='pictographic-primitives/office/tape_83b4c964-30b7-474e-a5b2-d8d32f7cc169.svg'
AUTHOR='gpt-6'

class TapeDispenserWithRaisedCutter(Solo48):
    icon_id='tape-dispenser-with-raised-cutter'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('tape', 'dispenser', 'cutter', 'roll', 'adhesive', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Omit the loose strip; retain the raised cutter, curved recess and circular opening.
        # Reference: No useful local Lucide tape match; tangent arcs join the recess to the roll.
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
        # Plan: narrow cutter stem, concave semicircle, three roll quarters, rounded base.
        line('cutter',(4,12),(4,24))
        arc('recess',(4,24),(12,24),4,sweep=False)
        arc('roll-tl',(12,24),(28,8),16)
        arc('roll-tr',(28,8),(44,24),16)
        arc('roll-br',(44,24),(28,40),16)
        line('base',(28,40),(8,40))
        arc('base-corner',(8,40),(4,36),4)
        line('left',(4,36),(4,24))
        self.add_contour('housing','recess','roll-tl','roll-tr','roll-br','base','base-corner','left',closed=True)
        circle('opening',28,24,5)
        join_contacts()
