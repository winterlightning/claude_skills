# Final reduction: Omit crowded internal wing; preserve hooked beak, domed head, chest and deliberate profile asymmetry.
'Eagle Profile with Hooked Beak.\nSymbol plan: An eagle faces right with a domed head and a large hooked beak. A sweeping inner line defines a broad folded wing, while the lower chest curves down beside it.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14a80802-3bb5-4ed7-8896-0c8f64e4e53d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/eagle_14a80802-3bb5-4ed7-8896-0c8f64e4e53d.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'eagle-profile-with-hooked-beak'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('eagle', 'bird', 'beak', 'wing', 'raptor', 'animal', 'profile')
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
        bez('head',(6,42),((14,26),(10,6),(26,6)),((32,6),(36,10),(36,14)))
        bez('beak',(36,14),((42,14),(42,18),(42,22)),((34,20),(32,24),(34,30)),((38,38),(32,42),(26,42)))
        # Omit the crowded inner wing; the hooked beak and chest remain.
        con('upper','head','beak')
        
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
