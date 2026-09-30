"""Restore a capsule-like diagonal handle and a slim pointed tapered blade joined by a narrow straight shaft.
Symbol plan: Restore a capsule-like diagonal handle and a slim pointed tapered blade joined by a narrow straight shaft.
Construction reference: No useful exact Lucide screwdriver match; source establishes the tool; rounded caps and tangent handle curves follow Lucide construction.
Omissions: None
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='48cac8d0-29e6-5bf5-b555-82d52e4397eb'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__pointed-tip-screwdriver/20260929T142009Z-thuan-mac/reference/tools screwdriver_48cac8d0-29e6-5bf5-b555-82d52e4397eb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='pointed-tip-screwdriver'
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
        # Diagonal rounded handle, shaft and tapered screwdriver blade share one axis.
        self.add_line('handle-a',(8,42),(6,40))
        self.add_arc('handle-round',(6,40),(6,34),radius_x=6,sweep=True)
        self.add_line('handle-b',(6,34),(16,24))
        self.add_arc('handle-top',(16,24),(22,24),radius_x=6)
        self.add_line('handle-c',(22,24),(24,26))
        self.add_arc('handle-right',(24,26),(24,32),radius_x=6)
        self.add_line('handle-d',(24,32),(14,42))
        self.add_arc('handle-bottom',(14,42),(8,42),radius_x=6)
        self.add_contour('handle','handle-a','handle-round','handle-b','handle-top','handle-c','handle-right','handle-d','handle-bottom',closed=True)
        self.add_line('shaft',(23,25),(32,16));self.relate('connect','handle','shaft')
        self.add_polyline('blade',(28,12),(42,6),(36,20),(32,16),closed=True)
        self.relate('connect','blade','shaft')
