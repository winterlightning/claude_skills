"""Immersion Stick Blender.
Symbol plan: Diagonal motor capsule and shaft; broad half-disc head. Bounds (6,6)-(42,42).
Construction reference: Supplied diagonal blender; Lucide blender for one broad motor silhouette.
Reduction: Motor button and twin shaft edges omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9639fa15-4ba6-492a-8a1f-5e66bf7fc04d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/hand mixer_9639fa15-4ba6-492a-8a1f-5e66bf7fc04d.svg'
AUTHOR = 'gpt-6'

class ImmersionStickBlender(Solo48):
    icon_id = 'immersion-stick-blender'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('immersion', 'stick', 'blender')

    def build(self):
        self.path('motor',(25,10),[((28,7),(30,6),(32,6)),((37,6),(42,11),(42,16)),((42,18),(41,20),(38,23)),(33,28),((31,30),(29,29),(27,27)),(24,24),(21,21),((19,19),(18,17),(20,15)),(25,10)],True)
        self.add_line('shaft',(24,24),(15,33));self.relate('connect','shaft','motor')
        self.path('head',(6,34),[((8,30),(12,30),(15,33)),((18,36),(18,40),(14,42)),(6,34)],True);self.relate('connect','shaft','head')

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
