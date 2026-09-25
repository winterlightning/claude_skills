"""A printer feeds a folded-corner document above a printed output page."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='022d70d7-c45e-470d-a79a-3f79fa268ec0'
SOURCE_PATH='pictographic-primitives/office/print text_022d70d7-c45e-470d-a79a-3f79fa268ec0.svg'
AUTHOR='gpt-6'

class PrinterFeedingDocument(Solo48):
    icon_id='printer-feeding-document'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('printer', 'document', 'paper', 'printing', 'machine', 'office')

    def build(self):
        # Centerline extremes (6,6)-(42,42).
        # Reduction: Retain the clipped page corner; omit fold seam and control, and reduce output text to one line.
        # Reference: Lucide printer: rounded housing and separate paper paths.
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
        # Plan: clipped input sheet, rounded housing, output sheet and text.
        path('input',(14,18),(14,6),(26,6),(34,14),(34,18))
        path('housing-top',(10,18),(14,18),(34,18),(38,18))
        arc('corner-tr',(38,18),(42,22),4)
        line('housing-right',(42,22),(42,30))
        arc('corner-br',(42,30),(38,34),4)
        line('ledge-right',(38,34),(34,34))
        line('ledge-left',(14,34),(10,34))
        arc('corner-bl',(10,34),(6,30),4)
        line('housing-left',(6,30),(6,22))
        arc('corner-tl',(6,22),(10,18),4)
        path('output',(14,34),(14,26),(34,26),(34,34),(34,42),(14,42),closed=True)
        line('text',(22,34),(26,34))
        join_contacts()
