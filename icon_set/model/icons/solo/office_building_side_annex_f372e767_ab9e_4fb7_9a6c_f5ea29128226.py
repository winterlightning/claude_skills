'Office Building with Side Annex.\nSymbol plan: A tall rectangular office building has four square windows arranged above a centered doorway. A shorter blank annex stands against its right side, with both structures resting on a shared horizontal baseline.\nConstruction: Lucide building: regular dot windows and a plain doorway.\nReduction: Windows reduced to four dots.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f372e767-ab9e-4fb7-9a6c-f5ea29128226'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/office_f372e767-ab9e-4fb7-9a6c-f5ea29128226.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'office-building-side-annex'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('office', 'building', 'windows', 'annex', 'city', 'architecture')
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
        poly('building',(6,42),(6,6),(30,6),(30,42))
        poly('annex',(30,26),(42,26),(42,42));line('ground',(6,42),(42,42))
        for i,(x,y) in enumerate(((14,14),(22,14),(14,24),(22,24))):self.add_dot('window'+str(i),(x,y))
        poly('door',(14,42),(14,34),(22,34),(22,42));self.relate('connect','door','ground')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
