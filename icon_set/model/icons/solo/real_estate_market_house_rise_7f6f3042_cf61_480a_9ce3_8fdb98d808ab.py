from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='7f6f3042-cf61-480a-9ce3-8fdb98d808ab'
SOURCE_PATH='icon_set/work/todo-references/real estate market house rise_7f6f3042-cf61-480a-9ce3-8fdb98d808ab.svg'
AUTHOR='gpt-6'
PLAN='An open-door house with a rising zigzag market arrow at lower right.'
OMISSIONS='Door arch retained; right wall and right jamb shortened to leave room for the rising trend.'
LUCIDE_REFERENCE='house'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='real-estate-market-house-rise'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('real', 'estate', 'market', 'house', 'rise')

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
        # An open-door house with a rising zigzag market arrow at lower right.

        self.add_polyline('roof',(6,20),(20,6),(34,20))
        self.add_polyline('walls',(10,16),(10,32),(18,32),(18,26))
        self.add_arc('door',(18,26),(26,26),radius_x=4)
        self.add_line('jamb',(26,26),(26,28));self.relate('connect','walls','door');self.relate('connect','door','jamb');self.relate('connect','roof','walls')
        self.add_line('right-wall',(30,16),(30,22));self.relate('connect','right-wall','roof')
        self.add_polyline('trend',(18,42),(26,36),(32,42),(42,30))
        self.add_polyline('tip',(34,30),(42,30),(42,38));self.relate('connect','trend','tip')

