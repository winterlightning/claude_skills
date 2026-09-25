# Final reduction: Reduce side battlements to broad stepped tower shoulders; omit slit.
'Castle with Central Roofed Tower.\nSymbol plan: A castle facade has two crenellated side towers and a taller central tower with a pointed roof. A rounded doorway opens below the central wall, beneath one narrow vertical window slit.\nConstruction: Lucide castle: joined towers, walls, and doorway.\nReduction: Omit central slit and reduce side battlements to broad parapets.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '08c7f4df-afaf-4c67-8624-2f123c81710a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/palace_08c7f4df-afaf-4c67-8624-2f123c81710a.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'castle-central-roofed-tower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('castle', 'towers', 'medieval', 'fortress', 'building', 'battlements')
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
        poly('outline',(6,42),(6,22),(14,22),(14,16),(24,6),(34,16),(34,22),(42,22),(42,42),(6,42))
        poly('door',(20,42),(20,32),(28,32),(28,42));self.relate('connect','door','outline')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
