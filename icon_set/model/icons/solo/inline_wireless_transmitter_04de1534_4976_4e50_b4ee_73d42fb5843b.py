'A small upright rounded transmitter body interrupts a thin vertical mast. Three nested semicircular signal arcs spread above the mast, centered over the body and opening downward.\nPlan: Central inline body and two signal waves, reducing three-wave series for clearance. Extrema8,4,40,44.\nConstruction reference: Lucide wifi and router: nested waves and an inline geometric body.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04de1534-4976-4e50-b4ee-73d42fb5843b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/antenna 2_04de1534-4976-4e50-b4ee-73d42fb5843b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'inline-wireless-transmitter'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('inline', 'wireless', 'transmitter')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        for n,r in enumerate((16,7)):path(f'wave-{n}',(24-r,20),[('A',(24,20-r),r,r,True),('A',(24+r,20),r,r,True)])
        path('body',(20,30),[('L',(24,30)),('L',(28,30)),('L',(28,40)),('L',(24,40)),('L',(20,40)),('L',(20,30))],True)
        line('upper-mast',(24,25),(24,30));line('lower-mast',(24,40),(24,44));join('body','upper-mast');join('body','lower-mast')
