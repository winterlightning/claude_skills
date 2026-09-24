"""Diagonal pipette with rounded bulb, straight crossbar and shaped nozzle. Parallel shaft edges share diagonal direction; square envelope6,6 to42,42.
Construction reference: Lucide pipette: continuous nozzle with diagonal collar.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ba14a04-c8da-5278-9772-abe74358faf2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broad-diagonal-eyedropper-with-crossbar/20260924T092136Z-thuan-mac/reference/color picker_8ba14a04-c8da-5278-9772-abe74358faf2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'broad-diagonal-eyedropper-with-crossbar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('color', 'picker')
    def build(self):
        self.path('outline',(6,42),[('C',(10,30),(11,37),(8,34)),('L',(21,19)),('L',(32,8)),('C',(36,6),(33,7),(34,6)),('A',(42,12),6,6,True),('C',(40,18),(42,14),(42,16)),('L',(31,27)),('L',(21,37)),('C',(6,42),(17,41),(12,37))],True)
        self.add_polyline('collar',(16,15),(21,19),(31,27),(36,31))
        self.relate('connect','collar','outline')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
