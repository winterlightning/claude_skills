"""trousers jeans.
Plan: Restored straight long trouser legs, a higher crotch, front pocket curves and a short central fly.
Construction: shirt: coherent garment outline and connected seams; trouser proportions follow the reference.
Keyshape: VRECT_L; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '1e2712a5-c98b-5804-829c-d642a1658577'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__jeans-with-front-pockets/20260929T033633Z-thuan-mac/reference/trousers jeans_1e2712a5-c98b-5804-829c-d642a1658577.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'jeans-with-front-pockets'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('trousers', 'jeans')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_polyline('jeans',(12,4),(36,4),(40,44),(28,44),(24,23),(20,44),(8,44),closed=True)
        self.add_bezier('pocket-left',(20,4),((20,10),(17,13),(11,13)))
        self.add_bezier('pocket-right',(28,4),((28,10),(31,13),(37,13)))
        self.add_line('fly',(24,4),(24,13))
        for n in ['pocket-left','pocket-right','fly']:self.relate('connect',n,'jeans')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve front pocket curves and the fly in long straight jeans. Small connected pocket interiors are intentional garment details, visually reviewed in both themes.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'c9e0701f5d69fa0c3a70da3756dfd95c41738631bef3c2592501648d90af8316'}
