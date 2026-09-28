"""square megaphone: standalone batch 17 repair.
Retained the diagonal megaphone cone and square enclosure. Replaced the crowded enclosed handle loop with a short open grip and moved the mouth edge inward.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '84596dd2-069a-450e-b70c-08a8dc22159b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__square-megaphone/20260927T140026Z-thuan-mac-1/reference/square megaphone_84596dd2-069a-450e-b70c-08a8dc22159b.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'megaphone'

class Drawing(Solo48):
    icon_id='square-megaphone'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('square', 'megaphone')


    def box(self,name,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,a in enumerate(pts):
            b=pts[(i+1)%8];part=f'{name}-{i}';members.append(part)
            if i%2:self.add_arc(part,a,b,radius_x=r)
            else:self.add_line(part,a,b)
        self.add_contour(name,*members,closed=True)





    def build(self):
        self.box('frame',6,6,36,36,4)
        self.add_polyline('bell',(15,26),(28,14),(34,26),(20,30),closed=True)
        self.add_line('grip',(20,30),(22,34))
        self.relate('connect','bell','grip')

