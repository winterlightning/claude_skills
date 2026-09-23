"""Manual repairs chosen after native and enlarged visual inspection."""
from pathlib import Path
import importlib.util, json, shutil, textwrap
SOURCE_ICON_ID='27005b33-be8e-4027-a5b5-311a85fa87c3'
SOURCE_PATH='icon_set/work/todo-references/signboard 1_27005b33-be8e-4027-a5b5-311a85fa87c3.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
spec=importlib.util.spec_from_file_location('batch',ROOT/'author_batch.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
BODIES={
0: '''
self.add_line('rail-left',(4,8),(10,8))
self.add_line('rail-middle',(10,8),(30,8))
self.add_line('rail-right',(30,8),(40,8))
self.add_arc('post-corner',(40,8),(44,12),radius_x=4)
self.add_line('post-vertical',(44,12),(44,40))
self.add_contour('post','rail-left','rail-middle','rail-right','post-corner','post-vertical')
self.rounded('sign',4,16,36,32,3,breaks={0:[(10,16),(30,16)]})
for i,x in enumerate((10,30)):
    self.add_line(f'hanger-{i}',(x,8),(x,16))
    self.relate('connect',f'hanger-{i}','post')
    self.relate('connect',f'hanger-{i}','sign')
''',
6: '''
self.add_line('device-top',(10,18),(22,18))
self.add_arc('device-tl',(6,22),(10,18),radius_x=4)
self.add_line('device-left',(6,36),(6,22))
self.add_arc('device-bl',(10,40),(6,36),radius_x=4)
self.add_line('device-bottom',(38,40),(10,40))
self.add_arc('device-br',(42,36),(38,40),radius_x=4)
self.add_line('device-right',(42,22),(42,36))
self.add_contour('device','device-right','device-br','device-bottom','device-bl','device-left','device-tl','device-top')
for name,x in [('left',10),('right',38)]:
    self.add_line('foot-'+name,(x,40),(x,42));self.relate('connect','foot-'+name,'device')
self.add_polyline('plus-horizontal',(15,29),(17,29),(19,29))
self.add_polyline('plus-vertical',(17,27),(17,29),(17,31))
self.relate('connect','plus-horizontal','plus-vertical')
self.circle('button',31,29,2)
self.add_polyline('z-big',(32,6),(42,6),(32,14),(42,14))
''',
18: '''
# A diagonal strap gives a true circular face room without closing the strap holes.
# The 5-12-13 triangle provides exact integer circular attachment points.
nodes=[(12,19),(19,12),(36,29),(29,36),(12,19)]
members=[]
for i,(a,b) in enumerate(zip(nodes,nodes[1:])):
    name=f'case-{i}';self.add_arc(name,a,b,radius_x=13);members.append(name)
self.add_contour('case',*members,closed=True)
self.add_polyline('strap-top',(12,19),(6,12),(12,6),(19,12))
self.add_polyline('strap-bottom',(36,29),(42,36),(36,42),(29,36))
self.relate('connect','case','strap-top')
self.relate('connect','case','strap-bottom')
''',
}
BODIES[19]=BODIES[18]
for i,e in enumerate(m.ENTRIES):
    d=Path(e['result_dir']);plan=json.loads((d/'plan.json').read_text());p=d/plan['python'];old=p.read_text();new=old
    if i in BODIES:
        a=old.index('    def build(self):');b=old.index('    def circle(',a)
        new=old[:a]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(BODIES[i]).strip()+'\n','        ')+'\n'+old[b:]
    if i==7:
        new=new.replace("        self.add_polyline('z-small',(26,14),(32,14),(26,22),(32,22))\n",'')
        plan['omissions']='The smaller repeated Z was removed to preserve spacing; the primary Z, open circular face and both hands remain.'
    if i==6:
        plan['omissions']='The smaller repeated Z was removed; the primary Z, both feet, plus control and round button remain. The button uses the permitted small-circle construction.'
    if i==11:
        new=new.replace("'toaster',8,18,40,44,4,breaks={0:[(14,18),(34,18)]}","'toaster',8,17,40,44,4,breaks={0:[(14,17),(34,17)]}")
        new=new.replace("'toast-left',(14,18),(14,12)","'toast-left',(14,17),(14,12)").replace("'toast-right',(34,12),(34,18)","'toast-right',(34,12),(34,17)")
        new=new.replace("'wireless-arc',24,29,8,4","'wireless-arc',24,30,8,4")
    if i==12:
        new=new.replace("'tv-top',(8,18),(23,18)","'tv-top',(8,19),(23,19)").replace("'tv-tl',(4,22),(8,18)","'tv-tl',(4,23),(8,19)").replace("'tv-left',(4,28),(4,22)","'tv-left',(4,28),(4,23)")
    if i in (18,19):
        new=new.replace('keyshape=Keyshape.VRECT_L','keyshape=Keyshape.SQUARE')
        plan['keyshape']='SQUARE';plan['omissions']='None. The whole watch is oriented diagonally so the circular face and open strap loops fit with legal clearance.'
        plan['construction_reference']='watch: circular case and paired tapered straps. Diagonal orientation uses exact 5-12-13 circular attachment nodes, preserving the complete blank watch.'
    if new!=old:
        backup=d/'initial-attempt';backup.mkdir(exist_ok=True)
        for f in d.iterdir():
            if f.is_file() and (f==p or f.suffix in ('.svg','.png') or f.name in ('validation.txt','export-status.json','plan.json')):shutil.copy2(f,backup/f.name)
        p.write_text(new);(d/'plan.json').write_text(json.dumps(plan,indent=2)+'\n');m.export(e)
