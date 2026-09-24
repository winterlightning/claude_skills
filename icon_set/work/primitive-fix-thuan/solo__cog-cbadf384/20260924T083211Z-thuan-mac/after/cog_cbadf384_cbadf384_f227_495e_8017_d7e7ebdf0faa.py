"""Six-tooth cog with smoothly concave roots and one round hub opening. Repeated mirrored tooth geometry avoids the rejected uneven gear lobes; no useful exact Lucide match."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cbadf384-f227-495e-8017-d7e7ebdf0faa'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__cog-cbadf384/20260924T083211Z-thuan-mac/reference/cog_cbadf384-f227-495e-8017-d7e7ebdf0faa.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='cog-cbadf384'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Six-tooth cog with smoothly concave roots and one round hub opening. Repeated mirrored tooth geometry avoids the rejected uneven gear lobes; no useful exact Lucide match.

        def path(n,start,commands,closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                m=f'{n}-{i}'
                if kind=='L': self.add_line(m,start,end)
                elif kind=='A': self.add_arc(m,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,start,(args[0],args[1],end))
                members.append(m);start=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry=None):
            ry=rx if ry is None else ry
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        right=[('L',(26,4)),('C',(29,11),(28,4),(27,9)),('C',(38,11),(32,13),(35,12)),('L',(40,17)),('C',(36,24),(36,20),(36,21)),('C',(40,31),(36,27),(37,28)),('L',(38,37)),('C',(29,37),(35,36),(32,35)),('C',(26,44),(27,39),(28,44)),('L',(24,44))]
        parts=[];a=(24,4)
        for k,b,*args in right:parts.append((k,a,b,args));a=b
        left=[]
        for k,a,b,args in reversed(parts):
         if k=='C':left.append((k,(48-a[0],a[1]),(48-args[1][0],args[1][1]),(48-args[0][0],args[0][1])))
         else:left.append((k,(48-a[0],a[1])))
        path('gear',(24,4),right+left,True);oval('hub',24,24,3)
