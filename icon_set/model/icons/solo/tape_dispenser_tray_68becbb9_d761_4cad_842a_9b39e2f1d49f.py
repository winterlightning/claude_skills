"""A trapezoidal tape tray holds a partly exposed right-hand roll."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='68becbb9-d761-4cad-842a-9b39e2f1d49f'
SOURCE_PATH='pictographic-primitives/office/tape_68becbb9-d761-4cad-842a-9b39e2f1d49f.svg'
AUTHOR='gpt-6'

class TapeDispenserTray(Solo48):
    icon_id='tape-dispenser-tray'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('tape', 'dispenser', 'tray', 'roll', 'adhesive', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Keep the roll opening and sloped left support; omit extra tray seams.
        # Reference: No useful local Lucide tape match; integer-centered circular arcs and a simple tray.
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
        # Plan: upper half of a roll and concentric hub above the tray lip.
        # The lower roll is hidden by the dispenser front. Shared center (32,20).
        arc('roll',(20,20),(44,20),12)
        circle('hub',32,20,3)
        path('tray',(4,32),(44,32),(40,40),(8,40),closed=True)
        path('support',(4,32),(4,16),(20,20))
        line('roll-right',(44,20),(44,32))
        join_contacts()
