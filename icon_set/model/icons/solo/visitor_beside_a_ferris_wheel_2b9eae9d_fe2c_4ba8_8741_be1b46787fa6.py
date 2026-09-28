'Visitor Beside a Ferris Wheel.\nSymbol plan: A small standing person occupies the left foreground beside a Ferris wheel. The wheel has a circular hub, wide triangular support, and an interrupted outer rim carrying three visible cabins on the right.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance.\nReduction: Use a complete four-spoke wheel above its support beside the visitor; omit tiny individual cabin rings.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2b9eae9d-fe2c-4ba8-8741-be1b46787fa6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/amusement park ferris wheel person_2b9eae9d-fe2c-4ba8-8741-be1b46787fa6.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'visitor-beside-a-ferris-wheel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('visitor', 'ferris wheel', 'person', 'amusement', 'carnival', 'ride', 'scene')
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
        circle('head',8,22,4);line('torso',(8,34),(8,40));poly('arms',(4,38),(8,34),(12,38));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        arc('wheel-a',(32,8),(44,20),12);arc('wheel-b',(44,20),(32,32),12);arc('wheel-c',(32,32),(20,20),12);arc('wheel-d',(20,20),(32,8),12)
        con('wheel','wheel-a','wheel-b','wheel-c','wheel-d',closed=True)
        line('vertical-spoke',(32,8),(32,32));line('horizontal-spoke',(20,20),(44,20));self.relate('connect','vertical-spoke','horizontal-spoke')
        poly('support',(24,40),(32,32),(40,40))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
