"""A printer holds an input sheet and a printed output page."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='a42143e2-1900-58a9-a129-97180c19c22e'
SOURCE_PATH='pictographic-primitives/office/office printer_a42143e2-1900-58a9-a129-97180c19c22e.svg'
AUTHOR='gpt-6'

class PrinterWithPaper(Solo48):
    icon_id='printer-with-paper'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('printer', 'paper', 'printing', 'document', 'machine', 'office')

    def build(self):
        # Plan: A printer holds an input sheet and a printed output page. Centerline extremes (6,6)-(42,42).
        # Reduction: Keep both sheets; reduce two printed lines to one.
        # Reference: Lucide printer: rounded housing surrounding an emerging sheet.
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
        path('input',(14,16),(14,6),(34,6),(34,16))
        path('housing-top',(10,16),(14,16),(34,16),(38,16))
        arc('corner-tr',(38,16),(42,20),4)
        line('housing-right',(42,20),(42,30))
        arc('corner-br',(42,30),(38,34),4)
        line('ledge-right',(38,34),(34,34))
        line('ledge-left',(14,34),(10,34))
        arc('corner-bl',(10,34),(6,30),4)
        line('housing-left',(6,30),(6,20))
        arc('corner-tl',(6,20),(10,16),4)
        path('output',(14,34),(14,26),(34,26),(34,34),(34,42),(14,42),closed=True)
        line('text',(22,34),(26,34))
        join_contacts()
