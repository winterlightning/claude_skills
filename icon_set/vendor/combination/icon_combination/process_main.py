import os
import numpy as np
import xml.etree.ElementTree as ET
from .utils import parse_svg_geometric_elements, parse_svg_path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from .constants import ASPECT_RATIO, ASPECT_RATIO_THRESHOLD, get_aspect_ratio


def _remove_clip_path_elements(root):
    """Remove clip path related elements to prevent squares around items"""
    ns = {'svg': 'http://www.w3.org/2000/svg'}

    # Remove clip-path attributes from all elements
    for elem in root.iter():
        if 'clip-path' in elem.attrib:
            del elem.attrib['clip-path']

    # Before removing defs, clipPath, and mask elements, preserve any geometric elements within them
    preserved_elements = []

    # Extract geometric elements from defs, clipPath, and mask before removal
    for container_tag in ['defs', 'clipPath', 'mask']:
        for container in root.findall(f'.//{{{ns["svg"]}}}{container_tag}'):
            # Find all geometric elements within this container
            for geom_tag in ['circle', 'ellipse', 'rect', 'line', 'polygon', 'polyline', 'path']:
                for elem in container.findall(f'.//{{{ns["svg"]}}}{geom_tag}'):
                    preserved_elements.append(elem)
                # Also check without namespace
                for elem in container.findall(f'.//{geom_tag}'):
                    preserved_elements.append(elem)

    # Add preserved elements directly to the root before removing containers
    for elem in preserved_elements:
        root.append(elem)

    # Remove defs elements (after preserving geometric content)
    for defs in root.findall('.//{http://www.w3.org/2000/svg}defs'):
        for parent in root.iter():
            if defs in parent:
                parent.remove(defs)
                break

    # Remove clipPath elements (after preserving geometric content)
    for clipPath in root.findall('.//{http://www.w3.org/2000/svg}clipPath'):
        for parent in root.iter():
            if clipPath in parent:
                parent.remove(clipPath)
                break

    # Remove mask elements (after preserving geometric content)
    for mask in root.findall('.//{http://www.w3.org/2000/svg}mask'):
        for parent in root.iter():
            if mask in parent:
                parent.remove(mask)
                break

# Constants are now imported from constants.py

# def determine_alignment_from_main_icon(main_icon_data, state_icon_alignment='bottom-right'):
#     """
#     Determine state icon alignment based on main icon's orientation and W/H ratio
#     """
#     orientation = main_icon_data.get('orientation', 'Square')
#     aspect_ratio = main_icon_data.get('aspect_ratio', 1.0)

#     print(f"Main icon orientation: {orientation}")
#     print(f"Main icon aspect ratio: {aspect_ratio:.3f}")

#     print(aspect_ratio, 'aspect_ratioaspect_ratioaspect_ratio')
#     if orientation == "Horizontal" and aspect_ratio > ASPECT_RATIO_THRESHOLD:
#         alignment = "top-right"
#         print(f"Horizontal icon with W/H ratio > {ASPECT_RATIO_THRESHOLD} → using alignment: {alignment}")
#     else:
#         # Default alignment for other cases
#         alignment = "bottom-right"
#         print(f"Other case → using default alignment: {alignment}")

#     print('Determined alignment:', alignment)
#     return alignment

def process_main_icon_with_dynamic_positioning(svg_file_path, x, y, final_canvas_width=1024, final_canvas_height=1024, position='bottom-right', show_plot=False):
    """
    Enhanced version of process_main_icon with positioning based on alignment
    """
    try:
        # print(f"STEP 1: Processing main icon with dynamic positioning - {svg_file_path}")
        tree = ET.parse(svg_file_path)
        root = tree.getroot()

        # Remove clip path related elements to prevent squares around items
        _remove_clip_path_elements(root)

        # Use unified parsing function to handle all SVG elements
        all_segments, all_points = parse_svg_geometric_elements(root, 1)

        if not all_segments:
            print("No valid elements found in main SVG")
            return None

        # Extract all points from segments
        all_points = []
        for segment in all_segments:
            all_points.extend(segment)

        if not all_points:
            print("No valid paths found in main SVG")
            return None

        # Get original bounds
        all_points_array = np.array(all_points)
        min_x, min_y = np.min(all_points_array, axis=0)
        max_x, max_y = np.max(all_points_array, axis=0)
        original_width = max_x - min_x
        original_height = max_y - min_y
        # print(f"Parsed paths bounds: ({min_x:.1f}, {min_y:.1f}) to ({max_x:.1f}, {max_y:.1f})")
        # print(f"Parsed paths dimensions: {original_width:.1f} x {original_height:.1f}")

        # Calculate aspect ratio based on orientation
        if original_width > original_height:
            # Horizontal: use W/H
            aspect_ratio = original_width / original_height if original_height > 0 else float('inf')
            orientation = "Horizontal"
            ratio_description = "W/H"
        elif original_height > original_width:
            # Vertical: use H/W
            aspect_ratio = original_height / original_width if original_width > 0 else float('inf')
            orientation = "Vertical"
            ratio_description = "H/W"
        else:
            # Square: W/H = H/W = 1
            aspect_ratio = 1.0
            orientation = "Square"
            ratio_description = "W/H (square)"

        # print(f"{orientation} icon - {ratio_description} ratio: {aspect_ratio:.3f}")

        # Scaling logic using position-specific aspect ratio
        position_aspect_ratio = get_aspect_ratio(position)
        if aspect_ratio > ASPECT_RATIO_THRESHOLD:
            # Don't scale if longer_side/shorter_side > ASPECT_RATIO_THRESHOLD
            # print(f"{ratio_description} ratio {aspect_ratio:.3f} > {ASPECT_RATIO_THRESHOLD} → keeping original size (no scaling)")
            scale = position_aspect_ratio
        else:
            # Scale to 1024 * position_aspect_ratio if longer_side/shorter_side ≤ ASPECT_RATIO_THRESHOLD
            # print(f"{ratio_description} ratio {aspect_ratio:.3f} ≤ {ASPECT_RATIO_THRESHOLD} → scaling to fit within 1024 * {position_aspect_ratio} x 1024 * {position_aspect_ratio}")
            scale_x = (1024 * position_aspect_ratio) / original_width if original_width > 0 else position_aspect_ratio
            scale_y = (1024 * position_aspect_ratio) / original_height if original_height > 0 else position_aspect_ratio
            scale = min(scale_x, scale_y)

        # Calculate final scaled dimensions
        scaled_width = original_width * scale
        scaled_height = original_height * scale

        # print(f"Scale factor: {scale:.3f}")
        # print(f"Scaled dimensions: {scaled_width:.1f} x {scaled_height:.1f}")

        # Determine position based on alignment and icon properties
        final_canvas_offset_x = x
        final_canvas_offset_y = y

        # Apply transformations
        final_segments = []
        for segment in all_segments:
            final_segment = [
                (
                    (segment[0][0] - min_x) * scale + final_canvas_offset_x,
                    (segment[0][1] - min_y) * scale + final_canvas_offset_y
                ),
                (
                    (segment[1][0] - min_x) * scale + final_canvas_offset_x,
                    (segment[1][1] - min_y) * scale + final_canvas_offset_y
                )
            ]
            final_segments.append(final_segment)

        final_icon_x = final_canvas_offset_x
        final_icon_y = final_canvas_offset_y
        s_w = scaled_width
        s_h = scaled_height
        result = {
            'segments': final_segments,
            'original_bounds': (min_x, min_y, max_x, max_y),
            'scale_factor': scale,
            'main_canvas_dimensions': (s_w, s_h),
            'final_canvas_dimensions': (final_canvas_width, final_canvas_height),
            'scaled_dimensions': (s_w, s_h),
            'main_canvas_offset': (x, y),
            'icon_offset_in_main_canvas': (0, 0),
            'final_icon_position': (final_icon_x, final_icon_y),
            'aspect_ratio': aspect_ratio,  # Use the correctly calculated aspect_ratio
            'orientation': orientation,
            'calculated_ratio': aspect_ratio,
            'ratio_type': ratio_description
        }

        # Optional matplotlib visualization
        if show_plot:
            _plot_icon_processing(result, original_width, original_height)

        return result

    except Exception as e:
        print(f"Error processing main icon: {e}")
        return None

def _plot_icon_processing(result, original_width, original_height):
    """Helper function to plot icon processing visualization"""

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

    # Plot 1: Original vs Scaled bounds
    ax1.set_title('Original vs Scaled Bounds')

    # Draw original icon bounds
    orig_rect = patches.Rectangle((0, 0), original_width, original_height,
                                linewidth=2, edgecolor='red', facecolor='red', alpha=0.3)
    ax1.add_patch(orig_rect)

    # Draw scaled icon bounds
    scaled_width, scaled_height = result['scaled_dimensions']
    scaled_rect = patches.Rectangle((0, 0), scaled_width, scaled_height,
                                  linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.3)
    ax1.add_patch(scaled_rect)

    max_dim = max(original_width, original_height, scaled_width, scaled_height)
    ax1.set_xlim(-max_dim*0.1, max_dim*1.1)
    ax1.set_ylim(-max_dim*0.1, max_dim*1.1)
    ax1.set_aspect('equal')
    ax1.legend(['Original', 'Scaled'])
    ax1.grid(True, alpha=0.3)

    # Plot 2: Actual SVG content
    ax2.set_title('SVG Content')

    # Draw the actual SVG segments
    segments = result['segments']
    for segment in segments:
        x_coords = [segment[0][0], segment[1][0]]
        y_coords = [segment[0][1], segment[1][1]]
        ax2.plot(x_coords, y_coords, 'b-', linewidth=1.5, alpha=0.8)

    # Draw bounding box around SVG content
    if segments:
        all_x = [point[0] for segment in segments for point in segment]
        all_y = [point[1] for segment in segments for point in segment]
        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)

        bbox_rect = patches.Rectangle((min_x, min_y), max_x - min_x, max_y - min_y,
                                    linewidth=2, edgecolor='red', facecolor='none', alpha=0.7)
        ax2.add_patch(bbox_rect)

    ax2.set_xlim(-50, scaled_width + 50)
    ax2.set_ylim(-50, scaled_height + 50)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)

    # Plot 3: Final positioning on canvas
    ax3.set_title('Final Icon Position on Canvas')

    # Draw canvas
    canvas_width, canvas_height = result['final_canvas_dimensions']
    canvas_rect = patches.Rectangle((0, 0), canvas_width, canvas_height,
                                  linewidth=2, edgecolor='black', facecolor='lightgray', alpha=0.3)
    ax3.add_patch(canvas_rect)

    # Draw final positioned SVG content
    for segment in segments:
        x_coords = [segment[0][0], segment[1][0]]
        y_coords = [segment[0][1], segment[1][1]]
        ax3.plot(x_coords, y_coords, 'b-', linewidth=1.5, alpha=0.8)

    # Draw bounding box for the positioned icon
    x_pos, y_pos = result['final_icon_position']
    final_rect = patches.Rectangle((x_pos, y_pos), scaled_width, scaled_height,
                                 linewidth=2, edgecolor='blue', facecolor='none', alpha=0.7)
    ax3.add_patch(final_rect)

    ax3.set_xlim(-50, canvas_width + 50)
    ax3.set_ylim(-50, canvas_height + 50)
    ax3.set_aspect('equal')
    ax3.grid(True, alpha=0.3)

    # Add info text
    info_text = f"Orientation: {result['orientation']}\n"
    info_text += f"Aspect Ratio: {result['aspect_ratio']:.3f}\n"
    info_text += f"Scale Factor: {result['scale_factor']:.3f}\n"
    info_text += f"Position: ({x_pos:.1f}, {y_pos:.1f})\n"
    info_text += f"Segments: {len(segments)}"

    ax3.text(10, canvas_height - 120, info_text, fontsize=10,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    process_main_icon_with_dynamic_positioning('b60751f1-8b96-5ced-96b0-7ccbd7848e87.svg', show_plot=True)
