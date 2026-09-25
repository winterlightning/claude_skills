from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='39d51711-cb0a-4cf4-bdca-37c1fe832458'
SOURCE_PATH='pictographic-primitives/other/bubble message pm text_39d51711-cb0a-4cf4-bdca-37c1fe832458.svg'
AUTHOR='gpt-6'
PLAN='PM now reuses typeface v2 at 0.8 uniform centerline scale, with4-unit strokes. Restored an oval bubble and reduced lettering to avoid overlap with its outline.'
CONSTRUCTION_REFERENCES='Lucide message-square original and atomic-debug: rounded enclosure and integrated tail; supplied reference governs PM.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='private-message-bubble'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('bubble', 'message', 'pm', 'text')

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
        self.path('bubble',(4,22),[('C',(24,8),(4,14),(13,8)),('C',(44,22),(35,8),(44,14)),('C',(24,36),(44,30),(35,36)),('L',(17,35)),('L',(4,40)),('L',(8,31)),('C',(4,22),(5,28),(4,25))],True)
        self.typeface_v2('PM',0.8,2,24,22)

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'PM now reuses typeface v2 at 0.8 uniform centerline scale, with4-unit strokes. Restored an oval bubble and reduced lettering to avoid overlap with its outline.', 'scope': ['typeface-v2 fractional coordinates', 'glyph internal and external spacing', 'text/bubble clearance'], 'svg_sha256': '4af48930c20b583c1f83ee935a0318ae6e1a604575c0c1dab0cfdb3b21014afb', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}
