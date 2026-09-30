"""Field rows: rejected boundary follows rather than crosses the main rows, reading as generic stripes. Restore intersecting hillside and arcing crop rows. Restore arcing crop rows and a separate hillside, joining at a shared node.
Symbol plan: Concentric crop arcs and opposing hill with a shared junction. Small left-side row fragment omitted for clarity.
Keyshape SQUARE: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3666c9ff-d6e0-450c-908c-4209907d1997'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-agricultural-field-rows/20260929T115456Z-thuan-mac/reference/plantation_3666c9ff-d6e0-450c-908c-4209907d1997.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curved-agricultural-field-rows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('curved', 'agricultural', 'field', 'rows')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('row-outer',(6,42),[('C',(18,18),(6,32),(10,26)),('C',(42,6),(26,10),(32,6))])
        path('row-middle',(18,42),[('A',(42,18),24,24,True)])
        path('row-inner',(30,42),[('A',(42,30),12,12,True)])
        path('hill',(6,8),[('C',(18,18),(10,8),(15,13))]);join('hill','row-outer')
