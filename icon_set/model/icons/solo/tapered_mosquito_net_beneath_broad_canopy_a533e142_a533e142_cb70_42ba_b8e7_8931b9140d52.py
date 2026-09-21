'Tapered Mosquito Net Beneath Broad Canopy.\nSymbol plan: A mosquito net has a broad flared canopy above a tapered lower enclosure. Three upright internal lines crossed by a horizontal line suggest the mesh structure inside the hanging sides.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One central warp and one weft retain the mesh without narrow holes.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a533e142-cb70-42ba-b8e7-8931b9140d52'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mosquito net_a533e142-cb70-42ba-b8e7-8931b9140d52.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'tapered-mosquito-net-beneath-broad-canopy-a533e142'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('mosquito', 'net', 'canopy', 'mesh', 'protection', 'bed', 'enclosure')
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
        poly('canopy',(6,14),(12,6),(36,6),(42,14),(6,14))
        poly('net',(14,22),(10,42),(38,42),(34,22))
        line('weft',(12,28),(36,28));line('warp',(24,22),(24,42))
        self.relate('connect','weft','net');self.relate('connect','warp','net')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
