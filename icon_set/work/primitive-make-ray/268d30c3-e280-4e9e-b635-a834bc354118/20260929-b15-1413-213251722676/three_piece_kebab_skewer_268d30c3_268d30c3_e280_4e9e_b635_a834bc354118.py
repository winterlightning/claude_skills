"""Restore three identical diagonally rotated food pieces, regular spacing, connecting shaft segments and exposed ends.
Symbol plan: Restore three identical diagonally rotated food pieces, regular spacing, connecting shaft segments and exposed ends.
Construction reference: Lucide candy: softened food contours arranged around one axis.
Omissions: None
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='268d30c3-e280-4e9e-b635-a834bc354118'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__three-piece-kebab-skewer-268d30c3/20260929T142009Z-thuan-mac/reference/kebab_268d30c3-e280-4e9e-b635-a834bc354118.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-piece-kebab-skewer-268d30c3'
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
        # Three rounded diamonds on one shared rising axis, each 13 units apart.
        for i,cx in enumerate((11,24,37)):
            cy=48-cx
            pts=[(-1,-5),(1,-5),(3,-3),(5,-1),(5,1),(1,5),(-1,5),(-3,3),(-5,1),(-5,-1)]
            self.add_polyline('food'+str(i),*[(cx+x,cy+y) for x,y in pts],closed=True)
        for i,(a,b) in enumerate([((6,42),(8,40)),((14,34),(21,27)),((27,21),(34,14)),((40,8),(42,6))]):
            self.add_line('shaft'+str(i),a,b)
            for j in range(3):
                if j==i or j==i-1:self.relate('connect','shaft'+str(i),'food'+str(j))
