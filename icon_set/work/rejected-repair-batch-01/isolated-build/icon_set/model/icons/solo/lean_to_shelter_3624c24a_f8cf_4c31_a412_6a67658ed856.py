"""lean-to-shelter: Open lean-to in side view; sloping roof, short post and ground retained as two connected runs. Rounded post-to-ground corner."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3624c24a-f8cf-4c31-a412-6a67658ed856'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors shelter_3624c24a-f8cf-4c31-a412-6a67658ed856.svg'
AUTHOR = 'gpt-6'

class LeanToShelter(Solo48):
    icon_id = 'lean-to-shelter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('shelter', 'lean-to', 'camping', 'roof', 'hut', 'survival', 'outdoors', 'outdoors-batch-03')

    def build(self):
        # Plan: Open lean-to in side view; sloping roof, short post and ground retained as two connected runs. Rounded post-to-ground corner.
        # Lucide construction reference: tent; original and atomic-debug inspected where named.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (4, 8, 44, 40).
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
        poly('roof',(4,28),(8,26),(44,8))
        path('post-ground',(8,26),[('L',(8,36)),('A',(12,40),4,4,False),('L',(44,40))]);join('roof','post-ground')
