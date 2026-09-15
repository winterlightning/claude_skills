"""Four open-box flaps surround the central diamond; the base descends below the lower flaps; mirrored shared vertices avoid duplicate edges; extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dda3f7df-db91-4e76-8ae0-b80cb00b541f'
SOURCE_PATH = 'pictographic-primitives/logos/dropbox logo_dda3f7df-db91-4e76-8ae0-b80cb00b541f.svg'
AUTHOR = 'gpt-6'

class DropboxLogo(Solo48):
    icon_id = 'dropbox-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('dropbox', 'cloud-storage', 'box', 'logo', 'brand', 'files', 'sync')

    def build(self):
        # Plan: Four open-box flaps surround the central diamond; the base descends below the lower flaps; mirrored shared vertices avoid duplicate edges; extremes (4,8)-(44,40).
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

        poly('flaps',(14,8),(24,14),(34,8),(44,14),(34,20),(44,26),(34,32),(24,26),(14,32),(4,26),(14,20),(4,14),closed=True)
        poly('centre',(14,20),(24,14),(34,20),(24,26),closed=True)
        poly('base',(14,32),(14,34),(24,40),(34,34),(34,32))
        join('flaps','centre');join('flaps','base')
