"""Walking hiker with rectangular backpack, level arm and short forward cane."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '12ce4cb7-a567-4bba-b7fa-b9991bdfc3b0'
SOURCE_PATH = 'pictographic-primitives/outdoors/trekking stick_12ce4cb7-a567-4bba-b7fa-b9991bdfc3b0.svg'
AUTHOR = 'gpt-6'

class HikerWithWalkingCane(Solo48):
    icon_id = 'hiker-with-walking-cane'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('hiker', 'with', 'walking', 'cane', 'outdoors', 'outdoors-batch-04')

    def build(self):
        # Plan: Walking hiker with rectangular backpack, level arm and short forward cane.
        # Envelope (6,6)-(42,42). Shared endpoints own all attachments.
        # Lucide original/atomic-debug reference: backpack.
        # Human reference: full_body_ref.png; head bottom12, shoulder20, ink gap4.
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

        circle('head',28,9,3)
        poly('body',(28,20),(24,25),(16,35),(26,35),(28,42))
        line('rear-leg',(16,35),(6,42));join('rear-leg','body')
        poly('pack',(24,25),(14,17),(6,27),(16,35));join('pack','body');join('pack','rear-leg')
        line('arm',(28,20),(42,20));join('arm','body')
        line('cane',(42,20),(39,42));join('cane','arm')
