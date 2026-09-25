"Camper behind Flagged Tent.\nSymbol plan: A triangular tent with a small entrance and pennant stands in front of a person. The person's circular head and rounded upper body remain visible at the right.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. Lucide tent construction.\nReduction: Omit narrow tent entrance; preserve camper, tent and pennant.\nKeyshape SQUARE."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5655244e-9c88-42c3-a2be-d90a6fab78b2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camping tent person_5655244e-9c88-42c3-a2be-d90a6fab78b2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'camper-behind-flagged-tent'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('camper', 'tent', 'flag', 'camping', 'person', 'outdoors', 'entrance')
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
        poly('tent',(6,42),(18,22),(30,42),closed=True);
        poly('flag',(18,22),(18,6),(30,14),(18,22))
        circle('head',38,26,4);line('torso',(38,38),(38,42));line('arm',(38,38),(42,38));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
