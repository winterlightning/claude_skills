"""Long-haired woman with a center-parted fringe and round lower face, neck, and broad closed bust; retain recognizable hairstyle rather than a circle inside an arch.
Construction: Human user.svg and full_body_ref.png: circular jaw and smooth shoulder curvature; source has an attached anatomical neck.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '163a9d8d-9ccd-53b0-b145-c50822422f8c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__woman-bust-long-hair/20260924T083118Z-thuan-mac/reference/woman half_163a9d8d-9ccd-53b0-b145-c50822422f8c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-bust-long-hair-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('woman', 'half')

    def build(self):
        # Symbol plan: Long-haired woman with a center-parted fringe and round lower face, neck, and broad closed bust; retain recognizable hairstyle rather than a circle inside an arch.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('face',(16,26),[('C',(16,20),(15,24),(16,22)),('C',(24,15),(19,18),(22,17)),('C',(32,20),(26,17),(29,18)),('C',(32,26),(32,22),(33,24)),('A',(30,28),10,10,True),('A',(18,28),10,10,True),('A',(16,26),10,10,True)],True)
        p('hair',(6,28),[('L',(6,20)),('A',(24,6),18,14,True),('A',(42,20),18,14,True),('L',(42,28))])
        p('left-neck',(18,28),[('L',(18,34)),('C',(6,42),(12,36),(6,36))]);join('left-neck','face')
        p('right-neck',(30,28),[('L',(30,34)),('C',(42,42),(36,36),(42,36))]);join('right-neck','face')
        line('base',(6,42),(42,42));join('base','left-neck');join('base','right-neck')

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
