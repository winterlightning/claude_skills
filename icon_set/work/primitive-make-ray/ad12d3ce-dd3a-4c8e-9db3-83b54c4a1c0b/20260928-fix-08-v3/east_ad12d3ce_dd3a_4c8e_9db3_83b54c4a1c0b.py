"""Rejected E is displaced left and the needle merges with the rim. Center E below the dial and restore an independent northeast compass pointer.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: compass. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__east/20260928T165531Z-thuan-mac/reference/east_ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'east'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('east',)
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        circle('dial',24,15,13)
        poly('needle',(18,15),(29,10),(25,22),closed=True)
        poly('e',(29,34),(19,34),(19,39),(19,44),(29,44))
        line('e-middle',(19,39),(27,39));join('e','e-middle')


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

