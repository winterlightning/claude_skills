"""snakes.
Plan: Restored four pointed snake heads around a rotationally repeated curved interweave.
Construction: No useful exact snake match; four quarter-turn instances share smooth S-body geometry.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '3746d55b-f09e-427d-9fe4-ccb75164b650'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__intertwined-snakes/20260929T033633Z-thuan-mac/reference/snakes_3746d55b-f09e-427d-9fe4-ccb75164b650.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'intertwined-snakes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('snakes',)

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

        for i in range(4):
         def p(x,y):
          x,y=x-24,y-24
          for _ in range(i):x,y=-y,x
          return (24+x,24+y)
         self.add_bezier('snake-body'+str(i),p(14,12),(p(4,15),p(3,24),p(10,28)),(p(17,32),p(23,26),p(25,22)))
         self.add_bezier('snake-head'+str(i),p(14,12),(p(12,8),p(16,6),p(19,7)),(p(21,7),p(21,5),p(22,4)),(p(24,10),p(19,14),p(14,12)))
         self.relate('connect','snake-body'+str(i),'snake-head'+str(i))
