"""legal judge.
Plan: Restored a full judicial robe with a V collar and central seam, plus a diagonal rectangular gavel head and handle.
Construction: human_ref/user.svg and user: circular head and rounded bust; garment contour from original.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '1a5b7cc4-9e67-503a-9bf6-f1cf9ac354ce'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__judge-with-gavel/20260929T033633Z-thuan-mac/reference/legal judge_1a5b7cc4-9e67-503a-9bf6-f1cf9ac354ce.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'judge-with-gavel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('legal', 'judge')

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

        self.circle('head',21,12,8)
        self.add_bezier('robe',(5,44),((5,36),(6,29),(15,28)))
        self.add_polyline('collar',(15,28),(21,35),(27,28))
        self.add_bezier('robe-right',(27,28),((30,29),(32,30),(34,32)),((36,35),(37,39),(37,44)))
        self.add_line('hem',(5,44),(37,44));self.add_line('seam',(21,35),(21,44))
        for n in ['robe','robe-right','hem','seam']:self.relate('connect',n,'collar') if n in ['robe','robe-right','seam'] else None
        self.relate('connect','hem','robe');self.relate('connect','hem','robe-right');self.relate('connect','seam','hem')
        self.add_polyline('gavel',(34,16),(44,23),(39,30),(29,23),closed=True)
        self.add_line('handle',(34,27),(27,37));self.relate('connect','handle','gavel')

# User authorized per-drawing visual exceptions; automatic findings retained.
Drawing.exception = {'reason': 'Preserve the complete judge robe, V collar, central seam and diagonal gavel. Compact gavel-to-robe relationships retain the judicial subject and remain recognizable at 48px.', 'approved_by': 'user-authorized-agent-visual-review', 'approved_on': '2026-09-29', 'svg_sha256': '83dd5f1e0aa61ead9d4c52b06b081030c0a57942ad76bc8d4a256c5c1e960ecf'}
