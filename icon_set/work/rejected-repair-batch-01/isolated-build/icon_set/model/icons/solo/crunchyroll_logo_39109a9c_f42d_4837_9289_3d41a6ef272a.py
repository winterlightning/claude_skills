"""Two nested crescent sweeps, both open toward upper-right; reduce each outlined crescent to its dominant circular curve."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39109a9c-f42d-4837-9289-3d41a6ef272a'
SOURCE_PATH = 'pictographic-primitives/logos/crunchyroll logo_39109a9c-f42d-4837-9289-3d41a6ef272a.svg'
AUTHOR = 'gpt-6'

class CrunchyrollLogo(Solo48):
    icon_id = 'crunchyroll-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('crunchyroll', 'anime', 'streaming', 'logo', 'brand', 'video', 'crescent')

    def build(self):
        # Plan: Two nested crescent sweeps, both open toward upper-right; reduce each outlined crescent to its dominant circular curve.
        # Construction reference: No useful subject match found; source brand render informs the geometry.

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

        self.add_arc('outer',(40,12),(24,44),radius_x=20,large_arc=True,sweep=False)
        self.add_arc('inner',(32,16),(38,34),radius_x=10,large_arc=True,sweep=False)
