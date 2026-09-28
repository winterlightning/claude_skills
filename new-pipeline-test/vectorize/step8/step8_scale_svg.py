import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
from matplotlib.collections import PatchCollection
import xml.etree.ElementTree as ET
import re
import os


def _sample_svg_arc(x1, y1, rx, ry, phi_deg, large_arc, sweep, x2, y2, n=16):
    """Sample n points along an SVG A-arc (W3C F.6.5 endpoint→center form)."""
    if rx == 0 or ry == 0 or (x1 == x2 and y1 == y2):
        return []
    rx, ry = abs(rx), abs(ry)
    phi = np.radians(phi_deg)
    cos_p, sin_p = np.cos(phi), np.sin(phi)
    dx, dy = (x1 - x2) / 2.0, (y1 - y2) / 2.0
    x1p = cos_p * dx + sin_p * dy
    y1p = -sin_p * dx + cos_p * dy
    lam = (x1p / rx) ** 2 + (y1p / ry) ** 2
    if lam > 1:  # radii too small — scale up per spec
        s = np.sqrt(lam)
        rx, ry = rx * s, ry * s
    num = rx**2 * ry**2 - rx**2 * y1p**2 - ry**2 * x1p**2
    den = rx**2 * y1p**2 + ry**2 * x1p**2
    coef = np.sqrt(max(num / den, 0.0))
    if large_arc == sweep:
        coef = -coef
    cxp = coef * rx * y1p / ry
    cyp = -coef * ry * x1p / rx
    cx = cos_p * cxp - sin_p * cyp + (x1 + x2) / 2.0
    cy = sin_p * cxp + cos_p * cyp + (y1 + y2) / 2.0
    theta1 = np.arctan2((y1p - cyp) / ry, (x1p - cxp) / rx)
    theta2 = np.arctan2((-y1p - cyp) / ry, (-x1p - cxp) / rx)
    dtheta = theta2 - theta1
    if sweep and dtheta < 0:
        dtheta += 2 * np.pi
    elif not sweep and dtheta > 0:
        dtheta -= 2 * np.pi
    ts = theta1 + dtheta * np.linspace(0.0, 1.0, n)
    xs = cx + rx * np.cos(ts) * cos_p - ry * np.sin(ts) * sin_p
    ys = cy + rx * np.cos(ts) * sin_p + ry * np.sin(ts) * cos_p
    return list(zip(xs.tolist(), ys.tolist()))


def parse_svg_path(path_data):
    """
    Parse SVG path data and convert it to a list of polygon vertices.
    This handles basic SVG path commands (M, L, Z, etc.)
    """
    # Define regex patterns for SVG path commands
    command_pattern = r'([MLHVZCQTSAmlhvzcqtsa])([^MLHVZCQTSAmlhvzcqtsa]*)'
    coord_pattern = r'(-?\d+\.?\d*)[,\s]?(-?\d+\.?\d*)?'
    
    polygons = []
    current_polygon = []
    current_point = (0, 0)
    
    # Parse commands
    commands = re.findall(command_pattern, path_data)
    
    for cmd, params in commands:
        # Get coordinates from parameters
        coords = re.findall(coord_pattern, params)
        
        if cmd == 'M' or cmd == 'm':  # Move to
            relative = (cmd == 'm')
            if current_polygon and len(current_polygon) >= 2:  # Changed from > 2 to >= 2
                polygons.append(np.array(current_polygon))
            current_polygon = []
            
            for x, y in coords:
                x, y = float(x), float(y)
                if relative:
                    current_point = (current_point[0] + x, current_point[1] + y)
                else:
                    current_point = (x, y)
                current_polygon.append(current_point)
        
        elif cmd == 'L' or cmd == 'l':  # Line to
            relative = (cmd == 'l')
            for x, y in coords:
                x, y = float(x), float(y)
                if relative:
                    current_point = (current_point[0] + x, current_point[1] + y)
                else:
                    current_point = (x, y)
                current_polygon.append(current_point)
        
        elif cmd == 'H' or cmd == 'h':  # Horizontal line
            relative = (cmd == 'h')
            for x, _ in coords:
                x = float(x)
                if relative:
                    current_point = (current_point[0] + x, current_point[1])
                else:
                    current_point = (x, current_point[1])
                current_polygon.append(current_point)
        
        elif cmd == 'V' or cmd == 'v':  # Vertical line
            relative = (cmd == 'v')
            for _, y in coords:
                if y:
                    y = float(y)
                    if relative:
                        current_point = (current_point[0], current_point[1] + y)
                    else:
                        current_point = (current_point[0], y)
                    current_polygon.append(current_point)
        
        elif cmd in ('C', 'Q', 'S', 'T'):  # Curves (absolute) — control points
            # bound the curve (convex-hull property), so including them gives
            # a conservative extrema estimate; the endpoint is exact.
            all_nums = re.findall(r'-?\d+\.?\d*', params)
            all_nums = [float(n) for n in all_nums]
            for i in range(0, len(all_nums) - 1, 2):
                current_point = (all_nums[i], all_nums[i + 1])
                current_polygon.append(current_point)

        elif cmd == 'A' or cmd == 'a':  # Arc — sample points along arc for extrema
            relative = (cmd == 'a')
            all_nums = re.findall(r'-?\d+\.?\d*', params)
            all_nums = [float(n) for n in all_nums]
            for i in range(0, len(all_nums) - 6, 7):
                rx_a, ry_a = all_nums[i], all_nums[i + 1]
                phi_a = all_nums[i + 2]
                laf_a, sf_a = all_nums[i + 3], all_nums[i + 4]
                x, y = all_nums[i + 5], all_nums[i + 6]
                x1, y1 = current_point
                if relative:
                    x2, y2 = x1 + x, y1 + y
                else:
                    x2, y2 = x, y
                # Sample the true arc: a wide arc (e.g. a dome crown) bulges
                # up to a full radius beyond its chord, so the old
                # chord-midpoint approximation under-measured the extents
                # and let Step 8 clip the crown off the canvas.
                for px, py in _sample_svg_arc(x1, y1, rx_a, ry_a, phi_a,
                                              laf_a, sf_a, x2, y2):
                    current_polygon.append((px, py))
                current_point = (x2, y2)
                current_polygon.append(current_point)

        elif cmd == 'Z' or cmd == 'z':  # Close path
            if current_polygon and len(current_polygon) > 0:
                current_polygon.append(current_polygon[0])  # Close the loop
                polygons.append(np.array(current_polygon))
                current_polygon = []

    # Add any remaining polygon
    if current_polygon and len(current_polygon) >= 2:  # Changed from > 2 to >= 2
        polygons.append(np.array(current_polygon))
    
    return polygons

def find_extrema_points(polygons):
    """
    Find the extrema points (top, bottom, left, right) of all polygons
    
    Returns:
        Dict with points and their coordinates
    """
    # Initialize with extreme values
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = float('-inf'), float('-inf')
    
    # Points to store
    top_point = None     # Highest y-value
    bottom_point = None  # Lowest y-value
    left_point = None    # Leftmost x-value
    right_point = None   # Rightmost x-value
    
    # Iterate through all polygons and their points
    for polygon in polygons:
        for point in polygon:
            x, y = point
            
            # Update leftmost point (minimum x)
            if x < min_x:
                min_x = x
                left_point = (x, y)
            
            # Update rightmost point (maximum x)
            if x > max_x:
                max_x = x
                right_point = (x, y)
            
            # Update top point (maximum y)
            # Note: In many SVG coordinate systems, the y-axis is inverted
            if y > max_y:
                max_y = y
                top_point = (x, y)
            
            # Update bottom point (minimum y)
            if y < min_y:
                min_y = y
                bottom_point = (x, y)
    
    # Create a dictionary with the results
    extrema = {
        'top': top_point,
        'bottom': bottom_point,
        'left': left_point,
        'right': right_point,
        'min_x': min_x,
        'max_x': max_x,
        'min_y': min_y,
        'max_y': max_y
    }
    
    return extrema

def clean_svg_improved(input_svg, output_svg):
    """
    Process an SVG file to clean it while preserving namespace functionality:
    1. Properly handle ns0 namespaces instead of removing them
    2. Change fill and stroke color from #0000FF to BLACK
    3. Add necessary style information if missing
    
    Args:
        input_svg: Path to the input SVG file
        output_svg: Path to save the processed SVG
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Read the SVG file as text to preserve formatting
        with open(input_svg, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        
        # Fix XML declaration only if missing
        if '<?xml' not in svg_content:
            svg_content = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg_content
        
        # Add DOCTYPE only if missing
        if '<!DOCTYPE' not in svg_content:
            svg_content = svg_content.replace('<?xml version="1.0" encoding="UTF-8"?>', 
                          '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">')
        
        # IMPROVED: Remove ns0 namespace completely and use standard SVG namespace
        # Clean up namespaces using the new cleanup function
        svg_content = clean_svg_namespaces(svg_content)
        
        # Change fill color from #0000FF to BLACK
        svg_content = svg_content.replace('fill="#0000FF"', 'fill="black"')
        svg_content = svg_content.replace('fill="#0000ff"', 'fill="black"')
        svg_content = svg_content.replace('fill="blue"', 'fill="black"')
        
        # Change stroke color from #0000FF to BLACK
        svg_content = svg_content.replace('stroke="#0000FF"', 'stroke="black"')
        svg_content = svg_content.replace('stroke="#0000ff"', 'stroke="black"')
        svg_content = svg_content.replace('stroke="blue"', 'stroke="black"')
        
        # Add default style if no style or color attributes are found
        if ('fill=' not in svg_content and 'stroke=' not in svg_content and 
            'style=' not in svg_content):
            # Find the first path tag and add style attributes
            svg_content = re.sub(r'(<path[^>]*)(>)', 
                               r'\1 fill="black" stroke="black"\2', 
                               svg_content)
        
        # Namespace cleanup is already handled above
        
        # Save the processed SVG
        with open(output_svg, 'w', encoding='utf-8') as f:
            f.write(svg_content)
            
        print(f"Successfully processed SVG: {input_svg}")
        print(f"Output saved to: {output_svg}")
        return True
    
    except Exception as e:
        print(f"Error processing SVG file: {e}")
        return False
    
def transform_path_coordinates_with_padding(path_data, extrema, scale_factor, offset_x, offset_y):
    """
    Transform SVG path coordinates to the new scaled coordinate system with padding offset
    """
    # Define regex patterns for SVG path commands
    command_pattern = r'([MLHVZCQTSAmlhvzcqtsa])([^MLHVZCQTSAmlhvzcqtsa]*)'
    coord_pattern = r'(-?\d+\.?\d*)'
    
    def transform_point(x, y, is_relative=False):
        """Transform a single point with padding offset"""
        if is_relative:
            # For relative coordinates, only scale (don't translate or offset)
            return x * scale_factor, y * scale_factor
        else:
            # For absolute coordinates, translate, scale, then add padding offset
            new_x = (x - extrema['min_x']) * scale_factor + offset_x
            new_y = (y - extrema['min_y']) * scale_factor + offset_y
            return new_x, new_y
    
    # Parse and transform commands
    commands = re.findall(command_pattern, path_data)
    transformed_parts = []
    
    for cmd, params in commands:
        is_relative = cmd.islower()
        cmd_upper = cmd.upper()
        
        # Extract all numbers from parameters
        coords = re.findall(coord_pattern, params)
        coords = [float(c) for c in coords]
        
        transformed_coords = []
        
        if cmd_upper in ['M', 'L']:  # Move to, Line to
            for i in range(0, len(coords), 2):
                if i + 1 < len(coords):
                    x, y = coords[i], coords[i + 1]
                    new_x, new_y = transform_point(x, y, is_relative)
                    transformed_coords.extend([new_x, new_y])
        
        elif cmd_upper == 'H':  # Horizontal line
            for x in coords:
                if is_relative:
                    new_x = x * scale_factor
                else:
                    new_x = (x - extrema['min_x']) * scale_factor + offset_x
                transformed_coords.append(new_x)
        
        elif cmd_upper == 'V':  # Vertical line
            for y in coords:
                if is_relative:
                    new_y = y * scale_factor
                else:
                    new_y = (y - extrema['min_y']) * scale_factor + offset_y
                transformed_coords.append(new_y)
        
        elif cmd_upper == 'C':  # Cubic Bezier curve
            for i in range(0, len(coords), 6):
                if i + 5 < len(coords):
                    for j in range(3):  # Three pairs of coordinates
                        x, y = coords[i + j*2], coords[i + j*2 + 1]
                        new_x, new_y = transform_point(x, y, is_relative)
                        transformed_coords.extend([new_x, new_y])
        
        elif cmd_upper == 'Q':  # Quadratic Bezier curve
            for i in range(0, len(coords), 4):
                if i + 3 < len(coords):
                    for j in range(2):  # Two pairs of coordinates
                        x, y = coords[i + j*2], coords[i + j*2 + 1]
                        new_x, new_y = transform_point(x, y, is_relative)
                        transformed_coords.extend([new_x, new_y])
        
        elif cmd_upper in ['S', 'T']:  # Smooth curves
            for i in range(0, len(coords), 2):
                if i + 1 < len(coords):
                    x, y = coords[i], coords[i + 1]
                    new_x, new_y = transform_point(x, y, is_relative)
                    transformed_coords.extend([new_x, new_y])
        
        elif cmd_upper == 'A':  # Arc
            for i in range(0, len(coords), 7):
                if i + 6 < len(coords):
                    rx, ry = coords[i], coords[i + 1]
                    x_axis_rotation = coords[i + 2]
                    large_arc_flag = coords[i + 3]
                    sweep_flag = coords[i + 4]
                    x, y = coords[i + 5], coords[i + 6]
                    
                    # Scale radii
                    new_rx = rx * scale_factor
                    new_ry = ry * scale_factor
                    
                    # Transform end point
                    new_x, new_y = transform_point(x, y, is_relative)
                    
                    transformed_coords.extend([
                        new_rx, new_ry, x_axis_rotation, 
                        large_arc_flag, sweep_flag, new_x, new_y
                    ])
        
        elif cmd_upper == 'Z':  # Close path
            pass
        
        # Build the transformed command string
        if cmd_upper == 'Z':
            transformed_parts.append(cmd)
        else:
            coord_strs = []
            for coord in transformed_coords:
                if abs(coord - round(coord)) < 0.001:
                    coord_strs.append(str(int(round(coord))))
                else:
                    coord_strs.append(f"{coord:.3f}")
            
            if coord_strs:
                transformed_parts.append(f"{cmd}{' '.join(coord_strs)}")
            else:
                transformed_parts.append(cmd)
    
    return ''.join(transformed_parts)

def clean_svg_namespaces(svg_content):
    """
    Clean up SVG namespaces and ensure proper structure without ns0 prefixes

    Args:
        svg_content (str): Raw SVG content

    Returns:
        str: Cleaned SVG content with proper namespaces
    """
    # Remove ns0: prefixes from elements and attributes
    svg_content = re.sub(r'<ns0:', '<', svg_content)
    svg_content = re.sub(r'</ns0:', '</', svg_content)
    svg_content = re.sub(r'ns0:', '', svg_content)

    # Ensure proper SVG namespace declaration
    if 'xmlns="http://www.w3.org/2000/svg"' not in svg_content:
        svg_content = svg_content.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"', 1)

    # Remove duplicate or unwanted namespace declarations
    svg_content = re.sub(r'xmlns:ns0="[^"]*"', '', svg_content)

    # Clean up any double spaces that might result from removals
    svg_content = re.sub(r'\s+', ' ', svg_content)
    svg_content = re.sub(r'\s+>', '>', svg_content)

    return svg_content

def transform_svg_consistent(svg_file_path, output_path, extrema, target_dimension=300, padding=20):
    """
    Transform SVG file with consistent scaling approach and visible padding
    The content is scaled to fit within (target_dimension - 2*padding)
    But the final SVG canvas is always target_dimension x target_dimension
    """
    try:
        # Parse the SVG
        tree = ET.parse(svg_file_path)
        root = tree.getroot()
        
        # Calculate scale factor with padding consideration
        original_width = extrema['max_x'] - extrema['min_x']
        original_height = extrema['max_y'] - extrema['min_y']
        max_original_dimension = max(original_width, original_height)
        
        # Scale to fit within (target_dimension - 2*padding)
        available_space = target_dimension - (2 * padding)
        scale_factor = available_space / max_original_dimension if max_original_dimension > 0 else 1
        
        # Calculate scaled content dimensions
        scaled_width = original_width * scale_factor
        scaled_height = original_height * scale_factor
        
        # Calculate offset to center the content with padding
        offset_x = (target_dimension - scaled_width) / 2
        offset_y = (target_dimension - scaled_height) / 2
        
        # Find all path elements and transform their coordinates
        paths = []
        ns = {'svg': 'http://www.w3.org/2000/svg'}
        
        # Get paths with different namespace approaches
        ns_paths = root.findall('.//svg:path', ns)
        if ns_paths: paths.extend(ns_paths)
        plain_paths = root.findall('.//path')
        if plain_paths: paths.extend(plain_paths)
        ns0_paths = root.findall('.//{*}path')
        if ns0_paths:
            for p in ns0_paths:
                if p not in paths: paths.append(p)
        
        # Transform each path's coordinates
        for path in paths:
            path_data = path.get('d')
            if path_data:
                # Transform the path data with padding offset
                transformed_path_data = transform_path_coordinates_with_padding(
                    path_data, extrema, scale_factor, offset_x, offset_y
                )
                path.set('d', transformed_path_data)
                # Scale stroke-width proportionally
                sw = path.get('stroke-width')
                if sw:
                    try:
                        path.set('stroke-width', f"{float(sw) * scale_factor:.2f}")
                    except ValueError:
                        pass

        # Transform circle elements
        circles = []
        ns_circles = root.findall('.//svg:circle', ns)
        if ns_circles: circles.extend(ns_circles)
        plain_circles = root.findall('.//circle')
        if plain_circles: circles.extend(plain_circles)
        wildcard_circles = root.findall('.//{*}circle')
        if wildcard_circles:
            for c in wildcard_circles:
                if c not in circles: circles.append(c)

        for circle in circles:
            cx = float(circle.get('cx', 0))
            cy = float(circle.get('cy', 0))
            r = float(circle.get('r', 0))
            new_cx = (cx - extrema['min_x']) * scale_factor + offset_x
            new_cy = (cy - extrema['min_y']) * scale_factor + offset_y
            new_r = r * scale_factor
            circle.set('cx', f"{new_cx:.2f}")
            circle.set('cy', f"{new_cy:.2f}")
            circle.set('r', f"{new_r:.2f}")
            sw = circle.get('stroke-width')
            if sw:
                try:
                    circle.set('stroke-width', f"{float(sw) * scale_factor:.2f}")
                except ValueError:
                    pass

        # Transform line elements
        lines = []
        ns_lines = root.findall('.//svg:line', ns)
        if ns_lines: lines.extend(ns_lines)
        plain_lines = root.findall('.//line')
        if plain_lines: lines.extend(plain_lines)
        wildcard_lines = root.findall('.//{*}line')
        if wildcard_lines:
            for l in wildcard_lines:
                if l not in lines: lines.append(l)

        for line in lines:
            x1 = float(line.get('x1', 0))
            y1 = float(line.get('y1', 0))
            x2 = float(line.get('x2', 0))
            y2 = float(line.get('y2', 0))
            new_x1 = (x1 - extrema['min_x']) * scale_factor + offset_x
            new_y1 = (y1 - extrema['min_y']) * scale_factor + offset_y
            new_x2 = (x2 - extrema['min_x']) * scale_factor + offset_x
            new_y2 = (y2 - extrema['min_y']) * scale_factor + offset_y
            line.set('x1', f"{new_x1:.2f}")
            line.set('y1', f"{new_y1:.2f}")
            line.set('x2', f"{new_x2:.2f}")
            line.set('y2', f"{new_y2:.2f}")
            sw = line.get('stroke-width')
            if sw:
                try:
                    line.set('stroke-width', f"{float(sw) * scale_factor:.2f}")
                except ValueError:
                    pass

        # Transform rect elements
        rects = []
        ns_rects = root.findall('.//svg:rect', ns)
        if ns_rects: rects.extend(ns_rects)
        plain_rects = root.findall('.//rect')
        if plain_rects: rects.extend(plain_rects)
        wildcard_rects = root.findall('.//{*}rect')
        if wildcard_rects:
            for r in wildcard_rects:
                if r not in rects: rects.append(r)

        for rect in rects:
            rx = float(rect.get('x', 0))
            ry = float(rect.get('y', 0))
            rw = float(rect.get('width', 0))
            rh = float(rect.get('height', 0))
            rrx = float(rect.get('rx', 0))
            rry = float(rect.get('ry', 0))

            new_x = (rx - extrema['min_x']) * scale_factor + offset_x
            new_y = (ry - extrema['min_y']) * scale_factor + offset_y
            new_w = rw * scale_factor
            new_h = rh * scale_factor
            new_rx = rrx * scale_factor
            new_ry = rry * scale_factor

            rect.set('x', f"{new_x:.2f}")
            rect.set('y', f"{new_y:.2f}")
            rect.set('width', f"{new_w:.2f}")
            rect.set('height', f"{new_h:.2f}")
            rect.set('rx', f"{new_rx:.2f}")
            rect.set('ry', f"{new_ry:.2f}")
            sw = rect.get('stroke-width')
            if sw:
                try:
                    rect.set('stroke-width', f"{float(sw) * scale_factor:.2f}")
                except ValueError:
                    pass

            # Update rotation center in transform attribute if present
            transform = rect.get('transform', '')
            if 'rotate(' in transform:
                import re as _re
                match = _re.search(r'rotate\(([^\s]+)\s+([^\s]+)\s+([^\)]+)\)', transform)
                if match:
                    rot_angle = match.group(1)
                    old_cx = float(match.group(2))
                    old_cy = float(match.group(3))
                    new_cx = (old_cx - extrema['min_x']) * scale_factor + offset_x
                    new_cy = (old_cy - extrema['min_y']) * scale_factor + offset_y
                    rect.set('transform', f"rotate({rot_angle} {new_cx:.2f} {new_cy:.2f})")

        # Set the viewBox to show the full canvas (always target_dimension x target_dimension)
        viewBox = f"0 0 {target_dimension} {target_dimension}"
        
        # Update the SVG root element
        root.set('viewBox', viewBox)
        root.set('width', f"{target_dimension}")
        root.set('height', f"{target_dimension}")
        
        # Remove preserveAspectRatio or set to none
        if 'preserveAspectRatio' in root.attrib:
            root.set('preserveAspectRatio', 'none')
        
        # Write the transformed SVG with namespace cleanup
        # First write to string to clean namespaces
        svg_string = ET.tostring(root, encoding='unicode')

        # Clean up namespaces
        cleaned_svg = clean_svg_namespaces(svg_string)

        # Add XML declaration if missing
        if not cleaned_svg.startswith('<?xml'):
            cleaned_svg = '<?xml version="1.0" encoding="UTF-8"?>\n' + cleaned_svg

        # Write cleaned SVG to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_svg)
        
        print(f"SVG transformation with padding applied:")
        print(f"  Original content: {original_width:.1f} x {original_height:.1f}")
        print(f"  Max original dimension: {max_original_dimension:.1f}")
        print(f"  Available space (with padding): {available_space}")
        print(f"  Scale factor: {scale_factor:.4f}")
        print(f"  Scaled content: {scaled_width:.1f} x {scaled_height:.1f}")
        print(f"  Final canvas: {target_dimension} x {target_dimension}")
        print(f"  Padding: {padding}px")
        print(f"  Content centered at: ({offset_x:.1f}, {offset_y:.1f})")
        
        return True
        
    except Exception as e:
        print(f"Error in SVG transformation: {e}")
        return False

def change_stroke_width(input_file, stroke_width = 8):
    """
    Change the stroke width of an SVG file
    
    Args:
        input_file: Path to the input SVG file
        stroke_width: Desired stroke width (default is 8)
    
    Returns:
        True if successful, False otherwise
    """
    try:
        # Read the SVG file
        with open(input_file, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        
        # Change stroke width
        svg_content = re.sub(r'stroke-width="[^"]*"', f'stroke-width="{stroke_width}"', svg_content)
        
        
        input_file_name = input_file.replace('.svg', '')
        output_file_name = os.path.basename(input_file_name) + f'_stroke_{stroke_width}.svg'
        output_file_path = os.path.join(os.path.dirname(input_file), output_file_name)
        # Save the modified SVG
        with open(output_file_path, 'w', encoding='utf-8') as f:    
            f.write(svg_content)
                    
        print(f"Stroke width changed to {stroke_width} in {input_file}")
        return True
    
    except Exception as e:
        print(f"Error changing stroke width: {e}")
        return False


def process_icon(input, output, stroke_width=None):
    print("=== SVG TRANSFORMATION WITH PADDING ===")
    
    # Parse SVG and extract polygons
    tree = ET.parse(input)
    root = tree.getroot()
    
    # Find all paths
    paths = []
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    ns_paths = root.findall('.//svg:path', ns)
    if ns_paths: paths.extend(ns_paths)
    plain_paths = root.findall('.//path')
    if plain_paths: paths.extend(plain_paths)
    ns0_paths = root.findall('.//{*}path')
    if ns0_paths:
        for p in ns0_paths:
            if p not in paths: paths.append(p)
    
    # Extract polygons
    all_polygons = []
    for path in paths:
        path_data = path.get('d')
        if path_data:
            polygons = parse_svg_path(path_data)
            if polygons: all_polygons.extend(polygons)

    # Also include circle bounds in extrema
    circles = []
    ns_circles = root.findall('.//svg:circle', ns)
    if ns_circles: circles.extend(ns_circles)
    plain_circles = root.findall('.//circle')
    if plain_circles: circles.extend(plain_circles)
    wildcard_circles = root.findall('.//{*}circle')
    if wildcard_circles:
        for c in wildcard_circles:
            if c not in circles: circles.append(c)

    for circle in circles:
        cx = float(circle.get('cx', 0))
        cy = float(circle.get('cy', 0))
        r = float(circle.get('r', 0))
        # Add circle bounding box as a polygon (4 corner points)
        all_polygons.append([
            (cx - r, cy - r),
            (cx + r, cy - r),
            (cx + r, cy + r),
            (cx - r, cy + r),
        ])

    # Also include line bounds in extrema
    lines = []
    ns_lines = root.findall('.//svg:line', ns)
    if ns_lines: lines.extend(ns_lines)
    plain_lines = root.findall('.//line')
    if plain_lines: lines.extend(plain_lines)
    wildcard_lines = root.findall('.//{*}line')
    if wildcard_lines:
        for l in wildcard_lines:
            if l not in lines: lines.append(l)

    for line in lines:
        x1 = float(line.get('x1', 0))
        y1 = float(line.get('y1', 0))
        x2 = float(line.get('x2', 0))
        y2 = float(line.get('y2', 0))
        all_polygons.append([
            (x1, y1),
            (x2, y2),
        ])

    # Also include rect bounds in extrema
    rects = []
    ns_rects = root.findall('.//svg:rect', ns)
    if ns_rects: rects.extend(ns_rects)
    plain_rects = root.findall('.//rect')
    if plain_rects: rects.extend(plain_rects)
    wildcard_rects = root.findall('.//{*}rect')
    if wildcard_rects:
        for r in wildcard_rects:
            if r not in rects: rects.append(r)

    for rect in rects:
        rx = float(rect.get('x', 0))
        ry = float(rect.get('y', 0))
        rw = float(rect.get('width', 0))
        rh = float(rect.get('height', 0))
        all_polygons.append([
            (rx, ry),
            (rx + rw, ry),
            (rx + rw, ry + rh),
            (rx, ry + rh),
        ])

    if all_polygons:
        # Find extrema points
        extrema = find_extrema_points(all_polygons)

        # Expand extrema by half the max stroke-width to prevent clipping
        max_sw = 0
        for elem_list in [paths, circles, lines, rects]:
            for elem in elem_list:
                sw = elem.get('stroke-width')
                if sw:
                    try:
                        max_sw = max(max_sw, float(sw))
                    except ValueError:
                        pass
        half_sw = max_sw / 2
        if half_sw > 0:
            extrema['min_x'] -= half_sw
            extrema['min_y'] -= half_sw
            extrema['max_x'] += half_sw
            extrema['max_y'] += half_sw

        # Transform and save SVG with padding
        success = transform_svg_consistent(
            input, output, extrema, 
            target_dimension=1024, padding=4
        )
        
        if success:
            print(f"✅ Transformed SVG saved to: {output}")
            # User-requested stroke width overrides every measurement.
            # Applied after scaling so the value the user typed lands in the
            # final SVG verbatim (no scale_factor multiplication).
            if stroke_width is not None:
                with open(output, 'r', encoding='utf-8') as f:
                    svg_content = f.read()
                svg_content = re.sub(
                    r'stroke-width="[^"]*"',
                    f'stroke-width="{stroke_width}"',
                    svg_content,
                )
                with open(output, 'w', encoding='utf-8') as f:
                    f.write(svg_content)
                print(f"  Stroke width forced to {stroke_width}")
        else:
            print("❌ Failed to save transformed SVG")
    else:
        print("No polygons found in SVG")
