'Peninsula with Shore Waves.\nSymbol plan: An irregular land shape has a broad upper section and a rounded lower projection. Two separate curved wave lines follow its indented left edge, bending around the lower part of the shoreline.\nConstruction: Reference-specific coherent contours; no useful exact Lucide match.\nReduction: One coastal wave replaces two closely spaced wave strokes.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c34ad66f-6cf1-4902-8302-f96199320d01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/peninsula_c34ad66f-6cf1-4902-8302-f96199320d01.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'peninsula-shore-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('peninsula', 'shore', 'land', 'water', 'waves', 'coast')
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
        bez('shore',(24,6),((14,6),(20,16),(16,18)),((16,20),(16,28),(24,28)),((30,28),(22,42),(32,42)),((44,42),(42,32),(38,26)),((32,18),(42,20),(42,12)),((42,6),(36,6),(24,6)))
        bez('wave',(6,26),((6,34),(14,30),(16,42)))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
