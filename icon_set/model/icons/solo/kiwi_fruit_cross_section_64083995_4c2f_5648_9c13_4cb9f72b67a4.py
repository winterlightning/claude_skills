"""Kiwi Fruit Slice.
Symbol plan: Concentric skin and small core with six repeated seed dots on integer ring. Radius20 centered24.
Construction reference: Supplied kiwi cross-section; Lucide citrus radial interior organization.
Reduction: Eight short seeds reduced to six dots to protect the core clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64083995-4c2f-5648-9c13-4cb9f72b67a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/kiwi_64083995-4c2f-5648-9c13-4cb9f72b67a4.svg'
AUTHOR = 'gpt-6'

class KiwiFruitCrossSection(Solo48):
    icon_id = 'kiwi-fruit-cross-section'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('kiwi', 'fruit', 'cross', 'section')

    def build(self):
        axis=24
        self.loop('skin',axis,axis,20)
        self.loop('core',axis,axis,2)
        for j,(dx,dy) in enumerate([(0,-11),(10,-5),(10,5),(0,11),(-10,5),(-10,-5)]):self.add_dot('seed-'+str(j),(axis+dx,axis+dy))

    def path(self, name, start, commands, closed=False):
        members=[]
        for j,c in enumerate(commands):
            tag=f'{name}-{j}'
            if len(c)==2:self.add_line(tag,start,c);start=c
            else:self.add_bezier(tag,start,c);start=c[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def loop(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(name+'-r',(x,y-ry),(x,y+ry),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-l',(x,y+ry),(x,y-ry),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-r',name+'-l',closed=True)

    def steam(self,x,top,bottom,name):
        mid=(top+bottom)//2
        self.add_bezier(name,(x+1,top),((x-2,top+2),(x-2,mid),(x,mid)),((x+2,mid),(x+2,bottom-2),(x-1,bottom)))
