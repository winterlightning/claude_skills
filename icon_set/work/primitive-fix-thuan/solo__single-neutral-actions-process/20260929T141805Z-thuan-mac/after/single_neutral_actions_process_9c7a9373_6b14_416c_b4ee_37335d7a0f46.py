"""Use a broad smooth shoulder arch and coherent straight torso beneath the circular head; keep two checks and one cross.
Symbol plan: Use a broad smooth shoulder arch and coherent straight torso beneath the circular head; keep two checks and one cross.
Construction reference: human_ref/user.svg: circular head and rounded shoulders; 4-unit visible head-body gap. Lucide check supplies unequal check arms.
Omissions: Small sleeve steps simplified into the torso silhouette.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='9c7a9373-6b14-416c-b4ee-37335d7a0f46'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__single-neutral-actions-process/20260929T141805Z-thuan-mac/reference/single neutral actions process_9c7a9373-6b14-416c-b4ee-37335d7a0f46.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='single-neutral-actions-process'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
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
        self.circle('head',15,12,6)
        self.add_arc('shoulders',(6,32),(24,32),radius_x=9,radius_y=6)
        self.add_polyline('torso',(24,32),(24,42),(6,42),(6,32));self.relate('connect','shoulders','torso')
        for i,y in enumerate((7,20)):
            self.add_polyline('check'+str(i),(34,y+3),(37,y+6),(42,y))
        self.add_polyline('cross-a',(34,34),(38,38),(42,42))
        self.add_polyline('cross-b',(34,42),(38,38),(42,34));self.relate('connect','cross-a','cross-b')
