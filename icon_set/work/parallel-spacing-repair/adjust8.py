from author import write,ROOT,TARGETS,WORK
# Keep the more recognizable shark silhouette after comparing both renderings.
old=(WORK/'pre-final-51.py').read_text();(ROOT/TARGETS[51]['source_path']).write_text(old)
write(74,'SQUARE','''
p('plane',(36,6),(24,12),(18,6),(10,10),(19,20),(10,24),(6,20),(6,34),(14,34),(36,18))
a('nose',(36,18),(36,6),6,sweep=False)
link('connect','plane','nose')
l('runway',(6,42),(42,42))
''','Departing plane: naturally balanced broad wing, tail and fuselage with a smooth nose above the runway.')
