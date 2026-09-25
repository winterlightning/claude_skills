'Upright Open Hand with Joined Fingers.\nSymbol plan: An upright open hand has four long rounded fingers held together above a broad palm. The thumb angles outward on the left, and the lower palm curves into a rounded wrist edge.\nConstruction: Lucide hand and human_ref: shared round fingertips and coherent palm contour.\nReduction: Use four round fingertips with 8-unit pitch; shorten finger creases for clarity.\nKeyshape HRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2642bb02-0d07-4d75-b214-cde16b5f0ce2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/skin_2642bb02-0d07-4d75-b214-cde16b5f0ce2.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'upright-open-hand-with-joined-fingers'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('hand', 'palm', 'fingers', 'thumb', 'body', 'gesture')
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
        first_x,radius=12,4
        heights=(14,12,14,20)
        parts=[]
        for i,y in enumerate(heights):
         x=first_x+i*8
         if i==0:line('rise',(12,28),(12,y));parts.append('rise')
         else:line('rise'+str(i),(x,heights[i-1]),(x,y));parts.append('rise'+str(i))
         arc('tip'+str(i),(x,y),(x+8,y),4);parts.append('tip'+str(i))
        line('side',(44,20),(44,28));arc('palm-round',(44,28),(32,40),12)
        bez('palm-left',(24,40),((16,40),(10,34),(4,28)),((4,22),(8,22),(12,28)))
        con('outline',*parts,'side','palm-round')
        for i,end in enumerate((24,24,26)):
         x=20+i*8;line('crease'+str(i),(x,max(heights[i],heights[i+1])),(x,end));self.relate('connect','crease'+str(i),'outline')
        line('wrist',(32,40),(24,40))
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
