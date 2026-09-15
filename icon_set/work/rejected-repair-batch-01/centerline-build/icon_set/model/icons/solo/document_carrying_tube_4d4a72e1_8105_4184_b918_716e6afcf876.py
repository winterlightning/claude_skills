"""A capped document tube has a broad looped carrying strap."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4d4a72e1-8105-4184-b918-716e6afcf876'
SOURCE_PATH='pictographic-primitives/office/paper holder tube_4d4a72e1-8105-4184-b918-716e6afcf876.svg'
AUTHOR='gpt-6'

class DocumentCarryingTube(Solo48):
    icon_id='document-carrying-tube'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('document', 'tube', 'carrier', 'strap', 'drawing', 'office')

    def build(self):
        # Plan: A capped document tube has a broad looped carrying strap. Centerline extremes (8,4)-(40,44).
        # Reduction: Keep one longitudinal rib; omit cap dots and duplicate ribs.
        # Reference: Lucide paperclip: coherent loop; source sets asymmetric shoulder strap.
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
        line('top',(28,4),(36,4))
        arc('cap-tr',(36,4),(40,8),4)
        line('right',(40,8),(40,40))
        arc('base-br',(40,40),(36,44),4)
        line('base',(36,44),(28,44))
        arc('base-bl',(28,44),(24,40),4)
        path('left',(24,40),(24,36),(24,12),(24,8))
        arc('cap-tl',(24,8),(28,4),4)
        line('cap-seam',(24,12),(40,12))
        arc('strap',(24,12),(24,36),16,12,sweep=False)
        line('rib',(32,22),(32,34))
        join_contacts()
