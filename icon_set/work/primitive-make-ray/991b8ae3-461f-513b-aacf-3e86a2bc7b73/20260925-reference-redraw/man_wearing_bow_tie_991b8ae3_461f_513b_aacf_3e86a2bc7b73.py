'Restored the closed bottom of the bust and placed the bow at the neckline. Reduced head radius to8 to clear the bow. VRECT_L preserves the portrait envelope. Complete drawing retained, but the two triangular tie counters fail full QA: no exception applied. Construction references: user-round and shared human_ref/user.svg.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='991b8ae3-461f-513b-aacf-3e86a2bc7b73'
SOURCE_PATH='pictographic-primitives/avatars/man_991b8ae3-461f-513b-aacf-3e86a2bc7b73.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/man_wearing_bow_tie_991b8ae3_461f_513b_aacf_3e86a2bc7b73.py'
class Drawing(Solo48):
    icon_id='man-wearing-bow-tie'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='avatars'
    aliases=()
    keywords=('man',)

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
        self.path('body',(14,28),[('A',(8,36),6,8,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,36)),('A',(34,28),6,8,False)])
        self.add_polyline('bow-left',(14,28),(24,32),(14,36),closed=True)
        self.add_polyline('bow-right',(34,28),(34,36),(24,32),closed=True)
        self.relate('connect','bow-left','bow-right');self.relate('connect','body','bow-left');self.relate('connect','body','bow-right')
