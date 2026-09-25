"""An upright pencil sits beside a lined notepad."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='0a986353-aa51-5b90-9b59-cd4231e45a16'
SOURCE_PATH='pictographic-primitives/office/office stationery_0a986353-aa51-5b90-9b59-cd4231e45a16.svg'
AUTHOR='gpt-6'

class PencilAndNotepad(Solo48):
    icon_id='pencil-and-notepad'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    aliases=()
    keywords=('pencil', 'notepad', 'notes', 'writing', 'stationery', 'office')

    def build(self):
        # Plan: An upright pencil sits beside a lined notepad. Centerline extremes (4,8)-(44,40).
        # Reduction: Keep two text lines; omit cap and tip divider lines to keep the pencil opening clear.
        # Reference: Lucide pencil: coherent tip and rounded cap.
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
        arc('cap',(4,12),(12,12),4)
        path('pencil',(12,12),(12,32),(8,40),(4,32),(4,12))
        path('notepad',(20,12),(44,12),(44,40),(20,40),closed=True)
        line('text-1',(28,22),(36,22))
        line('text-2',(28,30),(32,30))
        join_contacts()
