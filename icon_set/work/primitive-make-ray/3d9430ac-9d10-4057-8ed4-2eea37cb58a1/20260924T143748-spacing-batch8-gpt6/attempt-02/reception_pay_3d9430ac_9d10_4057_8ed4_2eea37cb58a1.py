from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='3d9430ac-9d10-4057-8ed4-2eea37cb58a1'
SOURCE_PATH='pictographic-primitives/hotels/reception pay_3d9430ac-9d10-4057-8ed4-2eea37cb58a1.svg'
AUTHOR='gpt-6'
PLAN='A receptionist behind a desk receives payment from a standing customer.'
OMISSIONS='Currency mark simplified to a dollar-style S with stem; hands reduced to gestures.'
LUCIDE_REFERENCE='user'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
FULL_BODY_REFERENCE='icon_set/references/human_ref/full_body_ref.png'
class Drawing(Solo48):
    icon_id='reception-pay'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('reception', 'pay')

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
        # Two detached circular heads share the human reference's exact 8u gap.
        # Payment is a circular coin; omit the crowded currency lettering.
        self.circle('clerk-head',12,10,4)
        self.add_line('clerk-torso',(12,22),(12,26))
        self.add_polyline('counter',(6,26),(8,26),(12,26),(18,26))
        self.add_line('desk',(8,26),(8,42))
        self.relate('connect','counter','clerk-torso')
        self.relate('connect','counter','desk')
        self.mark_human_figure('clerk',head='clerk-head',torso='clerk-torso',torso_junction='start')
        self.circle('head',38,10,4)
        self.add_line('torso',(38,22),(38,32))
        self.add_polyline('legs',(32,42),(38,32),(42,42))
        self.add_polyline('arms',(26,26),(38,22),(42,26))
        self.relate('connect','torso','legs')
        self.relate('connect','torso','arms')
        self.mark_human_figure('customer',head='head',torso='torso',torso_junction='start')
        self.circle('payment-coin',21,38,3)
