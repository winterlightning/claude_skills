"""Virtual reality goggles with smooth symmetric frame corners and nose recess.
Plan: Virtual reality goggles with smooth symmetric frame corners and nose recess.
Construction: Lucide glasses rounded frame vocabulary; original provides broad VR visor and side tabs.
Omissions: No concept-bearing detail omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '8a515529-35b3-4547-9b35-3ae486711582'
SOURCE_PATH = 'pictographic-primitives/other/device wearable vr goggles_8a515529-35b3-4547-9b35-3ae486711582.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='virtual-reality-headset-solo'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('virtual', 'reality', 'headset', 'solo')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        path('frame',(4,17),[('L',(8,17)),('L',(8,16)),('A',(16,8),8,8,True),('L',(32,8)),('A',(40,16),8,8,True),('L',(40,17)),('L',(44,17)),('L',(44,31)),('L',(40,31)),('A',(31,40),9,9,True),('L',(30,40)),('C',(24,35),(26,40),(27,35)),('C',(18,40),(21,35),(22,40)),('L',(17,40)),('A',(8,31),9,9,True),('L',(4,31)),('L',(4,17))],True)
