"""Two diamond solar panels connect to a larger circular central bus, with a broad broadcast arc. Shared panel definition and a diagonal axis. SQUARE centerlines (6,6)-(42,42)."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '22d0481f-c9b6-401c-ac60-eb38e2aabb27'
SOURCE_PATH = 'pictographic-primitives/tv/satellite signal_22d0481f-c9b6-401c-ac60-eb38e2aabb27.svg'
AUTHOR='gpt-6'
CONSTRUCTION_REFERENCE='satellite: diagonal panel arrangement and shared bus connections'
DESIGN_PLAN='Two diamond solar panels connect to a larger circular central bus, with a broad broadcast arc. Shared panel definition and a diagonal axis. SQUARE centerlines (6,6)-(42,42).'
OMISSIONS='Tiny central bolt and inner wave tier omitted for clearance.'
class Drawing(Solo48):
    icon_id='satellite-with-signal-waves'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/media'
    aliases=()
    keywords=('satellite', 'with', 'signal', 'waves')
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)



    def build(self):
        for n,cx,cy in [('panel-a',12,12),('panel-b',36,36)]:
            self.add_polyline(n,(cx-6,cy),(cx,cy-6),(cx+6,cy),(cx,cy+6),closed=True)
        self.circle('bus',24,24,6)
        self.add_line('strut-a',(18,12),(24,18));self.relate('connect','strut-a','panel-a');self.relate('connect','strut-a','bus')
        self.add_line('strut-b',(24,30),(30,36));self.relate('connect','strut-b','bus');self.relate('connect','strut-b','panel-b')
        self.add_arc('wave',(6,27),(21,42),radius_x=15,sweep=False)
