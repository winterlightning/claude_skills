"Standing Camper beside Tent.\nSymbol plan: A person stands at the left of a triangular camping tent. The figure has a round head and straight legs, while a smaller triangle marks the tent's entrance.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. Lucide tent construction.\nReduction: Keep the standing camper and triangular tent; omit the narrow entrance seam.\nKeyshape HRECT_L."
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '23426642-b56a-47a6-8d29-43fd4e1c68f1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/camping trekking tent_23426642-b56a-47a6-8d29-43fd4e1c68f1.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'standing-camper-beside-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('camper', 'person', 'tent', 'camping', 'outdoors', 'entrance', 'scene')
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
        circle('head',10,12,4);line('torso',(10,24),(10,32));poly('arms',(4,30),(10,24),(16,30));poly('legs',(6,40),(10,32),(14,40))
        self.relate('connect','arms','torso');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        poly('tent',(24,40),(34,20),(44,40),closed=True)
        
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
