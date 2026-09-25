'Blank Puppy Head with Round Ears.\nSymbol plan: A puppy head faces forward with a broad rounded forehead and softly curved cheeks. Two large floppy ears project from the upper sides, surrounding a completely blank face without eyes or muzzle marks.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '94b8a5bd-6c2a-457d-bc0a-50eda9816bdc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/puppy_94b8a5bd-6c2a-457d-bc0a-50eda9816bdc.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'blank-puppy-head-round-ears'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('puppy', 'dog', 'head', 'ears', 'pet', 'animal')
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
        bez('forehead',(14,12),((16,8),(20,8),(24,8)),((28,8),(32,8),(34,12)))
        bez('face-right',(34,12),((38,18),(38,24),(38,28)),((38,36),(34,40),(24,40)))
        bez('face-left',(24,40),((14,40),(10,36),(10,28)),((10,24),(10,18),(14,12)))
        con('face','forehead','face-right','face-left',closed=True)
        bez('left-ear',(14,12),((8,10),(4,14),(4,20)),((4,24),(6,28),(10,28)))
        bez('right-ear',(34,12),((40,10),(44,14),(44,20)),((44,24),(42,28),(38,28)))
        self.relate('connect','face','left-ear');self.relate('connect','face','right-ear')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
