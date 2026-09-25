'Square Cufflink Faces with Connecting Posts.\nSymbol plan: Two rounded square cufflink faces sit diagonally apart, one lower left and one upper right. A horizontal toggle projects from the lower face, joined by a slender upright post from the upper face.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Posts become single strokes to preserve separation between the two faces.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c0ec60f-ef40-4517-af95-c4858278c205'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/cuff link_7c0ec60f-ef40-4517-af95-c4858278c205.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'square-cufflink-faces-with-connecting-posts'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('cufflink', 'shirt', 'accessory', 'square', 'fastener', 'jewelry', 'formal')
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
        rect('front',6,26,16,16,3);rect('back',26,6,16,16,3)
        line('post',(34,22),(34,34));line('toggle',(22,34),(42,34))
        self.relate('connect','post','back');self.relate('connect','toggle','front');self.relate('connect','post','toggle')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
