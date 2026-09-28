"""A water-drop head and intrinsic infinity eye mask; mask meets the drop at its two widest nodes; omit the small smile to preserve space; extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3d5b7e05-9c03-43c3-9fca-83724a912e87'
SOURCE_PATH = 'pictographic-primitives/logos/drupal logo_3d5b7e05-9c03-43c3-9fca-83724a912e87.svg'
AUTHOR = 'gpt-6'

class DrupalLogo(Solo48):
    icon_id = 'drupal-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('drupal', 'cms', 'drop', 'logo', 'brand', 'web', 'open-source')

    def build(self):
        # Plan: A water-drop head and intrinsic infinity eye mask; mask meets the drop at its two widest nodes; omit the small smile to preserve space; extremes (8,4)-(40,44).
        # Construction reference: Lucide droplet: coherent shoulder curves and a round lower bowl.

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

        path('drop',(24,4),[('C',(40,28),(28,12),(40,16)),('A',(24,44),16,16,True),('A',(8,28),16,16,True),('C',(24,4),(8,16),(20,12))],True)
        path('mask-upper',(8,28),[('C',(24,28),(8,20),(16,20)),('C',(40,28),(32,36),(40,36))])
        path('mask-lower',(8,28),[('C',(24,28),(8,36),(16,36)),('C',(40,28),(32,20),(40,20))])
        join('drop','mask-upper');join('drop','mask-lower');join('mask-upper','mask-lower')
