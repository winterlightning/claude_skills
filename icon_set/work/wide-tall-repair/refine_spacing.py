from manual_repairs import *
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/wide-tall-repair/targets.json'
AUTHOR='gpt-6'
mods={
'classical-statue-bust':lambda r:move(r,lambda x,y:(x,35 if y==36 else y)),
'flaming-brazier':lambda r:move(r,lambda x,y:(x,17 if y==18 else y),lambda p:p['element_id'].startswith('flame')),
'inscribed-stone-tablet':lambda r:move(r,lambda x,y:(17 if x==16 else 31 if x==32 else x,y),lambda p:p['element_id'].startswith('inscription')),
'necklace-with-teardrop-pendant':lambda r:move(r,lambda x,y:(x,24 if y==25 else y)),
'paired-landscape-window-panels':lambda r:move(r,lambda x,y:(19 if x==20 else 29 if x==28 else x,y)),
'written-scroll':lambda r:move(r,lambda x,y:(x+1,y),lambda p:p['element_id']=='writing-top'),
}
for id,fn in mods.items():
 f=W/'candidates'/f'{id}.json';x=json.loads(f.read_text())
 if x.get('refined'):continue
 fn(x['record']);x['refined']=True;q=check(f,x);print(id,q['status'],q['errors']+q['warnings'],flush=True)
