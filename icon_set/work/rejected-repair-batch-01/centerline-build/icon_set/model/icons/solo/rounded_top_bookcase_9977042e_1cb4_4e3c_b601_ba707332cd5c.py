"""A rounded-top bookcase holds books on two shelves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='9977042e-1cb4-4e3c-b601-ba707332cd5c'
SOURCE_PATH='pictographic-primitives/office/shelf_9977042e-1cb4-4e3c-b601-ba707332cd5c.svg'
AUTHOR='gpt-6'

class RoundedTopBookcase(Solo48):
    icon_id='rounded-top-bookcase'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('bookcase', 'books', 'shelves', 'storage', 'furniture', 'office')

    def build(self):
        # Centerline extremes (8,4)-(40,44).
        # Reduction: Keep two books per level; omit spine marks and the fifth book.
        # Reference: Lucide library: upright books; book: consistent rounded upper corners.
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
        # Plan: mirrored round-topped frame, two shelves and paired books.
        axis=24
        line('top',(12,4),(36,4))
        arc('corner-right',(36,4),(40,8),4)
        path('right',(40,8),(40,24),(40,40),(40,44))
        path('left',(8,44),(8,40),(8,24),(8,8))
        arc('corner-left',(8,8),(12,4),4)
        for i,y in enumerate([24,40]):path(f'shelf-{i}',(8,y),(16,y),(axis,y),(32,y),(40,y))
        path('books-upper',(16,24),(16,12),(axis,12),(axis,16),(32,16),(32,24))
        line('upper-spine',(axis,16),(axis,24))
        path('books-lower',(16,40),(16,32),(axis,32),(32,32),(32,40))
        line('lower-spine',(axis,32),(axis,40))
        join_contacts()
