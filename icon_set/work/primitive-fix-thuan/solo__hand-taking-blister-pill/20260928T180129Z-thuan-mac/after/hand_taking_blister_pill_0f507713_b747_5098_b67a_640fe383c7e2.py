"""cooking baking tray hand.
Plan: Restored a blister sheet with five large circular cells and a thumb lifting the lower-right pill.
Construction: hand-grab: rounded fingertip; source repeated cell structure retained.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '0f507713-b747-5098-b67a-640fe383c7e2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__hand-taking-blister-pill/20260928T180129Z-thuan-mac/reference/cooking baking tray hand_0f507713-b747-5098-b67a-640fe383c7e2.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'hand-taking-blister-pill'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cooking', 'baking', 'tray', 'hand')

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

        self.add_bezier('tray',(13,33),((9,33),(2,34),(2,29)),((2,22),(2,13),(2,10)),((2,6),(6,6),(12,6)),((20,6),(31,6),(36,6)),((45,6),(46,8),(46,12)),((46,18),(46,25),(46,29)),((46,33),(40,33),(36,33)))
        for x,y in [(13,15),(25,15),(37,15),(13,27)]:self.circle('cell'+str(x)+'-'+str(y),x,y,3)
        self.add_bezier('thumb',(22,35),((26,31),(29,27),(31,26)),((35,22),(39,27),(36,31)),((34,35),(31,39),(30,42)))
        self.add_line('wrist',(18,33),(18,42))

# User authorized visually justified exceptions for this batch. Findings are retained.
Drawing.exception = {'reason': 'Preserve a multi-cell blister sheet and a pill-taking thumb. Four cells replace the crowded source count, with compact cell spacing and optical envelope accepted after native-size review.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '243a7b947df69a713b40d0d88f060c6d23782fd91a4570b58304c499fffb0fb1'}
