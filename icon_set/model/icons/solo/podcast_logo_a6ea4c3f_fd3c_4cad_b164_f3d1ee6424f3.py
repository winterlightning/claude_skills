"""One broad broadcast arch around a detached circular head and narrow capsule body. Omit the second arch. Human reference user.svg informs head/body construction; head bottom 19 and body top 27 give exactly four ink units of separation."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6ea4c3f-fd3c-4cad-b164-f3d1ee6424f3'
SOURCE_PATH = 'pictographic-primitives/logos/podcast logo_a6ea4c3f-fd3c-4cad-b164-f3d1ee6424f3.svg'
AUTHOR = 'gpt-6'

class PodcastLogo(Solo48):
    icon_id = 'podcast-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('podcast', 'apple-podcasts', 'broadcast', 'microphone', 'logo', 'brand', 'audio')

    def build(self):
        # Plan: One broad broadcast arch around a detached circular head and narrow capsule body. Omit the second arch. Human reference user.svg informs head/body construction; head bottom 19 and body top 27 give exactly four ink units of separation.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_line('left',(8,30),(8,20))
        self.add_arc('arch',(8,20),(40,20),radius_x=16)
        self.add_line('right',(40,20),(40,30))
        self.add_contour('broadcast','left','arch','right')
        circle('head',24,16,3)
        self.add_arc('shoulders',(20,31),(28,31),radius_x=4)
        self.add_line('body-right',(28,31),(28,40))
        self.add_arc('body-bottom',(28,40),(20,40),radius_x=4)
        self.add_line('body-left',(20,40),(20,31))
        self.add_contour('body','shoulders','body-right','body-bottom','body-left',closed=True)

