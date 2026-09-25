'man graduate. Cap now sits on its band and open face instead of floating above a circular head. Left tassel restored. Radius-8 circular jaw ends at y32; symmetric shoulders peak y36, giving the avatar-required zero ink gap. Detailed gown V and tassel droplet omitted because they crowd the 48px geometry. Construction reference: local Lucide graduation-cap + human_ref/user.svg.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7764a030-9bc6-4b16-aa7c-7ad4e9ca54bc'
SOURCE_PATH = 'pictographic-primitives/avatars/man graduate_7764a030-9bc6-4b16-aa7c-7ad4e9ca54bc.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/man_graduate_avatar.py'
class Drawing(Solo48):
    icon_id = 'man-graduate-avatar'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man graduate',)

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
        # Shared cap attachment nodes, round jaw, touching avatar shoulders.
        self.add_polyline('board',(8,10),(24,4),(40,10),(32,13),(24,16),(16,13),(8,10))
        self.add_polyline('cap-band',(16,13),(16,24),(24,24),(32,24),(32,13))
        self.relate('connect','board','cap-band')
        self.add_arc('jaw',(32,24),(16,24),radius_x=8)
        self.relate('connect','jaw','cap-band')
        self.add_line('tassel',(8,10),(8,24));self.relate('connect','board','tassel')
        self.path('shoulders',(8,44),[('A',(24,36),16,8,True),('A',(40,44),16,8,True)])
        self.relate('connect','jaw','shoulders')
