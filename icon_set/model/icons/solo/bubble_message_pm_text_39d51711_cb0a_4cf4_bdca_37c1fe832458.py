from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='39d51711-cb0a-4cf4-bdca-37c1fe832458'
SOURCE_PATH='pictographic-primitives/other/bubble message pm text_39d51711-cb0a-4cf4-bdca-37c1fe832458.svg'
AUTHOR='gpt-6'
PLAN='PM now reuses typeface v2 at 0.8 uniform centerline scale, with4-unit strokes. Restored an oval bubble and reduced lettering to avoid overlap with its outline.'
CONSTRUCTION_REFERENCES='Lucide message-square original and atomic-debug: rounded enclosure and integrated tail; supplied reference governs PM.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='bubble-message-pm-text'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
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
        catalog={'source': 'icon_set/typeface/glyphs-v2.json', 'glyphs': [{'icon_id': 'letter-p-uppercase', 'character': 'P', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [5.0, 2.0, 13.000000000000009, 17.0], 'measurement': 'source-body-band', 'paths': ['M 5.00908,2.00024 L 5.0,17.0', 'M 5.0,2.0 L 8.89593,2.00715 C 9.22987,2.01835 9.54538,2.0379 9.84227,2.06654 C 10.1601,2.11954 10.4702,2.20613 10.8165,2.33873 C 11.1758,2.51916 11.4846,2.71596 11.7996,2.967 C 12.0406,3.20356 12.2839,3.4995 12.493,3.82441 C 12.6216,4.0794 12.7535,4.4386 12.8631,4.83773 C 12.9397,5.24028 12.9841,5.62206 13.0,6.03741 C 12.9817,6.46046 12.9287,6.87417 12.8419,7.26915 C 12.7081,7.68078 12.5639,8.00909 12.3798,8.33697 C 12.1696,8.62889 11.8995,8.93065 11.6458,9.15791 C 11.3645,9.36138 11.0491,9.54295 10.7028,9.69859 C 10.3342,9.82264 9.91922,9.92049 9.53166,9.97652 L 5.00587,10.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': 'd3305af0872bda870a6692ff3612024341dce0628df454e3637afcd8308aa3fd', 'source_path': 'Letters/new/P.svg', 'source_sha256': '3fa844fbf052f501bf91b69ba674e1476fb5dbab24b9d9cdbb2307a167c554cf', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 12.000000000000009, 'ink_height': 19.0, 'ink_left': 3.0, 'ink_top': 0.0, 'centerline_width': 8.000000000000009, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}, {'icon_id': 'letter-m-uppercase', 'character': 'M', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [4.0, 2.00024, 14.0, 17.0002], 'measurement': 'source-body-band', 'paths': ['M 4.0,17.0002 L 4.0,2.00024 L 9.0,10.0002 L 14.0,2.00024 L 14.0,17.0002'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '23f593c7bdd03ae4f2ecefb43ed5ce83dc35ebfe71c23f008a39ecfa574547d3', 'source_path': 'Letters/new/M.svg', 'source_sha256': 'fcd4460d9f304aca9592ffb537bf155ec801117e90d1fa9a6fec595a8d9d9c86', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 14.0, 'ink_height': 18.99996, 'ink_left': 2.0, 'ink_top': 0.00023999999999979593, 'centerline_width': 10.0, 'centerline_height': 14.99996, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}]}
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

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': 'bca1554e798b9048fffe7d1a4268b2b87638ae69ed91647ebb4f8933c9e079dc', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '39d51711-cb0a-4cf4-bdca-37c1fe832458'}
