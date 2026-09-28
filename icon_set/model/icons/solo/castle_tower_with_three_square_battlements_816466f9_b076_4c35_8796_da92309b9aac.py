'Castle Tower with Three Square Battlements.\nSymbol plan: A square castle tower has three evenly spaced battlements separated by deep rectangular notches. A tall rounded arched doorway rises centrally from the flat base of the otherwise blank wall.\nConstruction: Lucide castle: continuous wall silhouette and open arched doorway.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '816466f9-b076-4c35-8796-da92309b9aac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/medieval fortress_816466f9-b076-4c35-8796-da92309b9aac.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'castle-tower-with-three-square-battlements'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('castle', 'tower', 'battlements', 'doorway', 'fortress', 'architecture', 'wall')
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
        poly('wall',(4,40),(4,8),(12,8),(12,16),(20,16),(20,8),(28,8),(28,16),(36,16),(36,8),(44,8),(44,40),(30,40),(30,30))
        arc('arch',(30,30),(18,30),6,s=False)
        poly('base',(18,30),(18,40),(4,40))
        con('tower',*['wall-'+str(i) for i in range(1,14)],'arch','base-1','base-2',closed=True)
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
