"""parasailing: Open canopy and short rigging above a parasailer connected to a small tow boat. Head center (28,25), radius 3; body y36 gives exact 4-unit ink clearance. Boat pilot, canopy ribs and scallops omitted; suspension lines shortened as in the reference."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'be90db18-f520-40cb-b813-e134392a43e1'
SOURCE_PATH = 'pictographic-primitives/outdoors/sport para sailing_be90db18-f520-40cb-b813-e134392a43e1.svg'
AUTHOR = 'gpt-6'

class Parasailing(Solo48):
    icon_id = 'parasailing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('parasailing', 'parachute', 'boat', 'tow', 'sport', 'sea', 'adventure', 'outdoors-batch-03')

    def build(self):
        # Plan: Open canopy and short rigging above a parasailer connected to a small tow boat. Head center (28,25), radius 3; body y36 gives exact 4-unit ink clearance. Boat pilot, canopy ribs and scallops omitted; suspension lines shortened as in the reference.
        # Lucide construction reference: umbrella; original and atomic-debug inspected where named.
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
            path(name, (cx,cy-r), [('A',(cx,cy+r),r,r,True),('A',(cx,cy-r),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('canopy',(16,12),[('A',(40,12),12,8,True)])
        line('rigging-left',(16,12),(18,16));join('rigging-left','canopy')
        line('rigging-right',(40,12),(38,16));join('rigging-right','canopy')
        circle('head',28,25,3)
        poly('body',(28,36),(28,40),(32,44))
        line('arm',(28,36),(36,36));join('arm','body')
        line('tow',(20,36),(28,36));join('tow','body')
        path('boat',(8,36),[('L',(20,36)),('L',(20,40)),('A',(16,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,36))],True);join('boat','tow')
