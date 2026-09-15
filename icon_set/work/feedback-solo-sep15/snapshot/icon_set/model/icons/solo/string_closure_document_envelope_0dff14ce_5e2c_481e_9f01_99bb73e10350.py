"""String fasteners secure a tall document envelope."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='0dff14ce-5e2c-481e-9f01-99bb73e10350'
SOURCE_PATH='pictographic-primitives/office/folder sealed_0dff14ce-5e2c-481e-9f01-99bb73e10350.svg'
AUTHOR='gpt-6'

class StringClosureDocumentEnvelope(Solo48):
    icon_id='string-closure-document-envelope'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('envelope', 'document', 'string', 'closure', 'folder', 'office')

    def build(self):
        # Plan: String fasteners secure a tall document envelope. Centerline extremes (8,4)-(40,44).
        # Reduction: Retain two fasteners and string; omit lower corner folds.
        # Reference: No close Lucide match; use symmetric geometric folds.
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
        path('envelope',(8,4),(40,4),(40,44),(8,44),closed=True)
        for n,y in enumerate([16,32]): circle(f'button-{n}',24,y,3)
        line('string',(24,19),(24,29))
        path('flap-left',(8,4),(16,16),(21,16))
        path('flap-right',(27,16),(32,16),(40,4))
        join_contacts()
