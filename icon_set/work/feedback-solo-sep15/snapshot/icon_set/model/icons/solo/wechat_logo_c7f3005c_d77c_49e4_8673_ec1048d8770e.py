"""Two similarly sized overlapping speech bubbles with opposite tails. Preserve the shared occlusion junctions and the unmarked interiors of this source."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7f3005c-d77c-49e4-8673-ec1048d8770e'
SOURCE_PATH = 'pictographic-primitives/logos/wechat logo_c7f3005c-d77c-49e4-8673-ec1048d8770e.svg'
AUTHOR = 'gpt-6'

class WechatLogo(Solo48):
    icon_id = 'wechat-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('wechat', 'chat', 'messenger', 'speech-bubbles', 'logo', 'brand', 'chinese')

    def build(self):
        # Plan: Two similarly sized overlapping speech bubbles with opposite tails. Preserve the shared occlusion junctions and the unmarked interiors of this source.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_bezier('rear',(32,18),((32,10),(26,6),(18,6)),((10,6),(6,12),(6,18)),((6,23),(8,26),(10,28)))
        self.add_polyline('rear-tail',(10,28),(8,34),(16,30),(18,30));self.relate('connect','rear','rear-tail')
        self.add_bezier('front-right',(32,18),((39,18),(42,22),(42,28)),((42,32),(40,34),(38,36)))
        self.add_polyline('front-tail',(38,36),(42,42),(34,39))
        self.add_bezier('front-left',(34,39),((26,42),(18,36),(18,30)),((18,23),(24,18),(32,18)))
        for a,b in [('front-right','front-tail'),('front-tail','front-left'),('front-left','front-right'),('rear','front-right'),('rear','front-left'),('rear-tail','front-left')]:self.relate('connect',a,b)

