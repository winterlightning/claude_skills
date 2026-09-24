from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='1228a3cf-b0ac-41b8-a4db-2d272fbe1241'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate market house_1228a3cf-b0ac-41b8-a4db-2d272fbe1241.svg'
AUTHOR = "gpt-6"
PLAN='A house sits inside an open circular market ring with a thick upper-right segment.'
OMISSIONS='Door retained; ring segment reduced to a clean double arc.'
LUCIDE_REFERENCE='house'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='real-estate-market-house'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('real', 'estate', 'market', 'house')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=3):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for j,a in enumerate(pts):
            b=pts[(j+1)%8];name=f'{n}-{j}';names.append(name)
            if j%2:self.add_arc(name,a,b,radius_x=r)
            else:self.add_line(name,a,b)
        self.add_contour(n,*names,closed=True)

    def house(self,n,x,y,w,h):
        mid=x+w//2
        self.add_polyline(n,(x,y+8),(mid,y),(x+w,y+8),(x+w,y+h),(x,y+h),closed=True)

    def bust(self,n,x,y,r,shoulder_w,shoulder_h):
        self.circle(n+'-head',x,y,r)
        body_top=y+r+8
        self.add_arc(n+'-shoulders',(x-shoulder_w,body_top+shoulder_h),(x+shoulder_w,body_top+shoulder_h),radius_x=shoulder_w,radius_y=shoulder_h)
        # Exact detached gap: (y+r+8) - (y+r) = 8 centerline / 4 ink.

    def build(self):
        # A house sits inside an open circular market ring with a thick upper-right segment.

        self.add_arc('ring',(24,6),(42,24),radius_x=18,large_arc=True,sweep=False)
        self.add_arc('segment-outer',(24,6),(42,24),radius_x=18)
        self.add_arc('segment-inner',(34,24),(24,14),radius_x=10,sweep=False)
        self.add_line('segment-end',(42,24),(34,24));self.add_line('segment-start',(24,14),(24,6))
        self.add_contour('segment','segment-outer','segment-end','segment-inner','segment-start',closed=True)
        self.house('house',15,20,18,13)
        self.add_polyline('door',(21,33),(21,27),(27,27),(27,33));self.relate('connect','door','house')

