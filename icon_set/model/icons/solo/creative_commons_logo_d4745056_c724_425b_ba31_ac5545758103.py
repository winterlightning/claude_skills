"""Circular roundel enclosing two identical open C letters; repeated radius and horizontal step maintain matching letterforms."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4745056-c724-425b-ba31-ac5545758103'
SOURCE_PATH = 'pictographic-primitives/logos/creative commons logo_d4745056-c724-425b-ba31-ac5545758103.svg'
AUTHOR = 'gpt-6'

class CreativeCommonsLogo(Solo48):
    icon_id = 'creative-commons-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('creative-commons', 'cc', 'license', 'logo', 'brand', 'copyright', 'open')

    def build(self):
        # Plan: Circular roundel enclosing two identical open C letters; repeated radius and horizontal step maintain matching letterforms.
        # Construction reference: Lucide creative-commons: repeated open arcs inside a circle.

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

        circle('roundel',24,24,20)
        for i,x in enumerate((17,31)):
            path(f'letter-{i}',(x+2,20),[('L',(x,20)),('A',(x,28),4,4,False),('L',(x+2,28))])
