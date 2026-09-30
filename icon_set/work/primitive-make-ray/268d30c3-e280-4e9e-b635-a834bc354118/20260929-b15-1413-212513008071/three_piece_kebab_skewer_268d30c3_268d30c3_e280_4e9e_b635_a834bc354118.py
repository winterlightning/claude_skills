"""Restore three identical diagonally arranged pieces and exposed skewer ends.
Symbol plan: Restore three identical diagonally arranged pieces and exposed skewer ends.
Construction reference: Lucide candy: rounded food silhouette around a shared axis.
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
        # Three repeated rounded diamonds share one diagonal axis and equal pitch.
        for i,c in enumerate((12,24,36)):
            pts=[(c-5,c-2),(c-2,c-5),(c+2,c-5),(c+5,c-2),(c+5,c+2),(c+2,c+5),(c-2,c+5),(c-5,c+2)]
            ids=[]
            for j,a in enumerate(pts):
                z=pts[(j+1)%8];n=f'piece{i}-{j}';ids.append(n)
                self.add_line(n,a,z)
            self.add_contour('piece'+str(i),*ids,closed=True)
        self.add_line('skewer-start',(6,42),(7,41))
