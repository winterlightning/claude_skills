'Otoscope Examining an Ear.\nSymbol plan: An otoscope extends horizontally toward a large ear outline on the right. Its tapered head ends in a short narrow tip, with a vertical handle below and a curved inner ear contour opposite it.\nConstruction: Lucide ear: smooth outer rim and curled lobe.\nReduction: Single handle stroke and outer ear outline keep the instrument-to-ear relationship clear.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '18aa2bbb-6394-45e4-800d-88d92fffff8e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/otoscope ear_18aa2bbb-6394-45e4-800d-88d92fffff8e.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'otoscope-examining-ear'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('otoscope', 'ear', 'medical', 'examination', 'instrument', 'hearing')
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
        poly('scope',(4,12),(20,16),(20,24),(4,28),closed=True)
        line('tip',(20,20),(28,20))
        line('handle',(12,26),(12,40))
        bez('ear',(32,12),((32,8),(36,8),(38,8)),((44,8),(44,12),(44,18)),((44,28),(36,27),(36,34)),((36,42),(28,42),(28,34)))
        self.relate('connect','tip','scope');self.relate('connect','handle','scope')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
