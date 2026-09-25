"""Three standing figures share an elliptical platform. Lucide person-standing informs the simple body strokes; doubled arms and trouser outlines are reduced to single strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e151c1ff-63ef-4cc8-afd7-f837ce1dd3a5'
SOURCE_PATH = 'pictographic-primitives/users/multiple circle_e151c1ff-63ef-4cc8-afd7-f837ce1dd3a5.svg'
AUTHOR = 'gpt-6'


class GroupOnPlatform(Solo48):
    icon_id = 'group-on-platform'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "users"
    aliases = ()
    keywords = ('group', 'team', 'people', 'platform', 'community', 'circle', 'crowd', 'users')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)


    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42); platform center (24,37), radii 15/5.
        self.add_arc('platform-left',(24,32),(12,34),radius_x=15,radius_y=5,sweep=False)
        self.add_arc('platform-bottom',(12,34),(36,34),radius_x=15,radius_y=5,large_arc=True,sweep=False)
        self.add_arc('platform-right',(36,34),(24,32),radius_x=15,radius_y=5,sweep=False)
        self.add_contour('platform','platform-left','platform-bottom','platform-right',closed=True)
        for name,cx,head_y,shoulder_y,foot_x,foot_y,arm in [('center',24,9,21,24,32,4),('left',9,12,24,12,34,3),('right',39,12,24,36,34,3)]:
            self.circle(name+'-head',cx,head_y,3)
            self.add_line(name+'-body',(cx,shoulder_y),(foot_x,foot_y))
            self.add_polyline(name+'-arms',(cx-arm,shoulder_y),(cx,shoulder_y),(cx+arm,shoulder_y))
            self.relate('connect',name+'-body',name+'-arms')
            self.relate('connect',name+'-body','platform')
