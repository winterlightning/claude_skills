"""The Clyde controller face with two solid eyes and mirrored horn/cheek features; omit the generic speech-bubble frame to retain face spacing; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a3cb5375-7633-4bb9-9752-15d41c52cc98'
SOURCE_PATH = 'pictographic-primitives/logos/discord logo_a3cb5375-7633-4bb9-9752-15d41c52cc98.svg'
AUTHOR = 'gpt-6'

class DiscordLogo(Solo48):
    icon_id = 'discord-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('discord', 'chat', 'gaming', 'logo', 'brand', 'community', 'voice')

    def build(self):
        # Plan: The Clyde controller face with two solid eyes and mirrored horn/cheek features; omit the generic speech-bubble frame to retain face spacing; extremes (4,8)-(44,40).
        # Construction reference: No useful subject-specific Lucide match; construction follows the supplied brand render.

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

        path('face',(14,8),[('C',(20,10),(16,8),(18,9)),('C',(28,10),(23,9),(25,9)),('C',(34,8),(30,9),(32,8)),('C',(44,34),(41,9),(43,24)),('C',(34,40),(41,38),(38,40)),('L',(30,36)),('C',(18,36),(26,38),(22,38)),('L',(14,40)),('C',(4,34),(10,40),(7,38)),('C',(14,8),(5,24),(7,9))],True)
        for i,x in enumerate((17,31)): circle(f'eye-{i}',x,24,2)
