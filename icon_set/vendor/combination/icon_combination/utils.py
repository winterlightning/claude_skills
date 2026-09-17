import os
import re
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Rectangle, Polygon
import xml.etree.ElementTree as ET
from shapely.geometry import LineString, Point, MultiPolygon, Polygon as ShapelyPolygon
from shapely.ops import unary_union
from shapely.affinity import translate
from scipy.spatial import ConvexHull

# =============================================================================
# CONVEX HULL FUNCTIONS
# =============================================================================
def create_convex_hull_buffer(segments, buffer_radius=16.0):
    """
    Create a convex hull buffer area around segments
    
    Args:
        segments: List of line segments
        buffer_radius: Buffer distance around segments (0 for no buffer)
        
    Returns:
        shapely Polygon: Convex hull with optional buffer
    """
    if not segments:
        return None
    
    # Get all points from segments
    all_points = []
    for segment in segments:
        all_points.extend(segment)
    
    if len(all_points) < 3:
        # Not enough points for convex hull, fall back to empty polygon
        print("Not enough points for convex hull, returning empty polygon")
        return ShapelyPolygon()
    
    # Convert to numpy array
    points_array = np.array(all_points)
    
    try:
        # Find convex hull using scipy
        hull_indices = ConvexHull(points_array).vertices
        hull_points = points_array[hull_indices]
        
        # Create convex hull polygon
        convex_polygon = ShapelyPolygon(hull_points)
        
        # Apply buffer only if buffer_radius > 0
        if buffer_radius > 0:
            buffered_convex_hull = convex_polygon.buffer(buffer_radius, cap_style=1, join_style=1)
        else:
            buffered_convex_hull = convex_polygon
        
        if not buffered_convex_hull.is_valid:
            buffered_convex_hull = buffered_convex_hull.buffer(0)
        
        # print(f"Created convex hull from {len(all_points)} points with {len(hull_points)} hull vertices")
        # print(f"Applied buffer radius: {buffer_radius}")
        # print(f"Hull bounds: {buffered_convex_hull.bounds}")
        
        return buffered_convex_hull
        
    except Exception as e:
        print(f"Error creating convex hull: {e}")
        return ShapelyPolygon()


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================
    
def clip_segments_outside_state_area_enhanced(main_segments, state_area, min_segment_length=1.0):
    """
    Enhanced clipping function that removes segments inside state area, including:
    - Single points (segments with same start/end coordinates)
    - Very short segments
    - Regular line segments
    
    Args:
        main_segments: List of line segments from main icon
        state_area: The merged state area polygon (light red area)
        min_segment_length: Minimum length for a segment to be kept (default 1.0)
        
    Returns:
        tuple: (clipped_segments, removed_segments, intersection_info)
    """
    if state_area is None or state_area.is_empty:
        print("No valid state area provided for clipping")
        return main_segments, [], []
    
    try:
        clipped_segments = []
        removed_segments = []
        intersection_info = []
        
        # print(f"Starting clipping process with {len(main_segments)} segments")
        # print(f"State area bounds: {state_area.bounds}")
        
        for i, segment in enumerate(main_segments):
            try:
                # Check if segment has valid coordinates
                if len(segment) < 2:
                    # print(f"Segment {i} has invalid format: {segment}")
                    removed_segments.append(segment)
                    intersection_info.append({
                        'original_segment': segment,
                        'action': 'removed',
                        'reason': 'invalid_format'
                    })
                    continue
                
                start_point = segment[0]
                end_point = segment[1]
                
                # Check if it's a single point (start == end)
                if start_point == end_point:
                    # Single point - check if it's inside state area
                    point = Point(start_point)
                    if state_area.contains(point) or state_area.intersects(point):
                        removed_segments.append(segment)
                        intersection_info.append({
                            'original_segment': segment,
                            'action': 'removed',
                            'reason': 'single_point_inside_state_area'
                        })
                    else:
                        clipped_segments.append(segment)
                        intersection_info.append({
                            'original_segment': segment,
                            'new_segments': [segment],
                            'action': 'kept',
                            'reason': 'single_point_outside_state_area'
                        })
                    continue
                
                # Calculate segment length
                segment_length = ((end_point[0] - start_point[0])**2 + 
                                (end_point[1] - start_point[1])**2)**0.5
                
                # Check if segment is too short
                if segment_length < min_segment_length:
                    # For very short segments, check if midpoint is inside state area
                    midpoint_x = (start_point[0] + end_point[0]) / 2
                    midpoint_y = (start_point[1] + end_point[1]) / 2
                    midpoint = Point(midpoint_x, midpoint_y)
                    
                    if state_area.contains(midpoint) or state_area.intersects(midpoint):
                        removed_segments.append(segment)
                        intersection_info.append({
                            'original_segment': segment,
                            'action': 'removed',
                            'reason': f'short_segment_inside_state_area_length_{segment_length:.2f}'
                        })
                    else:
                        clipped_segments.append(segment)
                        intersection_info.append({
                            'original_segment': segment,
                            'new_segments': [segment],
                            'action': 'kept',
                            'reason': f'short_segment_outside_state_area_length_{segment_length:.2f}'
                        })
                    continue
                
                # Regular line segment processing
                line = LineString([start_point, end_point])
                
                # Check if line is completely inside state area
                if state_area.contains(line):
                    # Entire segment is inside state area - remove it
                    removed_segments.append(segment)
                    intersection_info.append({
                        'original_segment': segment,
                        'action': 'removed',
                        'reason': 'entirely_inside_state_area'
                    })
                    continue
                
                # Check if both endpoints are inside state area
                start_pt = Point(start_point)
                end_pt = Point(end_point)
                start_inside = state_area.contains(start_pt) or state_area.intersects(start_pt)
                end_inside = state_area.contains(end_pt) or state_area.intersects(end_pt)
                
                if start_inside and end_inside:
                    # Both endpoints inside - remove entire segment
                    removed_segments.append(segment)
                    intersection_info.append({
                        'original_segment': segment,
                        'action': 'removed',
                        'reason': 'both_endpoints_inside_state_area'
                    })
                    continue
                
                # Check if line intersects with state area
                if line.intersects(state_area):
                    # Get the part of the line that is OUTSIDE the state area
                    try:
                        outside_parts = line.difference(state_area)
                    except Exception as e:
                        # print(f"Error computing line difference for segment {i}: {e}")
                        # If difference fails, check endpoints to decide
                        if start_inside or end_inside:
                            removed_segments.append(segment)
                            intersection_info.append({
                                'original_segment': segment,
                                'action': 'removed',
                                'reason': 'intersection_computation_failed_endpoint_inside'
                            })
                        else:
                            clipped_segments.append(segment)
                            intersection_info.append({
                                'original_segment': segment,
                                'new_segments': [segment],
                                'action': 'kept',
                                'reason': 'intersection_computation_failed_endpoints_outside'
                            })
                        continue
                    
                    if outside_parts.is_empty:
                        # Entire segment is inside state area - remove it
                        removed_segments.append(segment)
                        intersection_info.append({
                            'original_segment': segment,
                            'action': 'removed',
                            'reason': 'difference_result_empty'
                        })
                    else:
                        # Part of segment is outside - keep those parts
                        new_segments_created = []
                        
                        if outside_parts.geom_type == 'LineString':
                            # Single line segment outside
                            coords = list(outside_parts.coords)
                            if len(coords) >= 2:
                                # Create segment from first to last coordinate
                                new_segment = [(coords[0][0], coords[0][1]), (coords[-1][0], coords[-1][1])]
                                new_length = ((coords[-1][0] - coords[0][0])**2 + 
                                            (coords[-1][1] - coords[0][1])**2)**0.5
                                
                                if new_length >= min_segment_length:
                                    clipped_segments.append(new_segment)
                                    new_segments_created.append(new_segment)
                                    
                        elif outside_parts.geom_type == 'MultiLineString':
                            # Multiple line segments outside (segment was split)
                            for line_part in outside_parts.geoms:
                                coords = list(line_part.coords)
                                if len(coords) >= 2:
                                    new_segment = [(coords[0][0], coords[0][1]), (coords[-1][0], coords[-1][1])]
                                    new_length = ((coords[-1][0] - coords[0][0])**2 + 
                                                (coords[-1][1] - coords[0][1])**2)**0.5
                                    
                                    # Only keep segments that are long enough
                                    if new_length >= min_segment_length:
                                        new_segments_created.append(new_segment)
                                        clipped_segments.append(new_segment)
                        
                        # Record the result
                        if new_segments_created:
                            intersection_info.append({
                                'original_segment': segment,
                                'new_segments': new_segments_created,
                                'action': 'clipped_and_kept',
                                'reason': f'partial_intersection_kept_{len(new_segments_created)}_parts'
                            })
                        else:
                            removed_segments.append(segment)
                            intersection_info.append({
                                'original_segment': segment,
                                'action': 'removed',
                                'reason': 'clipped_parts_too_short_or_invalid'
                            })
                else:
                    # No intersection - keep the segment as is
                    clipped_segments.append(segment)
                    intersection_info.append({
                        'original_segment': segment,
                        'new_segments': [segment],
                        'action': 'kept',
                        'reason': f'no_intersection_length_{segment_length:.2f}'
                    })
                    
            except Exception as e:
                # print(f"Error processing segment {i}: {e}")
                # print(f"Segment data: {segment}")
                # If there's an error, remove the segment to be safe
                removed_segments.append(segment)
                intersection_info.append({
                    'original_segment': segment,
                    'action': 'removed',
                    'reason': f'processing_error: {str(e)}'
                })
        
        # Detailed statistics
        total_original = len(main_segments)
        total_clipped = len(clipped_segments)
        total_removed = len(removed_segments)
        
        # Count different types of actions
        action_counts = {}
        for info in intersection_info:
            action = info['action']
            reason = info['reason'].split('_')[0] if '_' in info['reason'] else info['reason']
            key = f"{action}_{reason}"
            action_counts[key] = action_counts.get(key, 0) + 1
            
        return clipped_segments, removed_segments, intersection_info
        
    except Exception as e:
        # print(f"Error in enhanced clip_segments_outside_state_area: {e}")
        return main_segments, [], []
    
def find_intersection_segments_detailed(main_segments, buffer_area):
    """Enhanced intersection detection with detailed information"""
    if buffer_area is None:
        # print("No buffer area provided")
        return main_segments, [], []
    
    try:
        non_intersecting_segments = []
        intersecting_segments = []
        intersection_points = []
        
        for i, segment in enumerate(main_segments):
            try:
                line = LineString([segment[0], segment[1]])
                
                # Check if the line intersects with the state area
                if line.intersects(buffer_area):
                    intersection = line.intersection(buffer_area)
                    if not intersection.is_empty:
                        intersecting_segments.append(segment)
                        
                        # Collect intersection points for visualization
                        if intersection.geom_type == 'Point':
                            intersection_points.append((intersection.x, intersection.y))
                        elif intersection.geom_type == 'MultiPoint':
                            intersection_points.extend([(pt.x, pt.y) for pt in intersection.geoms])
                        elif intersection.geom_type == 'LineString':
                            # If intersection is a line, get boundary points
                            coords = list(intersection.coords)
                            if len(coords) >= 2:
                                intersection_points.extend([(coords[0][0], coords[0][1]), (coords[-1][0], coords[-1][1])])
                        elif intersection.geom_type == 'MultiLineString':
                            # Handle multiple line intersections
                            for line_part in intersection.geoms:
                                coords = list(line_part.coords)
                                if len(coords) >= 2:
                                    intersection_points.extend([(coords[0][0], coords[0][1]), (coords[-1][0], coords[-1][1])])
                    else:
                        non_intersecting_segments.append(segment)
                else:
                    non_intersecting_segments.append(segment)
                
            except Exception as e:
                print(f"Error processing segment {i}: {e}")
                non_intersecting_segments.append(segment)
        
        return non_intersecting_segments, intersecting_segments, intersection_points
    
    except Exception as e:
        print(f"Error in find_intersection_segments_detailed: {e}")
        return main_segments, [], []
    

def parse_svg_path(path_data, curve_segments=20):
    """Parse SVG path data and convert it to a list of line segments"""
    number_pattern = r'[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?'
    command_pattern = rf'([MLHVZCQTSAmlhvzcqtsa])\s*([^MLHVZCQTSAmlhvzcqtsa]*)'
    
    lines = []
    current_point = (0, 0)
    start_point = (0, 0)
    last_control_point = None  # For smooth curves
    
    def cubic_bezier_point(t, p0, p1, p2, p3):
        """Calculate point on cubic Bezier curve at parameter t (0 to 1)"""
        x = (1-t)**3 * p0[0] + 3*(1-t)**2*t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
        y = (1-t)**3 * p0[1] + 3*(1-t)**2*t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
        return (x, y)
    
    def quadratic_bezier_point(t, p0, p1, p2):
        """Calculate point on quadratic Bezier curve at parameter t (0 to 1)"""
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        return (x, y)
    
    def approximate_arc(center, rx, ry, start_angle, end_angle, segments=10):
        """Approximate elliptical arc as line segments"""
        import math
        points = []
        angle_step = (end_angle - start_angle) / segments
        for i in range(segments + 1):
            angle = start_angle + i * angle_step
            x = center[0] + rx * math.cos(angle)
            y = center[1] + ry * math.sin(angle)
            points.append((x, y))
        return points

    def svg_arc_to_lines(start_x, start_y, rx, ry, x_axis_rotation, large_arc_flag, sweep_flag, end_x, end_y, segments=20):
        """Convert SVG arc to line segments using proper arc math"""
        import math

        # Handle degenerate cases
        if (start_x == end_x and start_y == end_y) or rx == 0 or ry == 0:
            return [[(start_x, start_y), (end_x, end_y)]]

        # Ensure radii are positive
        rx = abs(rx)
        ry = abs(ry)

        # Convert rotation angle to radians
        phi = math.radians(x_axis_rotation)
        cos_phi = math.cos(phi)
        sin_phi = math.sin(phi)

        # Compute center point
        dx = (start_x - end_x) / 2.0
        dy = (start_y - end_y) / 2.0

        # Rotate to align with coordinate axes
        x1_prime = cos_phi * dx + sin_phi * dy
        y1_prime = -sin_phi * dx + cos_phi * dy

        # Correct radii if necessary
        lambda_coeff = (x1_prime * x1_prime) / (rx * rx) + (y1_prime * y1_prime) / (ry * ry)
        if lambda_coeff > 1:
            rx *= math.sqrt(lambda_coeff)
            ry *= math.sqrt(lambda_coeff)

        # Compute center in prime coordinates
        sign = -1 if large_arc_flag == sweep_flag else 1

        sq = ((rx * rx) * (ry * ry) - (rx * rx) * (y1_prime * y1_prime) - (ry * ry) * (x1_prime * x1_prime))
        if sq < 0:
            sq = 0

        coeff = sign * math.sqrt(sq / ((rx * rx) * (y1_prime * y1_prime) + (ry * ry) * (x1_prime * x1_prime)))

        cx_prime = coeff * ((rx * y1_prime) / ry)
        cy_prime = coeff * (-(ry * x1_prime) / rx)

        # Compute center in original coordinates
        cx = cos_phi * cx_prime - sin_phi * cy_prime + (start_x + end_x) / 2
        cy = sin_phi * cx_prime + cos_phi * cy_prime + (start_y + end_y) / 2

        # Compute angles
        def angle_between_vectors(ux, uy, vx, vy):
            dot = ux * vx + uy * vy
            det = ux * vy - uy * vx
            return math.atan2(det, dot)

        ux = (x1_prime - cx_prime) / rx
        uy = (y1_prime - cy_prime) / ry
        vx = (-x1_prime - cx_prime) / rx
        vy = (-y1_prime - cy_prime) / ry

        theta1 = angle_between_vectors(1, 0, ux, uy)
        dtheta = angle_between_vectors(ux, uy, vx, vy)

        if sweep_flag == 0 and dtheta > 0:
            dtheta -= 2 * math.pi
        elif sweep_flag == 1 and dtheta < 0:
            dtheta += 2 * math.pi

        # Generate line segments
        line_segments = []
        theta = theta1

        for i in range(segments):
            t1 = i / segments
            t2 = (i + 1) / segments

            angle1 = theta1 + t1 * dtheta
            angle2 = theta1 + t2 * dtheta

            # Compute points on the arc
            x1_arc = rx * math.cos(angle1)
            y1_arc = ry * math.sin(angle1)
            x2_arc = rx * math.cos(angle2)
            y2_arc = ry * math.sin(angle2)

            # Rotate and translate back to original coordinates
            x1_final = cos_phi * x1_arc - sin_phi * y1_arc + cx
            y1_final = sin_phi * x1_arc + cos_phi * y1_arc + cy
            x2_final = cos_phi * x2_arc - sin_phi * y2_arc + cx
            y2_final = sin_phi * x2_arc + cos_phi * y2_arc + cy

            line_segments.append([(x1_final, y1_final), (x2_final, y2_final)])

        return line_segments
    
    commands = re.findall(command_pattern, path_data)
    
    for cmd, params in commands:
        numbers = [float(x) for x in re.findall(number_pattern, params)]
        
        if cmd in ['M', 'm']:  # Move to
            relative = (cmd == 'm')
            for i in range(0, len(numbers), 2):
                if i + 1 < len(numbers):
                    x, y = numbers[i], numbers[i + 1]
                    if relative:
                        current_point = (current_point[0] + x, current_point[1] + y)
                    else:
                        current_point = (x, y)
                    start_point = current_point
        
        elif cmd in ['L', 'l']:  # Line to
            relative = (cmd == 'l')
            for i in range(0, len(numbers), 2):
                if i + 1 < len(numbers):
                    x, y = numbers[i], numbers[i + 1]
                    prev_point = current_point
                    if relative:
                        current_point = (current_point[0] + x, current_point[1] + y)
                    else:
                        current_point = (x, y)
                    lines.append([prev_point, current_point])
        
        elif cmd in ['H', 'h']:  # Horizontal line
            relative = (cmd == 'h')
            for x in numbers:
                prev_point = current_point
                if relative:
                    current_point = (current_point[0] + x, current_point[1])
                else:
                    current_point = (x, current_point[1])
                lines.append([prev_point, current_point])
                last_control_point = None
        
        elif cmd in ['V', 'v']:  # Vertical line
            relative = (cmd == 'v')
            for y in numbers:
                prev_point = current_point
                if relative:
                    current_point = (current_point[0], current_point[1] + y)
                else:
                    current_point = (current_point[0], y)
                lines.append([prev_point, current_point])
        
        elif cmd in ['C', 'c']:  # Cubic Bezier curve
            relative = (cmd == 'c')
            for i in range(0, len(numbers), 6):
                if i + 5 < len(numbers):
                    cp1_x, cp1_y = numbers[i], numbers[i + 1]      # Control point 1
                    cp2_x, cp2_y = numbers[i + 2], numbers[i + 3]  # Control point 2
                    end_x, end_y = numbers[i + 4], numbers[i + 5]  # End point

                    if relative:
                        cp1 = (current_point[0] + cp1_x, current_point[1] + cp1_y)
                        cp2 = (current_point[0] + cp2_x, current_point[1] + cp2_y)
                        end_point = (current_point[0] + end_x, current_point[1] + end_y)
                    else:
                        cp1 = (cp1_x, cp1_y)
                        cp2 = (cp2_x, cp2_y)
                        end_point = (end_x, end_y)

                    # Generate multiple line segments to approximate the curve
                    start_point_curve = current_point
                    for j in range(curve_segments):
                        t1 = j / curve_segments
                        t2 = (j + 1) / curve_segments

                        point1 = cubic_bezier_point(t1, start_point_curve, cp1, cp2, end_point)
                        point2 = cubic_bezier_point(t2, start_point_curve, cp1, cp2, end_point)

                        lines.append([point1, point2])

                    current_point = end_point
                    last_control_point = cp2

        elif cmd in ['Q', 'q']:  # Quadratic Bezier curve
            relative = (cmd == 'q')
            for i in range(0, len(numbers), 4):
                if i + 3 < len(numbers):
                    cp_x, cp_y = numbers[i], numbers[i + 1]        # Control point
                    end_x, end_y = numbers[i + 2], numbers[i + 3]  # End point

                    if relative:
                        cp = (current_point[0] + cp_x, current_point[1] + cp_y)
                        end_point = (current_point[0] + end_x, current_point[1] + end_y)
                    else:
                        cp = (cp_x, cp_y)
                        end_point = (end_x, end_y)

                    # Generate multiple line segments to approximate the curve
                    start_point_curve = current_point
                    for j in range(curve_segments):
                        t1 = j / curve_segments
                        t2 = (j + 1) / curve_segments

                        point1 = quadratic_bezier_point(t1, start_point_curve, cp, end_point)
                        point2 = quadratic_bezier_point(t2, start_point_curve, cp, end_point)

                        lines.append([point1, point2])

                    current_point = end_point
                    last_control_point = cp

        elif cmd in ['A', 'a']:  # Elliptical arc
            relative = (cmd == 'a')
            for i in range(0, len(numbers), 7):
                if i + 6 < len(numbers):
                    rx = numbers[i]               # x-radius
                    ry = numbers[i + 1]           # y-radius
                    x_axis_rotation = numbers[i + 2]  # x-axis rotation
                    large_arc_flag = int(numbers[i + 3])  # large-arc-flag
                    sweep_flag = int(numbers[i + 4])      # sweep-flag
                    end_x = numbers[i + 5]        # end x
                    end_y = numbers[i + 6]        # end y

                    if relative:
                        end_point = (current_point[0] + end_x, current_point[1] + end_y)
                    else:
                        end_point = (end_x, end_y)

                    # Generate line segments to approximate the arc
                    arc_segments = svg_arc_to_lines(
                        current_point[0], current_point[1],
                        rx, ry, x_axis_rotation,
                        large_arc_flag, sweep_flag,
                        end_point[0], end_point[1],
                        curve_segments
                    )
                    lines.extend(arc_segments)

                    current_point = end_point
                    last_control_point = None
        
        elif cmd in ['Z', 'z']:  # Close path
            if current_point != start_point:
                lines.append([current_point, start_point])
                current_point = start_point
            last_control_point = None
    
    return lines

def parse_svg_geometric_elements(root, point_spacing=1.0):
    """Parse various SVG elements directly into line segments with consistent point spacing"""

    # Clean up the SVG before parsing - remove unwanted elements
    ns = {'svg': 'http://www.w3.org/2000/svg'}

    # Remove style elements
    for style in root.findall('.//{http://www.w3.org/2000/svg}style'):
        parent = root.find('.//{http://www.w3.org/2000/svg}style/..')
        if parent is not None:
            parent.remove(style)
        else:
            root.remove(style)

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
        # print(f"Preserved geometric element: {elem.tag.split('}')[-1] if '}' in elem.tag else elem.tag}")

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
    
    # Remove style attributes from all elements
    for elem in root.iter():
        if 'style' in elem.attrib:
            del elem.attrib['style']
    
    # Now proceed with parsing geometric elements
    all_segments = []
    all_points = []
    
    # Existing path parsing
    paths = []
    paths.extend(root.findall('.//svg:path', ns))
    paths.extend(root.findall('.//path'))
    paths.extend(root.findall('.//{*}path'))
    
    for path in paths:
        path_data = path.get('d')
        if path_data:
            segments = parse_svg_path(path_data)
            if segments:
                all_segments.extend(segments)
                for segment in segments:
                    all_points.extend(segment)
    
    # Parse circles with smooth spacing - improved with better error handling
    circles = []
    # Try multiple namespace approaches but avoid duplicates
    found_circles = set()

    for search_pattern in [
        ('.//svg:circle', ns),
        ('.//circle', {}),
        ('.//{*}circle', {}),
        ('.//{http://www.w3.org/2000/svg}circle', {})
    ]:
        pattern, namespace = search_pattern
        for circle in root.findall(pattern, namespace):
            # Use element's memory address to avoid duplicates
            if id(circle) not in found_circles:
                circles.append(circle)
                found_circles.add(id(circle))

    for i, circle in enumerate(circles):
        try:
            # More robust attribute parsing
            cx_attr = circle.get('cx', '0')
            cy_attr = circle.get('cy', '0')
            r_attr = circle.get('r', '0')

            # Handle empty or invalid attributes
            try:
                cx = float(cx_attr) if cx_attr.strip() else 0.0
            except (ValueError, AttributeError):
                print(f"Invalid cx attribute for circle {i}: '{cx_attr}', using 0")
                cx = 0.0

            try:
                cy = float(cy_attr) if cy_attr.strip() else 0.0
            except (ValueError, AttributeError):
                print(f"Invalid cy attribute for circle {i}: '{cy_attr}', using 0")
                cy = 0.0

            try:
                r = float(r_attr) if r_attr.strip() else 0.0
            except (ValueError, AttributeError):
                print(f"Invalid r attribute for circle {i}: '{r_attr}', using 0")
                r = 0.0

            if r > 0:
                circle_segments = create_circle_segments_smooth(cx, cy, r, point_spacing)
                # print(f"Generated {len(circle_segments)} segments for circle {i}")
                all_segments.extend(circle_segments)
                for segment in circle_segments:
                    all_points.extend(segment)
            else:
                print(f"Skipping circle {i} with radius {r} (must be > 0)")

        except Exception as e:
            print(f"Error processing circle {i}: {e}")
            print(f"Circle attributes: {dict(circle.attrib)}")
            continue
    
    # Parse rectangles (including rounded rects via rx / ry)
    rects = []
    found_rects = set()
    for pattern, namespace in [
        ('.//svg:rect', ns),
        ('.//rect', {}),
        ('.//{*}rect', {}),
        ('.//{http://www.w3.org/2000/svg}rect', {}),
    ]:
        for rect in root.findall(pattern, namespace):
            if id(rect) not in found_rects:
                rects.append(rect)
                found_rects.add(id(rect))

    def _safe_float(value, default=0.0):
        try:
            return float(value) if value is not None and str(value).strip() else default
        except (ValueError, TypeError):
            return default

    for rect in rects:
        x = _safe_float(rect.get('x'), 0.0)
        y = _safe_float(rect.get('y'), 0.0)
        width = _safe_float(rect.get('width'), 0.0)
        height = _safe_float(rect.get('height'), 0.0)
        rx_attr = rect.get('rx')
        ry_attr = rect.get('ry')
        rx = _safe_float(rx_attr, 0.0) if rx_attr is not None else None
        ry = _safe_float(ry_attr, 0.0) if ry_attr is not None else None
        # SVG spec: if only one of rx/ry is given, the other defaults to it
        if rx is None and ry is None:
            rx, ry = 0.0, 0.0
        elif rx is None:
            rx = ry
        elif ry is None:
            ry = rx
        if width > 0 and height > 0:
            rect_segments = create_rectangle_segments_smooth(x, y, width, height, point_spacing, rx=rx, ry=ry)
            all_segments.extend(rect_segments)
            for segment in rect_segments:
                all_points.extend(segment)
    
    # Parse ellipses with smooth spacing
    ellipses = []
    ellipses.extend(root.findall('.//svg:ellipse', ns))
    ellipses.extend(root.findall('.//ellipse'))
    ellipses.extend(root.findall('.//{*}ellipse'))
    
    for ellipse in ellipses:
        cx = float(ellipse.get('cx', 0))
        cy = float(ellipse.get('cy', 0))
        rx = float(ellipse.get('rx', 0))
        ry = float(ellipse.get('ry', 0))
        if rx > 0 and ry > 0:
            ellipse_segments = create_ellipse_segments_smooth(cx, cy, rx, ry, point_spacing)
            all_segments.extend(ellipse_segments)
            for segment in ellipse_segments:
                all_points.extend(segment)
    
    # Parse polygons with smooth edges
    polygons = []
    polygons.extend(root.findall('.//svg:polygon', ns))
    polygons.extend(root.findall('.//polygon'))
    polygons.extend(root.findall('.//{*}polygon'))
    
    for polygon in polygons:
        points_str = polygon.get('points', '')
        if points_str.strip():
            polygon_segments = create_polygon_segments_smooth(points_str, point_spacing)
            all_segments.extend(polygon_segments)
            for segment in polygon_segments:
                all_points.extend(segment)
    
    # Parse polylines with smooth spacing
    polylines = []
    polylines.extend(root.findall('.//svg:polyline', ns))
    polylines.extend(root.findall('.//polyline'))
    polylines.extend(root.findall('.//{*}polyline'))
    
    for polyline in polylines:
        points_str = polyline.get('points', '')
        if points_str.strip():
            polyline_segments = create_polyline_segments_smooth(points_str, point_spacing)
            all_segments.extend(polyline_segments)
            for segment in polyline_segments:
                all_points.extend(segment)
    
    # Parse lines (already smooth if short enough)
    lines = []
    lines.extend(root.findall('.//svg:line', ns))
    lines.extend(root.findall('.//line'))
    lines.extend(root.findall('.//{*}line'))
    
    for line in lines:
        x1 = float(line.get('x1', 0))
        y1 = float(line.get('y1', 0))
        x2 = float(line.get('x2', 0))
        y2 = float(line.get('y2', 0))
        line_segments = create_line_segments_smooth(x1, y1, x2, y2, point_spacing)
        all_segments.extend(line_segments)
        for segment in line_segments:
            all_points.extend(segment)

    return all_segments, all_points

def create_circle_segments_smooth(cx, cy, r, point_spacing=1.0):
    """Create line segments approximating a circle with consistent point spacing"""
    import math
    
    # Calculate circumference and number of segments needed
    circumference = 2 * math.pi * r
    num_segments = max(8, int(circumference / point_spacing))
    
    segments = []
    angle_step = 2 * math.pi / num_segments
    
    for i in range(num_segments):
        angle1 = i * angle_step
        angle2 = (i + 1) * angle_step
        
        x1 = cx + r * math.cos(angle1)
        y1 = cy + r * math.sin(angle1)
        x2 = cx + r * math.cos(angle2)
        y2 = cy + r * math.sin(angle2)
        
        segments.append([(x1, y1), (x2, y2)])
    
    return segments

def create_ellipse_segments_smooth(cx, cy, rx, ry, point_spacing=1.0):
    """Create line segments approximating an ellipse with consistent point spacing"""
    import math
    
    # Approximate ellipse perimeter using Ramanujan's approximation
    h = ((rx - ry) / (rx + ry)) ** 2
    perimeter = math.pi * (rx + ry) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
    num_segments = max(8, int(perimeter / point_spacing))
    
    segments = []
    angle_step = 2 * math.pi / num_segments
    
    for i in range(num_segments):
        angle1 = i * angle_step
        angle2 = (i + 1) * angle_step
        
        x1 = cx + rx * math.cos(angle1)
        y1 = cy + ry * math.sin(angle1)
        x2 = cx + rx * math.cos(angle2)
        y2 = cy + ry * math.sin(angle2)
        
        segments.append([(x1, y1), (x2, y2)])
    
    return segments

def create_rectangle_segments_smooth(x, y, width, height, point_spacing=1.0, rx=0.0, ry=0.0):
    """Create line segments for a rectangle (optionally with rounded corners) with consistent point spacing"""
    import math

    rx = max(0.0, rx or 0.0)
    ry = max(0.0, ry or 0.0)
    # SVG spec: clamp rx/ry to half of width/height
    rx = min(rx, width / 2)
    ry = min(ry, height / 2)

    # No rounded corners → straight rectangle
    if rx == 0 or ry == 0:
        segments = []
        segments.extend(create_line_segments_smooth(x, y, x + width, y, point_spacing))
        segments.extend(create_line_segments_smooth(x + width, y, x + width, y + height, point_spacing))
        segments.extend(create_line_segments_smooth(x + width, y + height, x, y + height, point_spacing))
        segments.extend(create_line_segments_smooth(x, y + height, x, y, point_spacing))
        return segments

    segments = []

    # Top edge: from (x+rx, y) to (x+width-rx, y)
    segments.extend(create_line_segments_smooth(x + rx, y, x + width - rx, y, point_spacing))
    # Top-right corner arc (-pi/2 -> 0)
    segments.extend(_arc_segments(x + width - rx, y + ry, rx, ry, -math.pi / 2, 0.0, point_spacing))
    # Right edge
    segments.extend(create_line_segments_smooth(x + width, y + ry, x + width, y + height - ry, point_spacing))
    # Bottom-right corner arc (0 -> pi/2)
    segments.extend(_arc_segments(x + width - rx, y + height - ry, rx, ry, 0.0, math.pi / 2, point_spacing))
    # Bottom edge (right to left)
    segments.extend(create_line_segments_smooth(x + width - rx, y + height, x + rx, y + height, point_spacing))
    # Bottom-left corner arc (pi/2 -> pi)
    segments.extend(_arc_segments(x + rx, y + height - ry, rx, ry, math.pi / 2, math.pi, point_spacing))
    # Left edge (bottom to top)
    segments.extend(create_line_segments_smooth(x, y + height - ry, x, y + ry, point_spacing))
    # Top-left corner arc (pi -> 3pi/2)
    segments.extend(_arc_segments(x + rx, y + ry, rx, ry, math.pi, 3 * math.pi / 2, point_spacing))

    return segments


def _arc_segments(cx, cy, rx, ry, start_angle, end_angle, point_spacing=1.0):
    """Approximate an elliptical arc (in standard math angles) as line segments."""
    import math

    # Estimate arc length to choose number of segments
    avg_r = (rx + ry) / 2
    arc_len = abs(end_angle - start_angle) * avg_r
    num = max(4, int(arc_len / max(point_spacing, 0.5)))

    segments = []
    for i in range(num):
        t1 = start_angle + (end_angle - start_angle) * (i / num)
        t2 = start_angle + (end_angle - start_angle) * ((i + 1) / num)
        p1 = (cx + rx * math.cos(t1), cy + ry * math.sin(t1))
        p2 = (cx + rx * math.cos(t2), cy + ry * math.sin(t2))
        segments.append([p1, p2])
    return segments

def create_line_segments_smooth(x1, y1, x2, y2, point_spacing=1.0):
    """Create line segments with consistent point spacing"""
    import math
    
    # Calculate distance and number of segments needed
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distance <= point_spacing:
        # Line is short enough, return as single segment
        return [[(x1, y1), (x2, y2)]]
    
    num_segments = max(1, int(distance / point_spacing))
    segments = []
    
    # Create evenly spaced points along the line
    for i in range(num_segments):
        t1 = i / num_segments
        t2 = (i + 1) / num_segments
        
        px1 = x1 + t1 * (x2 - x1)
        py1 = y1 + t1 * (y2 - y1)
        px2 = x1 + t2 * (x2 - x1)
        py2 = y1 + t2 * (y2 - y1)
        
        segments.append([(px1, py1), (px2, py2)])
    
    return segments

def create_polygon_segments_smooth(points_str, point_spacing=1.0):
    """Create line segments from polygon points with consistent spacing"""
    import re
    coords = re.findall(r'[-+]?(?:\d*\.?\d+)', points_str)
    if len(coords) < 4:  # Need at least 2 points
        return []
    
    segments = []
    points = [(float(coords[i]), float(coords[i+1])) for i in range(0, len(coords)-1, 2)]
    
    # Connect consecutive points with smooth segments
    for i in range(len(points)):
        next_i = (i + 1) % len(points)  # Wrap around to close polygon
        p1, p2 = points[i], points[next_i]
        line_segments = create_line_segments_smooth(p1[0], p1[1], p2[0], p2[1], point_spacing)
        segments.extend(line_segments)
    
    return segments

def create_polyline_segments_smooth(points_str, point_spacing=1.0):
    """Create line segments from polyline points with consistent spacing (no closing)"""
    import re
    coords = re.findall(r'[-+]?(?:\d*\.?\d+)', points_str)
    if len(coords) < 4:  # Need at least 2 points
        return []
    
    segments = []
    points = [(float(coords[i]), float(coords[i+1])) for i in range(0, len(coords)-1, 2)]
    
    # Connect consecutive points with smooth segments (no closing)
    for i in range(len(points) - 1):
        p1, p2 = points[i], points[i + 1]
        line_segments = create_line_segments_smooth(p1[0], p1[1], p2[0], p2[1], point_spacing)
        segments.extend(line_segments)
    
    return segments

def remove_overlapping_segments(main_segments, buffer_area, state_offset_x, state_offset_y):
    """Remove main icon segments whose both endpoints are inside the state icon's buffer area"""
    if buffer_area is None:
        print("No buffer area provided")
        return main_segments, []
    
    try:
        offset_buffer = translate(buffer_area, xoff=state_offset_x, yoff=state_offset_y)
        
        if not offset_buffer.is_valid:
            offset_buffer = offset_buffer.buffer(0)
        
        # print(f"Created buffer area at ({state_offset_x:.1f}, {state_offset_y:.1f})")
        
    except Exception as e:
        print(f"Error creating buffer area: {e}")
        return main_segments, []
    
    cleaned_segments = []
    removed_segments = []
    
    for i, segment in enumerate(main_segments):
        try:
            start_point = Point(segment[0])
            end_point = Point(segment[1])
            
            start_inside = offset_buffer.contains(start_point) or offset_buffer.touches(start_point)
            end_inside = offset_buffer.contains(end_point) or offset_buffer.touches(end_point)
            
            if start_inside and end_inside:
                removed_segments.append(segment)
            else:
                cleaned_segments.append(segment)
                
        except Exception as e:
            print(f"Error processing segment {i}: {e}")
            cleaned_segments.append(segment)
    
    return cleaned_segments, removed_segments


def get_buffer_outlines(buffer_area):
    """Extract all exterior outlines from the buffer area (handles MultiPolygon)"""
    outlines = []
    if isinstance(buffer_area, MultiPolygon):
        for poly in buffer_area.geoms:
            if hasattr(poly, 'exterior') and poly.exterior:
                coords = list(poly.exterior.coords)[:-1]  # Remove duplicate closing point
                outline_segments = [[coords[i], coords[i+1]] for i in range(len(coords)-1)]
                outlines.extend(outline_segments)
    else:
        if hasattr(buffer_area, 'exterior') and buffer_area.exterior:
            coords = list(buffer_area.exterior.coords)[:-1]
            outline_segments = [[coords[i], coords[i+1]] for i in range(len(coords)-1)]
            outlines.extend(outline_segments)
    return outlines

def find_buffer_extreme_points(buffer_area, state_offset_x, state_offset_y):
    """Find the extreme points (topmost, leftmost, rightmost, bottommost) of the buffer area"""
    if buffer_area is None:
        print("No buffer area provided")
        return None
    
    try:
        # Translate buffer area to its final position
        offset_buffer = translate(buffer_area, xoff=state_offset_x, yoff=state_offset_y)
        
        if not offset_buffer.is_valid:
            offset_buffer = offset_buffer.buffer(0)
        
        # Extract all coordinates from the buffer area
        all_coords = []
        
        if isinstance(offset_buffer, MultiPolygon):
            for poly in offset_buffer.geoms:
                if hasattr(poly, 'exterior') and poly.exterior:
                    coords = list(poly.exterior.coords)
                    all_coords.extend(coords)
        else:
            if hasattr(offset_buffer, 'exterior') and offset_buffer.exterior:
                coords = list(offset_buffer.exterior.coords)
                all_coords.extend(coords)
        
        if not all_coords:
            print("No coordinates found in buffer area")
            return None
        
        # Convert to numpy array for easier processing
        coords_array = np.array(all_coords)
        
        # Find extreme points
        min_x_idx = np.argmin(coords_array[:, 0])
        max_x_idx = np.argmax(coords_array[:, 0])
        min_y_idx = np.argmin(coords_array[:, 1])
        max_y_idx = np.argmax(coords_array[:, 1])
        
        extreme_points = {
            'leftmost': coords_array[min_x_idx],
            'rightmost': coords_array[max_x_idx],
            'topmost': coords_array[min_y_idx],  # In SVG, y=0 is at top
            'bottommost': coords_array[max_y_idx]
        }
        
        return extreme_points
        
    except Exception as e:
        print(f"Error finding extreme points: {e}")
        return None


def create_third_state_rectangle(extreme_points, canvas_width, canvas_height, alignment):
    """
    Create a third state rectangle based on alignment and extreme points, respecting flipped y-axis.
    In matplotlib/SVG: (0,0) is top-left, y increases downward.

    Args:
        extreme_points: Dict with leftmost, rightmost, topmost, bottommost points
        canvas_width: Width of the final canvas
        canvas_height: Height of the final canvas
        alignment: Position of state icon ("top-left", "top", etc.)

    Returns:
        shapely Polygon: Third state rectangle
    """
    if extreme_points is None:
        print("No extreme points provided for third state rectangle")
        return None

    try:
        x_left, y_left = float(extreme_points['leftmost'][0]), float(extreme_points['leftmost'][1])
        x_right, y_right = float(extreme_points['rightmost'][0]), float(extreme_points['rightmost'][1])
        x_top, y_top = float(extreme_points['topmost'][0]), float(extreme_points['topmost'][1])
        x_bottom, y_bottom = float(extreme_points['bottommost'][0]), float(extreme_points['bottommost'][1])

        if alignment == "middle":
            return None  # No third rectangle for middle alignment

        rectangle_coords = None
        
        if alignment == "top-left":
            # 3rd: Right-most point → draw up to y=0 → draw left to x=0 → close rectangle
            rectangle_coords = [
                (x_right, y_right),  # Start at right-most point
                (x_right, 0),        # Draw up to y=0
                (0, 0),              # Draw left to x=0
                (0, y_right),        # Draw down to same y as right-most
                (x_right, y_right)   # Close
            ]
            
        elif alignment == "top":
            # 3rd: Right-most point → draw up to y=0 → draw left to x(left-most) → draw down to y(right-most) → close
            rectangle_coords = [
                (x_right, y_right),  # Start at right-most point
                (x_right, 0),        # Draw up to y=0
                (x_left, 0),         # Draw left to x(left-most)
                (x_left, y_right),   # Draw down to y(right-most)
                (x_right, y_right)   # Close
            ]
            
        elif alignment == "top-right":
            # 3rd: Left-most point → draw up to y=0 → draw right to x=canvas_width → close rectangle
            rectangle_coords = [
                (x_left, y_left),         # Start at left-most point
                (x_left, 0),              # Draw up to y=0
                (canvas_width, 0),        # Draw right to canvas edge
                (canvas_width, y_left),   # Draw down to same y as left-most
                (x_left, y_left)          # Close
            ]
            
        elif alignment == "right":
            # 3rd: Top-most point → draw right to x=canvas_width → draw down to y(bottom-most) → draw left to x(top-most) → close
            rectangle_coords = [
                (x_top, y_top),           # Start at top-most point
                (canvas_width, y_top),    # Draw right to canvas edge
                (canvas_width, y_bottom), # Draw down to y(bottom-most)
                (x_top, y_bottom),        # Draw left to x(top-most)
                (x_top, y_top)            # Close
            ]
            
        elif alignment == "bottom-right":
            # 3rd: Left-most point → draw down to y=canvas_height → draw right to x=canvas_width → close rectangle
            rectangle_coords = [
                (x_left, y_left),         # Start at left-most point
                (x_left, canvas_height),  # Draw down to canvas bottom
                (canvas_width, canvas_height), # Draw right to canvas edge
                (canvas_width, y_left),   # Draw up to same y as left-most
                (x_left, y_left)          # Close
            ]
            
        elif alignment == "bottom":
            # 3rd: Right-most point → draw down to y=canvas_height → draw left to x(left-most) → draw up to y(right-most) → close
            rectangle_coords = [
                (x_right, y_right),       # Start at right-most point
                (x_right, canvas_height), # Draw down to canvas bottom
                (x_left, canvas_height),  # Draw left to x(left-most)
                (x_left, y_right),        # Draw up to y(right-most)
                (x_right, y_right)        # Close
            ]
            
        elif alignment == "bottom-left":
            # 3rd: Right-most point → draw down to y=canvas_height → draw left to x=0 → close rectangle
            rectangle_coords = [
                (x_right, y_right),       # Start at right-most point
                (x_right, canvas_height), # Draw down to canvas bottom
                (0, canvas_height),       # Draw left to x=0
                (0, y_right),             # Draw up to same y as right-most
                (x_right, y_right)        # Close
            ]
            
        elif alignment == "left":
            # 3rd: Top-most point → draw left to x=0 → draw down to y(bottom-most) → draw right to x(top-most) → close
            rectangle_coords = [
                (x_top, y_top),      # Start at top-most point
                (0, y_top),          # Draw left to x=0
                (0, y_bottom),       # Draw down to y(bottom-most)
                (x_top, y_bottom),   # Draw right to x(top-most)
                (x_top, y_top)       # Close
            ]

        if rectangle_coords is None:
            print(f"No third state rectangle defined for alignment: {alignment}")
            return None

        third_state_rectangle = ShapelyPolygon(rectangle_coords)
        if not third_state_rectangle.is_valid:
            third_state_rectangle = third_state_rectangle.buffer(0)

        # print(f"Created third state rectangle for alignment '{alignment}' with bounds: {third_state_rectangle.bounds}")
        return third_state_rectangle

    except Exception as e:
        print(f"Error creating third state rectangle: {e}")
        return None


def create_fourth_state_rectangle(extreme_points, canvas_width, canvas_height, alignment):
    """
    Create a fourth state rectangle based on alignment and extreme points, respecting flipped y-axis.
    In matplotlib/SVG: (0,0) is top-left, y increases downward.

    Args:
        extreme_points: Dict with leftmost, rightmost, topmost, bottommost points
        canvas_width: Width of the final canvas
        canvas_height: Height of the final canvas
        alignment: Position of state icon ("top-left", "top", etc.)

    Returns:
        shapely Polygon: Fourth state rectangle
    """
    if extreme_points is None:
        print("No extreme points provided for fourth state rectangle")
        return None

    try:
        x_left, y_left = float(extreme_points['leftmost'][0]), float(extreme_points['leftmost'][1])
        x_right, y_right = float(extreme_points['rightmost'][0]), float(extreme_points['rightmost'][1])
        x_top, y_top = float(extreme_points['topmost'][0]), float(extreme_points['topmost'][1])
        x_bottom, y_bottom = float(extreme_points['bottommost'][0]), float(extreme_points['bottommost'][1])

        if alignment == "middle":
            return None  # No fourth rectangle for middle alignment

        rectangle_coords = None
        
        if alignment == "top-left":
            # 4th: Bottom-most point → draw up to y=0 → draw left to x=0 → close rectangle
            rectangle_coords = [
                (x_bottom, y_bottom),  # Start at bottom-most point
                (x_bottom, 0),         # Draw up to y=0
                (0, 0),                # Draw left to x=0
                (0, y_bottom),         # Draw down to same y as bottom-most
                (x_bottom, y_bottom)   # Close
            ]
            
        elif alignment == "top":
            # 4th: Left-most point → draw up to y=0 → draw right to x(right-most) → draw down to y(left-most) → close
            rectangle_coords = [
                (x_left, y_left),    # Start at left-most point
                (x_left, 0),         # Draw up to y=0
                (x_right, 0),        # Draw right to x(right-most)
                (x_right, y_left),   # Draw down to y(left-most)
                (x_left, y_left)     # Close
            ]
            
        elif alignment == "top-right":
            # 4th: Bottom-most point → draw up to y=0 → draw right to x=canvas_width → close rectangle
            rectangle_coords = [
                (x_bottom, y_bottom),     # Start at bottom-most point
                (x_bottom, 0),            # Draw up to y=0
                (canvas_width, 0),        # Draw right to canvas edge
                (canvas_width, y_bottom), # Draw down to same y as bottom-most
                (x_bottom, y_bottom)      # Close
            ]
            
        elif alignment == "right":
            # 4th: Bottom-most point → draw right to x=canvas_width → draw up to y(top-most) → draw left to x(bottom-most) → close
            rectangle_coords = [
                (x_bottom, y_bottom),     # Start at bottom-most point
                (canvas_width, y_bottom), # Draw right to canvas edge
                (canvas_width, y_top),    # Draw up to y(top-most)
                (x_bottom, y_top),        # Draw left to x(bottom-most)
                (x_bottom, y_bottom)      # Close
            ]
            
        elif alignment == "bottom-right":
            # 4th: Top-most point → draw down to y=canvas_height → draw right to x=canvas_width → close rectangle
            rectangle_coords = [
                (x_top, y_top),           # Start at top-most point
                (x_top, canvas_height),   # Draw down to canvas bottom
                (canvas_width, canvas_height), # Draw right to canvas edge
                (canvas_width, y_top),    # Draw up to same y as top-most
                (x_top, y_top)            # Close
            ]
            
        elif alignment == "bottom":
            # 4th: Left-most point → draw down to y=canvas_height → draw right to x(right-most) → draw up to y(left-most) → close
            rectangle_coords = [
                (x_left, y_left),         # Start at left-most point
                (x_left, canvas_height),  # Draw down to canvas bottom
                (x_right, canvas_height), # Draw right to x(right-most)
                (x_right, y_left),        # Draw up to y(left-most)
                (x_left, y_left)          # Close
            ]
            
        elif alignment == "bottom-left":
            # 4th: Top-most point → draw down to y=canvas_height → draw left to x=0 → close rectangle
            rectangle_coords = [
                (x_top, y_top),         # Start at top-most point
                (x_top, canvas_height), # Draw down to canvas bottom
                (0, canvas_height),     # Draw left to x=0
                (0, y_top),             # Draw up to same y as top-most
                (x_top, y_top)          # Close
            ]
            
        elif alignment == "left":
            # 4th: Bottom-most point → draw left to x=0 → draw up to y(top-most) → draw right to x(bottom-most) → close
            rectangle_coords = [
                (x_bottom, y_bottom), # Start at bottom-most point
                (0, y_bottom),        # Draw left to x=0
                (0, y_top),           # Draw up to y(top-most)
                (x_bottom, y_top),    # Draw right to x(bottom-most)
                (x_bottom, y_bottom)  # Close
            ]

        if rectangle_coords is None:
            print(f"No fourth state rectangle defined for alignment: {alignment}")
            return None

        fourth_state_rectangle = ShapelyPolygon(rectangle_coords)
        if not fourth_state_rectangle.is_valid:
            fourth_state_rectangle = fourth_state_rectangle.buffer(0)

        # print(f"Created fourth state rectangle for alignment '{alignment}' with bounds: {fourth_state_rectangle.bounds}")
        return fourth_state_rectangle

    except Exception as e:
        print(f"Error creating fourth state rectangle: {e}")
        return None
    
def create_merged_light_red_area(buffer_area_stroke, buffer_area_convex, extreme_points, canvas_width, canvas_height, state_offset_x, state_offset_y, alignment):
    """
    Merge all state areas into a single light red area based on alignment.

    Args:
        buffer_area_stroke: Stroke buffer area around segments
        buffer_area_convex: Convex hull buffer area
        extreme_points: Dict with leftmost, rightmost, topmost, bottommost points
        canvas_width: Width of the final canvas
        canvas_height: Height of the final canvas
        state_offset_x: X offset for positioning
        state_offset_y: Y offset for positioning
        alignment: Position of state icon ("top-left", "top", etc.)

    Returns:
        shapely Polygon: Merged area for light red visualization
    """
    try:
        # print("Creating merged light red area from state areas...")
        
        areas_to_merge = []
        
        # Translate and add stroke buffer area
        if buffer_area_stroke is not None:
            offset_stroke = translate(buffer_area_stroke, xoff=state_offset_x, yoff=state_offset_y)
            if not offset_stroke.is_valid:
                offset_stroke = offset_stroke.buffer(0)
            areas_to_merge.append(offset_stroke)
        
        # Translate and add convex buffer area
        if buffer_area_convex is not None:
            offset_convex = translate(buffer_area_convex, xoff=state_offset_x, yoff=state_offset_y)
            if not offset_convex.is_valid:
                offset_convex = offset_convex.buffer(0)
            areas_to_merge.append(offset_convex)
        
        # Add third and fourth state rectangles only for non-middle alignments
        if alignment != "middle":
            third_state_rectangle = create_third_state_rectangle(extreme_points, canvas_width, canvas_height, alignment)
            if third_state_rectangle is not None:
                if not third_state_rectangle.is_valid:
                    third_state_rectangle = third_state_rectangle.buffer(0)
                areas_to_merge.append(third_state_rectangle)
                # print(f"Added third state rectangle with bounds: {third_state_rectangle.bounds}")
            
            fourth_state_rectangle = create_fourth_state_rectangle(extreme_points, canvas_width, canvas_height, alignment)
            if fourth_state_rectangle is not None:
                if not fourth_state_rectangle.is_valid:
                    fourth_state_rectangle = fourth_state_rectangle.buffer(0)
                areas_to_merge.append(fourth_state_rectangle)
                # print(f"Added fourth state rectangle with bounds: {fourth_state_rectangle.bounds}")
        
        if not areas_to_merge:
            print("No valid areas to merge")
            return None
        
        # Merge all areas using unary_union
        merged_area = unary_union(areas_to_merge)
        
        if not merged_area.is_valid:
            merged_area = merged_area.buffer(0)

        return merged_area
        
    except Exception as e:
        print(f"Error creating merged light red area: {e}")
        return None
