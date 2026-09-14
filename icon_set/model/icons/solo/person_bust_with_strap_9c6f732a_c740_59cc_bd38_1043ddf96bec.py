"""A head above rounded shoulders and a short diagonal strap rising from the base. Lucide users informs the shoulders. The strap stays short, preserving the distinction from the full sash."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c6f732a-c740-59cc-bd38-1043ddf96bec'
SOURCE_PATH = 'pictographic-primitives/users/neutral actions_9c6f732a-c740-59cc-bd38-1043ddf96bec.svg'
AUTHOR = 'gpt-6'


class PersonBustWithStrap(Solo48):
    icon_id = 'person-bust-with-strap'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/groups"
    aliases = ()
    keywords = ('person', 'bust', 'user', 'strap', 'avatar', 'profile', 'account', 'neutral')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-a',top,bottom,radius_x=radius)
        self.add_arc(name+'-b',bottom,top,radius_x=radius)
        self.add_contour(name,name+'-a',name+'-b',closed=True)


    def build(self) -> None:
        # Portrait centerline extremes (8,6)-(40,42).
        self.circle('head',24,12,8)
        self.add_arc('shoulder-left',(8,37),(16,29),radius_x=8)
        self.add_line('shoulders',(16,29),(32,29))
        self.add_arc('shoulder-right',(32,29),(40,37),radius_x=8)
        self.add_line('side-right',(40,37),(40,42))
        self.add_line('base-right',(40,42),(28,42))
        self.add_line('base-left',(28,42),(8,42))
        self.add_line('side-left',(8,42),(8,37))
        self.add_contour('body','shoulder-left','shoulders','shoulder-right','side-right','base-right','base-left','side-left',closed=True)
        self.add_line('strap',(28,42),(34,37))
        self.relate('connect','body','strap')
