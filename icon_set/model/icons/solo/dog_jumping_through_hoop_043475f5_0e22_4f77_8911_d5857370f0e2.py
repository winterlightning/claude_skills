"""Flowing leaping dog silhouette and open vertical hoop; retain directional pose.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '043475f5-0e22-4f77-8911-d5857370f0e2'
SOURCE_PATH = 'pictographic-primitives/pets/dog jump_043475f5-0e22-4f77-8911-d5857370f0e2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='dog-jumping-through-hoop'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'pets'
    categories = ('pets', 'primitives')
    aliases=()
    keywords=('dog jump',)
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
        path('hoop',(14,8),[('A',(4,24),10,16,False),('A',(14,40),10,16,False)])
        path('dog',(4,24),[('L',(30,16)),('L',(34,8)),('L',(38,16)),('L',(44,18)),('A',(38,24),6,6,True),('L',(32,24)),('A',(38,30),6,6,True),('A',(34,34),4,4,True),('L',(26,28)),('L',(18,30)),('A',(12,38),6,8,False)])
        join('hoop','dog')
