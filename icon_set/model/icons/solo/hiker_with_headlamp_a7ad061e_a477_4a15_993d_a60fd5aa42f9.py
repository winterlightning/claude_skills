"""hiker-with-headlamp: Bent walking hiker with a backpack and one forward lamp ray. Shared full_body_ref.png construction: head center (28,9), radius 3; shoulder (28,20), exactly 4 units of ink clearance. Small headband omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7ad061e-a477-4a15-993d-a60fd5aa42f9'
SOURCE_PATH = 'pictographic-primitives/outdoors/climbing head light_a7ad061e-a477-4a15-993d-a60fd5aa42f9.svg'
AUTHOR = 'gpt-6'


class HikerWithHeadlamp(Solo48):
    icon_id = 'hiker-with-headlamp'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('headlamp', 'climbing', 'hiker', 'caving', 'night', 'backpack', 'light', 'explorer', 'outdoors-batch-01')

    def build(self):
        # Plan: Bent walking hiker with a backpack and one forward lamp ray. Shared full_body_ref.png construction: head center (28,9), radius 3; shoulder (28,20), exactly 4 units of ink clearance. Small headband omitted.
        # Lucide backpack: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (6, 6, 42, 42).

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
        shoulder=(28,20);hip=(16,35)
        poly('body',shoulder,(24,25),hip,(30,35),(30,42))
        poly('arm',shoulder,(34,26),(42,26));join('body','arm')
        poly('leg',hip,(14,38),(6,42));join('body','leg')
        poly('pack',(24,25),(14,17),(6,27),hip);join('pack','body');join('pack','leg')
        line('beam',(39,9),(42,9))
