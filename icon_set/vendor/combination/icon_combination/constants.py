"""
Centralized constants for icon processing and combination
"""

# Main icon scaling constants
def get_aspect_ratio(position='bottom-right'):
    """Get aspect ratio based on position"""
    if position == 'center':
        return 1.0  # 100% scale for center position
    return 0.9 if position in ['top', 'bottom'] else 0.75

ASPECT_RATIO = 0.9  # Default value, use get_aspect_ratio() for position-specific values
ASPECT_RATIO_THRESHOLD = 1.45

# Canvas dimensions
DEFAULT_MAIN_CANVAS_WIDTH = 1024
DEFAULT_MAIN_CANVAS_HEIGHT = 1024
DEFAULT_STATE_WIDTH = 512
DEFAULT_STATE_HEIGHT = 512
DEFAULT_FINAL_CANVAS_WIDTH = 1024
DEFAULT_FINAL_CANVAS_HEIGHT = 1024

# Stroke settings
DEFAULT_MAIN_STROKE_WIDTH = 30
DEFAULT_STATE_STROKE_WIDTH = 8
SAVE_MAIN_STROKE_WIDTH = 25
SAVE_STATE_STROKE_WIDTH = 25

# Buffer settings
DEFAULT_BUFFER_RADIUS = 16.0
EXAMPLE_BUFFER_RADIUS = 64

# Colors
DEFAULT_MAIN_COLOR = "red"
DEFAULT_STATE_COLOR = "blue"
DEFAULT_BLACK_COLOR = "#000000"

# Processing settings
MIN_SEGMENT_LENGTH = 1.0
DEFAULT_STROKE_WIDTH = 8

# Offset settings for thin icons
DEFAULT_OFFSET_PERCENTAGE = 0.25  # 25% of canvas as default offset
