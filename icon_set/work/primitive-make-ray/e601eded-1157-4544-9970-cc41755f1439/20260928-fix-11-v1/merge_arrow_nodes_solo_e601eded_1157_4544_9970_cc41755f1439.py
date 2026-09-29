"""Rejected alternate merge also has tiny node openings and an unbalanced loop. Restore three clear circular nodes, a diagonal merge arrow and a smooth lower-right sweep.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: merge. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e601eded-1157-4544-9970-cc41755f1439'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__merge-arrow-nodes-solo/20260928T165531Z-thuan-mac/reference/internet of thing green grass_e601eded-1157-4544-9970-cc41755f1439.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'merge-arrow-nodes-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('internet', 'of', 'thing', 'green', 'grass')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        circle('source',9,9,5)
        circle('upper-node',39,9,5)
        circle('lower-node',9,33,5)
        line('inward',(13,13),(30,30));join('source','inward')
        poly('head',(21,30),(30,30),(30,21));join('inward','head')
        path('sweep',(43,12),[('C',(44,30),(47,18),(47,25)),('C',(25,44),(41,39),(34,44)),('C',(12,37),(19,44),(14,40))])
        join('sweep','upper-node');join('sweep','lower-node')


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

