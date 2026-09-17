import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Rectangle
import xml.etree.ElementTree as ET
from shapely.geometry import Polygon as ShapelyPolygon
from shapely.geometry import LineString, MultiPolygon
from shapely.ops import unary_union
from scipy.spatial import ConvexHull
from .alignment_decision import calculate_main_icon_position
# Import from new modular files
from .process_main import (
    process_main_icon_with_dynamic_positioning
)
from .process_state import process_state_icon
from .constants import ASPECT_RATIO, ASPECT_RATIO_THRESHOLD, get_aspect_ratio
from .utils import (
    parse_svg_geometric_elements,
    clip_segments_outside_state_area_enhanced,
    create_convex_hull_buffer,
    find_intersection_segments_detailed,
    parse_svg_path,
    get_buffer_outlines,
    find_buffer_extreme_points,
    create_merged_light_red_area,
    create_third_state_rectangle,
    create_fourth_state_rectangle
)

class CombineConfig:
    """Centralized configuration for icon combination processing"""

    # Canvas dimensions
    DEFAULT_MAIN_CANVAS_WIDTH = 1024
    DEFAULT_MAIN_CANVAS_HEIGHT = 1024
    DEFAULT_STATE_WIDTH = 512
    DEFAULT_STATE_HEIGHT = 512
    DEFAULT_FINAL_CANVAS_WIDTH = 1024
    DEFAULT_FINAL_CANVAS_HEIGHT = 1024

    # Aspect ratio settings
    ASPECT_RATIO = 1
    ASPECT_RATIO_THRESHOLD = 1.45

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
    DEFAULT_OFFSET_PERCENTAGE = 0.25  # 10% of canvas as default offset

    # Matplotlib settings
    FIGURE_SIZE = (8, 8)
    PLOT_MARGIN = 30
    STATS_TEXT_FONT_SIZE = 9
    LEGEND_FONT_SIZE = 8
    GRID_ALPHA = 0.3

    # Line collection settings
    CLIPPED_LINE_WIDTH = 2
    REMOVED_LINE_WIDTH = 1
    STATE_LINE_WIDTH = 2
    MAIN_BORDER_LINE_WIDTH = 2
    STATE_CANVAS_BORDER_LINE_WIDTH = 3
    STATE_OBJECT_BORDER_LINE_WIDTH = 2

    # Colors for visualization
    VIZ_CLIPPED_COLOR = 'darkblue'
    VIZ_REMOVED_COLOR = 'gray'
    VIZ_STATE_COLOR = 'purple'
    VIZ_MERGED_AREA_COLOR = 'lightcoral'
    VIZ_MERGED_AREA_ALPHA = 0.3
    VIZ_THIRD_STATE_COLOR = 'green'
    VIZ_FOURTH_STATE_COLOR = 'orange'
    VIZ_EXTREME_POINT_COLOR = 'red'
    VIZ_EXTREME_POINT_SIZE = 100
    VIZ_MAIN_BORDER_COLOR = 'black'
    VIZ_STATE_CANVAS_BORDER_COLOR = 'blue'
    VIZ_STATE_OBJECT_BORDER_COLOR = 'red'

    # Text positioning
    TEXT_OFFSET_X = 5
    TEXT_OFFSET_Y = 5
    STATS_TEXT_X = 0.02

    @classmethod
    def get_default_config(cls):
        """Return a dictionary with all default configuration values"""
        return {
            'main_canvas_width': cls.DEFAULT_MAIN_CANVAS_WIDTH,
            'main_canvas_height': cls.DEFAULT_MAIN_CANVAS_HEIGHT,
            'state_width': cls.DEFAULT_STATE_WIDTH,
            'state_height': cls.DEFAULT_STATE_HEIGHT,
            'final_canvas_width': cls.DEFAULT_FINAL_CANVAS_WIDTH,
            'final_canvas_height': cls.DEFAULT_FINAL_CANVAS_HEIGHT,
            'main_stroke_width': cls.DEFAULT_MAIN_STROKE_WIDTH,
            'state_stroke_width': cls.DEFAULT_STATE_STROKE_WIDTH,
            'buffer_radius': cls.DEFAULT_BUFFER_RADIUS,
            'main_color': cls.DEFAULT_MAIN_COLOR,
            'state_color': cls.DEFAULT_STATE_COLOR,
            'min_segment_length': cls.MIN_SEGMENT_LENGTH,
            'stroke_width': cls.DEFAULT_STROKE_WIDTH,
            'offset_percentage': cls.DEFAULT_OFFSET_PERCENTAGE
        }

# =============================================================================
# ALIGNMENT MAPPING
# =============================================================================

# State icon alignment to main icon alignment mapping
state_alignment_map_to_main_icon = {
    # Mean state icon is bottom-right, main icon is top-left
    'bottom-right': 'top-left',
    'right': 'left',
    'top-right': 'bottom-left',
    'bottom': 'top',
    'bottom-left': 'top-right',
    'top-left': 'bottom-right',
    'left': 'right',
    'top': 'bottom',
    'center': 'center',
}

# =============================================================================
# THIN ICON OFFSET ADJUSTMENT FUNCTIONS
# =============================================================================

def is_thin_icon(aspect_ratio, threshold=None):
    """
    Determine if an icon is considered 'thin' based on aspect ratio threshold

    Args:
        aspect_ratio: The aspect ratio of the icon (W/H or H/W, whichever is larger)
        threshold: Aspect ratio threshold (defaults to CombineConfig.ASPECT_RATIO_THRESHOLD)

    Returns:
        bool: True if the icon is considered thin
    """
    if threshold is None:
        threshold = CombineConfig.ASPECT_RATIO_THRESHOLD
    return aspect_ratio > threshold

def adjust_position_for_horizontal_thin_icon(position, canvas_width, canvas_height, offset_percentage=None):
    """
    Adjust position for horizontal thin icons based on the rules in comments

    Args:
        position: Current alignment position
        canvas_width: Canvas width
        canvas_height: Canvas height
        offset_percentage: Offset as percentage of canvas (defaults to CombineConfig.DEFAULT_OFFSET_PERCENTAGE)

    Returns:
        tuple: (adjusted_x_offset, adjusted_y_offset)
    """
    if offset_percentage is None:
        offset_percentage = CombineConfig.DEFAULT_OFFSET_PERCENTAGE

    offset_x = canvas_width * offset_percentage
    offset_y = canvas_height * offset_percentage

    if position in ['bottom', 'bottom-right', 'bottom-left']:
        # Shift to top
        return (0, -offset_y)
    elif position in ['top', 'top-left', 'top-right']:
        # Shift to bottom
        return (0, offset_y)
    else:
        # left, right, middle - do nothing
        return (0, 0)

def adjust_position_for_vertical_thin_icon(position, canvas_width, canvas_height, offset_percentage=None):
    """
    Adjust position for vertical thin icons based on the rules in comments

    Args:
        position: Current alignment position
        canvas_width: Canvas width
        canvas_height: Canvas height
        offset_percentage: Offset as percentage of canvas (defaults to CombineConfig.DEFAULT_OFFSET_PERCENTAGE)

    Returns:
        tuple: (adjusted_x_offset, adjusted_y_offset)
    """
    if offset_percentage is None:
        offset_percentage = CombineConfig.DEFAULT_OFFSET_PERCENTAGE

    offset_x = canvas_width * offset_percentage
    offset_y = canvas_height * offset_percentage

    # Rules for vertical thin icons:
    # if main icon is align bottom -> do nothing
    # if main icon is align top -> do nothing
    # if main icon is align left -> shift to right
    # if main icon is align right -> shift to left
    # if main icon is align bottom-right -> shift to left
    # if main icon is align bottom-left -> shift to right
    # if main icon is align top-left -> shift to right
    # if main icon is align top-right -> shift to left

    if position in ['left', 'bottom-left', 'top-left']:
        # Shift to right
        return (offset_x, 0)
    elif position in ['right', 'bottom-right', 'top-right']:
        # Shift to left
        return (-offset_x, 0)
    else:
        # top, bottom, middle - do nothing
        return (0, 0)

def apply_thin_icon_offset(x, y, aspect_ratio, orientation, position, canvas_width, canvas_height, offset_percentage=None):
    """
    Apply offset adjustments for thin icons based on orientation and position

    Args:
        x, y: Current position coordinates
        aspect_ratio: Icon aspect ratio
        orientation: Icon orientation ('Horizontal', 'Vertical', or 'Square')
        position: Alignment position
        canvas_width, canvas_height: Canvas dimensions
        offset_percentage: Offset as percentage of canvas

    Returns:
        tuple: (adjusted_x, adjusted_y)
    """
    if not is_thin_icon(aspect_ratio):
        return x, y

    if orientation == "Horizontal":
        offset_x, offset_y = adjust_position_for_horizontal_thin_icon(
            position, canvas_width, canvas_height, offset_percentage
        )
    elif orientation == "Vertical":
        offset_x, offset_y = adjust_position_for_vertical_thin_icon(
            position, canvas_width, canvas_height, offset_percentage
        )
    else:
        # Square icons don't need offset
        offset_x, offset_y = 0, 0

    return x + offset_x, y + offset_y

def calculate_combined_bounding_box(main_icon_x, main_icon_y, main_icon_width, main_icon_height,
                                   state_icon_x, state_icon_y, state_icon_width, state_icon_height):
    """
    Calculate the bounding box that encompasses both main and state icons

    Args:
        main_icon_x, main_icon_y: Main icon position (top-left corner)
        main_icon_width, main_icon_height: Main icon dimensions
        state_icon_x, state_icon_y: State icon position (top-left corner)
        state_icon_width, state_icon_height: State icon dimensions

    Returns:
        tuple: (combined_x, combined_y, combined_width, combined_height)
    """
    # Calculate bounds for main icon
    main_left = main_icon_x
    main_right = main_icon_x + main_icon_width
    main_top = main_icon_y
    main_bottom = main_icon_y + main_icon_height

    # Calculate bounds for state icon
    state_left = state_icon_x
    state_right = state_icon_x + state_icon_width
    state_top = state_icon_y
    state_bottom = state_icon_y + state_icon_height

    # Find combined bounding box
    combined_left = min(main_left, state_left)
    combined_right = max(main_right, state_right)
    combined_top = min(main_top, state_top)
    combined_bottom = max(main_bottom, state_bottom)

    combined_width = combined_right - combined_left
    combined_height = combined_bottom - combined_top

    return combined_left, combined_top, combined_width, combined_height

def center_combined_result(main_icon_x, main_icon_y, main_icon_width, main_icon_height,
                          state_icon_x, state_icon_y, state_icon_width, state_icon_height,
                          canvas_width, canvas_height):
    """
    Calculate position adjustments to center the combined result within the canvas

    Args:
        main_icon_x, main_icon_y: Current main icon position
        main_icon_width, main_icon_height: Main icon dimensions
        state_icon_x, state_icon_y: Current state icon position
        state_icon_width, state_icon_height: State icon dimensions
        canvas_width, canvas_height: Canvas dimensions

    Returns:
        tuple: (main_icon_new_x, main_icon_new_y, state_icon_new_x, state_icon_new_y)
    """
    # Get current combined bounding box
    combined_x, combined_y, combined_width, combined_height = calculate_combined_bounding_box(
        main_icon_x, main_icon_y, main_icon_width, main_icon_height,
        state_icon_x, state_icon_y, state_icon_width, state_icon_height
    )

    # Calculate center point of canvas
    canvas_center_x = canvas_width / 2
    canvas_center_y = canvas_height / 2

    # Calculate center point of combined result
    combined_center_x = combined_x + combined_width / 2
    combined_center_y = combined_y + combined_height / 2

    # Calculate offset needed to center the combined result
    offset_x = canvas_center_x - combined_center_x
    offset_y = canvas_center_y - combined_center_y

    # Apply offset to both icons
    new_main_x = main_icon_x + offset_x
    new_main_y = main_icon_y + offset_y
    new_state_x = state_icon_x + offset_x
    new_state_y = state_icon_y + offset_y

    print(f"Combined bounding box: ({combined_x:.1f}, {combined_y:.1f}) {combined_width:.1f}x{combined_height:.1f}")
    print(f"Canvas center: ({canvas_center_x:.1f}, {canvas_center_y:.1f})")
    print(f"Combined center: ({combined_center_x:.1f}, {combined_center_y:.1f})")
    print(f"Centering offset: ({offset_x:.1f}, {offset_y:.1f})")

    return new_main_x, new_main_y, new_state_x, new_state_y

# =============================================================================
# MAIN ORCHESTRATION FUNCTIONS
# =============================================================================

def merged_icons_and_remove_overlapping(main_icon_data, state_icon_data,
                                       state_position_x, state_position_y,
                                       canvas_width, canvas_height,
                                       show_matplotlib=False,
                                       min_segment_length=None, alignment="middle", config=None):
    """
    Merge main and state icons, clip main icon segments inside state area, and visualize.
    Add main icon W/H ratio to Matplotlib stats text and handle missing buffer_area_stroke.
    Enhanced with state canvas and state object border visualization.

    Args:
        config: CombineConfig instance for configuration values
    """
    try:
        # Initialize configuration
        if config is None:
            config = CombineConfig()
        if min_segment_length is None:
            min_segment_length = config.MIN_SEGMENT_LENGTH
        # Extract data with safety checks
        main_segments = main_icon_data['segments']
        main_scaled_width, main_scaled_height = main_icon_data['scaled_dimensions']
        main_icon_x, main_icon_y = main_icon_data['final_icon_position']
        main_aspect_ratio = main_icon_data.get('aspect_ratio', 0.0)
        
        state_segments = state_icon_data.get('segments', [])
        buffer_area_stroke = state_icon_data.get('buffer_area_by_stroke', None)  # Fixed key name
        buffer_area_convex = state_icon_data.get('buffer_area_by_convex', None)   # Fixed key name
        state_width, state_height = state_icon_data.get('dimensions', (0, 0))
        
        # Calculate state object bounds within its local coordinate system (before positioning)
        if state_segments:
            state_points = []
            for segment in state_segments:
                state_points.extend(segment)
            state_points_array = np.array(state_points)
            state_obj_min_x, state_obj_min_y = np.min(state_points_array, axis=0)
            state_obj_max_x, state_obj_max_y = np.max(state_points_array, axis=0)
            state_obj_width = state_obj_max_x - state_obj_min_x
            state_obj_height = state_obj_max_y - state_obj_min_y
            
            print(f"State object bounds within canvas: ({state_obj_min_x:.1f}, {state_obj_min_y:.1f}) to ({state_obj_max_x:.1f}, {state_obj_max_y:.1f})")
            print(f"State object dimensions: {state_obj_width:.1f} x {state_obj_height:.1f}")
        else:
            state_obj_min_x = state_obj_min_y = 0
            state_obj_max_x = state_obj_max_y = 0
            state_obj_width = state_obj_height = 0
        
        # Check for missing or invalid buffer_area_stroke
        if buffer_area_stroke is None:
            print("Warning: buffer_area_stroke is None. Falling back to buffer_area_convex only.")
        if buffer_area_convex is None:
            print("Warning: buffer_area_convex is None. Clipping may be incomplete.")
        
        # Position state icon segments
        positioned_state_segments = []
        for segment in state_segments:
            new_segment = [
                (segment[0][0] + state_position_x, segment[0][1] + state_position_y),
                (segment[1][0] + state_position_x, segment[1][1] + state_position_y)
            ]
            positioned_state_segments.append(new_segment)
        
        # Find extreme points of convex buffer area
        extreme_points = find_buffer_extreme_points(buffer_area_convex, state_position_x, state_position_y)
        
        # Create third and fourth state rectangles
        third_state_rectangle = create_third_state_rectangle(extreme_points, canvas_width, canvas_height, alignment)
        fourth_state_rectangle = create_fourth_state_rectangle(extreme_points, canvas_width, canvas_height, alignment)
        
        # Create merged light red area with fallback
        merged_light_red_area = create_merged_light_red_area(
            buffer_area_stroke, buffer_area_convex, extreme_points,
            canvas_width, canvas_height, state_position_x, state_position_y, alignment
        )
        
        if merged_light_red_area is None:
            print("Error: merged_light_red_area is None. Using empty polygon for clipping.")
            merged_light_red_area = ShapelyPolygon()
        
        # Clip main icon segments
        clipped_segments, removed_segments, intersection_info = clip_segments_outside_state_area_enhanced(
            main_segments, merged_light_red_area, min_segment_length
        )
        
        # Find intersection segments for visualization
        non_intersecting_segments, intersecting_segments, intersection_points = find_intersection_segments_detailed(
            main_segments, merged_light_red_area
        )
        
        # Get main icon aspect ratio and orientation (already correctly calculated)
        main_icon_width, main_icon_height = main_icon_data['scaled_dimensions']
        main_icon_aspect_ratio = main_icon_data['aspect_ratio']  # Use the correctly calculated ratio
        orientation = main_icon_data['orientation']  # Use the already determined orientation
        if show_matplotlib:
            fig, ax = plt.subplots(figsize=config.FIGURE_SIZE)

            # Plot clipped segments (dark blue)
            if clipped_segments:
                clipped_lines = LineCollection(clipped_segments, colors=config.VIZ_CLIPPED_COLOR, linewidths=config.CLIPPED_LINE_WIDTH, label='Clipped Segments')
                ax.add_collection(clipped_lines)

            # Plot removed segments (gray, dashed)
            if removed_segments:
                removed_lines = LineCollection(removed_segments, colors=config.VIZ_REMOVED_COLOR, linewidths=config.REMOVED_LINE_WIDTH, linestyles='--', label='Removed Segments')
                ax.add_collection(removed_lines)

            # Plot state icon segments (purple)
            if positioned_state_segments:
                state_lines = LineCollection(positioned_state_segments, colors=config.VIZ_STATE_COLOR, linewidths=config.STATE_LINE_WIDTH, label='State Icon Segments')
                ax.add_collection(state_lines)
            
            # Plot merged light red area (light coral)
            if merged_light_red_area and not merged_light_red_area.is_empty:
                if isinstance(merged_light_red_area, ShapelyPolygon):
                    x, y = merged_light_red_area.exterior.xy
                    ax.fill(x, y, facecolor=config.VIZ_MERGED_AREA_COLOR, alpha=config.VIZ_MERGED_AREA_ALPHA, label='Merged Light Red Area')
                elif isinstance(merged_light_red_area, MultiPolygon):
                    for poly in merged_light_red_area.geoms:
                        x, y = poly.exterior.xy
                        ax.fill(x, y, facecolor=config.VIZ_MERGED_AREA_COLOR, alpha=config.VIZ_MERGED_AREA_ALPHA)

            # Plot third state rectangle (green)
            if third_state_rectangle:
                x, y = third_state_rectangle.exterior.xy
                ax.plot(x, y, color=config.VIZ_THIRD_STATE_COLOR, linewidth=config.MAIN_BORDER_LINE_WIDTH, linestyle='--', label='Third State Rectangle')

            # Plot fourth state rectangle (orange)
            if fourth_state_rectangle:
                x, y = fourth_state_rectangle.exterior.xy
                ax.plot(x, y, color=config.VIZ_FOURTH_STATE_COLOR, linewidth=config.MAIN_BORDER_LINE_WIDTH, linestyle='--', label='Fourth State Rectangle')

            # Plot extreme points
            if extreme_points:
                for point_name, coords in extreme_points.items():
                    ax.scatter(coords[0], coords[1], c=config.VIZ_EXTREME_POINT_COLOR, s=config.VIZ_EXTREME_POINT_SIZE, label=point_name if point_name == 'leftmost' else '')
                    ax.annotate(point_name, (coords[0], coords[1]), xytext=(config.TEXT_OFFSET_X, config.TEXT_OFFSET_Y), textcoords='offset points')
            
            # Plot main icon border (black dashed)
            main_border = Rectangle(
                (main_icon_x, main_icon_y), main_scaled_width, main_scaled_height,
                fill=False, color=config.VIZ_MAIN_BORDER_COLOR, linestyle='--', linewidth=config.MAIN_BORDER_LINE_WIDTH, label='Main Icon Border'
            )
            ax.add_patch(main_border)

            # Plot state canvas border (blue dashed, thick)
            state_canvas_border = Rectangle(
                (state_position_x, state_position_y), state_width, state_height,
                fill=False, color=config.VIZ_STATE_CANVAS_BORDER_COLOR, linestyle='--', linewidth=config.STATE_CANVAS_BORDER_LINE_WIDTH, label='State Canvas Border'
            )
            ax.add_patch(state_canvas_border)

            # Plot state object border (red dashed, positioned)
            if state_segments:
                state_obj_border = Rectangle(
                    (state_position_x + state_obj_min_x, state_position_y + state_obj_min_y),
                    state_obj_width, state_obj_height,
                    fill=False, color=config.VIZ_STATE_OBJECT_BORDER_COLOR, linestyle='--', linewidth=config.STATE_OBJECT_BORDER_LINE_WIDTH, label='State Object Border'
                )
                ax.add_patch(state_obj_border)
            
            # Enhanced stats text with requested legend details
            main_canvas_width, main_canvas_height = main_icon_data['main_canvas_dimensions']
            main_icon_canvas = f"1024 * ASPECT_RATIO x 1024 * ASPECT_RATIO" if main_icon_data['scale_factor'] < 1.0 else f"{main_scaled_width:.1f} x {main_scaled_height:.1f} (no scaling)"
            orientation_explanation = (
                f"{'W/H' if main_icon_aspect_ratio >= 1 else 'H/W'} ratio = {main_icon_aspect_ratio:.2f}"
            )
            
            stats_text = (
                f"Full Icon Canvas: {canvas_width} x {canvas_height}\n"
                f"Main Icon Canvas: {main_canvas_width:.1f} x {main_canvas_height:.1f}\n"
                f"Main Icon Object: {main_scaled_width:.1f} x {main_scaled_height:.1f}\n"
                f"Type: {orientation} ({orientation_explanation})\n"
                f"Ratio: {main_icon_aspect_ratio:.2f} ({'W/H' if main_icon_aspect_ratio >= 1 else 'H/W'})\n"
                f"State Icon Canvas: {state_width} x {state_height}\n"
                f"State Icon Object: {state_obj_width:.1f} x {state_obj_height:.1f}\n"
                f"Alignment: {alignment}\n"
                f"Original Segments: {len(main_segments)}\n"
                f"Clipped Segments: {len(clipped_segments)}\n"
                f"Removed Segments: {len(removed_segments)}\n"
                f"Intersecting Segments: {len(intersecting_segments)}"
            )
            ax.text(config.STATS_TEXT_X, config.ASPECT_RATIO, stats_text, transform=ax.transAxes, fontsize=config.STATS_TEXT_FONT_SIZE,
                    verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

            # Configure plot
            ax.set_xlim(-config.PLOT_MARGIN, canvas_width + config.PLOT_MARGIN)
            ax.set_ylim(canvas_height + config.PLOT_MARGIN, -config.PLOT_MARGIN)  # Flipped y-axis
            ax.set_aspect('equal')
            ax.legend(loc='lower right', fontsize=config.LEGEND_FONT_SIZE)
            ax.set_title(f'SVG Icon Merge - Alignment: {alignment}')
            ax.grid(True, alpha=config.GRID_ALPHA)
            plt.show()
        
        return {
            'original_segments': main_segments,
            'non_intersecting_segments': non_intersecting_segments,
            'intersecting_segments': intersecting_segments,
            'clipped_segments': clipped_segments,
            'removed_segments': removed_segments,
            'clipping_info': intersection_info,
            'positioned_state_segments': positioned_state_segments,
            'merged_light_red_area': merged_light_red_area,
            'intersection_points': intersection_points,
            'buffer_area_stroke': buffer_area_stroke,
            'buffer_area_convex': buffer_area_convex,
            'extreme_points': extreme_points,
            'third_state_rectangle': third_state_rectangle,
            'fourth_state_rectangle': fourth_state_rectangle,
            'state_object_bounds': {
                'min_x': state_obj_min_x,
                'min_y': state_obj_min_y,
                'max_x': state_obj_max_x,
                'max_y': state_obj_max_y,
                'width': state_obj_width,
                'height': state_obj_height
            }
        }
        
    except Exception as e:
        return None
    
def save_clipped_result_to_svg(merged_data, output_svg_path, canvas_width=None, canvas_height=None,
                                main_stroke_width=None, state_stroke_width=None,
                                main_color=None, state_color=None, config=None):
    """
    Save the clipped result to SVG file with customizable colors
    Uses path elements instead of line elements

    Args:
        config: CombineConfig instance for configuration values
    """
    try:
        # Initialize configuration
        if config is None:
            config = CombineConfig()

        # Set default values from config
        if canvas_width is None:
            canvas_width = config.DEFAULT_FINAL_CANVAS_WIDTH
        if canvas_height is None:
            canvas_height = config.DEFAULT_FINAL_CANVAS_HEIGHT
        if main_stroke_width is None:
            main_stroke_width = config.DEFAULT_MAIN_STROKE_WIDTH
        if state_stroke_width is None:
            state_stroke_width = config.DEFAULT_STATE_STROKE_WIDTH
        if main_color is None:
            main_color = config.DEFAULT_MAIN_COLOR
        if state_color is None:
            state_color = config.DEFAULT_STATE_COLOR

        if not merged_data:
            print("No merged data available to save")
            return False
        
        # Get the clipped segments and positioned state segments
        clipped_segments = merged_data.get('clipped_segments', [])
        positioned_state_segments = merged_data.get('positioned_state_segments', [])
        
        
        def segments_to_path_data(segments):
            """Convert line segments to SVG path data"""
            if not segments:
                return ""
            
            path_commands = []
            for segment in segments:
                x1, y1 = segment[0]
                x2, y2 = segment[1]
                # Each segment becomes a Move-to and Line-to command
                path_commands.append(f"M{x1:.2f},{y1:.2f}L{x2:.2f},{y2:.2f}")
            
            return " ".join(path_commands)
        
        # Convert segments to path data
        main_path_data = segments_to_path_data(clipped_segments)
        state_path_data = segments_to_path_data(positioned_state_segments)
        
        # Create SVG content
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{canvas_width}" height="{canvas_height}" viewBox="0 0 {canvas_width} {canvas_height}" 
     xmlns="http://www.w3.org/2000/svg">
  
  <!-- Main Icon (Clipped) -->
  <g id="main-icon-clipped" stroke="{main_color}" stroke-width="{main_stroke_width}" fill="none" stroke-linecap="round" stroke-linejoin="round">
'''
        
        # Add main icon path (clipped)
        if main_path_data:
            svg_content += f'    <path d="{main_path_data}"/>\n'
        
        svg_content += f'''  </g>
  
  <!-- State Icon -->
  <g id="state-icon" stroke="{state_color}" stroke-width="{state_stroke_width}" fill="none" stroke-linecap="round" stroke-linejoin="round">
'''
        
        # Add state icon path
        if state_path_data:
            svg_content += f'    <path d="{state_path_data}"/>\n'
        
        svg_content += '''  </g>
</svg>'''
        
        # Write to file
        with open(output_svg_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"Successfully saved clipped result to: {output_svg_path}")
        print(f"Main icon segments ({main_color}): {len(clipped_segments)}")
        print(f"State icon segments ({state_color}): {len(positioned_state_segments)}")
        
        return True
        
    except Exception as e:
        print(f"Error saving clipped result to SVG: {e}")
        return False


def save_clipped_result_to_svg_with_scaling(merged_data, output_svg_path,
                                          processing_canvas_width, processing_canvas_height,
                                          final_canvas_width, final_canvas_height, scale_factor,
                                          main_stroke_width=None, state_stroke_width=None,
                                          main_color=None, state_color=None, config=None):
    """
    Save the clipped result to SVG file with scaling from processing canvas to final canvas
    """
    try:
        # Initialize configuration
        if config is None:
            config = CombineConfig()

        # Set default values from config
        if main_stroke_width is None:
            main_stroke_width = config.DEFAULT_MAIN_STROKE_WIDTH
        if state_stroke_width is None:
            state_stroke_width = config.DEFAULT_STATE_STROKE_WIDTH
        if main_color is None:
            main_color = config.DEFAULT_MAIN_COLOR
        if state_color is None:
            state_color = config.DEFAULT_STATE_COLOR

        if not merged_data:
            print("No merged data available to save")
            return False

        # Get the clipped segments and positioned state segments
        clipped_segments = merged_data.get('clipped_segments', [])
        positioned_state_segments = merged_data.get('positioned_state_segments', [])

        def scale_segments(segments, scale_factor, processing_canvas_width, processing_canvas_height,
                          final_canvas_width, final_canvas_height):
            """Scale segments from processing canvas to final canvas"""
            if not segments:
                return []

            scaled_segments = []
            for segment in segments:
                # Scale coordinates
                x1, y1 = segment[0]
                x2, y2 = segment[1]

                # Apply scaling
                x1_scaled = x1 * scale_factor
                y1_scaled = y1 * scale_factor
                x2_scaled = x2 * scale_factor
                y2_scaled = y2 * scale_factor

                # Center in final canvas
                processing_center_x = processing_canvas_width / 2
                processing_center_y = processing_canvas_height / 2
                final_center_x = final_canvas_width / 2
                final_center_y = final_canvas_height / 2

                # Translate to final canvas center
                offset_x = final_center_x - (processing_center_x * scale_factor)
                offset_y = final_center_y - (processing_center_y * scale_factor)

                x1_final = x1_scaled + offset_x
                y1_final = y1_scaled + offset_y
                x2_final = x2_scaled + offset_x
                y2_final = y2_scaled + offset_y

                scaled_segments.append([(x1_final, y1_final), (x2_final, y2_final)])

            return scaled_segments

        # Scale both segment sets
        scaled_main_segments = scale_segments(clipped_segments, scale_factor,
                                            processing_canvas_width, processing_canvas_height,
                                            final_canvas_width, final_canvas_height)
        scaled_state_segments = scale_segments(positioned_state_segments, scale_factor,
                                             processing_canvas_width, processing_canvas_height,
                                             final_canvas_width, final_canvas_height)

        def segments_to_path_data(segments):
            """Convert line segments to SVG path data"""
            if not segments:
                return ""

            path_commands = []
            for segment in segments:
                x1, y1 = segment[0]
                x2, y2 = segment[1]
                # Each segment becomes a Move-to and Line-to command
                path_commands.append(f"M{x1:.2f},{y1:.2f}L{x2:.2f},{y2:.2f}")

            return " ".join(path_commands)

        # Convert segments to path data
        main_path_data = segments_to_path_data(scaled_main_segments)
        state_path_data = segments_to_path_data(scaled_state_segments)

        # Scale stroke widths proportionally
        scaled_main_stroke = main_stroke_width * scale_factor
        scaled_state_stroke = state_stroke_width * scale_factor

        # Create SVG content
        svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{final_canvas_width}" height="{final_canvas_height}" viewBox="0 0 {final_canvas_width} {final_canvas_height}"
     xmlns="http://www.w3.org/2000/svg">

  <!-- Main Icon (Clipped, Scaled) -->
  <g id="main-icon-clipped" stroke="{main_color}" stroke-width="{scaled_main_stroke:.2f}" fill="none" stroke-linecap="round" stroke-linejoin="round">
'''

        # Add main icon path (clipped and scaled)
        if main_path_data:
            svg_content += f'    <path d="{main_path_data}"/>\n'

        svg_content += f'''  </g>

  <!-- State Icon (Scaled) -->
  <g id="state-icon" stroke="{state_color}" stroke-width="{scaled_state_stroke:.2f}" fill="none" stroke-linecap="round" stroke-linejoin="round">
'''

        # Add state icon path
        if state_path_data:
            svg_content += f'    <path d="{state_path_data}"/>\n'

        svg_content += '''  </g>
</svg>'''

        # Write to file
        with open(output_svg_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)

        print(f"Successfully saved scaled result to: {output_svg_path}")
        print(f"Scaled from {processing_canvas_width:.1f}x{processing_canvas_height:.1f} to {final_canvas_width}x{final_canvas_height} (scale: {scale_factor:.3f})")
        print(f"Main icon segments ({main_color}): {len(scaled_main_segments)}")
        print(f"State icon segments ({state_color}): {len(scaled_state_segments)}")

        return True

    except Exception as e:
        print(f"Error saving scaled result to SVG: {e}")
        return False


# Functions now imported from process_main.py and process_state.py
        
def process_svg_icons_4_steps_with_dynamic_alignment(main_svg_path, state_svg_path, output_svg_path,
                                                    main_canvas_width=None, main_canvas_height=None,
                                                    state_width=None, state_height=None,
                                                    final_canvas_width=None, final_canvas_height=None,
                                                    show_matplotlib=False, stroke_width=None, buffer_radius=None,
                                                    main_color=None, state_color=None,
                                                    main_stroke_width=None, state_stroke_width=None, position='bottom-right',
                                                    is_text=False, config=None, is_custom_center_point=False,
                                                    center_point_x=None, center_point_y=None, is_shifted=False):
    """
    Enhanced version that automatically determines alignment based on main icon properties

    Args:
        main_svg_path: Path to the main SVG icon file
        state_svg_path: Path to the state SVG icon file
        output_svg_path: Path where the combined result will be saved
        main_canvas_width: Width of main icon canvas (default from config)
        main_canvas_height: Height of main icon canvas (default from config)
        state_width: Width of state icon canvas (default from config, ignored if is_text=True)
        state_height: Height of state icon canvas (default from config)
        final_canvas_width: Width of final combined canvas (default from config)
        final_canvas_height: Height of final combined canvas (default from config)
        show_matplotlib: Whether to show matplotlib visualization (default False)
        stroke_width: Width of stroke for processing (default from config)
        buffer_radius: Radius for buffer calculations (default from config)
        main_color: Color for main icon in output (default from config)
        state_color: Color for state icon in output (default from config)
        main_stroke_width: Stroke width for main icon in output (default from config)
        state_stroke_width: Stroke width for state icon in output (default from config)
        position: Position alignment for state icon (default 'bottom-right')
        is_text: If True, calculate dynamic state canvas width based on content while keeping height=512 (default False)
        config: CombineConfig instance for configuration values
        is_custom_center_point: If True, use custom center point for state icon positioning (default False)
        center_point_x: X coordinate for custom center point (used when is_custom_center_point=True)
        center_point_y: Y coordinate for custom center point (used when is_custom_center_point=True)
        is_shifted: If True, use alignment-based positioning with offsets instead of centering formula (default False)
    """
    try:
        print('state_height, state_width', state_height, state_width)
        # Initialize configuration
        if config is None:
            config = CombineConfig()

        # Set default values from config
        if main_canvas_width is None:
            main_canvas_width = config.DEFAULT_MAIN_CANVAS_WIDTH
        if main_canvas_height is None:
            main_canvas_height = config.DEFAULT_MAIN_CANVAS_HEIGHT
        if state_width is None:
            state_width = config.DEFAULT_STATE_WIDTH
        if state_height is None:
            state_height = config.DEFAULT_STATE_HEIGHT
        if final_canvas_width is None:
            final_canvas_width = config.DEFAULT_FINAL_CANVAS_WIDTH
        if final_canvas_height is None:
            final_canvas_height = config.DEFAULT_FINAL_CANVAS_HEIGHT
        if stroke_width is None:
            stroke_width = config.DEFAULT_STROKE_WIDTH
        if buffer_radius is None:
            buffer_radius = config.DEFAULT_BUFFER_RADIUS
        if main_color is None:
            main_color = config.DEFAULT_MAIN_COLOR
        if state_color is None:
            state_color = config.DEFAULT_STATE_COLOR
        if main_stroke_width is None:
            main_stroke_width = config.SAVE_MAIN_STROKE_WIDTH
        if state_stroke_width is None:
            state_stroke_width = config.SAVE_STATE_STROKE_WIDTH
        print("="*60)
        print("STARTING 4-STEP SVG ICON PROCESSING WITH DYNAMIC ALIGNMENT")
        print("="*60)

        # STEP 1: First analyze main icon to calculate scaling, then determine positioning
        print("\n" + "="*50)
        print("PRE-STEP: Analyzing main icon for scaling and positioning")

        # Quick parse to get main icon properties for scaling calculation
        segments, _ = parse_svg_geometric_elements(ET.parse(main_svg_path).getroot())

        if not segments:
            print("No valid segments found in main SVG")
            return None

        # Get all points from segments to calculate bounds
        all_points = []
        for segment in segments:
            all_points.extend(segment)

        # Get original bounds
        all_points_array = np.array(all_points)
        min_x, min_y = np.min(all_points_array, axis=0)
        max_x, max_y = np.max(all_points_array, axis=0)
        original_width = max_x - min_x
        original_height = max_y - min_y

        # Calculate aspect ratio and scaling (using same logic as process_main.py)
        if original_width > original_height:
            aspect_ratio = original_width / original_height if original_height > 0 else float('inf')
            orientation = "Horizontal"
        elif original_height > original_width:
            aspect_ratio = original_height / original_width if original_width > 0 else float('inf')
            orientation = "Vertical"
        else:
            aspect_ratio = 1.0
            orientation = "Square"

        # Calculate scaling factor using position-specific aspect ratio
        if position == 'center':
            # For center position, use 100% scale (no scaling)
            scale = 1.0
            print(f"Center position: using 100% scale (no scaling)")
        else:
            position_aspect_ratio = get_aspect_ratio(position)
            if aspect_ratio > ASPECT_RATIO_THRESHOLD:
                scale = position_aspect_ratio
            else:
                scale_x = (1024 * position_aspect_ratio) / original_width if original_width > 0 else position_aspect_ratio
                scale_y = (1024 * position_aspect_ratio) / original_height if original_height > 0 else position_aspect_ratio
                scale = min(scale_x, scale_y)

        # Calculate scaled dimensions
        scaled_width = original_width * scale
        scaled_height = original_height * scale

        print(f"Original dimensions: {original_width:.1f} x {original_height:.1f}")
        print(f"Scale factor: {scale:.3f}")
        print(f"Scaled dimensions: {scaled_width:.1f} x {scaled_height:.1f}")

        # Now calculate position using scaled dimensions
        print('state_icon_alignment before calculation', position)
        if position == 'center':
            # For center position, place main icon at the center of the canvas
            x = (final_canvas_width - scaled_width) / 2
            y = (final_canvas_height - scaled_height) / 2
            print(f"Center position: main icon at ({x:.1f}, {y:.1f})")
        else:
            x, y, _ = calculate_main_icon_position(position, scaled_width, scaled_height, final_canvas_width)

        # Apply thin icon offset adjustments
        if aspect_ratio > ASPECT_RATIO_THRESHOLD:
            # Determine actual main icon position based on state icon position
            main_icon_position = state_alignment_map_to_main_icon.get(position, position)

            print(f"Applying thin icon offset for aspect ratio: {aspect_ratio:.2f}")
            print(f"State icon position: {position} -> Main icon position: {main_icon_position}")
            adjusted_x, adjusted_y = apply_thin_icon_offset(
                x, y, aspect_ratio, orientation, main_icon_position,
                final_canvas_width, final_canvas_height
            )
            print(f"Original position: ({x}, {y}) -> Adjusted position: ({adjusted_x}, {adjusted_y})")
            x, y = adjusted_x, adjusted_y

        print(f"Initial determined position: ({x}, {y})")

        # Handle text icons - calculate dynamic width while keeping height at 512
        if is_text:
            print("Processing as text icon - calculating dynamic state canvas with proportional scaling")

            # Parse the state SVG to get its natural dimensions
            try:
                state_tree = ET.parse(state_svg_path)
                state_root = state_tree.getroot()
                _, state_points = parse_svg_geometric_elements(state_root)

                if state_points:
                    state_points_array = np.array(state_points)
                    state_min_x, state_min_y = np.min(state_points_array, axis=0)
                    state_max_x, state_max_y = np.max(state_points_array, axis=0)
                    state_natural_width = state_max_x - state_min_x
                    state_natural_height = state_max_y - state_min_y

                    # Calculate scales for both dimensions
                    if state_natural_height > 0 and state_natural_width > 0:
                        scale_for_height = state_height / state_natural_height
                        calculated_width = state_natural_width * scale_for_height

                        # Apply maximum width constraint for long text
                        maximum_width = 920

                        if calculated_width > maximum_width:
                            # Recalculate scale based on width constraint
                            scale_for_width = maximum_width / state_natural_width
                            # Use the more restrictive scale to maintain proportions
                            final_scale = min(scale_for_height, scale_for_width)

                            state_width = state_natural_width * final_scale
                            state_height = state_natural_height * final_scale

                            print(f"Width {calculated_width:.1f} exceeds maximum {maximum_width}")
                            print(f"Using width-constrained scale: {final_scale:.3f}")
                            print(f"Final dimensions: {state_width:.1f} x {state_height:.1f} (proportionally scaled)")
                        else:
                            # Use height-based scaling
                            state_width = calculated_width
                            print(f"Using height-based scale: {scale_for_height:.3f}")
                            print(f"Final dimensions: {state_width:.1f} x {state_height} (height-constrained)")

                        print(f"State icon natural dimensions: {state_natural_width:.1f} x {state_natural_height:.1f}")
                    else:
                        print("Warning: State icon has zero dimensions, using default state width")
                else:
                    print("Warning: No valid elements found in state SVG, using default state width")
            except Exception as e:
                print(f"Warning: Could not calculate dynamic state dimensions: {e}, using default state width")

        # Calculate initial state icon canvas position based on determined alignment or custom center point
        if is_custom_center_point and center_point_x is not None and center_point_y is not None:
            # Convert to float in case they're passed as strings from JSON
            center_x = float(center_point_x)
            center_y = float(center_point_y)
            print(f"Using custom center point: ({center_x}, {center_y})")

            # Calculate state icon position so that its center aligns with the custom center point
            if is_shifted:
                # Use alignment-based positioning plus the x and y offsets
                if position == "top-left":
                    base_x, base_y = 0, 0
                elif position == "top":
                    base_x, base_y = (final_canvas_width - state_width) / 2, 0
                elif position == "top-right":
                    base_x, base_y = final_canvas_width - state_width, 0
                elif position == "left":
                    base_x, base_y = 0, (final_canvas_height - state_height) / 2
                elif position == "middle" or position == "center":
                    base_x, base_y = (final_canvas_width - state_width) / 2, (final_canvas_height - state_height) / 2
                elif position == "right":
                    base_x, base_y = final_canvas_width - state_width, (final_canvas_height - state_height) / 2
                elif position == "bottom-left":
                    base_x, base_y = 0, final_canvas_height - state_height
                elif position == "bottom":
                    base_x, base_y = (final_canvas_width - state_width) / 2, final_canvas_height - state_height
                elif position == "bottom-right":
                    base_x, base_y = final_canvas_width - state_width, final_canvas_height - state_height
                else:
                    base_x, base_y = final_canvas_width - state_width, final_canvas_height - state_height

                # Add the x and y offsets to the alignment-based position
                state_position_x = base_x + center_x
                state_position_y = base_y + center_y
                print(f"Shifted positioning: base position ({base_x:.1f}, {base_y:.1f}) + offset ({center_x}, {center_y}) = ({state_position_x:.1f}, {state_position_y:.1f})")
            else:
                # The center of the state icon canvas should match the provided center point
                state_position_x = center_x - (state_width / 2)
                state_position_y = center_y - (state_height / 2)

            print(f"Custom center point state icon position: ({state_position_x:.1f}, {state_position_y:.1f}) to center {state_width:.1f} x {state_height} canvas at ({center_x}, {center_y})")
        else:
            # Use standard alignment-based positioning
            if position == "top-left":
                state_position_x, state_position_y = 0, 0
            elif position == "top":
                state_position_x, state_position_y = (final_canvas_width - state_width) / 2, 0
            elif position == "top-right":
                state_position_x, state_position_y = final_canvas_width - state_width, 0
            elif position == "left":
                state_position_x, state_position_y = 0, (final_canvas_height - state_height) / 2
            elif position == "middle":
                state_position_x, state_position_y = (final_canvas_width - state_width) / 2, (final_canvas_height - state_height) / 2
            elif position == "center":
                state_position_x, state_position_y = (final_canvas_width - state_width) / 2, (final_canvas_height - state_height) / 2
            elif position == "right":
                state_position_x, state_position_y = final_canvas_width - state_width, (final_canvas_height - state_height) / 2
            elif position == "bottom-left":
                state_position_x, state_position_y = 0, final_canvas_height - state_height
            elif position == "bottom":
                state_position_x, state_position_y = (final_canvas_width - state_width) / 2, final_canvas_height - state_height
            elif position == "bottom-right":
                state_position_x, state_position_y = final_canvas_width - state_width, final_canvas_height - state_height

            print(f"Initial state icon position: ({state_position_x:.1f}, {state_position_y:.1f}) based on alignment '{position}' with state canvas: {state_width:.1f} x {state_height}")

        # Apply centering after thin icon offset adjustments (skip if using custom center point)
        if is_custom_center_point:
            print("\n" + "="*50)
            print("CUSTOM CENTER POINT: Calculating combined bounding box and rescaling if needed")

            # Calculate combined bounding box
            main_icon_width, main_icon_height = scaled_width, scaled_height
            combined_left, combined_top, combined_width, combined_height = calculate_combined_bounding_box(
                x, y, main_icon_width, main_icon_height,
                state_position_x, state_position_y, state_width, state_height
            )

            print(f"Combined bounding box: ({combined_left:.1f}, {combined_top:.1f}) {combined_width:.1f}x{combined_height:.1f}")
            print(f"Canvas size: {final_canvas_width}x{final_canvas_height}")

            # Check if rescaling is needed (with some margin for safety)
            margin = 20  # 20px margin
            max_allowed_width = final_canvas_width - 2 * margin
            max_allowed_height = final_canvas_height - 2 * margin

            scale_factor = 1.0
            # Check if combined result exceeds canvas boundaries
            exceeds_boundaries = (
                combined_left < 0 or
                combined_top < 0 or
                combined_left + combined_width > final_canvas_width or
                combined_top + combined_height > final_canvas_height
            )

            if combined_width > max_allowed_width or combined_height > max_allowed_height or exceeds_boundaries:
                # Calculate scale factor to fit within full canvas (not just margin-reduced area)
                scale_x = final_canvas_width / combined_width if combined_width > 0 else 1.0
                scale_y = final_canvas_height / combined_height if combined_height > 0 else 1.0
                scale_factor = min(scale_x, scale_y)
                print(f"Rescaling needed: scale_factor = {scale_factor:.3f} (calculated to use full canvas)")

                # Calculate required canvas size to accommodate the unscaled result
                required_canvas_width = combined_width + 2 * margin
                required_canvas_height = combined_height + 2 * margin

                print(f"Required canvas size: {required_canvas_width:.1f} x {required_canvas_height:.1f}")
                print(f"Will process with larger virtual canvas and scale down the final result")

                # Adjust positions to center in the larger virtual canvas
                virtual_canvas_center_x = required_canvas_width / 2
                virtual_canvas_center_y = required_canvas_height / 2

                current_combined_center_x = combined_left + combined_width / 2
                current_combined_center_y = combined_top + combined_height / 2

                # Calculate offsets to center the combined result in virtual canvas
                offset_x = virtual_canvas_center_x - current_combined_center_x
                offset_y = virtual_canvas_center_y - current_combined_center_y

                # Apply centering offsets
                x += offset_x
                y += offset_y
                state_position_x += offset_x
                state_position_y += offset_y

                # Store scale factor and virtual canvas size for later use in SVG generation
                virtual_canvas_width = required_canvas_width
                virtual_canvas_height = required_canvas_height

                print(f"Virtual canvas: {virtual_canvas_width:.1f} x {virtual_canvas_height:.1f}")
                print(f"Adjusted positions - Main: ({x:.1f}, {y:.1f}), State: ({state_position_x:.1f}, {state_position_y:.1f})")
            else:
                # No rescaling needed, but still apply centering
                virtual_canvas_width = final_canvas_width
                virtual_canvas_height = final_canvas_height
                scale_factor = 1.0
                print("No rescaling needed - combined result fits within canvas")

                # Apply final centering to ensure proper positioning in 1024x1024 canvas
                centered_main_x, centered_main_y, centered_state_x, centered_state_y = center_combined_result(
                    x, y, main_icon_width, main_icon_height,
                    state_position_x, state_position_y, state_width, state_height,
                    final_canvas_width, final_canvas_height
                )

                print(f"Applying final centering - Main: ({x:.1f}, {y:.1f}) -> ({centered_main_x:.1f}, {centered_main_y:.1f})")
                print(f"Applying final centering - State: ({state_position_x:.1f}, {state_position_y:.1f}) -> ({centered_state_x:.1f}, {centered_state_y:.1f})")

                # Update positions
                x, y = centered_main_x, centered_main_y
                state_position_x, state_position_y = centered_state_x, centered_state_y

            print(f"Final positions - Main: ({x:.1f}, {y:.1f}), State: ({state_position_x:.1f}, {state_position_y:.1f})")
        else:
            print("\n" + "="*50)
            print("CENTERING: Calculating combined bounding box and centering result")

            # Get main icon dimensions from processed data
            main_icon_width, main_icon_height = scaled_width, scaled_height

            print(f"Before centering - Main: ({x:.1f}, {y:.1f}), State: ({state_position_x:.1f}, {state_position_y:.1f})")

            # Center the combined result
            centered_main_x, centered_main_y, centered_state_x, centered_state_y = center_combined_result(
                x, y, main_icon_width, main_icon_height,
                state_position_x, state_position_y, state_width, state_height,
                final_canvas_width, final_canvas_height
            )

            print(f"Main icon: ({x:.1f}, {y:.1f}) -> ({centered_main_x:.1f}, {centered_main_y:.1f})")
            print(f"State icon: ({state_position_x:.1f}, {state_position_y:.1f}) -> ({centered_state_x:.1f}, {centered_state_y:.1f})")

            # Calculate and display the offset applied
            offset_x = centered_main_x - x
            offset_y = centered_main_y - y
            print(f"Centering offset applied: ({offset_x:.1f}, {offset_y:.1f})")

            # Update positions for processing
            x, y = centered_main_x, centered_main_y
            state_position_x, state_position_y = centered_state_x, centered_state_y

            print(f"Final centered positions - Main: ({x:.1f}, {y:.1f}), State: ({state_position_x:.1f}, {state_position_y:.1f})")

        # STEP 1: Process main icon with final centered position
        print("\n" + "="*50)
        # Use virtual canvas size when custom center point requires larger space
        if is_custom_center_point:
            processing_canvas_width = virtual_canvas_width
            processing_canvas_height = virtual_canvas_height
        else:
            processing_canvas_width = final_canvas_width
            processing_canvas_height = final_canvas_height

        main_icon_data = process_main_icon_with_dynamic_positioning(main_svg_path, x, y, processing_canvas_width, processing_canvas_height, position)
        if not main_icon_data:
            print("Failed at Step 1: Processing main icon")
            return None

        # STEP 2: Process state icon with determined alignment
        print("\n" + "="*50)
        state_icon_data = process_state_icon(state_svg_path, state_width, state_height, buffer_radius, position)
        if not state_icon_data:
            print("Failed at Step 2: Processing state icon")
            return None

        # STEP 3: Merge icons and clip segments
        print("\n" + "="*50)
        merged_data = merged_icons_and_remove_overlapping(
            main_icon_data, state_icon_data,
            state_position_x, state_position_y,
            processing_canvas_width, processing_canvas_height,
            show_matplotlib, alignment=position, config=config
        )
    
        # STEP 4: Save the clipped result to SVG
        if merged_data:
            print("\n" + "="*50)
            print("STEP 4: Saving clipped result to SVG")
            
            # Add scale factor and canvas size info for custom center point scaling
            if is_custom_center_point:
                save_success = save_clipped_result_to_svg_with_scaling(
                    merged_data,
                    output_svg_path,
                    processing_canvas_width, processing_canvas_height,
                    final_canvas_width, final_canvas_height,
                    scale_factor,
                    main_stroke_width=main_stroke_width,
                    state_stroke_width=state_stroke_width,
                    main_color=main_color,
                    state_color=state_color,
                    config=config
                )
            else:
                save_success = save_clipped_result_to_svg(
                    merged_data,
                    output_svg_path,
                    final_canvas_width,
                    final_canvas_height,
                    main_stroke_width=main_stroke_width,
                    state_stroke_width=state_stroke_width,
                    main_color=main_color,
                    state_color=state_color,
                    config=config
                )
            
            step4_saved = save_success
            if save_success:
                print(f"✓ Successfully saved to: {output_svg_path}")
            else:
                print("✗ Failed to save SVG file")
        else:
            step4_saved = False
        
        return {
            'step1_main_icon': main_icon_data,
            'step2_state_icon': state_icon_data,
            'step3_merged': merged_data,
            'step4_saved': step4_saved,
            'output_path': output_svg_path,
            'determined_alignment': position
        }
        
    except Exception as e:
        print(f"Error in enhanced 4-step processing: {e}")
        return None


# Example usage with dynamic alignment
if __name__ == "__main__":
    # Create a custom configuration or use defaults
    config = CombineConfig()

    is_text = False
    if is_text:
        config.DEFAULT_STATE_HEIGHT = 330

    # Example with text combination (dynamic width, height=512)
    result = process_svg_icons_4_steps_with_dynamic_alignment(
        main_svg_path='5750e430-753a-4a39-bed0-3831d4899816.svg',
        state_svg_path='(square_circle)_(572c8adc-4237-4879-b02b-30d084c17f24).svg',
        output_svg_path='file_svg.svg',
        stroke_width=30,
        buffer_radius=config.EXAMPLE_BUFFER_RADIUS,
        main_color=config.DEFAULT_BLACK_COLOR,
        state_color=config.DEFAULT_BLACK_COLOR,
        position='bottom-right',
        is_text=False,  # Dynamic width based on text, height=512
        config=config,
        is_custom_center_point=True,
        center_point_x=600,
        center_point_y=900,
        show_matplotlib=True
    )

    if result and result['step4_saved']:
        print("✓ Example combination completed successfully")
    else:
        print("✗ Example combination failed")
