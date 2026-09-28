'Blank Open Laptop.\nSymbol plan: An open laptop has a broad blank screen with rounded upper corners. Its lower edge joins a shallow base that slopes outward toward two rounded front corners and a straight horizontal front edge.\nConstruction: Lucide laptop: blank rounded screen and shallow flared base.\nReduction: \nKeyshape HRECT_M.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7b74abd1-6530-4972-a359-b5ebb36734a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/netbook_7b74abd1-6530-4972-a359-b5ebb36734a5.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'blank-open-laptop'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('laptop', 'computer', 'screen', 'device', 'keyboard', 'notebook')
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
        rect('screen',8,10,32,20,3)
        poly('base',(8,30),(4,38),(44,38),(40,30))
        self.relate('connect','screen','base')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
