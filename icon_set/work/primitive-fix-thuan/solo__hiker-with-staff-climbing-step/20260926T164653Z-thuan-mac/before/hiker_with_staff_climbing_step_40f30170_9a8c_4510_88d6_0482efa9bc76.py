"""Backpacked hiker lifting a knee onto a short ledge with a tall upright staff."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '40f30170-9a8c-4510-88d6-0482efa9bc76'
SOURCE_PATH = 'pictographic-primitives/outdoors/trekking top_40f30170-9a8c-4510-88d6-0482efa9bc76.svg'
AUTHOR = 'gpt-6'

class HikerWithStaffClimbingStep(Solo48):
    icon_id = 'hiker-with-staff-climbing-step'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('hiker', 'with', 'staff', 'climbing', 'step', 'outdoors', 'outdoors-batch-04')

    def build(self):
        # Plan: Backpacked hiker lifting a knee onto a short ledge with a tall upright staff.
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
        poly('body',(28,20),(24,24),(16,32),(6,42))
        poly('pack',(24,24),(14,16),(6,26),(16,32));join('pack','body')
        poly('front-leg',(16,32),(28,32),(28,36));join('front-leg','body')
        line('arm',(28,20),(42,20));join('arm','body')
        poly('staff',(42,10),(42,20),(42,42));join('staff','arm')
        poly('step',(24,40),(28,36),(33,36));join('step','front-leg')
