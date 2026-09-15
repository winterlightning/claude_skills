"""A paper shredder pulls a sheet into a bin with three descending strips."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='f9bc359a-c877-4bc5-b8b6-05a036162690'
SOURCE_PATH='pictographic-primitives/office/shredder_f9bc359a-c877-4bc5-b8b6-05a036162690.svg'
AUTHOR='gpt-6'

class PaperShredder(Solo48):
    icon_id='paper-shredder'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('shredder', 'paper', 'document', 'shredding', 'machine', 'office')

    def build(self):
        # Centerline extremes (8,4)-(40,44).
        # Reduction: Straighten shredded strips; retain input sheet and two feet.
        # Reference: Lucide printer: input paper and housing; library: repeated vertical strokes.
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
        # Plan: input sheet, two horizontal head rails, bin and three strip instances.
        axis=24;left=8;right=2*axis-left
        path('input',(16,16),(16,4),(32,4),(32,16))
        path('body',(left,40),(left,24),(left,16),(16,16),(32,16),(right,16),(right,24),(right,40),closed=True)
        path('cutter',(left,24),(16,24),(axis,24),(32,24),(right,24))
        for i in range(3):
            x=axis-8+i*8
            line(f'strip-{i}',(x,24),(x,32))
        for i,x in enumerate([left,right]):line(f'foot-{i}',(x,40),(x,44))
        join_contacts()
