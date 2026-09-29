"""islamic women hijab.
Plan: Rebuilt the complete hijab bust with broad shoulders and two sweeping wrap folds around a circular face.
Construction: human_ref/user.svg: head proportions and soft shoulder construction; source controls head covering.
Keyshape: VRECT_L; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '2da10a1c-94d1-53ec-a2db-86f6dd5377fd'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__islamic-women-hijab-1-avatar/20260929T033633Z-thuan-mac/reference/islamic women hijab_2da10a1c-94d1-53ec-a2db-86f6dd5377fd.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'islamic-women-hijab-1-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('islamic', 'women', 'hijab')

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

        self.add_arc('hood-top',(12,16),(36,16),radius_x=12)
        self.add_bezier('left',(12,16),((12,24),(13,28),(10,33)),((6,38),(6,40),(6,44)))
        self.add_bezier('right',(36,16),((36,24),(35,28),(38,33)),((42,38),(42,40),(42,44)))
        self.add_contour('outer','left',closed=False)
        self.relate('connect','hood-top','left');self.relate('connect','hood-top','right')
        self.circle('face',24,19,7)
        self.add_bezier('scarf-fold',(10,33),((18,32),(24,43),(37,31)))
        self.add_bezier('lower-fold',(24,43),((29,41),(36,38),(40,36)))

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve the enclosed face, hood, broad shoulders and two wrapped scarf folds. Close enclosure spacing is intentional and reviewed at native size.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': 'e9ec079c790b510df49096a5c51b4741248bf4ec48bc1bfce48b639999d4b7e2'}
