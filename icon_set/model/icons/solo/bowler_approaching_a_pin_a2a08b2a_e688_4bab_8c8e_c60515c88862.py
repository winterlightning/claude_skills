'Bowler Approaching a Pin.\nSymbol plan: A person leans forward with one leg extended and both arms spread. A small ball appears beside the trailing hand, and a lone bowling pin stands to the right.\nConstruction: Human full_body_ref.png: circular heads, coherent torso/limbs, exact 8u centerline / 4u ink head-to-neck clearance. The neck is intentionally upright before the torso bends forward.\nReduction: Keep bowler, detached ball and lone pin.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a2a08b2a-e688-4bab-8c8e-c60515c88862'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bowling player_a2a08b2a-e688-4bab-8c8e-c60515c88862.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'bowler-approaching-a-pin'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('bowler', 'bowling', 'ball', 'pin', 'sport', 'person', 'game')
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
        circle('head',24,12,4);line('torso',(24,24),(24,28));line('lower-torso',(24,28),(20,32));poly('arms',(8,24),(24,24),(30,26));poly('legs',(16,40),(20,32),(28,36),(28,40))
        circle('ball',6,34,2)
        bez('pin',(38,40),((34,34),(38,32),(38,28)),((38,24),(42,24),(42,28)),((42,32),(44,32),(44,36)),((44,38),(42,40),(42,40)))
        line('pin-base',(42,40),(38,40));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
