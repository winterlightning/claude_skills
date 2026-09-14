"""A round head above rounded shoulders and a diagonal sash. Lucide users informs the shoulders. One sash stroke replaces a filled band."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '44158074-bf2d-513c-9a22-5d1f8f2c94d3'
SOURCE_PATH = 'pictographic-primitives/users/man half_44158074-bf2d-513c-9a22-5d1f8f2c94d3.svg'
AUTHOR = 'gpt-6'


class PersonBustWithSash(Solo48):
    icon_id = 'person-bust-with-sash'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people/identity"
    aliases = ()
    keywords = ('person', 'bust', 'sash', 'user', 'man', 'avatar', 'strap', 'profile')

    def circle(self, name, cx, cy, radius):
        top, bottom = (cx, cy-radius), (cx, cy+radius)
        self.add_arc(name+'-right', top, bottom, radius_x=radius)
        self.add_arc(name+'-left', bottom, top, radius_x=radius)
        self.add_contour(name, name+'-right', name+'-left', closed=True)

    def build(self) -> None:
        # Portrait extremes (8,6)-(40,42); torso mirrors, sash is diagonal.
        self.circle('head',24,12,8)
        self.add_arc('shoulder-left',(8,37),(16,29),radius_x=8)
        self.add_line('shoulders',(16,29),(32,29))
        self.add_arc('shoulder-right',(32,29),(40,37),radius_x=8)
        self.add_line('body-base-1',(40,37),(40,42))
        self.add_line('body-base-2',(40,42),(20,42))
        self.add_line('body-base-3',(20,42),(8,42))
        self.add_line('body-base-4',(8,42),(8,37))
        self.add_contour('body','shoulder-left','shoulders','shoulder-right','body-base-1','body-base-2','body-base-3','body-base-4',closed=True)
        self.add_line('sash',(32,29),(20,42))
        self.relate('connect','body','sash')
