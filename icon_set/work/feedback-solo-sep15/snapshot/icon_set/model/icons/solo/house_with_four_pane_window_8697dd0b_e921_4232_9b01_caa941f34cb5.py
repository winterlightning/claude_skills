"""A house has a central four-pane window and a short right chimney."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='8697dd0b-e921-4232-9b01-caa941f34cb5'
SOURCE_PATH='pictographic-primitives/office/work from home office_8697dd0b-e921-4232-9b01-caa941f34cb5.svg'
AUTHOR='gpt-6'

class HouseWithFourPaneWindow(Solo48):
    icon_id='house-with-four-pane-window'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/office"
    aliases=()
    keywords=('house', 'home', 'window', 'roof', 'building', 'office')

    def build(self):
        # Centerline extremes (6,6)-(42,42).
        # Reduction: Use a shallower roof pitch and omit projecting eaves to retain all four panes with clear openings.
        # Reference: Lucide house: pitched silhouette; shared window grid constructed from one axis.
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
        # Plan: shallow pitched roof and walls around a 2x2 window; right chimney.
        axis=24;left=6;right=2*axis-left
        path('house',(left,12),(axis,6),(33,9),(right,12),(right,42),(left,42),closed=True)
        line('chimney',(33,6),(33,9))
        wl=16;wr=2*axis-wl;top=18;step=8
        path('window',(wl,top),(axis,top),(wr,top),(wr,top+step),(wr,top+2*step),(axis,top+2*step),(wl,top+2*step),(wl,top+step),closed=True)
        line('mullion',(axis,top),(axis,top+step))
        line('mullion-lower',(axis,top+step),(axis,top+2*step))
        path('transom',(wl,top+step),(axis,top+step),(wr,top+step))
        join_contacts()
