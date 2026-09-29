"""carpool.
Plan: Restored two outlined heads and paired shoulder curves behind the windscreen, plus lamps and tires.
Construction: car-front and human_ref/user.svg: rounded body and small repeated busts.
Keyshape: SQUARE; semantic arrangement prioritized within 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '1f4d1069-f84c-4b28-abe2-500ccee986de'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__car-with-two-seated-occupants/20260928T180129Z-thuan-mac/reference/carpool_1f4d1069-f84c-4b28-abe2-500ccee986de.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'car-with-two-seated-occupants'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('carpool',)

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

        self.rect('body',4,30,40,10,3)
        self.add_polyline('roof',(7,30),(10,6),(38,6),(41,30));self.relate('connect','roof','body')
        for x in [17,31]:
         self.circle('head'+str(x),x,15,3)
         self.add_bezier('shoulders'+str(x),(x-5,30),((x-5,26),(x+5,26),(x+5,30)))
         self.add_dot('lamp'+str(x),(x-5 if x==17 else x+5,35))
        for x in [10,38]:
         self.add_line('tire'+str(x),(x,40),(x,43));self.relate('connect','tire'+str(x),'body')
