"""Low classic convertible with equal wheels and a single rounded hood; wheel joins occur at explicit cardinal nodes instead of cutting across tires.
Construction: Lucide car: equal circular wheels, split body edges, coherent curved hood.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a2bf7811-1380-54da-8d4f-f8603540fa5a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vintage-convertible/20260924T071425Z-thuan-mac/reference/car convertible_a2bf7811-1380-54da-8d4f-f8603540fa5a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'vintage-convertible'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('car', 'convertible')

    def build(self):
        # Symbol plan: Low classic convertible with equal wheels and a single rounded hood; wheel joins occur at explicit cardinal nodes instead of cutting across tires.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        for n,x in [('rear',12),('front',36)]:oval(n,x,32,6,6)
        p('body',(6,32),[('L',(4,32)),('L',(4,25)),('A',(9,20),5,5,True),('L',(25,20)),('L',(33,20)),('C',(44,32),(39,20),(44,25)),('L',(42,32))])
        line('chassis',(18,32),(30,32))
        for n in ('rear','front'):join('body',n);join('chassis',n)
        p('windscreen',(25,20),[('L',(19,10)),('L',(16,10))]);join('windscreen','body')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            n=f'{name}-{i}'
            if kind=='L': self.add_line(n,start,end)
            elif kind=='A': self.add_arc(n,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(n,start,(args[0],args[1],end))
            members.append(n);start=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def mirror(self,n,start,commands,closed=True):
        axis=24
        m=lambda p:(2*axis-p[0],p[1])
        nodes=[start]+[c[1] for c in commands]
        rev=[]
        for i,c in reversed(list(enumerate(commands))):
            k,end,*args=c
            if k=='C':rev.append((k,m(nodes[i]),m(args[1]),m(args[0])))
            elif k=='A':rev.append((k,m(nodes[i]),*args))
            else:rev.append((k,m(nodes[i])))
        self.path(n,start,commands+rev,closed)
