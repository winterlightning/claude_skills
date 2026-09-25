"""camping-gas-lantern: Upright gas lantern with flared cap, straight glass chamber, teardrop flame on a burner stem, and broad fuel base. Symmetry about x24; tiny valve and extra bands omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a4fac5c-4d71-43e9-80e2-c8bf9b73c686'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors camp flame_5a4fac5c-4d71-43e9-80e2-c8bf9b73c686.svg'
AUTHOR = 'gpt-6'


class CampingGasLantern(Solo48):
    icon_id = 'camping-gas-lantern'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('lantern', 'camping', 'gas', 'flame', 'light', 'outdoors', 'lamp', 'outdoors-batch-02')

    def build(self):
        # Plan: Upright gas lantern with flared cap, straight glass chamber, teardrop flame on a burner stem, and broad fuel base. Symmetry about x24; tiny valve and extra bands omitted.
        # Lucide flame original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (8, 4, 40, 44).
        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        poly('lantern',(8,44),(8,32),(10,32),(10,12),(8,12),(12,4),(36,4),(40,12),(38,12),(38,32),(40,32),(40,44),closed=True)
        poly('base-top',(8,32),(10,32),(24,32),(38,32),(40,32));join('base-top','lantern')
        path('flame',(24,14),[('A',(28,20),10,10,True),('A',(24,24),4,4,True),('A',(20,20),4,4,True),('A',(24,14),10,10,True)],True)
        line('burner',(24,24),(24,32));join('burner','base-top');join('burner','flame')
