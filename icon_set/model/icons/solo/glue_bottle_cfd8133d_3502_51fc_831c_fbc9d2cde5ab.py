"""A squeeze bottle has a long tapered glue nozzle."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='cfd8133d-3502-51fc-831c-fbc9d2cde5ab'
SOURCE_PATH='pictographic-primitives/office/office glue_cfd8133d-3502-51fc-831c-fbc9d2cde5ab.svg'
AUTHOR='gpt-6'

class GlueBottle(Solo48):
    icon_id='glue-bottle'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('glue', 'bottle', 'adhesive', 'nozzle', 'stationery', 'office')

    def build(self):
        # Plan: A squeeze bottle has a long tapered glue nozzle. Centerline extremes (8,4)-(40,44).
        # Reduction: Simplify the label to a bar and omit the nozzle divider that creates a tiny opening.
        # Reference: Lucide milk: bottle silhouette with geometric shoulders.
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
        path('body',(12,20),(20,20),(28,20),(36,20))
        arc('top-right',(36,20),(40,24),4)
        line('right',(40,24),(40,40))
        arc('bottom-right',(40,40),(36,44),4)
        line('bottom',(36,44),(12,44))
        arc('bottom-left',(12,44),(8,40),4)
        line('left',(8,40),(8,24))
        arc('top-left',(8,24),(12,20),4)
        path('nozzle',(20,20),(20,12),(24,4),(28,12),(28,20))
        line('label',(16,32),(32,32))
        join_contacts()
