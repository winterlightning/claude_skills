from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='37ae4172-af70-4ae7-8de2-52970a6302ab'
SOURCE_PATH='icon_set/work/todo-references/recruiting resume document_37ae4172-af70-4ae7-8de2-52970a6302ab.svg'
AUTHOR='gpt-6'
PLAN='An open résumé document is overlaid by a full applicant silhouette on the right.'
OMISSIONS='Document text reduced to two rows and one square photo placeholder.'
LUCIDE_REFERENCE='user'
HUMAN_REFERENCE='icon_set/references/human_ref/user.svg'
FULL_BODY_REFERENCE=None
class Drawing(Solo48):
    icon_id='recruiting-resume-document'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('recruiting', 'resume', 'document')

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
        # An open résumé document is overlaid by a full applicant silhouette on the right.

        self.add_polyline('document',(36,6),(6,6),(6,42),(24,42))
        self.add_polyline('photo',(14,14),(22,14),(22,22),(14,22),closed=True)
        for i,y in enumerate((30,38)):self.add_line('text'+str(i),(14,y),(22,y))
        self.circle('head',34,18,4)
        self.add_arc('shoulders',(26,36),(42,36),radius_x=8,radius_y=6)
        self.add_polyline('body',(42,36),(39,36),(38,42),(30,42),(29,36),(26,36));self.relate('connect','shoulders','body')
        # Head bottom 22; shoulders top 30: exact 4-unit visible gap.

