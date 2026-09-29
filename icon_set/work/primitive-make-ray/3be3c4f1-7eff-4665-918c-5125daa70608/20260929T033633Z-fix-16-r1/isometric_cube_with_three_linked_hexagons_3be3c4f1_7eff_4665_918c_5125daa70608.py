"""scale 3d.
Plan: Restored a symmetric three-face cube with three explicit hexagonal nodes and straight radial connectors.
Construction: network: repeated node ownership; the original isometric cube and hexagons define the geometry.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '3be3c4f1-7eff-4665-918c-5125daa70608'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__isometric-cube-with-three-linked-hexagons/20260929T033633Z-thuan-mac/reference/scale 3d_3be3c4f1-7eff-4665-918c-5125daa70608.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'isometric-cube-with-three-linked-hexagons'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('scale', '3d')

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

        self.add_polyline('cube',(24,18),(33,23),(33,33),(24,38),(15,33),(15,23),closed=True)
        self.add_polyline('seams',(15,23),(24,28),(33,23));self.add_line('vertical',(24,28),(24,38));self.relate('connect','seams','cube');self.relate('connect','vertical','cube');self.relate('connect','vertical','seams')
        for n,x,y in [('top',24,7),('left',7,39),('right',41,39)]:
         self.add_polyline(n,(x,y-5),(x+4,y-3),(x+4,y+3),(x,y+5),(x-4,y+3),(x-4,y-3),closed=True)
        self.add_line('top-link',(24,12),(24,18));self.add_line('left-link',(15,33),(11,36));self.add_line('right-link',(33,33),(37,36))
        for n in ['top','left','right']:
         self.relate('connect',n+'-link',n);self.relate('connect',n+'-link','cube')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve three explicit hexagonal nodes around the three-face cube. The exact natural envelope extends beyond the chosen keyshape but remains inside the 48px canvas.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '305874bd74c21052dd48eecd7245312efbbb93c20839d9837a319d8cf6fc4a95'}
