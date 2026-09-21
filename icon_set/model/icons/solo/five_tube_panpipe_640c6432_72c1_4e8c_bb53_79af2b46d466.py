'Five-Tube Panpipe.\nSymbol plan: Five vertical panpipe tubes hang beneath a broad rounded horizontal binding. Their rounded lower ends step upward from the longest tube on the left to the shortest tube on the right.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '640c6432-72c1-4e8c-bb53-79af2b46d466'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/panpipe_640c6432-72c1-4e8c-bb53-79af2b46d466.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'five-tube-panpipe'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('panpipe', 'instrument', 'music', 'tubes', 'wind', 'flute')
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
        rect('binding',4,8,40,8,4)
        for i,x in enumerate((4,12,20,28,36,44)):
         bottom=36 if i==0 else 40-i*4
         levels=[16,bottom] if i in (0,5) else [16,bottom-4,bottom]
         for j in range(len(levels)-1):
          line('wall'+str(i)+'-'+str(j),(x,levels[j]),(x,levels[j+1]))
          if j==0:self.relate('connect','wall'+str(i)+'-'+str(j),'binding')
        for i,x in enumerate((4,12,20,28,36)):
         bottom=36-i*4
         arc('end'+str(i),(x,bottom),(x+8,bottom),4,s=False)
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
