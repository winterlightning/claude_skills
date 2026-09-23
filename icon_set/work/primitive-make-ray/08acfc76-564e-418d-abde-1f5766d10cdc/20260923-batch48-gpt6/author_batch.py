"""Standalone, ordered batch authoring; no registry or build writes."""
from pathlib import Path
import json, importlib.util, traceback
import cairosvg
from PIL import Image, ImageDraw

SOURCE_ICON_ID = '08acfc76-564e-418d-abde-1f5766d10cdc'
SOURCE_PATH = 'icon_set/work/todo-references/square xmark_08acfc76-564e-418d-abde-1f5766d10cdc.svg'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).resolve().parent
ROWS = json.loads((ROOT / 'batch-inputs.json').read_text())

HELPERS = '''
    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rect(self, name, x, y, w, h, r=4):
        # One owning rectangle; four equal tangent corner arcs.
        points = [(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                  (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        members=[]
        for i,p in enumerate(points):
            q=points[(i+1)%8]; n=f'{name}-{i}'
            if i%2: self.add_arc(n,p,q,radius_x=r)
            else: self.add_line(n,p,q)
            members.append(n)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        # Four rays share the true intersection node.
        offsets=[(-r,-r),(r,r),(-r,r),(r,-r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        ids=[]
        for i,(dx,dy) in enumerate(offsets):
            n=f'{name}-{i}';self.add_line(n,(x,y),(x+dx,y+dy));ids.append(n)
        for i,a in enumerate(ids):
            for b in ids[i+1:]: self.relate('connect',a,b)
'''

SPECS = [
('SQUARE','A rounded square containing an X.','Equal square sides and a centered four-ray X.',[],'''
        self.rect('frame',6,6,36,36,6)
        self.cross('x',24,24,8,True)
'''),
('SQUARE','A rounded square containing a horizontal dash.','Centered horizontal mark within a shared rounded-square frame.',[],'''
        self.rect('frame',6,6,36,36,6)
        self.add_line('dash',(16,24),(32,24))
'''),
('SQUARE','A rounded square containing a dash over a small circle.','Vertical mark stack centered on x=24.',[],'''
        self.rect('frame',6,6,36,36,6)
        self.add_line('dash',(16,18),(32,18))
        self.circle('lower-ring',24,30,3)
'''),
('SQUARE','A hand squeezes a phone between inward arrows.','Phone owns its frame; a repeated three-finger grip and paired arrows flank it.',['Four finger lobes reduced to three to allocate an 8-unit pitch.'],'''
        self.rect('phone',14,6,20,36,4)
        for i in range(3):
            self.rect(f'finger-{i}',6,18+i*8,16,8,4)
        self.add_polyline('left-arrow',(6,8),(10,12),(6,16))
        self.add_polyline('right-arrow',(42,8),(38,12),(42,16))
        self.add_polyline('thumb',(34,20),(40,20),(40,30),(42,32))
        self.add_line('wrist',(34,38),(42,42))
'''),
('VRECT_M','A phone with opposed inward-curving squeeze marks.','Tall rounded phone with mirrored curved marks and a lower home bar.',['The smaller nested ripple on each side is omitted to open the central band.'],'''
        self.rect('phone',10,4,28,40,4)
        self.add_arc('left-squeeze',(18,14),(18,26),radius_x=10,sweep=True)
        self.add_arc('right-squeeze',(30,14),(30,26),radius_x=10,sweep=False)
        self.add_line('home-bar',(18,36),(30,36))
'''),
('SQUARE','Scissors beside a partial female-operation symbol.','Two equal finger loops and converging blades; right curved symbol retains its diagonal cross.',[],'''
        for x in (12,26): self.circle(f'loop-{x}',x,36,6)
        self.add_polyline('blade-left',(18,36),(18,22),(20,8),(26,30))
        self.add_line('blade-cut',(18,28),(24,22))
        self.relate('connect','loop-12','blade-left')
        self.relate('connect','loop-26','blade-left')
        self.add_arc('female-arc',(30,14),(34,30),radius_x=10)
        self.add_line('female-shaft',(36,18),(42,12))
        self.cross('female-cross',38,10,4,True)
'''),
('VRECT_L','Five square blocks step downward beside two turning arrows.','Repeated 8-unit cells advance diagonally; arrows repeat at two levels.',[],'''
        # Adjacent cells share edges: emit the union outline plus dividers once.
        self.add_polyline('column',(8,4),(16,4),(16,20),(24,20),(24,36),(32,36),(32,44),(24,44),(24,36),(16,36),(16,20),(8,20),closed=True)
        self.add_line('split-top',(8,12),(16,12))
        self.add_line('split-middle',(16,28),(24,28))
        for name in ('split-top','split-middle'): self.relate('connect',name,'column')
        for i,(x,y) in enumerate(((24,8),(32,24))):
            self.add_arc(f'turn-{i}',(x,y),(x+8,y+8),radius_x=8)
            self.add_polyline(f'arrow-{i}',(x+8,y+8),(x,y+16),(x+8,y+16))
            self.relate('connect',f'turn-{i}',f'arrow-{i}')
'''),
('SQUARE','Three pollen-bearing stamens rise from a rounded base.','Paired outer anthers mirror around one taller central filament.',[],'''
        self.rect('base',14,34,20,8,4)
        for name,x,y in [('left',10,14),('middle',24,10),('right',38,14)]:
            self.circle(name+'-anther',x,y,4)
            self.add_line(name+'-filament',(x,y+4),(24,30))
            self.relate('connect',name+'-anther',name+'-filament')
        self.add_line('stem',(24,30),(24,34))
        for name in ('left','middle','right'):
            self.relate('connect',name+'-filament','stem')
        for a,b in [('left','middle'),('left','right'),('middle','right')]: self.relate('connect',a+'-filament',b+'-filament')
        self.relate('connect','stem','base')
'''),
('HRECT_L','A folded map accompanies a connected four-node learning diagram.','Map folds remain at upper left; one large node connects to a triangular group.',[],'''
        self.add_polyline('map',(4,26),(4,8),(13,12),(22,8),(22,20))
        self.add_line('map-fold',(13,12),(13,23));self.relate('connect','map','map-fold')
        self.circle('root',23,29,6)
        nodes=[('top',37,16,4),('right',41,28,3),('bottom',37,37,3)]
        for name,x,y,r in nodes: self.circle(name,x,y,r)
        self.add_line('upper-link',(27,25),(34,19))
        self.add_line('middle-link',(29,29),(38,28))
        self.add_line('lower-link',(27,33),(34,36))
        self.add_polyline('node-chain',(39,20),(42,25),(40,31),(38,34))
'''),
('SQUARE','A woman with shoulder-length hair and a circular relationship badge.','Circular face, long surrounding hair, smooth shoulders and lower-right badge.',['Neck seam omitted; head and shoulder ink touch at the bust junction.'], 'PORTRAIT_FEMALE'),
('SQUARE','A boy with short hair and a circular relationship badge.','Circular face, short swept hair line, smooth shoulders and lower-right badge.',['Neck seam omitted; head and shoulder ink touch at the bust junction.'], 'PORTRAIT_BOY'),
('SQUARE','A plain-headed man with a circular relationship badge.','Circular head, smooth shoulders and lower-right badge.',['Neck seam omitted; head and shoulder ink touch at the bust junction.'], 'PORTRAIT_MAN'),
('SQUARE','A girl with long hair and a circular relationship badge.','Circular face, long surrounding hair, smooth shoulders and lower-right badge.',['Neck seam omitted; head and shoulder ink touch at the bust junction.'], 'PORTRAIT_FEMALE'),
('CIRCLE','A story button with a circular center and broken outer ring.','Concentric circles; a large outer sweep and isolated upper-left arc.',['Three small upper-left segments reduced to one isolated arc.'],'''
        self.circle('inner',24,24,11)
        self.add_arc('outer-main',(24,4),(4,24),radius_x=20,large_arc=True)
        self.add_arc('outer-dash',(8,12),(12,8),radius_x=20)
'''),
('SQUARE','A circular strainer with a diagonal rounded handle.','Large round bowl with a diagonal capsule handle at lower left.',[],'''
        self.circle('bowl',29,19,13)
        self.add_line('handle-left',(18,26),(7,37))
        self.add_arc('handle-end',(7,37),(13,43),radius_x=4,radius_y=4,sweep=False)
        self.add_line('handle-right',(13,43),(24,32))
        self.add_contour('handle','handle-left','handle-end','handle-right')
'''),
('SQUARE','A standing person beside a location pin and street lines.','Left aligned figure, right pin, two road levels. Head radius 4; torso starts exactly 8 below its lower centerline.',[],'''
        self.circle('head',14,10,4)
        self.add_line('torso',(14,22),(14,32))
        self.add_polyline('arms',(6,30),(6,26),(10,22),(14,22),(18,22),(22,26),(22,30))
        self.add_polyline('legs',(8,42),(14,32),(20,42))
        self.relate('connect','torso','arms');self.relate('connect','torso','legs')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_arc('pin-top',(28,14),(42,14),radius_x=7)
        self.add_polyline('pin-point',(42,14),(35,26),(28,14))
        self.add_contour('pin','pin-top','pin-point-1','pin-point-2',closed=True)
        self.add_dot('pin-hole',(35,13))
        self.add_line('road-near',(28,42),(42,42))
        self.add_line('road-far',(30,34),(40,34))
'''),
('SQUARE','A head in profile contains plus, minus and multiplication signs.','Smooth cranial silhouette, stepped facial profile, three mathematical operators.',[],'''
        self.add_bezier('cranium',(10,20),((10,10),(19,6),(27,6)),((36,6),(42,13),(42,22)),((42,28),(36,30),(36,36)))
        self.add_polyline('neck',(36,36),(36,42))
        self.add_polyline('face',(10,20),(6,29),(10,30),(10,34),(18,34),(18,42))
        self.add_contour('profile','face-6','face-5') if False else None
        self.relate('connect','cranium','face');self.relate('connect','cranium','neck')
        self.cross('plus',23,16,3)
        self.add_line('minus',(18,27),(23,27))
        self.cross('times',32,27,3,True)
'''),
('SQUARE','A rounded speech bubble contains a rising slash.','Rounded rectangular speech body with a deliberate pointed lower-right tail.',[],'''
        self.add_line('top',(12,6),(36,6))
        self.add_arc('tr',(36,6),(42,12),radius_x=6)
        self.add_line('right',(42,12),(42,28))
        self.add_arc('br',(42,28),(36,34),radius_x=6)
        self.add_polyline('tail',(36,34),(36,42),(28,34),(12,34))
        self.add_arc('bl',(12,34),(6,28),radius_x=6)
        self.add_line('left',(6,28),(6,12))
        self.add_arc('tl',(6,12),(12,6),radius_x=6)
        self.add_contour('bubble','top','tr','right','br','tail-1','tail-2','tail-3','bl','left','tl',closed=True)
        self.add_line('slash',(17,25),(31,15))
'''),
]

def portrait(kind):
    body='''
        # human_ref/user.svg: circular head and broad smooth shoulders.
        # Head lower centerline y=26, shoulder apex y=30: touching ink.
        self.circle('head',22,16,10)
        self.add_arc('shoulder-left',(6,42),(22,30),radius_x=16,radius_y=12)
        self.add_bezier('shoulder-right',(22,30),((27,30),(30,31),(32,34)))
        self.add_line('base',(6,42),(26,42))
        self.add_contour('body','shoulder-left','shoulder-right')
        self.relate('connect','head','body')
        self.relate('connect','base','body')
        self.circle('badge',36,36,6)
'''
    if kind=='PORTRAIT_FEMALE':
        body+='''
        self.add_polyline('hair-left',(12,14),(10,27),(15,28))
        self.add_polyline('hair-right',(32,14),(34,27),(29,28))
        self.add_polyline('hair-part',(13,14),(20,13),(25,10),(31,14))
'''
    elif kind=='PORTRAIT_BOY':
        body+='''
        self.add_polyline('hair-part',(13,14),(18,12),(24,14),(30,11))
'''
    return body

def main():
    for i,(row,spec) in enumerate(zip(ROWS,SPECS)):
        out=Path(row['result_dir'])
        if (out/'result.json').exists(): continue
        key,subject,plan,omissions,body=spec
        is_portrait=body.startswith('PORTRAIT')
        if is_portrait: body=portrait(body)
        refs=['supplied reference SVG']
        if i in (0,1,2,3,4): refs+=['lucide/original/square-x.svg and atomic-debug/square-x.svg: equal corner radii and centered marks']
        if is_portrait or i==15: refs+=['human_ref/user.svg and human_ref/full_body_ref.png: circular heads and smooth shoulders or limbs']
        if i==15: refs+=['lucide/original/map-pin.svg and atomic-debug/map-pin.svg: rounded crown and pointed base']
        if i==17: refs+=['lucide/original/message-square.svg and atomic-debug/message-square.svg: rounded frame and integrated tail']
        if len(refs)==1: refs+=['No useful local Lucide subject match used; shared geometric construction principles applied.']
        module_name=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
        code=f'''"""{subject}
Plan: {plan}
Keyshape: {key}; extrema follow the profile contract.
References: {'; '.join(refs)}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
'''+("    human_construction = 'bust'\n" if is_portrait else '')+HELPERS+'\n    def build(self):\n'+body
        (out/module_name).write_text(code)
        findings=dict(row,keyshape=key,subject=subject,construction_plan=plan,omissions=omissions,references=refs,python=module_name)
        try:
            spec_mod=importlib.util.spec_from_file_location(f'batch48_{i}',out/module_name)
            mod=importlib.util.module_from_spec(spec_mod);spec_mod.loader.exec_module(mod)
            icon=mod.Drawing(); report=icon.validate_icon()
            findings['validation_status']=report.status
            (out/'validation.txt').write_text(report.describe())
            svg=icon.to_svg();(out/(row['icon_id']+'.svg')).write_text(svg)
            for size in (48,192):
                raw=cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)
                import io
                alpha=Image.open(io.BytesIO(raw)).convert('RGBA').getchannel('A')
                for theme,bg,ink in [('light','white','black'),('dark','#16191d','#f4f5f6')]:
                    im=Image.new('RGB',(size,size),bg);im.paste(ink,(0,0,size,size),alpha);im.save(out/f'{theme}-{size}.png')
        except Exception:
            findings['validation_status']='error';findings['error']=traceback.format_exc()
            (out/'validation.txt').write_text(findings['error'])
        (out/'attempt-findings.json').write_text(json.dumps(findings,indent=2))
        print(i+1,row['concept'],findings['validation_status'],flush=True)
    sheet=Image.new('RGB',(1080,6*270),'#dadde0');d=ImageDraw.Draw(sheet)
    for i,row in enumerate(ROWS):
        out=Path(row['result_dir']);x=(i%3)*360;y=(i//3)*270
        d.text((x+4,y+4),f"{i+1}. {row['concept'][:32]}",fill='black')
        for j,theme in enumerate(('light','dark')):
            p=out/f'{theme}-192.png'
            if p.exists():
                im=Image.open(p).resize((160,160));sheet.paste(im,(x+j*180,y+26))
                sheet.paste(Image.open(out/f'{theme}-48.png'),(x+j*180+56,y+198))
    sheet.save(ROOT/'authored-review.png')

if __name__=='__main__': main()
