"""Restore a tall arched headphone band with separate vertical earpieces around an unobstructed circular head and broad shoulders.
Symbol plan: Restore a tall arched headphone band with separate vertical earpieces around an unobstructed circular head and broad shoulders.
Construction reference: human_ref/user.svg: circular face and smooth shoulders; Lucide headphones: overhead arch and two descending earpieces.
Omissions: Facial microdetails and headset cable omitted.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='a43a1b34-ba30-51e2-8567-7e92fc1abc1c'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__support-agent-with-headphones/20260929T142009Z-thuan-mac/reference/headphones customer support human_a43a1b34-ba30-51e2-8567-7e92fc1abc1c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='support-agent-with-headphones'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='avatars'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,k=3):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        ids=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]
            if a==z:continue
            q=n+str(i);ids.append(q)
            if i%2:self.add_arc(q,a,z,radius_x=k)
            else:self.add_line(q,a,z)
        self.add_contour(n,*ids,closed=True)

    def build(self):
        self.add_arc('headband',(8,24),(40,24),radius_x=16,radius_y=20)
        self.add_line('ear-left',(8,24),(8,30));self.add_line('ear-right',(40,24),(40,30))
        self.relate('connect','headband','ear-left');self.relate('connect','headband','ear-right')
        self.circle('head',24,24,7)
        self.add_arc('shoulder-l',(8,44),(24,35),radius_x=16,radius_y=9)
        self.add_arc('shoulder-r',(24,35),(40,44),radius_x=16,radius_y=9)
        self.add_contour('shoulders','shoulder-l','shoulder-r');self.relate('connect','head','shoulders')
