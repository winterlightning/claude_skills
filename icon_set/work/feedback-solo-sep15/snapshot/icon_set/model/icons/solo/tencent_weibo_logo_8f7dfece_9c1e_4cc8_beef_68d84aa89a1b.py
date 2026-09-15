"""Open circular sweep around a small ring with a descending curved stem. Use concentric circles and attach the stem at an exact 3-4-5 circle point."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f7dfece-9c1e-4cc8-beef-68d84aa89a1b'
SOURCE_PATH = 'pictographic-primitives/logos/tencent weibo logo_8f7dfece-9c1e-4cc8-beef-68d84aa89a1b.svg'
AUTHOR = 'gpt-6'

class TencentWeiboLogo(Solo48):
    icon_id = 'tencent-weibo-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('tencent-weibo', 'weibo', 'tencent', 'social', 'logo', 'brand', 'chinese')

    def build(self):
        # Plan: Open circular sweep around a small ring with a descending curved stem. Use concentric circles and attach the stem at an exact 3-4-5 circle point.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        nodes=[(8,20),(24,4),(40,20),(24,36)]
        for j in range(3):self.add_arc('outer-'+str(j),nodes[j],nodes[j+1],radius_x=16)
        self.add_contour('outer',*[f'outer-{j}' for j in range(3)])
        self.add_arc('eye-a',(21,24),(27,16),radius_x=5);self.add_arc('eye-b',(27,16),(21,24),radius_x=5);self.add_contour('eye','eye-a','eye-b',closed=True)
        self.add_bezier('stem',(21,24),((13,30),(12,36),(12,44)));self.relate('connect','eye','stem')

