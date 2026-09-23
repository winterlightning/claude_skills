# Both main and sub — 1 result from offset 0
python3 icon_set/scripts/side_generation_queue.py 1 0

# Main only
python3 icon_set/scripts/side_generation_queue.py 1 0 --role main

# Sub only
python3 icon_set/scripts/side_generation_queue.py 1 0 --role sub

# Every remaining item
python3 icon_set/scripts/side_generation_queue.py --all
