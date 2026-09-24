"""Rounded muzzle and open jaw, pointed ear and separate ball; natural side-view asymmetry.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide dog: coherent rounded animal contours.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '08cdc871-2ff7-4c1a-9e75-3415928459cf'
SOURCE_PATH = 'pictographic-primitives/pets/dog carrying bring play ball_08cdc871-2ff7-4c1a-9e75-3415928459cf.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dog-carrying-ball'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/pets'
    aliases=()
    keywords=('dog carrying bring play ball',)
    def build(self):
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                k,end,*args=c; name=f'{n}-{j}'
                if k=='L': self.add_line(name,here,end)
                elif k=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif k=='C': self.add_bezier(name,here,(args[0],args[1],end))
                here=end; members.append(name)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('head',(42,16),[('C',(38,6),(42,12),(40,8)),('L',(34,14)),('L',(24,14)),('L',(16,14)),('A',(16,22),4,4,False),('L',(28,22)),('A',(28,32),5,5,True),('L',(28,34)),('A',(32,40),4,4,False),('L',(36,36)),('L',(42,42))])
        circle('ball',12,36,6)
