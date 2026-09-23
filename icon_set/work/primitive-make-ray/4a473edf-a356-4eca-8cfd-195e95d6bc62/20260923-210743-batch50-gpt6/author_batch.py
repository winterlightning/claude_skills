"""Ordered standalone authoring for the exact nineteen batch-50 references."""
from pathlib import Path
import importlib.util, json, io, traceback
import cairosvg
from PIL import Image, ImageDraw

SOURCE_ICON_ID = '4a473edf-a356-4eca-8cfd-195e95d6bc62'
SOURCE_PATH = 'icon_set/work/todo-references/team approve disapprove_4a473edf-a356-4eca-8cfd-195e95d6bc62.svg'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).resolve().parent
ROWS = json.loads((ROOT/'batch-inputs.json').read_text())

HELPERS = '''
    def path(self, name, start, operations, closed=False):
        # A coherent path owns its members exactly once.
        current=start; members=[]
        for i,op in enumerate(operations):
            n=f'{name}-{i}'
            if op[0]=='L':
                end=op[1]; self.add_line(n,current,end)
            elif op[0]=='A':
                end,rx,ry,sweep=op[1:]; self.add_arc(n,current,end,radius_x=rx,radius_y=ry,sweep=sweep)
            else:
                c1,c2,end=op[1:]; self.add_bezier(n,current,(c1,c2,end))
            members.append(n);current=end
        if closed and current!=start:
            n=f'{name}-close';self.add_line(n,current,start);members.append(n)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def rect(self,name,x,y,w,h,r=4,split_x=(),split_y=()):
        ops=[]
        for xx in sorted(v for v in split_x if x+r<v<x+w-r): ops.append(('L',(xx,y)))
        ops += [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True)]
        for yy in sorted(v for v in split_y if y+r<v<y+h-r): ops.append(('L',(x+w,yy)))
        ops += [('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True)]
        for xx in sorted((v for v in split_x if x+r<v<x+w-r),reverse=True): ops.append(('L',(xx,y+h)))
        ops += [('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True)]
        for yy in sorted((v for v in split_y if y+r<v<y+h-r),reverse=True): ops.append(('L',(x,yy)))
        ops += [('L',(x,y+r)),('A',(x+r,y),r,r,True)]
        # Capsules can have zero-length straight runs; omit those.
        cleaned=[];p=(x+r,y)
        for op in ops:
            if op[0]!='L' or op[1]!=p: cleaned.append(op)
            p=op[1]
        self.path(name,(x+r,y),cleaned,True)

    def join(self,*names):
        for i,a in enumerate(names):
            for b in names[i+1:]: self.relate('connect',a,b)

    def cross(self,name,x,y,r,diagonal=False):
        offsets=[(-r,-r),(r,r),(-r,r),(r,-r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        names=[]
        for i,(dx,dy) in enumerate(offsets):
            n=f'{name}-{i}';self.add_line(n,(x,y),(x+dx,y+dy));names.append(n)
        self.join(*names)

    def letter_a(self,name,apex,left,right,bar_left,bar_right):
        self.add_polyline(name,left,bar_left,apex,bar_right,right)
        self.add_line(name+'-bar',bar_left,bar_right)
        self.join(name,name+'-bar')
'''

# keyshape, subject, owning construction plan, omissions, construction reference, body
SPECS = [
('SQUARE','Two people receive approval and disapproval in speech bubbles.',
 'Two repeated busts and mirrored bubble frames; the check and X remain distinct.',[], 'human;message', '''
        axis=24
        for i,x in enumerate((14,34)):
            self.path(f'bubble-{i}',(x-8,6),[('L',(x+8,6)),('L',(x+8,18)),('L',(x+3,18)),('L',(x,22)),('L',(x-3,18)),('L',(x-8,18))],True)
            self.circle(f'head-{i}',x,29,3)
            self.add_bezier(f'shoulders-{i}',(x-8,42),((x-6,40),(x-3,40),(x,40)),((x+3,40),(x+6,40),(x+8,42)))
        self.add_polyline('approve',(10,12),(13,15),(18,10))
        self.cross('disapprove',34,12,3,True)
'''),
('SQUARE','Two people face off above a game controller.',
 'Identical head and shoulder definitions flank a centered controller.',[], 'human', '''
        for i,x in enumerate((13,35)):
            self.circle(f'head-{i}',x,11,5)
            # Head lower y16, shoulder apex y24: exact detached 4-unit ink gap.
            self.path(f'body-{i}',(x-7,31),[('A',(x,24),7,7,True),('A',(x+7,31),7,7,True)])
        self.path('controller',(18,32),[('L',(30,32)),('C',(33,32),(33,34),(34,37)),('L',(36,40)),('C',(36,43),(32,42),(30,39)),('L',(18,39)),('C',(16,42),(12,43),(12,40)),('L',(14,35)),('C',(15,32),(16,32),(18,32))],True)
        self.add_polyline('controller-v',(21,34),(24,38),(27,34))
'''),
('SQUARE','A raised index finger selects a floating cube.',
 'Isometric cube at upper left; one coherent pointing-hand silhouette at lower right.',[], 'hand', '''
        self.add_polyline('cube-top',(6,12),(18,6),(30,12),(18,18),(6,12))
        self.add_polyline('cube-left',(6,12),(6,24),(18,30),(18,18))
        self.add_line('cube-right',(30,12),(30,18))
        self.add_line('cube-bottom',(18,30),(22,28))
        self.join('cube-top','cube-left');self.join('cube-top','cube-right');self.join('cube-left','cube-bottom')
        self.path('hand',(24,42),[('L',(19,35)),('C',(17,31),(21,29),(24,32)),('L',(28,36)),('L',(28,24)),('A',(36,24),4,4,True),('L',(36,32)),('L',(38,32)),('A',(42,36),4,4,True),('L',(42,42))])
'''),
('SQUARE','An open hand with a palm mark sits beside a microchip.',
 'Three tall fingertips and a thumb form one outline; the chip owns an evenly spaced pin series.',[], 'hand', '''
        self.path('hand',(6,42),[('L',(6,14)),('A',(12,14),3,3,True),('L',(12,9)),('A',(18,9),3,3,True),('L',(18,13)),('A',(24,13),3,3,True),('L',(24,22)),('A',(30,22),3,3,True),('L',(30,29)),('C',(30,34),(22,35),(22,39)),('L',(22,42))])
        self.add_line('finger-division-left',(12,14),(12,22));self.join('hand','finger-division-left')
        self.add_line('finger-division-right',(18,13),(18,22));self.join('hand','finger-division-right')
        self.path('palm-mark',(15,26),[('C',(11,30),(11,32),(15,36)),('C',(19,32),(19,30),(15,26))],True)
        self.rect('chip',32,28,8,8,1,split_x=(34,38),split_y=(30,34))
        for i,p in enumerate((34,38)):
            for name,a,b in [(f'pin-top-{i}',(p,26),(p,28)),(f'pin-bottom-{i}',(p,36),(p,38))]:
                self.add_line(name,a,b);self.join('chip',name)
        for i,p in enumerate((30,34)):
            for name,a,b in [(f'pin-left-{i}',(30,p),(32,p)),(f'pin-right-{i}',(40,p),(42,p))]:
                self.add_line(name,a,b);self.join('chip',name)
'''),
('SQUARE','A television has a rounded inset screen and two short splayed feet.',
 'Nested rounded rectangles share an axis; split bottom frame nodes own the feet.',
 ['Two small control dashes omitted because a second detail row cannot retain the required screen-to-case clearance.'], 'tv', '''
        self.rect('case',6,6,36,32,4,split_x=(14,34))
        self.rect('screen',15,15,18,14,3)
        for name,a,b in [('foot-left',(14,38),(12,42)),('foot-right',(34,38),(36,42))]:
            self.add_line(name,a,b);self.join('case',name)
'''),
('VRECT_L','A two-leaf plant grows inside a house-shaped terrarium.',
 'A pointed enclosure owns a lower soil band; paired lens leaves attach to a central stem.',[], 'leaf', '''
        self.path('glass',(24,4),[('L',(40,16)),('L',(40,36)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,36)),('L',(8,16))],True)
        self.add_polyline('soil',(8,36),(24,36),(40,36));self.join('glass','soil')
        self.add_polyline('stem',(24,36),(24,28),(24,24));self.join('stem','soil')
        self.path('leaf-left',(24,28),[('A',(16,20),8,8,True),('A',(24,28),8,8,True)],True)
        self.path('leaf-right',(24,24),[('A',(32,16),8,8,False),('A',(24,24),8,8,False)],True)
        self.join('stem','leaf-left');self.join('stem','leaf-right')
'''),
('VRECT_L','A clipped-corner test sheet contains A and B answer rows.',
 'One page outline encloses two hand-authored letters and repeated answer rules.',[], 'file', '''
        self.path('page',(12,4),[('L',(30,4)),('L',(40,14)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.letter_a('a',(20,14),(16,24),(24,24),(18,19),(22,19))
        self.path('b',(16,38),[('L',(16,33)),('L',(16,28)),('L',(19,28)),('C',(25,28),(25,33),(19,33)),('L',(16,33))])
        self.path('b-lower',(16,33),[('L',(19,33)),('C',(25,33),(25,38),(19,38)),('L',(16,38))])
        self.join('b','b-lower')
        for i,y in enumerate((22,35)):self.add_line(f'answer-{i}',(31,y),(34,y))
'''),
('SQUARE','A large A is followed by a raised numeral one.',
 'The A owns its shared crossbar nodes; the superscript is a separate upper-right stroke group.',[], 'type', '''
        self.letter_a('a',(18,12),(6,42),(30,42),(10,32),(26,32))
        self.add_polyline('one',(36,10),(40,6),(40,18))
        self.add_polyline('one-base',(36,18),(40,18),(42,18));self.join('one','one-base')
'''),
('SQUARE','A serif A sits over a dropdown field.',
 'Centered A with matched foot serifs; rounded dropdown with a right chevron.',[], 'type', '''
        self.letter_a('a',(24,6),(14,26),(34,26),(19,16),(29,16))
        for name,x in [('serif-left',14),('serif-right',34)]:
            self.add_polyline(name,(x-3,26),(x,26),(x+3,26));self.join('a',name)
        self.rect('dropdown',6,34,36,8,4)
        self.add_polyline('chevron',(32,37),(34,39),(36,37))
'''),
('SQUARE','A large A appears beside a plus sign.',
 'A crossbar derives from the two legs; the plus is centered in the remaining right-hand band.',[], 'type', '''
        self.letter_a('a',(18,6),(6,42),(30,42),(10,30),(26,30))
        self.cross('plus',38,26,4)
'''),
('VRECT_L','A Thaipusam spearhead contains a scalloped central emblem and triangular base.',
 'The outer teardrop and center emblem mirror about x24; the base forms a deliberate angular junction.',
 ['Two tiny central ticks omitted because they disappear inside the small scalloped emblem at native size.'], 'none', '''
        self.path('spearhead',(24,4),[('C',(32,10),(40,20),(40,28)),('C',(40,36),(34,41),(30,44)),('L',(18,44)),('C',(14,41),(8,36),(8,28)),('C',(8,20),(16,10),(24,4))],True)
        self.add_polyline('base-triangle',(18,44),(24,38),(30,44));self.join('spearhead','base-triangle')
        self.path('emblem',(20,18),[('L',(28,18)),('A',(31,21),3,3,True),('C',(31,23),(29,23),(31,26)),('C',(29,29),(31,29),(31,31)),('A',(28,34),3,3,True),('L',(20,34)),('A',(17,31),3,3,True),('C',(17,29),(19,29),(17,26)),('C',(19,23),(17,23),(17,21)),('A',(20,18),3,3,True)],True)
'''),
('SQUARE','A basketball and small circular mark sit behind an angled admission ticket.',
 'A large circular ball is partially open behind the ticket; the ticket has opposed inward notches.',[], 'ticket', '''
        self.add_arc('ball',(32,19),(19,32),radius_x=13,large_arc=True,sweep=False)
        self.add_bezier('seam-one',(10,10),((19,14),(24,20),(27,27)))
        self.add_bezier('seam-two',(6,20),((17,20),(24,14),(25,8)))
        self.add_bezier('seam-three',(15,31),((17,23),(23,19),(31,16)))
        self.circle('small-mark',38,10,4)
        self.path('ticket',(16,30),[('L',(38,22)),('L',(40,27)),('C',(34,28),(36,34),(42,33)),('L',(42,34)),('L',(20,42)),('L',(18,37)),('C',(23,35),(21,29),(16,32)),('L',(16,30))],True)
        self.add_line('ticket-rule-0',(26,31),(32,29))
        self.add_line('ticket-rule-1',(28,36),(34,34))
'''),
('SQUARE','A rounded square tile is divided into four equal quadrants.',
 'The square owns four midpoint nodes; a four-ray divider meets exactly at the center.',[], 'tv', '''
        axis=24
        self.rect('tile',6,6,36,36,4,split_x=(axis,),split_y=(axis,))
        rays=[]
        for i,p in enumerate(((6,axis),(42,axis),(axis,6),(axis,42))):
            n=f'divider-{i}';self.add_line(n,(axis,axis),p);rays.append(n);self.join('tile',n)
        self.join(*rays)
'''),
('VRECT_L','A tire-pressure warning outline encloses a vertical warning stroke.',
 'Mirrored throat caps lead into a broad U-shaped bulb; paired lower stems stay aligned.',[], 'none', '''
        self.path('tire',(12,8),[('A',(20,8),4,4,True),('L',(20,14)),('C',(20,20),(16,22),(16,27)),('C',(16,32),(19,34),(24,34)),('C',(29,34),(32,32),(32,27)),('C',(32,22),(28,20),(28,14)),('L',(28,8)),('A',(36,8),4,4,True),('C',(36,18),(40,20),(40,28)),('C',(40,36),(34,40),(28,40)),('L',(20,40)),('C',(14,40),(8,36),(8,28)),('C',(8,20),(12,18),(12,8))],True)
        self.add_line('warning',(24,15),(24,23))
        for name,x in [('stem-left',20),('stem-right',28)]:
            self.add_line(name,(x,40),(x,44));self.join('tire',name)
'''),
('SQUARE','A diagonal rounded tag has a circular hole near its square end.',
 'One continuous rounded tag silhouette; intentional diagonal orientation matches the source.',[], 'tag', '''
        self.path('tag',(26,6),[('L',(36,6)),('A',(42,12),6,6,True),('L',(42,22)),('C',(42,24),(42,25),(40,27)),('L',(26,40)),('C',(24,42),(23,42),(22,42)),('C',(20,42),(19,41),(18,40)),('L',(8,30)),('C',(6,28),(6,27),(6,26)),('C',(6,24),(7,23),(8,22)),('L',(22,8)),('C',(23,7),(24,6),(26,6))],True)
        self.circle('hole',30,18,3)
'''),
('SQUARE','A person sits correctly on a toilet beside a check mark.',
 'Seated torso axis sets the circular head; an angled shin and folded arm retain the correct-use pose.',[], 'human', 'TOILET_RIGHT'),
('SQUARE','A person uses a toilet incorrectly beside an X.',
 'Seated torso axis sets the circular head; upright lower leg and an X preserve the alternate pose.',[], 'human', 'TOILET_WRONG'),
('SQUARE','An eye sheds a tear above a tear-gas canister and drifting gas.',
 'Four semantic groups retain the source positions: eye, tear, horizontal canister, and two-part gas cloud.',
 ['Canister end-band stripe omitted to avoid an extra narrow parallel band.'], 'none', '''
        self.add_arc('eye-upper',(6,14),(28,14),radius_x=11,radius_y=8)
        self.add_bezier('eye-lower',(28,14),((26,19),(22,22),(18,22)));self.join('eye-upper','eye-lower')
        self.circle('pupil',16,13,3)
        self.path('tear',(11,19),[('C',(9,23),(7,25),(7,28)),('A',(15,28),4,4,False),('C',(15,25),(13,23),(11,19))],True)
        self.rect('canister',6,32,18,10,3,split_y=(35,39))
        self.add_polyline('nozzle',(24,35),(28,35),(28,39),(24,39));self.join('canister','nozzle')
        self.path('gas',(34,26),[('C',(30,26),(28,24),(30,21)),('C',(27,18),(29,12),(34,10)),('C',(38,8),(42,12),(42,16)),('C',(42,20),(38,22),(36,22)),('C',(36,25),(35,26),(34,26))],True)
        self.circle('gas-dot',32,31,2)
'''),
('CIRCLE','An upward arrow rises out of an open circular touch target.',
 'A circular major arc leaves an upper opening; the arrow shares its apex node and stays on the vertical axis.',[], 'none', '''
        self.add_arc('target',(8,12),(40,12),radius_x=20,large_arc=True,sweep=False)
        self.add_line('shaft',(24,4),(24,24))
        self.add_polyline('arrowhead',(18,10),(24,4),(30,10));self.join('shaft','arrowhead')
'''),
]

def toilet(right):
    # 5-12-13 triangle: head radius5, center-to-neck13 =>8 centerline /4 ink gap.
    cx=23 if right else 27
    neck=(cx-5,23);hip=(cx-10,35)
    s=f'''
        self.circle('head',{cx},11,5)
        self.add_line('torso',{neck!r},{hip!r})
        self.add_polyline('leg',{hip!r},(31,35),{(37,42) if right else (31,42)!r})
        self.join('torso','leg')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        self.add_polyline('toilet',(6,42),(6,24),(10,24),(10,36),(26,36))
        self.add_bezier('bowl',(26,36),((26,40),(20,40),(20,42)))
        self.join('toilet','bowl')
'''
    if right:
        s+='''
        self.add_polyline('arm',(18,23),(28,30),(22,32));self.join('torso','arm')
        self.add_polyline('check',(33,12),(37,16),(42,6))
'''
    else:s+="        self.cross('wrong',38,10,4,True)\n"
    return s

def references(code):
    result=[]
    for n in code.split(';'):
        if n=='human': result.append('icon_set/references/human_ref/user.svg and full_body_ref.png: circular heads, smooth shoulders, coherent limb strokes and exact detached-head spacing.')
        elif n=='none':result.append('No useful local Lucide subject match found; shared geometric construction principles used.')
        else:
            actual='message-square' if n=='message' else n
            result.append(f'icon_set/references/lucide/original/{actual}.svg and atomic-debug/{actual}.svg: coherent contours, shared junctions, and consistent rounding; re-authored on SOLO48.')
    return result

def main():
    for i,(row,spec) in enumerate(zip(ROWS,SPECS)):
        if 'result_dir' not in row:continue
        out=Path(row['result_dir'])
        if (out/'result.json').exists():continue
        key,subject,plan,omissions,refs,body=spec
        if body.startswith('TOILET_'):body=toilet(body=='TOILET_RIGHT')
        ref_list=references(refs)
        module_name=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
        code=f'''"""{subject}
Plan: {plan}
Keyshape: {key}. All bounds derive from the SOLO48 keyshape contract.
Construction references: {' '.join(ref_list)}
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
'''+HELPERS+'\n    def build(self):\n'+body
        (out/module_name).write_text(code)
        data=dict(row,keyshape=key,subject=subject,construction_plan=plan,omissions=omissions,construction_references=ref_list,python=module_name)
        try:
            module_spec=importlib.util.spec_from_file_location(f'batch50_{i}',out/module_name)
            module=importlib.util.module_from_spec(module_spec);module_spec.loader.exec_module(module)
            icon=module.Drawing();report=icon.validate_icon();data['validation_status']=report.status
            (out/'validation.txt').write_text(report.describe())
            svg=icon.to_svg();(out/(row['icon_id']+'.svg')).write_text(svg)
            data['export_status']='success'
            for size in (48,192):
                raw=cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)
                alpha=Image.open(io.BytesIO(raw)).convert('RGBA').getchannel('A')
                for theme,bg,ink in [('light','white','black'),('dark','#16191d','#f4f5f6')]:
                    im=Image.new('RGB',(size,size),bg);im.paste(ink,(0,0,size,size),alpha);im.save(out/f'{theme}-{size}.png')
        except Exception:
            data.setdefault('validation_status','error');data['export_status']='error';data['error']=traceback.format_exc()
            (out/'error.txt').write_text(data['error'])
        (out/'attempt-findings.json').write_text(json.dumps(data,indent=2)+'\n')
        print(i+1,row['concept'],data['validation_status'],data.get('export_status'),flush=True)
    sheet=Image.new('RGB',(1080,7*270),'#dadde0');draw=ImageDraw.Draw(sheet)
    for i,row in enumerate(ROWS):
        if 'result_dir' not in row:continue
        out=Path(row['result_dir']);x=i%3*360;y=i//3*270
        draw.text((x+4,y+4),f"{i+1}. {row['concept'][:36]}",fill='black')
        for j,theme in enumerate(('light','dark')):
            if (out/f'{theme}-192.png').exists():
                sheet.paste(Image.open(out/f'{theme}-192.png').resize((160,160)),(x+j*180,y+26))
                sheet.paste(Image.open(out/f'{theme}-48.png'),(x+j*180+56,y+198))
    sheet.save(ROOT/'authored-review.png')

if __name__=='__main__':main()
