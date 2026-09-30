"""A circular award medal with a ribbon hanging below it, cut into two notched tails.

Plan: medal circle r10 on axis x=24; the ribbon leaves the circle at its (6, 8) integer points,
splays to the canvas edge and is cut by one V notch, so each tail ends in a point.
Repair (2026-09-30): the earlier forked tails enclosed two holes under 6 units (build gate
holes/pinches); the tails now share one open band whose interior stays at least 13 tall.
Keyshape: VRECT_M.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b54db383-db23-4859-92c2-e71b7abb5e7a'
SOURCE_PATH = 'icon_set/work/todo-references/ribbon_b54db383-db23-4859-92c2-e71b7abb5e7a.svg'
AUTHOR = 'claude-opus-5-5'

class Drawing(Solo48):
    icon_id = 'ribbon'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('ribbon',)

    def build(self):
        cx, cy, r = 24, 14, 10
        # Medal split at the ribbon's two attachment points.
        self.add_arc('medal-top', (cx - 6, cy + 8), (cx + 6, cy + 8), radius_x=r, large_arc=True)
        self.add_arc('medal-bottom-right', (cx + 6, cy + 8), (cx, cy + r), radius_x=r)
        self.add_arc('medal-bottom-left', (cx, cy + r), (cx - 6, cy + 8), radius_x=r)
        self.add_contour('medal', 'medal-top', 'medal-bottom-right', 'medal-bottom-left', closed=True)
        self.add_polyline('ribbon', (cx - 6, cy + 8), (10, 44), (cx, 37), (38, 44), (cx + 6, cy + 8))
        self.relate('connect', 'ribbon-1', 'medal-top', 'medal-bottom-left')
        self.relate('connect', 'ribbon-4', 'medal-top', 'medal-bottom-right')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, l, t, r, b, rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i in range(8):
            a,z=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def arrow(self, name, start, tip, wing1, wing2):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',wing1,tip,wing2)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')

    def heart(self, name, x, top, half, bottom):
        # Mirrored lobes share dimensions and meet the pointed lower silhouette.
        self.add_bezier(name+'-left',(x,top+2),((x-half,top-5),(x-half-3,top+4),(x-half,top+7)),((x-half+2,top+10),(x, bottom),(x,bottom)))
        self.add_bezier(name+'-right',(x,bottom),((x,bottom),(x+half-2,top+10),(x+half,top+7)),((x+half+3,top+4),(x+half,top-5),(x,top+2)))
        self.add_contour(name,name+'-left',name+'-right',closed=True)
