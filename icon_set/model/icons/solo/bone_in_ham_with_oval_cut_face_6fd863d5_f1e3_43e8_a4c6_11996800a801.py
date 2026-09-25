# Final reduction: Ellipse represents the ham cut face; round marrow dot and branched bone with two knuckles replace the cramped taper.
'Bone-In Ham with Oval Cut Face.\nSymbol plan: A ham joint lies horizontally with a broad oval cut face on the left and a narrow bone extending right. A smaller oval appears on the cut surface, and the bone ends in two rounded lobes.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_M: ink extremes (2, 8, 46, 40).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6fd863d5-f1e3-43e8-a4c6-11996800a801'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/sparerib_6fd863d5-f1e3-43e8-a4c6-11996800a801.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'bone-in-ham-with-oval-cut-face'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('ham', 'meat', 'bone', 'food', 'joint', 'cut')
    def build(self):



        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry,sweep=s)
        def bez(n,a,*s): self.add_bezier(n,a,*s)
        def con(n,*p,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members)&set(p)]
            self.add_contour(n,*p,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            ps=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(n+str(j),ps[j],ps[(j+1)%8],r)
                else: line(n+str(j),ps[j],ps[(j+1)%8])
            con(n,*(n+str(j) for j in range(8)),closed=True)
        arc('face-upper-left',(4,24),(14,10),10,14)
        arc('face-upper-right',(14,10),(24,20),10)
        line('face-right',(24,20),(24,28))
        arc('face-lower-right',(24,28),(14,38),10)
        arc('face-lower-left',(14,38),(4,24),10,14)
        con('cut-face','face-upper-left','face-upper-right','face-right','face-lower-right','face-lower-left',closed=True)
        self.add_dot('marrow',(14,24))
        poly('neck-top',(24,20),(34,20),(36,18))
        arc('upper-lobe',(36,18),(44,18),4)
        bez('notch-top',(44,18),((44,21),(40,21),(40,24)))
        bez('notch-bottom',(40,24),((40,27),(44,27),(44,30)))
        arc('lower-lobe',(44,30),(36,30),4)
        poly('neck-bottom',(36,30),(34,28),(24,28))
        con('bone','neck-top-1','neck-top-2','upper-lobe','notch-top','notch-bottom','lower-lobe','neck-bottom-1','neck-bottom-2')
        self.relate('connect','cut-face','bone')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
