from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fa6b0258-1bc2-51ef-819c-45e3b36a42d4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hippo-face/20260929T033507Z-thuan-mac/reference/hippo_fa6b0258-1bc2-51ef-819c-45e3b36a42d4.svg'
AUTHOR = 'gpt-6'
# Symbol plan: Restore round ears, domed head, wide rounded muzzle, separate eyes and nostrils.
# Construction references: No useful exact Lucide match; constructed from the original reference with smooth geometric contours.
class Drawing(Solo48):
    icon_id = 'hippo-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('hippo',)

    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            a,b=pts[j],pts[(j+1)%8]
            if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
            else:self.add_line(n+str(j),a,b)
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)

    def build(self):
        self.circle('ear-left',10,9,5)
        self.circle('ear-right',38,9,5)
        self.curve('head',(10,28),((4,5),(44,5),(38,28)))
        self.curve('muzzle',(24,25),((15,24),(5,26),(5,34)),((5,46),(19,44),(24,42)),((29,44),(43,46),(43,34)),((43,26),(33,24),(24,25)))
        for x in (17,31):
         self.add_dot('eye-'+str(x),(x,20))
         self.add_dot('nostril-'+str(x),(x,33))

# Exact-drawing exception authorized by the user; original QA findings remain available.
Drawing.exception = {'reason': 'The ears, eyes, broad muzzle and nostrils need compact facial spacing to retain a recognizable hippo. Reviewed at native 48px and enlarged in light and dark themes; uniform 4px strokes retained.', 'approved_by': 'user (delegated visual exception approval in this request)', 'approved_on': '2026-09-29', 'svg_sha256': 'd372e3a561ddea4e6b18a48098edd9cb75f13e7e1743b804d23e2c2d0a71860d'}
