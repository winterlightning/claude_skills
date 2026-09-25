"""An isometric cube with three broad faces; shared centre seam and boundary attachment nodes; extremes (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c8c52b8-cfbd-4bd4-a74b-317df1c226ad'
SOURCE_PATH = 'pictographic-primitives/logos/code sandbox logo_6c8c52b8-cfbd-4bd4-a74b-317df1c226ad.svg'
AUTHOR = 'gpt-6'

class CodesandboxLogo(Solo48):
    icon_id = 'codesandbox-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('codesandbox', 'cube', 'logo', 'brand', 'developer', 'sandbox', 'ide')

    def build(self):
        # Plan: An isometric cube with three broad faces; shared centre seam and boundary attachment nodes; extremes (6,6)-(42,42).
        # Construction reference: Lucide box: broad faces and common seam nodes.

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

        axis=24; left=6; right=2*axis-left
        top=(axis,6); bottom=(axis,42); centre=(axis,25)
        poly('outline',top,(right,16),(right,32),bottom,(left,32),(left,16),closed=True)
        poly('top-seam',(left,16),centre,(right,16))
        line('vertical-seam',centre,bottom)
        join('outline','top-seam');join('outline','vertical-seam');join('top-seam','vertical-seam')
