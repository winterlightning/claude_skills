"""Notched eye silhouette and small pupil, with one upper-right signal arc. Preserve the diagonal rising forehead; omit the crowded second signal arc."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edb96e95-95f4-402c-a201-5a151babd338'
SOURCE_PATH = 'pictographic-primitives/logos/sina weibo logo_edb96e95-95f4-402c-a201-5a151babd338.svg'
AUTHOR = 'gpt-6'

class SinaWeiboLogo(Solo48):
    icon_id = 'sina-weibo-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('sina-weibo', 'weibo', 'social', 'chinese', 'logo', 'brand', 'microblog')

    def build(self):
        # Plan: Notched eye silhouette and small pupil, with one upper-right signal arc. Preserve the diagonal rising forehead; omit the crowded second signal arc.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.
        def circle(name,cx,cy,r):
            self.add_arc(name+'-upper',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-lower',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-upper',name+'-lower',closed=True)

        self.add_bezier('eye',(6,30),((6,23),(12,16),(20,13)),((24,11),(24,16),(24,18)),((34,14),(34,18),(34,22)),((35,26),(35,30),(34,34)),((30,40),(24,42),(20,42)),((12,42),(6,38),(6,30)))
        self.add_contour('eye-outline','eye',closed=True)
        circle('pupil',20,30,3)
        self.add_arc('signal',(28,6),(42,20),radius_x=14)

