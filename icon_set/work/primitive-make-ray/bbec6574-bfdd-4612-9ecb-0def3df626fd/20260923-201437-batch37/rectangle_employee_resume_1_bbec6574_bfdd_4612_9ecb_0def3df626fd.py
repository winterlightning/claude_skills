from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='bbec6574-bfdd-4612-9ecb-0def3df626fd'
SOURCE_PATH='icon_set/work/todo-references/rectangle employee resume 1_bbec6574-bfdd-4612-9ecb-0def3df626fd.svg'
AUTHOR='gpt-6'
PLAN='An employee résumé with a portrait above two long text rows.'
OMISSIONS='Detached portrait head uses exact 4-unit visible clearance to shoulders.'
LUCIDE_REFERENCE='user'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='rectangle-employee-resume-1'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('rectangle', 'employee', 'resume', '1')

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
        # An employee résumé with a portrait above two long text rows.

        self.add_polyline('frame',(8,4),(40,4),(40,44),(8,44),closed=True)
        self.bust('person',22,13,3,6,2)
        for i,y in enumerate((32,38)):self.add_line('text'+str(i),(16,y),(32,y))

