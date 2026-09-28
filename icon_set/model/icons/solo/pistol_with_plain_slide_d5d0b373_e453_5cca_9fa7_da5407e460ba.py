"""Modern Handgun Pistol.

Symbol plan: Plain slide with rounded muzzle, slanted grip and broad guard. Visible (2,6)-(46,42). Omit small sight and inner trigger.
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5d0b373-e453-5cca-9fa7-da5407e460ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/modern weapon gun_d5d0b373-e453-5cca-9fa7-da5407e460ba.svg'
AUTHOR = 'gpt-6'


class PistolWithPlainSlide(Solo48):
    icon_id = 'pistol-with-plain-slide'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('pistol', 'with', 'plain', 'slide')

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

        path('pistol',(4,8),[(40,8),((44,12),4,4,True),(44,20),((40,24),4,4,True),(36,24),(24,24),(22,32),(20,40),(8,40),(12,24),(4,24),(4,8)],True)
        path('guard',(36,24),[((28,32),8,8,True),(22,32)])
        self.relate('connect','pistol','guard')
