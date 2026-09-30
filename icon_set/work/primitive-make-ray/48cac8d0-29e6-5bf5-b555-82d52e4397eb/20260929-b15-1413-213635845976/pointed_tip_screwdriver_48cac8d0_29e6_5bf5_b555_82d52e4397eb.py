"""Restore a rounded diagonal handle, narrow shaft and pointed tapered blade.
Symbol plan: Restore a rounded diagonal handle, narrow shaft and pointed tapered blade.
Construction reference: No useful exact local Lucide screwdriver match; source establishes the tool, with smooth handle curves following Lucide construction.
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
        self.add_bezier('handle-left',(6,36),((6,34),(7,32),(9,30)))
        self.add_line('handle-upper-left',(9,30),(17,22))
        self.add_bezier('handle-crown',(17,22),((19,20),(21,20),(23,22)))
        self.add_polyline('handle-upper-right',(23,22),(25,24),(26,25))
        self.add_bezier('handle-round-right',(26,25),((28,27),(28,29),(26,31)))
        self.add_line('handle-lower-right',(26,31),(17,40))
        self.add_bezier('handle-bottom',(17,40),((15,42),(13,42),(12,42)),((6,42),(6,40),(6,36)))
        self.add_contour('handle','handle-left','handle-upper-left','handle-crown','handle-upper-right-1','handle-upper-right-2','handle-round-right','handle-lower-right','handle-bottom',closed=True)
        self.add_line('shaft',(25,24),(33,16));self.relate('connect','handle','shaft')
        self.add_polyline('blade',(29,12),(42,6),(36,20),(33,16),closed=True);self.relate('connect','blade','shaft')
