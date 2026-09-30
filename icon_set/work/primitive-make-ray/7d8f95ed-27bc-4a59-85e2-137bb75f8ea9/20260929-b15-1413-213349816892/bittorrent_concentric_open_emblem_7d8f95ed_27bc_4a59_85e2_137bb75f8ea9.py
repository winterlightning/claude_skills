"""Restore the continuous enclosing sweep, horizontal lower-right tails and a large open inner C.
Symbol plan: Restore the continuous enclosing sweep, horizontal lower-right tails and a large open inner C.
Construction reference: No useful exact local Lucide match; supplied BitTorrent original defines the circular emblem.
Omissions: One intermediate turn omitted to keep the surviving C opening readable at 48px.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='7d8f95ed-27bc-4a59-85e2-137bb75f8ea9'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__bittorrent-concentric-open-emblem/20260929T141805Z-thuan-mac/reference/virtual coin crypto bittorrent_7d8f95ed-27bc-4a59-85e2-137bb75f8ea9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='bittorrent-concentric-open-emblem'
    keyshape=Keyshape.CIRCLE
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
        # A coherent outer sweep returns into the inner C through a horizontal tail.
        self.add_arc('outer-top',(4,24),(44,24),radius_x=20)
        self.add_arc('outer-bottom',(36,40),(4,24),radius_x=20,sweep=True)
        self.add_arc('right-turn',(44,24),(36,32),radius_x=8)
        self.add_line('tail',(36,32),(24,32))
        self.add_arc('inner',(24,32),(24,16),radius_x=8)
        self.add_contour('outer-inner','outer-bottom','outer-top','right-turn','tail','inner')
        self.add_polyline('return',(36,40),(24,40))
        self.relate('connect','outer-inner','return')
