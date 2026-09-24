"""Woman portrait with a smooth circular jaw, center-parted fringe, bobbed hair and broad curved shoulders. Preserve the naturally connected neck.
Construction: Human user.svg and full_body_ref.png: rounded jaw and paired shoulders, with natural continuous neck from the source.
Omissions: No facial microdetail; hair tips separated from the shoulders.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '502e497c-5b3c-40a4-a052-442908922554'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bust/20260924T083118Z-thuan-mac/reference/woman actions_502e497c-5b3c-40a4-a052-442908922554.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-bust'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('woman', 'actions')

    def build(self):
        # Symbol plan: Woman portrait with a smooth circular jaw, center-parted fringe, bobbed hair and broad curved shoulders. Preserve the naturally connected neck.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('face',(14,20),[('C',(24,16),(18,19),(22,17)),('C',(34,20),(26,17),(30,19)),('A',(30,28),10,10,True),('A',(18,28),10,10,True),('A',(14,20),10,10,True)],True)
        p('hair',(6,26),[('L',(6,16)),('A',(24,6),18,10,True),('A',(42,16),18,10,True),('L',(42,26))])
        p('left-neck',(18,28),[('L',(18,34)),('C',(6,42),(12,36),(6,36))]);join('left-neck','face')
        p('right-neck',(30,28),[('L',(30,34)),('C',(42,42),(36,36),(42,36))]);join('right-neck','face')

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
