"""Lockpicking Tool Set.

Symbol plan: Two rounded grips: upright left tool, diagonal right tool; shared exposed attachment nodes. Visible (4,4)-(44,44). Omit tiny tooth on right.
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81ef6eef-313b-4e94-9969-a0db39ee190f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/tools loackpick_81ef6eef-313b-4e94-9969-a0db39ee190f.svg'
AUTHOR = 'gpt-6'


class LockpickingToolPair(Solo48):
    icon_id = 'lockpicking-tool-pair'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crime"
    aliases = ()
    keywords = ('lockpicking', 'tool', 'pair')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x,y-r), [((x+r,y),r,r,True), ((x,y+r),r,r,True), ((x-r,y),r,r,True), ((x,y-r),r,r,True)], True)

        path('left-grip',(10,26),[((14,30),4,4,True),(14,38),((10,42),4,4,True),((6,38),4,4,True),(6,30),((10,26),4,4,True)],True)
        path('left-shaft',(10,26),[(10,14),(10,6),(18,6)])
        self.add_line('tooth',(10,14),(14,14))
        self.relate('connect','left-shaft','left-grip')
        self.relate('connect','left-shaft','tooth')
        self.add_line('grip-top',(24,34),(32,26))
        self.add_bezier('grip-cap-top',(32,26),((33,25),(34,24),(36,24)),((38,24),(40,26),(40,28)),((40,30),(39,31),(38,32)))
        self.add_line('grip-bottom',(38,32),(30,40))
        self.add_bezier('grip-cap-bottom',(30,40),((29,41),(28,42),(26,42)),((24,42),(22,40),(22,38)),((22,36),(23,35),(24,34)))
        self.add_contour('right-grip','grip-top','grip-cap-top','grip-bottom','grip-cap-bottom',closed=True)
        path('right-shaft',(36,24),[(42,18),(42,10),(38,10)])
        self.relate('connect','right-shaft','right-grip')
