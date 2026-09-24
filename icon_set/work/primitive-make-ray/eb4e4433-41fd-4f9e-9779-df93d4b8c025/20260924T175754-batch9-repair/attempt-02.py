from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='eb4e4433-41fd-4f9e-9779-df93d4b8c025'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/real estate search house 2_eb4e4433-41fd-4f9e-9779-df93d4b8c025.svg'
AUTHOR = 'gpt-6'
PLAN='An extended index finger selects a house above the hand.'
OMISSIONS='Palm creases omitted; house door retained.'
LUCIDE_REFERENCE='hand'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='real-estate-search-house-2'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('real', 'estate', 'search', 'house', '2')

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
        # Upright house and a widened single pointing index finger; folded fingers form one palm curve.
        self.add_polyline('house',(28,10),(34,4),(40,10),(40,16),(28,16),closed=True)
        self.add_bezier('palm-left',(16,44),((16,38),(8,36),(8,28)))
        self.add_polyline('thumb-index',(8,28),(12,32),(12,20))
        self.add_arc('index-tip',(12,20),(20,20),radius_x=4)
        self.add_line('index-right',(20,20),(20,28))
        self.add_bezier('folded-fingers',(20,28),((24,24),(36,26),(36,32)))
        self.add_bezier('palm-right',(36,32),((36,36),(34,40),(34,44)))
        self.relate('connect','palm-left','thumb-index')
        self.relate('connect','thumb-index','index-tip')
        self.relate('connect','index-tip','index-right')
        self.relate('connect','index-right','folded-fingers')
        self.relate('connect','folded-fingers','palm-right')
