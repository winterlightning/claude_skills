"""Cropped pregnant torso with a smooth protruding belly and a resting bent arm. Shared hand/back attachment; retain natural directional asymmetry.
Construction: Human user.svg and full_body_ref.png: coherent torso and curved limbs. Cropped torso has no head, so no detached-head gap applies.
Omissions: Fingers omitted; preserve the broad resting hand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ce2544a1-dff2-53f8-bb11-5a8ddc78ee9d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/pregnancy pregnant_ce2544a1-dff2-53f8-bb11-5a8ddc78ee9d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-on-pregnant-belly-ce2544a1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ()
    keywords = ('pregnancy', 'pregnant')

    def build(self):
        # Symbol plan: Cropped pregnant torso with a smooth protruding belly and a resting bent arm. Shared hand/back attachment; retain natural directional asymmetry.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('belly',(18,4),[('C',(18,12),(14,7),(14,9)),('C',(8,28),(12,16),(8,21)),('C',(18,40),(8,35),(12,39)),('L',(18,44))])
        p('arm',(30,4),[('C',(26,17),(30,9),(29,13)),('L',(20,23)),('C',(23,31),(15,27),(18,31)),('C',(36,22),(30,31),(34,26))])
        p('back',(40,4),[('C',(36,22),(40,11),(39,17)),('C',(40,44),(36,30),(38,38))]);join('arm','back')

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
