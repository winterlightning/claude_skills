'Overlapping Socks with Heel Patches.\nSymbol plan: Two long socks overlap diagonally, with their toes pointing toward the lower left and straight cuffs above. Horizontal cuff seams and curved heel patches distinguish the separate parts of each sock.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Omit small heel patches to preserve two overlapping sock silhouettes.\nKeyshape SQUARE.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '475d6268-69ce-4239-b4c4-1056472b99de'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/socks_475d6268-69ce-4239-b4c4-1056472b99de.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'overlapping-socks-with-heel-patches'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('socks', 'clothing', 'footwear', 'heel', 'cuff', 'pair')
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
        poly('front',(26,14),(42,14),(42,30),(26,42))
        arc('toe',(26,42),(16,32),8,s=False)
        poly('instep',(16,32),(26,24),(26,14))
        con('front-sock','front-1','front-2','front-3','toe','instep-1','instep-2',closed=True)
        poly('back',(10,6),(26,6),(26,14))
        poly('back-side',(10,6),(10,22),(6,26))
        bez('back-toe',(6,26),((6,34),(10,38),(16,32)))
        line('cuff',(26,22),(42,22));self.relate('connect','cuff','front-sock')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
