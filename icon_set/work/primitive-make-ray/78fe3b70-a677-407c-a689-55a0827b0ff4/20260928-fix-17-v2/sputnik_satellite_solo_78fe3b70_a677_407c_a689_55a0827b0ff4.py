"""Rejected Sputnik sphere dominates while rods are shortened and steepened. Restore smaller spherical body and three long, unequal antenna rods at original angles.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: satellite. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '78fe3b70-a677-407c-a689-55a0827b0ff4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sputnik-satellite-solo/20260928T165531Z-thuan-mac/reference/sputnik_78fe3b70-a677-407c-a689-55a0827b0ff4.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'sputnik-satellite-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('sputnik',)
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('sphere',(29,4),[('A',(42,17),13,True),('A',(41,22),13,True),('A',(29,30),13,True),('A',(17,22),13,True),('A',(16,17),13,True),('A',(24,5),13,True),('A',(29,4),13,True)],closed=True)
        for n,a,b in [('upper',(4,11),(24,5)),('lower-left',(4,44),(17,22)),('lower-right',(36,44),(41,22))]:
            line(n,a,b);join(n,'sphere')


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

