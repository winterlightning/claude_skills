"""Stressed person with a jagged open head and a detached broad shoulder arch.
Symbol plan: shared parameters and coherent contours.
Construction: human_ref/user.svg: broad shoulders and detached head.
Omissions: Peripheral stress rays and center shirt mark removed to preserve clear head and body.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a909b542-9eea-596a-b3f1-76f310afb7f5'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__person-with-jagged-open-head/20260924T065933Z-thuan-mac/reference/human resources employee stress_a909b542-9eea-596a-b3f1-76f310afb7f5.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='person-with-jagged-open-head'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('person', 'with', 'jagged', 'open', 'head')

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
        # Open cranium zigzag retained; smooth semicircular jaw; body apex36 minus jaw28=8.
        self.path('head',(14,18),[('L',(14,16)),('L',(14,4)),('L',(19,9)),('L',(24,4)),('L',(29,9)),('L',(34,4)),('L',(34,16)),('L',(34,18)),('A',(14,18),10,10,True)],True)
        self.add_line('opening',(14,16),(34,16));self.relate('connect','opening','head')
        self.path('shoulders',(8,44),[('A',(40,44),16,8,True)])
