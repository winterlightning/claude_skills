import os
import numpy as np
import xml.etree.ElementTree as ET
from shapely.geometry import LineString, MultiPolygon, Polygon as ShapelyPolygon
from shapely.ops import unary_union
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.collections import LineCollection
from .constants import ASPECT_RATIO, get_aspect_ratio
from .utils import (
    parse_svg_geometric_elements,
    create_convex_hull_buffer,
    get_buffer_outlines,
    find_buffer_extreme_points,
    create_merged_light_red_area,
    create_third_state_rectangle,
    create_fourth_state_rectangle
)


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

def process_state_icon(svg_file_path, target_width=512, target_height=512, buffer_radius=64.0, alignment="middle"):
    """Process state icon with resizing and align object within canvas based on alignment"""
    try:
        # print(f"STEP 2: Processing state icon - {svg_file_path}")

        tree = ET.parse(svg_file_path)
        root = tree.getroot()

        # Remove clip path related elements to prevent squares around items
        _remove_clip_path_elements(root)

        # Parse all SVG elements into segments
        all_segments, all_points = parse_svg_geometric_elements(root, 1)

        if not all_points:
            print("No valid elements found in state SVG")
            return None

        # Rest of your existing code remains the same...
        all_points_array = np.array(all_points)
        min_x, min_y = np.min(all_points_array, axis=0)
        max_x, max_y = np.max(all_points_array, axis=0)

        bbox_width = max_x - min_x
        bbox_height = max_y - min_y


        # Scale to fit within target dimensions (maintain aspect ratio)

        scale_x = target_width / bbox_width if bbox_width > 0 else 1
        scale_y = target_height / bbox_height if bbox_height > 0 else 1
        scale = min(scale_x, scale_y)


        # Scale and normalize segments (move to origin first)
        scaled_segments = []
        for segment in all_segments:
            scaled_segment = [
                ((segment[0][0] - min_x) * scale, (segment[0][1] - min_y) * scale),
                ((segment[1][0] - min_x) * scale, (segment[1][1] - min_y) * scale)
            ]
            scaled_segments.append(scaled_segment)

        # Get bounds of scaled object
        if scaled_segments:
            scaled_points = []
            for segment in scaled_segments:
                scaled_points.extend(segment)
            scaled_points_array = np.array(scaled_points)
            scaled_min_x, scaled_min_y = np.min(scaled_points_array, axis=0)
            scaled_max_x, scaled_max_y = np.max(scaled_points_array, axis=0)
            scaled_obj_width = scaled_max_x - scaled_min_x
            scaled_obj_height = scaled_max_y - scaled_min_y

            # print(f"Scaled object bounds: ({scaled_min_x:.1f}, {scaled_min_y:.1f}) to ({scaled_max_x:.1f}, {scaled_max_y:.1f})")
            # print(f"Scaled object dimensions: {scaled_obj_width:.1f} x {scaled_obj_height:.1f}")

            # Calculate alignment offset within the state canvas
            offset_x = 0
            offset_y = 0

            if alignment in ["top-left", "left", "bottom-left"]:
                # Align to left: object's left edge to canvas left (x=0)
                offset_x = -scaled_min_x
            elif alignment in ["top", "middle", "bottom"]:
                # Align to center: object center to canvas center
                object_center_x = (scaled_min_x + scaled_max_x) / 2
                canvas_center_x = target_width / 2
                offset_x = canvas_center_x - object_center_x
            elif alignment in ["top-right", "right", "bottom-right"]:
                # Align to right: object's right edge to canvas right (x=target_width)
                offset_x = target_width - scaled_max_x

            if alignment in ["top-left", "top", "top-right"]:
                # Align to top: object's top edge to canvas top (y=0)
                offset_y = -scaled_min_y
            elif alignment in ["left", "middle", "right"]:
                # Align to center: object center to canvas center
                object_center_y = (scaled_min_y + scaled_max_y) / 2
                canvas_center_y = target_height / 2
                offset_y = canvas_center_y - object_center_y
            elif alignment in ["bottom-left", "bottom", "bottom-right"]:
                # Align to bottom: object's bottom edge to canvas bottom (y=target_height)
                offset_y = target_height - scaled_max_y

                # object_center_y = (scaled_min_y + scaled_max_y) / 2
                # canvas_center_y = target_height / 2
                # offset_y = canvas_center_y - object_center_y

            # print(f"Alignment '{alignment}' - applying offset: ({offset_x:.1f}, {offset_y:.1f})")

            # Apply alignment offset to all segments
            aligned_segments = []
            for segment in scaled_segments:
                aligned_segment = [
                    (segment[0][0] + offset_x, segment[0][1] + offset_y),
                    (segment[1][0] + offset_x, segment[1][1] + offset_y)
                ]
                aligned_segments.append(aligned_segment)

            # Verify final alignment
            final_points = []
            for segment in aligned_segments:
                final_points.extend(segment)
            final_points_array = np.array(final_points)
            final_min_x, final_min_y = np.min(final_points_array, axis=0)
            final_max_x, final_max_y = np.max(final_points_array, axis=0)

            # print(f"Final aligned object bounds: ({final_min_x:.1f}, {final_min_y:.1f}) to ({final_max_x:.1f}, {final_max_y:.1f})")

        else:
            aligned_segments = scaled_segments
            final_min_x = final_min_y = final_max_x = final_max_y = 0

        buffer_areas = []
        for segment in aligned_segments:
            line = LineString([segment[0], segment[1]])
            buffer_area = line.buffer(buffer_radius, cap_style=1, join_style=1)
            buffer_areas.append(buffer_area)
        buffer_area_by_stroke = unary_union(buffer_areas)
        method_stroke = 'circular_buffer_from_paths'

        if not buffer_area_by_stroke.is_valid:
            buffer_area_by_stroke = buffer_area_by_stroke.buffer(0)

        # Create convex hull buffer (no buffer radius)
        # print("Creating convex hull buffer from aligned path segments")
        buffer_area_by_convex = create_convex_hull_buffer(aligned_segments, buffer_radius=0)
        method_convex = 'convex_hull_from_paths'

        if not buffer_area_by_convex.is_valid:
            buffer_area_by_convex = buffer_area_by_convex.buffer(0)

        # Extract outlines for both buffers
        buffer_outlines_stroke = get_buffer_outlines(buffer_area_by_stroke)
        buffer_outlines_convex = get_buffer_outlines(buffer_area_by_convex)

        # Get convex hull points for visualization
        convex_hull_points = None
        if aligned_segments:
            all_aligned_points = []
            for segment in aligned_segments:
                all_aligned_points.extend(segment)

            if len(all_aligned_points) >= 3:
                try:
                    points_array = np.array(all_aligned_points)
                    hull_indices = ConvexHull(points_array).vertices
                    convex_hull_points = points_array[hull_indices].tolist()
                except Exception as e:
                    print(f"Could not create convex hull points for visualization: {e}")

        return {
            'segments': aligned_segments,
            'buffer_area_by_stroke': buffer_area_by_stroke,
            'buffer_area_by_convex': buffer_area_by_convex,
            'buffer_outlines_stroke': buffer_outlines_stroke,
            'buffer_outlines_convex': buffer_outlines_convex,
            'dimensions': (target_width, target_height),
            'scale_factor': scale,
            'method_stroke': method_stroke,
            'method_convex': method_convex,
            'convex_hull_points': convex_hull_points,
            'original_bounds': (min_x, min_y, max_x, max_y),
            'parsed_dimensions': (bbox_width, bbox_height),
            'alignment': alignment,
            'alignment_offset': (offset_x, offset_y),
            'final_object_bounds': (final_min_x, final_min_y, final_max_x, final_max_y)
        }

    except Exception as e:
        print(f"Error processing state icon: {e}")
        return None


def visualize_state_processing(result, save_path=None, show_plot=True):
    """Visualize the state icon processing with matplotlib"""
    if not result:
        print("No result to visualize")
        return

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('State Icon Processing Visualization', fontsize=16)

    # Extract data from result
    segments = result['segments']
    buffer_stroke = result['buffer_area_by_stroke']
    buffer_convex = result['buffer_area_by_convex']
    convex_hull_points = result['convex_hull_points']
    target_width, target_height = result['dimensions']

    # Plot 1: Original segments
    ax1.set_title('Original Segments')
    ax1.set_xlim(0, target_width)
    ax1.set_ylim(0, target_height)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)

    if segments:
        lines = LineCollection(segments, colors='blue', linewidths=2)
        ax1.add_collection(lines)

    # Plot 2: Stroke buffer
    ax2.set_title('Stroke Buffer')
    ax2.set_xlim(0, target_width)
    ax2.set_ylim(0, target_height)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)

    if segments:
        lines = LineCollection(segments, colors='blue', linewidths=1, alpha=0.7)
        ax2.add_collection(lines)

    # Plot buffer area
    if hasattr(buffer_stroke, 'geoms'):
        for geom in buffer_stroke.geoms:
            if hasattr(geom, 'exterior'):
                x, y = geom.exterior.xy
                ax2.fill(x, y, alpha=0.3, color='red', label='Stroke Buffer')
    elif hasattr(buffer_stroke, 'exterior'):
        x, y = buffer_stroke.exterior.xy
        ax2.fill(x, y, alpha=0.3, color='red', label='Stroke Buffer')

    # Plot 3: Convex hull buffer
    ax3.set_title('Convex Hull Buffer')
    ax3.set_xlim(0, target_width)
    ax3.set_ylim(0, target_height)
    ax3.set_aspect('equal')
    ax3.grid(True, alpha=0.3)

    if segments:
        lines = LineCollection(segments, colors='blue', linewidths=1, alpha=0.7)
        ax3.add_collection(lines)

    # Plot convex hull points
    if convex_hull_points:
        hull_points = np.array(convex_hull_points + [convex_hull_points[0]])  # Close the hull
        ax3.plot(hull_points[:, 0], hull_points[:, 1], 'g-', linewidth=2, label='Convex Hull')
        ax3.scatter([p[0] for p in convex_hull_points], [p[1] for p in convex_hull_points],
                   c='green', s=50, zorder=5)

    # Plot convex buffer area
    if hasattr(buffer_convex, 'geoms'):
        for geom in buffer_convex.geoms:
            if hasattr(geom, 'exterior'):
                x, y = geom.exterior.xy
                ax3.fill(x, y, alpha=0.3, color='orange', label='Convex Buffer')
    elif hasattr(buffer_convex, 'exterior'):
        x, y = buffer_convex.exterior.xy
        ax3.fill(x, y, alpha=0.3, color='orange', label='Convex Buffer')

    # Plot 4: Combined view
    ax4.set_title('Combined View')
    ax4.set_xlim(0, target_width)
    ax4.set_ylim(0, target_height)
    ax4.set_aspect('equal')
    ax4.grid(True, alpha=0.3)

    # Original segments
    if segments:
        lines = LineCollection(segments, colors='blue', linewidths=2, label='Original Segments')
        ax4.add_collection(lines)

    # Both buffers with transparency
    if hasattr(buffer_stroke, 'geoms'):
        for geom in buffer_stroke.geoms:
            if hasattr(geom, 'exterior'):
                x, y = geom.exterior.xy
                ax4.fill(x, y, alpha=0.2, color='red')
    elif hasattr(buffer_stroke, 'exterior'):
        x, y = buffer_stroke.exterior.xy
        ax4.fill(x, y, alpha=0.2, color='red')

    if hasattr(buffer_convex, 'geoms'):
        for geom in buffer_convex.geoms:
            if hasattr(geom, 'exterior'):
                x, y = geom.exterior.xy
                ax4.fill(x, y, alpha=0.2, color='orange')
    elif hasattr(buffer_convex, 'exterior'):
        x, y = buffer_convex.exterior.xy
        ax4.fill(x, y, alpha=0.2, color='orange')

    # Add legends
    ax2.legend()
    ax3.legend()

    # Add canvas boundaries
    for ax in [ax1, ax2, ax3, ax4]:
        rect = patches.Rectangle((0, 0), target_width, target_height,
                               linewidth=2, edgecolor='black', facecolor='none')
        ax.add_patch(rect)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Visualization saved to: {save_path}")

    if show_plot:
        plt.show()

    return fig


if __name__ == "__main__":
    result = process_state_icon('8a80ee4f-5c0f-47e3-8f69-d4a34318a6b1.svg')
    if result:
        visualize_state_processing(result, save_path='state_processing_visualization.png', show_plot=True)
