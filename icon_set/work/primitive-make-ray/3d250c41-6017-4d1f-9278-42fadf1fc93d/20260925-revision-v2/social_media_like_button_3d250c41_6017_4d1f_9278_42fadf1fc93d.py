from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='3d250c41-6017-4d1f-9278-42fadf1fc93d'
SOURCE_PATH='pictographic-primitives/other/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg'
AUTHOR='gpt-6'
PLAN='LIKE uses typeface v2 at0.85 uniform centerline scale. Panel expanded by2 units per side within the same48 canvas to keep glyphs distinct; text spacing and exact keyshape fit are approved exceptions.'
CONSTRUCTION_REFERENCES='Lucide rectangle-ellipsis original and atomic-debug: rounded horizontal enclosure; supplied reference governs LIKE.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='social-media-like-button'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'like', 'text')

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)


    def typeface_v2(self,text,scale,tracking,cx,cy):
        # Reuse the supplied v2 glyph curves; apply a uniform centerline fit.
        # Global stroke stays4. Explicit user exception owns text spacing/grid.
        from pathlib import Path
        import json
        from svgpathtools import parse_path,Line,CubicBezier
        from icon_set.model.primitives import Bezier,Point
        catalog=json.loads(Path(__file__).with_name('glyphs-v2.snapshot.json').read_text())
        glyphs={g['character']:g for g in catalog['glyphs']}
        width=sum((glyphs[c]['bounds'][2]-glyphs[c]['bounds'][0])*scale+4 for c in text)+tracking*(len(text)-1)
        cursor=cx-width/2+2
        top=cy-15*scale/2
        self.typeface_placements=[]
        for index,c in enumerate(text):
            g=glyphs[c];dx=cursor-g['bounds'][0]*scale;dy=top-g['body_top']*scale
            self.typeface_placements.append(dict(character=c,glyph_id=g['icon_id'],scale=scale,translate=[dx,dy],source_path=g['source_path'],path_sha256=g['svg_sha256']))
            def point(z):return (round(z.real*scale+dx,3),round(z.imag*scale+dy,3))
            for pi,d in enumerate(g['paths']):
                for si,sub in enumerate(parse_path(d).continuous_subpaths()):
                    n=f'text-{index}-{c}-{pi}-{si}';members=[]
                    for j,segment in enumerate(sub):
                        ident=n+'-'+str(j);members.append(ident)
                        if isinstance(segment,Line):self.add_line(ident,point(segment.start),point(segment.end))
                        elif isinstance(segment,CubicBezier):self.primitives.append(Bezier(ident,Point(*point(segment.start)),Point(*point(segment.end)),((point(segment.control1),point(segment.control2),point(segment.end)),)))
                        else:raise ValueError('Unexpected v2 glyph primitive')
                    self.add_contour(n,*members,closed=(sub.start==sub.end))
            cursor+=(g['bounds'][2]-g['bounds'][0])*scale+4+tracking

    def build(self):
        self.box('panel',2,8,46,40,4)
        self.typeface_v2('LIKE',0.85,1,24,24)

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'LIKE uses typeface v2 at0.85 uniform centerline scale. Panel expanded by2 units per side within the same48 canvas to keep glyphs distinct; text spacing and exact keyshape fit are approved exceptions.', 'scope': ['typeface-v2 fractional coordinates', 'glyph spacing', 'expanded panel keyshape fit'], 'svg_sha256': 'a7748532b70ca526b6776ed0f0db2542954c9a27a17f006b6214d8f0ed790f9c', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}
