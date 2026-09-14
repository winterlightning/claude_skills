"""A standing person stands at the right end of a low bed with a raised pillow. Lucide person-standing and bed-single inform limbs and the bed rail; hands and mattress thickness detail are reduced."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '46e8e840-52d0-4c78-aab3-c23fdb5e0ef4'
SOURCE_PATH = 'pictographic-primitives/users/neutral actions share_46e8e840-52d0-4c78-aab3-c23fdb5e0ef4.svg'
AUTHOR = 'gpt-6'


class PersonBesideBed(Solo48):
    icon_id = 'person-beside-bed'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ()
    keywords = ('person', 'bed', 'hotel', 'room', 'sleep', 'share', 'accommodation', 'rest')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)


    def build(self) -> None:
        # Square centerline extremes (6,6)-(42,42); bed left, standing figure right.
        self.circle('head',36,12,6)
        self.add_polyline('torso',(36,27),(36,34))
        self.add_polyline('arms',(24,34),(36,27),(42,34))
        self.add_polyline('legs',(32,42),(36,34),(40,42))
        self.relate('connect','torso','arms')
        self.relate('connect','torso','legs')
        self.add_polyline('bed-post',(6,26),(6,30),(6,42))
        self.add_polyline('mattress',(6,30),(14,30),(18,34),(24,34),(24,42),(6,42))
        self.relate('connect','bed-post','mattress')
        self.relate('connect','arms','mattress')
