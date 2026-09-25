"""Wheat Grain Stalk.

Two mirrored pairs of pointed wheat leaves, regular 20-unit vertical repeat; omit the third pair after its retained-count layout failed the minimum hole size check. Centerline extremes (8,4)-(40,44). Lucide wheat informs repeated leaf symbols; retain source upright symmetry and omit veins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ad5de78-6fc3-4900-a9ce-73905938cee9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/barley_9ad5de78-6fc3-4900-a9ce-73905938cee9.svg'
AUTHOR = 'gpt-6'

class WheatStalkThreeLeafPairs(Solo48):
    icon_id = 'wheat-stalk-three-leaf-pairs'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    categories = ('primitives', 'food')
    aliases = ()
    keywords = ('wheat', 'grain', 'stalk')

    def build(self):
        # Symbol plan: Two mirrored pairs of pointed wheat leaves, regular 20-unit vertical repeat; omit the third pair after its retained-count layout failed the minimum hole size check. Centerline extremes (8,4)-(40,44). Lucide wheat informs repeated leaf symbols; retain source upright symmetry and omit veins.

        def path(name, start, commands, closed=False):
            members=[]
            for i, command in enumerate(commands):
                kind,end,*args=command
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,start,end)
                elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
                members.append(member)
                start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)

        for i,y in enumerate((4,24)):
            for side in (-1,1):
                n=f'leaf-{i}-{side}'
                path(n,(24,y+10),[('C',(24+side*16,y),(24+side*13,y+10),(24+side*16,y+8)),('C',(24,y+10),(24+side*8,y+2),(24+side*3,y+5))],True)
            join(f'leaf-{i}--1',f'leaf-{i}-1')
            line(f'stalk-{i}',(24,y+10),(24,y+30 if i<1 else 44))
            for s in (-1,1): join(f'stalk-{i}',f'leaf-{i}-{s}')
            if i:
                for s in (-1,1): join(f'stalk-{i-1}',f'leaf-{i}-{s}')
