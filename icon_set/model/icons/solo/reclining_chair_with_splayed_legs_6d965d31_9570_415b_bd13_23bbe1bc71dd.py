'Reclining Chair with Splayed Legs.\nSymbol plan: A reclining chair has a long flat seat and an inclined backrest rising to the upper left. Two slender legs splay outward beneath its bent cushion outline at the front and rear.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: \nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6d965d31-9570-415b-bd13-23bbe1bc71dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/lounge_6d965d31-9570-415b-bd13-23bbe1bc71dd.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'reclining-chair-with-splayed-legs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('lounger', 'chair', 'recliner', 'seat', 'furniture', 'backrest', 'outdoor')
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
        poly('top',(4,12),(12,8),(26,26),(38,26))
        arc('end',(38,26),(38,34),4)
        poly('bottom',(38,34),(18,34),(4,12))
        con('chair','top-1','top-2','top-3','end','bottom-1','bottom-2',closed=True)
        line('leg-a',(17,29),(12,40));line('leg-b',(38,34),(44,40))
        self.relate('connect','leg-a','chair')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
