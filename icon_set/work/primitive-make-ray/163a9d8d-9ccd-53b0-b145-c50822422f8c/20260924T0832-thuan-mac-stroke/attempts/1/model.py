"""Long-haired woman with a center-parted fringe and round lower face, neck, and broad closed bust; retain recognizable hairstyle rather than a circle inside an arch.
Construction: Human user.svg and full_body_ref.png: circular jaw and smooth shoulder curvature; source has an attached anatomical neck.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '163a9d8d-9ccd-53b0-b145-c50822422f8c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bust-long-hair/20260924T083118Z-thuan-mac/reference/woman half_163a9d8d-9ccd-53b0-b145-c50822422f8c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-bust-long-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('woman', 'half')

    def build(self):
        # Symbol plan: Long-haired woman with a center-parted fringe and round lower face, neck, and broad closed bust; retain recognizable hairstyle rather than a circle inside an arch.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('face',(16,18),[('C',(24,13),(20,17),(23,15)),('C',(32,18),(25,15),(28,17)),('A',(24,26),8,8,True),('A',(16,18),8,8,True)],True)
        p('hair',(12,31),[('L',(8,31)),('L',(10,18)),('C',(24,4),(10,9),(16,4)),('C',(38,18),(32,4),(38,9)),('L',(40,31)),('L',(36,31))])
        p('bust',(20,25),[('L',(20,33)),('C',(8,42),(14,35),(8,36)),('L',(8,44)),('L',(40,44)),('L',(40,42)),('C',(28,33),(40,36),(34,35)),('L',(28,25))]);join('bust','face')

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
