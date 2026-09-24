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
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('woman', 'actions')

    def build(self):
        # Symbol plan: Woman portrait with a smooth circular jaw, center-parted fringe, bobbed hair and broad curved shoulders. Preserve the naturally connected neck.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('face',(16,18),[('C',(24,13),(19,17),(22,15)),('C',(32,18),(26,15),(29,17)),('A',(24,26),8,8,True),('A',(16,18),8,8,True)],True)
        p('hair',(12,29),[('C',(8,28),(10,29),(9,29)),('L',(10,18)),('C',(24,4),(10,9),(16,4)),('C',(38,18),(32,4),(38,9)),('L',(40,28)),('C',(36,29),(39,29),(38,29))])
        p('shoulders',(8,44),[('C',(14,35),(8,39),(10,36)),('L',(20,32)),('L',(20,25))])
        p('shoulders-right',(28,25),[('L',(28,32)),('L',(34,35)),('C',(40,44),(38,36),(40,39))])
        join('shoulders','face');join('shoulders-right','face')

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
