from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ca0b86cd-f823-4251-8d27-7775eddb1f7a'
SOURCE_PATH='pictographic-primitives/other/lock person_ca0b86cd-f823-4251-8d27-7775eddb1f7a.svg'
AUTHOR='gpt-6'
PLAN='Padlock with circular head above broad shoulders. Shoulders own the inset lower silhouette, removing the narrow enclosed pocket at the old base.'
CONSTRUCTION_REFERENCES='lock: curved shackle; human_ref/user.svg: circular head and broad symmetric shoulders.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='secure-user-account-lock'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('lock', 'person')

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Bottom outline is the shoulder contour; no separate baseline traps a sliver.
        self.path('body',(12,16),[('L',(16,16)),('L',(32,16)),('L',(36,16)),('A',(40,20),4,4,True),('L',(40,44)),('A',(24,40),16,4,False),('A',(8,44),16,4,False),('L',(8,20)),('A',(12,16),4,4,True)],True)
        self.path('shackle',(16,16),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,16))]);self.relate('connect','shackle','body')
        self.circle('head',24,28,4)
        # Human reference: head bottom32; shoulder crest40, exactly4 ink gap.
