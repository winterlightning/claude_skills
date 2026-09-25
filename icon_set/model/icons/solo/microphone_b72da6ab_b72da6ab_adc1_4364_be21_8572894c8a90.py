"""Microphone capsule with a smooth semicircular cradle and short stem.
Symbol plan: shared parameters and coherent contours.
Construction: mic: capsule and concentric cradle.
Omissions: Small grille notch removed because it crowds the capsule opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b72da6ab-adc1-4364-be21-8572894c8a90'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__microphone-b72da6ab/20260924T065933Z-thuan-mac/reference/microphone_b72da6ab-adc1-4364-be21-8572894c8a90.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='microphone-b72da6ab-solo'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "audio"
    aliases=()
    keywords=('microphone', 'b72da6ab')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        self.path('capsule',(18,10),[('A',(30,10),6,6,True),('L',(30,20)),('A',(18,20),6,6,True),('L',(18,10))],True)
        self.path('cradle',(8,22),[('L',(8,24)),('A',(24,40),16,16,False),('A',(40,24),16,16,False),('L',(40,22))])
        self.add_line('stem',(24,40),(24,44));self.relate('connect','stem','cradle')
