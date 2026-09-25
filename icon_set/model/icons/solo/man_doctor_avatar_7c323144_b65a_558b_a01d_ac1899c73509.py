'Rebalanced onto VRECT_L (centerline bounds 8,4 to 40,44): taller portrait, circular head and cap band, curved shoulders, chest medical cross and offset coat fastening. Head bottom20 and shoulder top24 give zero visible ink gap. Cross and fastening retain full 4-unit ink clearance. Fine collar detail omitted. Full QA passes without exceptions. References: human_ref/user.svg and Lucide user-round.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7c323144-b65a-558b-a01d-ac1899c73509'
SOURCE_PATH='pictographic-primitives/avatars/man doctor_7c323144-b65a-558b-a01d-ac1899c73509.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/man_doctor_avatar.py'
class Drawing(Solo48):
    icon_id='man-doctor-avatar-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='avatars'
    aliases=()
    keywords=('man doctor',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.circle('head',24,12,8)
        self.add_line('cap-band',(16,12),(32,12));self.relate('connect','head','cap-band')
        self.add_line('body-left-side',(8,44),(8,36))
        self.add_arc('body-left-shoulder',(8,36),(16,24),radius_x=8,radius_y=12)
        self.add_line('body-top',(16,24),(32,24))
        self.add_arc('body-right-shoulder',(32,24),(40,36),radius_x=8,radius_y=12)
        self.add_line('body-right-side',(40,36),(40,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-right-shoulder','body-right-side')
        self.relate('connect','head','body')
        self.add_line('fastening',(29,24),(29,44));self.relate('connect','fastening','body')
        self.add_polyline('cross-h',(17,38),(19,38),(21,38));self.add_polyline('cross-v',(19,36),(19,38),(19,40));self.relate('connect','cross-h','cross-v')
