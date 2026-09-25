"""Law Enforcement Nightstick.

Symbol plan: One diagonal rounded baton and a perpendicular side handle. Visible (6,2)-(42,46). Deliberately diagonal; no grip texture.
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e56d856b-d6f4-5ba1-af0b-3ed9dcdf53ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/police nightstick_e56d856b-d6f4-5ba1-af0b-3ed9dcdf53ff.svg'
AUTHOR = 'gpt-6'


class DiagonalSideHandleNightstick(Solo48):
    icon_id = 'diagonal-side-handle-nightstick'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('diagonal', 'side', 'handle', 'nightstick')

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

        self.add_bezier('cap-top',(30,6),((30,5),(31,4),(32,4)),((38,4),(40,6),(40,10)),((40,12),(39,13),(38,14)))
        self.add_line('shaft-right',(38,14),(20,42))
        self.add_bezier('cap-bottom',(20,42),((19,44),(16,44),(14,44)),((10,44),(10,40),(12,36)))
        self.add_line('shaft-left-0',(12,36),(18,26))
        self.add_line('shaft-left-1',(18,26),(30,6))
        self.add_contour('shaft','cap-top','shaft-right','cap-bottom','shaft-left-0','shaft-left-1',closed=True)
        self.add_line('side-handle',(8,20),(18,26))
        self.relate('connect','side-handle','shaft')
