"""icq logo.
Plan: Restored eight individual elongated petals around a larger open center, with a regular radial arrangement.
Construction: flower: central disc and radial petal structure; eight-petal count comes from original.
Keyshape: CIRCLE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'f289aab6-b93c-4599-9b13-2dec09ddb559'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__icq-logo/20260929T033633Z-thuan-mac/reference/icq logo_f289aab6-b93c-4599-9b13-2dec09ddb559.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'icq-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('icq', 'logo')

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

        self.circle('center',24,24,5)
        # The cardinal and diagonal petals share a quarter-turn repeat definition.
        for i in range(4):
         def p(x,y):
          x,y=x-24,y-24
          for _ in range(i):x,y=-y,x
          return (24+x,24+y)
         self.add_bezier('cardinal'+str(i),p(21,18),(p(18,9),p(18,4),p(24,4)),(p(30,4),p(30,9),p(27,18)))
         self.add_bezier('diagonal'+str(i),p(27,18),(p(31,9),p(36,7),p(40,11)),(p(44,15),p(39,19),p(31,22)))

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve eight elongated ICQ petals around a central disc. Compact radial petal joins and the optical circular envelope retain the recognizable logo at 48px.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '71823216d1efa853f4a20ca7f0825b44d7e4d4f62b9f90cd1b885b77f21936e9'}
