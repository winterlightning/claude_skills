"""A computer desk faces a separate pedestal office chair on the right."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='622546fc-95f1-4b41-b61f-18515fc257cd'
SOURCE_PATH='pictographic-primitives/office/worker needed computer_622546fc-95f1-4b41-b61f-18515fc257cd.svg'
AUTHOR='gpt-6'

class ComputerDeskWithChair(Solo48):
    icon_id='computer-desk-with-chair'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('computer', 'desk', 'chair', 'monitor', 'workstation', 'office')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Omit desktop thickness and chair armrests; keep screen, sloping desk leg and curved chair back.
        # Reference: Lucide monitor: blank screen and centered stem; armchair: flowing seat/back construction.
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
        # Plan: monitor with central stand, short desk, separate side-view chair.
        path('monitor',(14,24),(4,24),(4,8),(24,8),(24,24),(14,24),closed=True)
        line('monitor-stand',(14,24),(14,32))
        path('desktop',(4,32),(8,32),(14,32),(24,32))
        line('desk-leg',(8,32),(4,40))
        path('seat',(32,32),(36,32),(40,32))
        arc('chair-back',(40,32),(44,16),4,16,sweep=False)
        line('chair-stem',(36,32),(36,40))
        path('chair-foot',(28,40),(36,40),(44,40))
        join_contacts()
