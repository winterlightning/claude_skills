"""statue-with-flag: Standing figure statue on a tapered pedestal, with an attached flagpole. Head radius 3 at (14,9); body begins y20 for exact 4-unit ink gap. Pole straightened to reserve room for the figure; the pedestal top is open beneath its feet."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7134d6f-1d86-40a4-ba79-82ee018f9bfd'
SOURCE_PATH = 'pictographic-primitives/outdoors/landmarks statue flag_b7134d6f-1d86-40a4-ba79-82ee018f9bfd.svg'
AUTHOR = 'gpt-6'


class StatueWithFlag(Solo48):
    icon_id = 'statue-with-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('statue', 'flag', 'monument', 'landmark', 'pedestal', 'memorial', 'sculpture', 'outdoors-batch-02')

    def build(self):
        # Plan: Standing figure statue on a tapered pedestal, with an attached flagpole. Head radius 3 at (14,9); body begins y20 for exact 4-unit ink gap. Pole straightened to reserve room for the figure; the pedestal top is open beneath its feet.
        # Lucide flag original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (6, 6, 42, 42).
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
        circle('head',14,9,3)
        poly('body',(14,20),(14,26),(10,34))
        line('leg',(14,26),(18,34));join('leg','body')
        poly('arm',(14,20),(20,22),(26,22));join('arm','body')
        poly('pole',(26,34),(26,22),(26,14),(26,6),(42,6),(42,14),(26,14));join('pole','arm')
        poly('pedestal',(10,34),(6,34),(10,42),(26,42),(30,34),(26,34),(18,34))
        join('pedestal','body');join('pedestal','leg');join('pedestal','pole')
