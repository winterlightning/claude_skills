'Computer Desk with Drawer Pedestal.\nSymbol plan: A desktop monitor rests on a short central stand above a wide desk. The desk has a narrow left leg and a rounded right pedestal divided by one horizontal drawer seam.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit drawer handles to retain the pedestal divisions.\nKeyshape HRECT_L: ink extremes (2, 6, 46, 42).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3475478d-0c8c-4cc2-8282-5dd80961921d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/office desk 2_3475478d-0c8c-4cc2-8282-5dd80961921d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'computer-desk-drawer-pedestal-3475478d'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('desk', 'computer', 'monitor', 'drawers', 'office', 'furniture')
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
        rect('monitor',12,8,24,12,2)
        line('stand',(24,20),(24,28));line('desk',(4,28),(44,28))
        line('left-leg',(6,28),(6,40))
        poly('drawers',(30,28),(30,40),(44,40),(44,28))
        self.relate('connect','stand','monitor')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
