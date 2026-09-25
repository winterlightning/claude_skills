"""Extended index finger and thumb, with a blood drop below the fingertip. Lucide droplets informs tangent-continuous teardrop. Other folded fingers reduced to smooth palm edge. HRECT_L holds directional hand and detached drop.
Keyshape HRECT_L; clean centerlines revision. Shared symbol parameters own paired geometry."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3dc0da0-bd87-41fd-95b9-89f6eee043aa'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/laboratory test blood finger_e3dc0da0-bd87-41fd-95b9-89f6eee043aa.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='finger-prick-blood-sample'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    aliases=()
    keywords=('finger', 'prick', 'blood', 'sample')
    def build(self):

        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,k=2):
            path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
        line=self.add_line
        poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        path('hand',(4,16),[('L',(13,10)),('C',(17,8),(15,9),(16,8)),('C',(24,12),(21,8),(24,9)),('L',(40,12)),('A',(40,20),4,4,True),('L',(25,20))])
        path('palm',(4,28),[('C',(18,32),(10,30),(12,32)),('L',(24,32))])
        path('drop',(39,29),[('C',(44,35),(41,31),(44,33)),('A',(34,35),5,5,True),('C',(39,29),(34,33),(37,31))],True)
