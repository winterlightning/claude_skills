"""Smooth mirrored torso sides, a curved upper garment edge and lower waistband around the navel; preserve cropped anatomy without a detached head.
Construction: Human full_body_ref.png and user.svg: coherent anatomy curves; cropped torso has no detached head.
Omissions: Omit the small upper cleavage mark to give the garment breathing room.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4b8d4eae-62c7-4831-876a-5e8fd95eb63b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__slim-waist/20260924T071425Z-thuan-mac/reference/slim waist_4b8d4eae-62c7-4831-876a-5e8fd95eb63b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'slim-waist'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('slim', 'waist')

    def build(self):
        # Symbol plan: Smooth mirrored torso sides, a curved upper garment edge and lower waistband around the navel; preserve cropped anatomy without a detached head.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        for side in (-1,1):
         m=lambda x,y:(24+side*x,y)
         p('upper-'+str(side),m(17,6),[('C',m(12,18),m(18,14),m(17,18))])
         p('waist-'+str(side),m(12,18),[('C',m(13,35),m(8,25),m(9,30)),('C',m(18,42),m(16,38),m(18,40))])
         join('upper-'+str(side),'waist-'+str(side))
        p('top-edge',(12,18),[('C',(24,17),(16,19),(20,17)),('C',(36,18),(28,17),(32,19))])
        p('waistband',(11,35),[('C',(24,37),(15,34),(19,37)),('C',(37,35),(29,37),(33,34))])
        for side in (-1,1):
         join('top-edge','upper-'+str(side));join('top-edge','waist-'+str(side));join('waistband','waist-'+str(side))
        dot('navel',(24,28))

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
