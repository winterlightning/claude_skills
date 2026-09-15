SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-ai-shapes-refine/batch.json'
AUTHOR='gpt-6'
design('casino-clover','SQUARE','Soft curved shamrock','clover','Three broad heart-shaped leaves flow through smooth rounded curves. The two side leaves mirror, with shallow soft notches and a curved stem instead of the prior bumpy corners.', """
# One left half owns the complete mirrored leaf outline.
left=[('C',(11,36),(20,29),(15,36)),('C',(6,30),(8,36),(6,34)),('C',(8,26),(6,28),(8,28)),('C',(6,22),(8,24),(6,24)),('C',(12,16),(6,18),(8,16)),('C',(16,18),(14,16),(17,19)),('C',(14,12),(15,17),(14,15)),('C',(19,6),(14,8),(16,6)),('C',(24,9),(22,6),(22,9))]
commands=list(left)
starts=[(24,29)]+[c[1] for c in left[:-1]]
mirror=lambda p:(48-p[0],p[1])
for start,(kind,end,c1,c2) in reversed(list(zip(starts,left))):commands.append(('C',mirror(start),mirror(c2),mirror(c1)))
path('leaves',(24,29),commands,True)
path('stem',(24,29),[('C',(30,42),(21,37),(24,42))]);join('stem','leaves')
""")
