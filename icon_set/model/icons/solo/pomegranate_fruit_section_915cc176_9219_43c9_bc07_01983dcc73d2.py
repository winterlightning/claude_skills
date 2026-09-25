"""Pomegranate fruit slice.
Symbol plan: Round pomegranate with pointed crown and four seeds. Bounds (8,4)-(40,44).
Construction reference: Supplied pomegranate; Lucide citrus sparse seed organization.
Reduction: Four seed strokes reduced to dots; crown silhouette retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '915cc176-9219-43c9-bc07-01983dcc73d2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/pomegranate slice_915cc176-9219-43c9-bc07-01983dcc73d2.svg'
AUTHOR = 'gpt-6'

class PomegranateFruitSection(Solo48):
    icon_id = 'pomegranate-fruit-section'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('pomegranate', 'fruit', 'section')

    def build(self):
        self.path('fruit',(18,12),[((10,16),(8,21),(8,28)),((8,37),(15,44),(24,44)),((33,44),(40,37),(40,28)),((40,21),(38,16),(30,12)),(32,4),(26,7),(24,4),(22,7),(16,4),(18,12)],True)
        for j,p in enumerate([(24,21),(17,29),(31,29),(24,35)]):self.add_dot('seed-'+str(j),p)

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
