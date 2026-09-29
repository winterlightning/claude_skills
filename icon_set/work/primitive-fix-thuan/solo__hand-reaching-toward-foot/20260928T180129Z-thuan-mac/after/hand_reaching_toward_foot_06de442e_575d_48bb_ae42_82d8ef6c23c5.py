"""guru purnima hand.
Plan: Restored the ankle, heel, instep and toes below a coherent extended finger and thumb.
Construction: hand-helping: finger and palm silhouette; no useful foot match.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '06de442e-575d-48bb-ae42-82d8ef6c23c5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-reaching-toward-foot/20260928T180129Z-thuan-mac/reference/guru purnima hand_06de442e-575d-48bb-ae42-82d8ef6c23c5.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hand-reaching-toward-foot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('guru', 'purnima', 'hand')

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

        self.add_polyline('ankle',(6,29),(6,39))
        self.add_bezier('foot',(6,39),((6,42),(8,42),(12,42)),((19,42),(27,42),(33,42)),((38,42),(38,38),(33,36)),((24,32),(18,31),(18,27)))
        self.add_polyline('ankle-top',(18,27),(18,23),(6,23),(6,29));self.relate('connect','ankle','foot');self.relate('connect','foot','ankle-top');self.relate('connect','ankle','ankle-top')
        self.add_bezier('hand',(42,6),((34,6),(29,5),(27,7)),((23,10),(19,13),(17,15)),((14,16),(14,20),(18,18)),((22,16),(26,14),(29,13)))
        self.add_bezier('thumb',(25,15),((27,20),(34,20),(42,13)))

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve an extended hand above an anatomically recognizable ankle, heel and forefoot. Compact finger spacing and the natural silhouette are intentional.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '230d999cd65fcd91e0935f29b3793ac122511053d9426bdf2957f3e579916da4'}
