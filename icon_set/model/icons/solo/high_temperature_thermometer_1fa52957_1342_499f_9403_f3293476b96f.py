"""High Temperature Thermometer.
Symbol plan: Upright stem and broad bulb, high mercury column, three scale ticks. Bounds (8,4)-(40,44).
Construction reference: Lucide thermometer: connected rounded stem/bulb; supplied reference: tall mercury and right ticks.
Reduction: No duplicate inner stem outline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fa52957-1342-499f-9403-f3293476b96f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/temperature thermometer high_1fa52957-1342-499f-9403-f3293476b96f.svg'
AUTHOR = 'gpt-6'

class HighTemperatureThermometer(Solo48):
    icon_id = 'high-temperature-thermometer'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('high', 'temperature', 'thermometer')

    def build(self):
        self.path('outline',(10,13),[((10,1),(28,1),(28,13)),(28,24),((30,27),(30,30),(30,33)),((30,39),(25,44),(19,44)),((13,44),(8,39),(8,33)),((8,30),(8,27),(10,24)),(10,13)],True)
        self.loop('mercury-bulb',19,33,2)
        self.add_line('mercury',(19,13),(19,31))
        self.relate('connect','mercury','mercury-bulb')
        for j,y in enumerate((10,20,28)):self.add_line(f'tick-{j}',(38,y),(40,y))

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
