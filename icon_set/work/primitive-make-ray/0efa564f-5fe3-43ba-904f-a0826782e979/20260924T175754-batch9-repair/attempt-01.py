from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0efa564f-5fe3-43ba-904f-a0826782e979'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/rectangle code_0efa564f-5fe3-43ba-904f-a0826782e979.svg'
AUTHOR = 'gpt-6'
PLAN='A QR-code card with three square finder marks and a broken lower-right mark.'
OMISSIONS='Small code strokes reduced to a corner and a dash.'
LUCIDE_REFERENCE='scan-qr-code'
HUMAN_REFERENCE=None
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-code'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'code')

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
        # QR marks share a spaced two-by-two layout; one complete finder plus two open marks.
        self.box('frame',6,6,36,36,4)
        self.add_polyline('finder',(15,15),(23,15),(23,23),(15,23),closed=True)
        self.add_line('top-right',(33,15),(33,23))
        self.add_polyline('bottom-left',(15,33),(23,33),(23,34))
        self.add_dot('bottom-right',(33,33))
