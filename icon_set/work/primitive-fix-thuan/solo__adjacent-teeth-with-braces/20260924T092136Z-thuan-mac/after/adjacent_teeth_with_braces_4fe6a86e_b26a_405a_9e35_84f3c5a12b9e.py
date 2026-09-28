"""Two adjacent molars with two square brace brackets and a horizontal wire. Shared mirrored tooth shape; bounds4,8 to44,40.
Construction reference: No useful local Lucide tooth match; repeated mirrored molars.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4fe6a86e-b26a-405a-9e35-84f3c5a12b9e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__adjacent-teeth-with-braces/20260924T092136Z-thuan-mac/reference/dental brace_4fe6a86e-b26a-405a-9e35-84f3c5a12b9e.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'adjacent-teeth-with-braces'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/other'
    aliases = ()
    keywords = ('dental', 'brace')
    def build(self):
        for i,x in enumerate((4,26)):
            n='tooth-'+str(i)
            self.path(n,(x,18),[('C',(x+18,18),(x,5),(x+18,5)),('C',(x+16,40),(x+18,28),(x+18,40)),('C',(x+9,32),(x+12,40),(x+13,32)),('C',(x+2,40),(x+5,32),(x+6,40)),('C',(x,18),(x,40),(x,27))],True)
            self.add_polyline('bracket-'+str(i),(x+5,17),(x+13,17),(x+13,25),(x+5,25),closed=True)
        self.add_line('wire',(4,21),(44,21))

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
