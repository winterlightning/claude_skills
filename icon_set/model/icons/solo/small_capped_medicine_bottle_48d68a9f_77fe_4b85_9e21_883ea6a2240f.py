'Small Capped Medicine Bottle.\nSymbol plan: A small bottle has a rounded rectangular body and curved shoulders narrowing into a short neck. A broad rounded cap sits above the neck, with slight gaps where the outlines meet.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Retain the source parts and arrangement.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48d68a9f-77fe-4b85-9e21-883ea6a2240f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plastic_48d68a9f-77fe-4b85-9e21-883ea6a2240f.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'small-capped-medicine-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('bottle', 'medicine', 'vial', 'cap', 'container', 'pharmacy')
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
        rect('cap',14,4,20,8,2)
        poly('neck',(16,12),(16,20),(12,24))
        bez('shoulder-left',(12,24),((8,28),(8,29),(8,32)))
        line('left',(8,32),(8,38));arc('lower-left',(8,38),(14,44),6,s=False)
        line('base',(14,44),(34,44));arc('lower-right',(34,44),(40,38),6,s=False)
        line('right',(40,38),(40,32));bez('shoulder-right',(40,32),((40,29),(40,28),(36,24)))
        poly('neck-right',(36,24),(32,20),(32,12))
        con('body','neck-1','neck-2','shoulder-left','left','lower-left','base','lower-right','right','shoulder-right','neck-right-1','neck-right-2')
        self.relate('connect','cap','body')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)
