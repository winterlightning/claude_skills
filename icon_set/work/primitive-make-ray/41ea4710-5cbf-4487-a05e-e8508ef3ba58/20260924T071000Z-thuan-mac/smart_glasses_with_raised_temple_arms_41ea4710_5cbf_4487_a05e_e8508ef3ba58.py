"""Broad smart-glasses frame with mirrored smooth raised temples.
Symbol plan: shared parameters and coherent contours.
Construction: glasses: mirrored temples and nose bridge.
Omissions: None
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='41ea4710-5cbf-4487-a05e-e8508ef3ba58'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__smart-glasses-with-raised-temple-arms/20260924T065933Z-thuan-mac/reference/google glass_41ea4710-5cbf-4487-a05e-e8508ef3ba58.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='smart-glasses-with-raised-temple-arms'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('smart', 'glasses', 'with', 'raised', 'temple', 'arms')

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
        self.path('frame',(4,24),[('L',(44,24)),('L',(44,36)),('A',(40,40),4,4,True),('L',(32,40)),('A',(28,36),4,4,True),('A',(20,36),4,4,False),('A',(16,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,24))],True)
        # The long elliptical shoulder ends with a horizontal tangent at each tip.
        for i in range(2):
            def q(x,y):return (x if i==0 else 48-x,y)
            self.path('temple-'+str(i),q(4,24),[('A',q(14,8),10,16,i==0),('L',q(16,8))])
            self.relate('connect','temple-'+str(i),'frame')
