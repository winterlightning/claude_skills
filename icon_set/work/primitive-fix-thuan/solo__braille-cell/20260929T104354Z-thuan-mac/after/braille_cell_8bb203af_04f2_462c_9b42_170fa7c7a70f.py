'Enlarged all six circles and used a shared regular two-column, three-row construction.\nOriginal/current comparison: The rejected six circles have pinhole centers and overly wide columns relative to their diameter.\nPlan: VRECT_L, bounds (6, 2, 42, 46); shared circles, mirrored pairs and explicit joined nodes.\nReference: No useful subject-specific Lucide match; geometric arcs and smooth coherent contours.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8bb203af-04f2-462c-9b42-170fa7c7a70f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__braille-cell/20260929T104354Z-thuan-mac/reference/disability braille_8bb203af-04f2-462c-9b42-170fa7c7a70f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'braille-cell'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('braille', 'cell')

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r)
            arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        for x in (12,36):
            for y in (8,24,40): circle(f'dot-{x}-{y}',x,y,4)
