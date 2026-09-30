"""Draw a longer curved body, forked tail, small fin strokes and a short curved gill.
Symbol plan: Draw a longer curved body, forked tail, small fin strokes and a short curved gill.
Construction reference: Lucide fish: paired body curves, forked tail and gill; supplied original establishes the minnow proportions.
Omissions: Tiny enclosed fin shapes simplified to short strokes.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='f6111608-d0fc-4660-be8f-16a26d108353'
SOURCE_PATH='/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__swimming-minnow/20260929T142009Z-thuan-mac/reference/minnow_f6111608-d0fc-4660-be8f-16a26d108353.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='swimming-minnow'
    keyshape=Keyshape.HRECT_M
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
        self.add_bezier('body-top',(14,20),((18,17),(22,15),(26,15)),((33,15),(40,17),(44,24)))
        self.add_bezier('body-bottom',(44,24),((40,31),(33,33),(26,33)),((22,33),(18,31),(14,28)))
        for i,(a,b) in enumerate(zip([(14,28),(4,38),(8,24),(4,10)],[(4,38),(8,24),(4,10),(14,20)])):self.add_line('tail'+str(i),a,b)
        self.add_contour('fish','body-top','body-bottom','tail0','tail1','tail2','tail3',closed=True)
        self.add_line('dorsal',(26,15),(26,10));self.relate('connect','fish','dorsal')
        self.add_line('ventral',(26,33),(24,38));self.relate('connect','fish','ventral')
        self.add_arc('gill',(34,20),(34,28),radius_x=8,sweep=False)
