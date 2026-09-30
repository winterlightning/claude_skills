"""Separate the softly domed hat and broad brim from two complete round lenses and a circular jaw; keep smooth uniform shoulders.
Symbol plan: Separate the softly domed hat and broad brim from two complete round lenses and a circular jaw; keep smooth uniform shoulders.
Construction reference: human_ref/user.svg: circular jaw and smooth shoulders. Lucide hat-glasses: distinct hat, brim and paired round lenses.
Omissions: Small pocket and sleeve details omitted; hair implied by the framing hat and jaw.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='6b34cbad-4ecd-49c6-8fa7-dde6ddbf9011'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__policewoman-with-round-glasses/20260929T142009Z-thuan-mac/reference/police woman_6b34cbad-4ecd-49c6-8fa7-dde6ddbf9011.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='policewoman-with-round-glasses'
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
        self.add_arc('hat-top',(14,10),(34,10),radius_x=10,radius_y=6)
        self.add_line('hat-left',(14,10),(12,14));self.add_line('hat-right',(34,10),(36,14))
        self.add_polyline('brim',(8,14),(12,14),(36,14),(40,14))
        self.relate('connect','hat-top','hat-left');self.relate('connect','hat-top','hat-right')
        self.relate('connect','brim','hat-left');self.relate('connect','brim','hat-right')
        self.circle('glasses-left',16,25,3);self.circle('glasses-right',32,25,3)
        self.add_line('bridge',(19,25),(29,25))
        for n in ('glasses-left','glasses-right'):self.relate('connect',n,'bridge')
        self.add_arc('jaw',(35,25),(13,25),radius_x=11)
        for n in ('glasses-left','glasses-right'):self.relate('connect',n,'jaw')
        self.add_arc('shoulder-l',(8,44),(24,40),radius_x=16,radius_y=4)
        self.add_arc('shoulder-r',(24,40),(40,44),radius_x=16,radius_y=4)
        self.add_contour('shoulders','shoulder-l','shoulder-r');self.relate('connect','jaw','shoulders')
