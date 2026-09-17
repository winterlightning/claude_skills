"""person-pointing-at-map-board: Person points at an easel map board with one clear bent route. Head center (8,19), radius 3; shoulder y30 gives exact 4-unit ink clearance. Tiny X omitted and the tight S simplified to one bend."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '49b5e4e8-1776-4137-8537-56f05c3dec41'
SOURCE_PATH = 'pictographic-primitives/outdoors/trekking map_49b5e4e8-1776-4137-8537-56f05c3dec41.svg'
AUTHOR = 'gpt-6'

class PersonPointingAtMapBoard(Solo48):
    icon_id = 'person-pointing-at-map-board'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('map', 'trekking', 'route', 'board', 'briefing', 'person', 'guide', 'planning', 'outdoors-batch-03')

    def build(self):
        # Plan: Person points at an easel map board with one clear bent route. Head center (8,19), radius 3; shoulder y30 gives exact 4-unit ink clearance. Tiny X omitted and the tight S simplified to one bend.
        # Lucide construction reference: presentation; original and atomic-debug inspected where named.
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
        circle('head',8,19,3)
        poly('body',(4,40),(4,34),(8,30),(12,30),(12,40))
        line('pointing-arm',(12,30),(20,24));join('pointing-arm','body')
        poly('board',(20,8),(44,8),(44,34),(32,34),(20,34),(20,24),closed=True);join('board','pointing-arm')
        line('stand',(32,34),(32,40));join('stand','board')
        poly('route',(29,25),(29,17),(35,17))
