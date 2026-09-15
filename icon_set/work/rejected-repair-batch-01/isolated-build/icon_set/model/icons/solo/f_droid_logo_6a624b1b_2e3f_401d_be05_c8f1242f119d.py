"""A rounded robot housing with two antennas, two eyes and an open curl; merge head/body walls and omit the badge ring to preserve spacing; extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6a624b1b-2e3f-401d-be05-c8f1242f119d'
SOURCE_PATH = 'pictographic-primitives/logos/f droid logo_6a624b1b-2e3f-401d-be05-c8f1242f119d.svg'
AUTHOR = 'gpt-6'

class FDroidLogo(Solo48):
    icon_id = 'f-droid-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('f-droid', 'android', 'robot', 'app-store', 'logo', 'brand', 'open-source')

    def build(self):
        # Plan: A rounded robot housing with two antennas, two eyes and an open curl; merge head/body walls and omit the badge ring to preserve spacing; extremes (8,4)-(40,44).
        # Construction reference: Lucide bot: rounded housing, antenna attachments and spaced eyes.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i, command in enumerate(commands):
                kind, end, *args=command
                part=f"{name}-{i}"
                if kind=='L': self.add_line(part,here,end)
                elif kind=='A':
                    rx,ry,sweep=args
                    self.add_arc(part,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
                elif kind=='C': self.add_bezier(part,here,(args[0],args[1],end))
                members.append(part); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def c_ring(name):
            # Exact radius-20 points on the circle about (24,24).
            self.add_arc(name,(36,8),(36,40),radius_x=20,large_arc=True,sweep=False)
        poly=self.add_polyline
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        def graph(edges):
            for name,a,b in edges: line(name,a,b)
            for i,(name,a,b) in enumerate(edges):
                for other,c,d in edges[:i]:
                    if {a,b}&{c,d}: join(name,other)

        path('body',(12,10),[('L',(16,10)),('L',(32,10)),('L',(36,10)),('A',(40,14),4,4,True),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,14)),('A',(12,10),4,4,True)],True)
        for i,(a,b) in enumerate((((12,4),(16,10)),((36,4),(32,10)))):line(f'antenna-{i}',a,b);join(f'antenna-{i}','body')
        for i,x in enumerate((18,30)):self.add_dot(f'eye-{i}',(x,19))
        path('curl',(26,27),[('L',(24,27)),('A',(24,35),4,4,False),('L',(26,35))])
