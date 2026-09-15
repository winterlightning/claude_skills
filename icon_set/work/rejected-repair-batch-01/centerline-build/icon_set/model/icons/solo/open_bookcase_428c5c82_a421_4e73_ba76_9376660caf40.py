"""An open bookcase has books on its upper left and lower right shelves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='428c5c82-a421-4e73-ba76-9376660caf40'
SOURCE_PATH='pictographic-primitives/office/shelf_428c5c82-a421-4e73-ba76-9376660caf40.svg'
AUTHOR='gpt-6'

class OpenBookcase(Solo48):
    icon_id='open-bookcase'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('bookcase', 'books', 'shelf', 'storage', 'furniture', 'office')

    def build(self):
        # Centerline extremes (6,6)-(42,42).
        # Reduction: Keep two books on each level instead of five total; omit spine decorations.
        # Reference: Lucide library: unequal book heights and repeated upright spines.
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
        # Plan: two open rails and shelves, staggered paired-book groups.
        axis=24
        for i,x in enumerate([6,2*axis-6]):path(f'rail-{i}',(x,6),(x,22),(x,42))
        path('shelf-upper',(6,22),(14,22),(22,22),(30,22),(42,22))
        path('shelf-lower',(6,42),(18,42),(26,42),(34,42),(42,42))
        path('books-upper',(14,22),(14,10),(22,10),(22,14),(30,14),(30,22))
        line('spine-upper',(22,14),(22,22))
        path('books-lower',(18,42),(18,34),(26,34),(26,30),(34,30),(34,42))
        line('spine-lower',(26,34),(26,42))
        join_contacts()
