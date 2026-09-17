"""Japanese Bento Box Meal.
Symbol plan: Rounded box, full-height partition and one cross partition; two food dots. Bounds (6,6)-(42,42).
Construction reference: Supplied bento subdivisions; Lucide microwave for rounded enclosure construction.
Reduction: Dense rice and clustered food contours reduced to two food marks.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba617c30-affd-453a-9840-5a1b6cb3e0ff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/japanese launchbox bento ekiben_ba617c30-affd-453a-9840-5a1b6cb3e0ff.svg'
AUTHOR = 'gpt-6'

class JapaneseBentoMeal(Solo48):
    icon_id = 'japanese-bento-meal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/food'
    aliases = ()
    keywords = ('japanese', 'bento', 'meal')

    def build(self):
        self.path('box',(24,6),[(38,6),((40,6),(42,8),(42,10)),(42,24),(42,38),((42,40),(40,42),(38,42)),(24,42),(10,42),((8,42),(6,40),(6,38)),(6,10),((6,8),(8,6),(10,6)),(24,6)],True)
        self.add_polyline('divider',(24,6),(24,24),(24,42));self.relate('connect','divider','box')
        self.add_line('cross',(24,24),(42,24));self.relate('connect','cross','box');self.relate('connect','cross','divider')
        for y in (15,33):self.add_dot('food-'+str(y),(33,y))

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
