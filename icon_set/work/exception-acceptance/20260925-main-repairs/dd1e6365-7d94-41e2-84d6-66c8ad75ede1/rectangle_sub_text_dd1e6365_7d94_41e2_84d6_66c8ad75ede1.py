from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='dd1e6365-7d94-41e2-84d6-66c8ad75ede1'
SOURCE_PATH='pictographic-primitives/other/rectangle sub text_dd1e6365-7d94-41e2-84d6-66c8ad75ede1.svg'
AUTHOR='gpt-6'
PLAN='SUB uses typeface v2 at0.9 uniform centerline scale. Rounded panel expanded by2 units per side within the48 canvas. Original v2 bowls and letter shapes replace the handmade lettering.'
CONSTRUCTION_REFERENCES='Lucide rectangle-ellipsis original and atomic-debug: rounded panel; supplied reference governs SUB.'
OMISSIONS=[]
class Drawing(Solo48):
    icon_id='rectangle-sub-text'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'sub', 'text')

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
        catalog={'source': 'icon_set/typeface/glyphs-v2.json', 'glyphs': [{'icon_id': 'letter-s-uppercase', 'character': 'S', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [5.0, 2.0, 13.0, 17.0], 'measurement': 'source-body-band', 'paths': ['M 13.0,2.0 L 9.0,2.0 C 5.5941,2.0 4.37177,6.0 7.0,8.0 L 11.0,11.0 C 14.1534,13.0 13.1174,17.0 9.0,17.0 L 5.0,17.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': 'a089fe0102693dac859db0bcb1b919ba77dcac3c53f73c5a04c2932106fc44b6', 'source_path': 'Letters/new/S.svg', 'source_sha256': 'acd1c93e00de9f45ed308e91cc7c28fc83a58e92142446e9eaf8901f0bf2e85b', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 12.0, 'ink_height': 19.0, 'ink_left': 3.0, 'ink_top': 0.0, 'centerline_width': 8.0, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}, {'icon_id': 'letter-u-uppercase', 'character': 'U', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [5.0, 2.0, 13.0002, 17.0], 'measurement': 'source-body-band', 'paths': ['M 13.0002,2.0 L 13.0002,14.0 C 13.0002,14.0 13.0,17.0 8.99998,17.0 C 5.0,17.0 5.0,14.0 5.0,14.0 L 5.0,2.0'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': '9590f0af9d63c209a9c5a42ee65f826585b003c23e75a460a5dbd565c69d163d', 'source_path': 'Letters/new/U.svg', 'source_sha256': '5e31591f7d1fd564afb26b84b4be21b089035d1584afc493accd93725bcc7ece', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 12.0002, 'ink_height': 19.0, 'ink_left': 3.0, 'ink_top': 0.0, 'centerline_width': 8.0002, 'centerline_height': 15.0, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}, {'icon_id': 'letter-b-uppercase', 'character': 'B', 'kind': 'uppercase', 'preferred': True, 'body_top': 2, 'baseline': 17.0, 'body_height': 15.0, 'bounds': [5.0, 2.0, 13.000000000000004, 17.000100000000014], 'measurement': 'source-body-band', 'paths': ['M 5.0,2.0 L 8.14474,2.0 C 10.1398,2.0 11.7571,3.61729 11.7571,5.61233 L 11.7571,5.88768 C 11.7571,7.88271 10.1402,9.0 8.14519,9.0 L 5.00045,9.0 L 5.0,2.0', 'M 5.0009,9.00952 L 9.38812,9.00952 C 11.3832,9.00952 13.0,11.1268 13.0,13.1218 L 13.0,13.3878 C 13.0,15.3828 11.3827,17.0001 9.38767,17.0001 L 5.00045,17.0001 L 5.0009,9.00952'], 'preview_box': [0.0, 0.0, 19.0, 19.0], 'svg_sha256': 'e7880d8091633d137b88aa3bd8cc344c8eff9b93055c79342cfa38afb9bad796', 'source_path': 'Letters/new/B.svg', 'source_sha256': '459dee3ba1fa8c01dd81bd14154b0b83fd3e63a435051cce7f692caa977a0c5d', 'author': 'user-supplied', 'geometry_policy': 'source-native-20', 'construction': 'source centerlines and native canvas used unchanged', 'stroke_width': 4, 'ink_width': 12.000000000000004, 'ink_height': 19.000100000000014, 'ink_left': 3.0, 'ink_top': 0.0, 'centerline_width': 8.000000000000004, 'centerline_height': 15.000100000000014, 'canvas_width': 19.0, 'canvas_height': 19.0, 'centerline_band_height': 15.0}]}
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
        self.typeface_v2('SUB',0.9,1,24,24)

USER_APPROVED_EXCEPTION = {'approved_by': 'user', 'approved_on': '2026-09-25', 'source_request': 'user-account-lock and car look bad, revise please, for cases related with text, use typeface v2 to fix it, we can make its as exception that the text not necesary to be have distance 4 unit, other unresolve could make as eception, global could use v-rect to amke passport bigger', 'reason': 'SUB uses typeface v2 at0.9 uniform centerline scale. Rounded panel expanded by2 units per side within the48 canvas. Original v2 bowls and letter shapes replace the handmade lettering.', 'scope': ['typeface-v2 fractional coordinates', 'glyph spacing', 'expanded panel keyshape fit'], 'svg_sha256': 'b222c1615dfe572bb2920bf8a3fd95a7c8c6e320b874db70bf67cdd63a5e0175', 'recording': 'local SOLO48 approval; automatic QA is retained unchanged'}

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '7852bda8941796f56f38991edadc3fcd39ef443a0856120d21679798c0be9409', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': 'dd1e6365-7d94-41e2-84d6-66c8ad75ede1'}
