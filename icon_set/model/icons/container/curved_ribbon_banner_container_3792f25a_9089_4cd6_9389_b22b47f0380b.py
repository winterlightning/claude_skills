"""A curved horizontal ribbon banner with folded, pointed tails at both lower sides. Exclude the star; preserve its top-overlap relationship in the later composition.

Plan: A bowed band and mirrored folded tails; band owns paired elliptical arches. Bounds (2,10)-(62,54).
Hosting at the standard slot: add-sub32: valid, heart-state-63: review, check-mark: valid.
Construction reference: No close Lucide subject; use simple connected contours."""
from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = '3792f25a-9089-4cd6-9389-b22b47f0380b'
SOURCE_PATH = 'pictographic-primitives/rewards/ranking ribbon_3792f25a-9089-4cd6-9389-b22b47f0380b.svg'
SOURCE_ICON_IDS = ('3792f25a-9089-4cd6-9389-b22b47f0380b',)
AUTHOR = 'gpt-6'

class CurvedRibbonBannerContainer(Container64):
    icon_id = 'curved-ribbon-banner-container'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'rewards'
    aliases = ()
    keywords = ('curved', 'ribbon', 'banner', 'container')

    def build(self) -> None:
        self.add_arc('band-top',(10,20),(54,20),radius_x=22,radius_y=10)
        self.add_line('band-right',(54,20),(54,40))
        self.add_bezier('band-bottom',(54,40),((51,36),(47,33),(44,32)),((40,30),(36,30),(32,30)),((28,30),(24,30),(20,32)),((17,33),(13,36),(10,40)))
        self.add_line('band-left',(10,40),(10,20))
        self.add_contour('band','band-top','band-right','band-bottom','band-left',closed=True)
        for sign,name in ((1,'left'),(-1,'right')):
            def pt(x,y): return (32+sign*(x-32),y)
            self.add_polyline(name,*[pt(x,y) for x,y in ((10,40),(2,44),(8,46),(6,54),(20,46),(20,32))])
            self.relate('connect',name,'band')
