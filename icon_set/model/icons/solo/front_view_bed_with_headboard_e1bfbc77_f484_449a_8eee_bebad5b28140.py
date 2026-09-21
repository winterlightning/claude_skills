# Final reduction: Pillow and mattress share a boundary rather than overlapping outlines.
'Front View Bed with Headboard.\nSymbol plan: A bed faces forward beneath a broad rounded rectangular headboard and smaller raised pillow. Its mattress projects toward the viewer above a deep front panel and two short legs.\nConstruction: Lucide bed: separate headboard and mattress with clear horizontal bands.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e1bfbc77-f484-449a-8eee-bebad5b28140'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boxspring_e1bfbc77-f484-449a-8eee-bebad5b28140.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'front-view-bed-with-headboard'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('bed', 'bedroom', 'headboard', 'mattress', 'pillow', 'furniture', 'sleep')
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
        poly('headboard',(10,24),(10,6),(38,6),(38,24))
        poly('pillow',(18,24),(18,14),(30,14),(30,24))
        poly('mattress',(6,32),(10,24),(38,24),(42,32),(6,32))
        poly('front',(6,32),(6,40),(42,40),(42,32))
        line('leg-left',(10,40),(10,42));line('leg-right',(38,40),(38,42))
        self.relate('connect','pillow','mattress');self.relate('connect','headboard','mattress');self.relate('connect','leg-left','front');self.relate('connect','leg-right','front')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
