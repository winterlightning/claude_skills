"""A small blank building has a broad roof fascia and centered arched doorway."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='8678ab0b-c74e-5f87-8c88-edaf06396cc3'
SOURCE_PATH='pictographic-primitives/office/small office middle building_8678ab0b-c74e-5f87-8c88-edaf06396cc3.svg'
AUTHOR='gpt-6'

class SmallFlatRoofBuilding(Solo48):
    icon_id='small-flat-roof-building'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "office"
    categories = ("office", "primitives")
    aliases=()
    keywords=('building', 'office', 'door', 'roof', 'architecture', 'workplace')

    def build(self):
        # Centerline extremes (4,8)-(44,40).
        # Reduction: Retain roof band, broad plain facade and central doorway.
        # Reference: Lucide building: symmetric facade and arched entrance.
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
        # Plan: capsule roof fascia over mirrored walls and central entrance.
        axis=24
        line('roof-top',(8,8),(40,8))
        arc('roof-tr',(40,8),(44,12),4)
        arc('roof-br',(44,12),(40,16),4)
        line('roof-bottom',(40,16),(8,16))
        arc('roof-bl',(8,16),(4,12),4)
        arc('roof-tl',(4,12),(8,8),4)
        self.add_contour('fascia','roof-top','roof-tr','roof-br','roof-bottom','roof-bl','roof-tl',closed=True)
        path('wall-left',(8,16),(8,40),(20,40))
        path('wall-right',(28,40),(40,40),(40,16))
        line('door-left',(20,40),(20,32))
        arc('door-arch',(20,32),(28,32),4)
        line('door-right',(28,32),(28,40))
        line('threshold',(20,40),(28,40))
        join_contacts()
