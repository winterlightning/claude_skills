'Open End Wrench with Rounded Handle.\nSymbol plan: A wrench angles toward the upper right with a broad open jaw and a long narrow handle. The jaw has curved outer shoulders, while the lower handle ends in a rounded cap.\nConstruction: Lucide wrench: open jaw integrated with a rounded diagonal handle.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee54ecd1-dacb-44d6-bb14-618638eed18c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/maintenance tool_ee54ecd1-dacb-44d6-bb14-618638eed18c.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'open-end-wrench-with-rounded-handle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('wrench', 'spanner', 'tool', 'jaw', 'handle', 'repair', 'mechanical')
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
        bez('heel',(8,30),((6,32),(6,34),(6,36)),((6,40),(8,42),(12,42)),((14,42),(16,40),(18,38)))
        line('handle-right',(18,38),(29,25))
        bez('outer-right',(29,25),((38,28),(42,20),(42,15)),((42,12),(41,8),(40,6)))
        poly('mouth',(40,6),(30,18),(22,12),(30,6))
        bez('outer-left',(30,6),((18,6),(16,12),(16,17)),((16,20),(18,22),(19,23)))
        line('handle-left',(19,23),(8,30))
        con('wrench','heel','handle-right','outer-right','mouth-1','mouth-2','mouth-3','outer-left','handle-left',closed=True)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
