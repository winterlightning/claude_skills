'A tall boot faces left with a straight upright shaft and a broad rounded toe. Its curved sole steps upward into a distinct squared heel at the back.\nPlan: Left-facing rain boot, continuous smooth shaft-to-toe transition and an integral back heel. Extremes (8,4)-(40,44).\nConstruction reference: footprints: a few smooth silhouette curves, preserving the boot shaft.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74cb04e1-aad2-49e3-a0a6-99254c186818'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boot_74cb04e1-aad2-49e3-a0a6-99254c186818.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tall-rain-boot-with-heel'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tall', 'rain', 'boot', 'with', 'heel')

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

        path('boot',(24,4),[('L',(40,4)),('L',(40,44)),('L',(30,44)),('L',(30,36)),('C',(16,40),(25,40),(20,40)),('L',(8,40)),('L',(8,34)),('C',(16,28),(8,30),(12,28)),('C',(24,18),(22,28),(24,24)),('L',(24,4))],True)
