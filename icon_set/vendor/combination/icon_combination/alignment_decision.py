import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Tuple

def calculate_main_icon_position(main_icon_alignment: str, scaled_width, scaled_height,
                                 canvas_size: int = 1024) -> Tuple[float, float]:
    """
    Calculates the (X, Y) position for the main icon based on the state icon alignment.
    Assumes y=0 at top, y=canvas_size at bottom (image coordinates).

    Args:
        main_icon_alignment (str): The alignment of the state icon (e.g., 'bottom-right', 'right', etc.).
        scaled_width (float): The scaled width of the main icon after scaling transformations.
        scaled_height (float): The scaled height of the main icon after scaling transformations.
        canvas_size (int): Size of the square canvas (default 1024).

    Returns:
        tuple[float, float, bool]: (X, Y) position for the main icon's top-left corner and is_corner_case flag.
    """
    # Compute scaled dimensions preserving aspect ratio

    # If state icon is aligned to one side, swap to opposite side for main icon
    alignment_map = {
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
    main_icon_alignment = alignment_map.get(main_icon_alignment, main_icon_alignment)
    
    # Define positions based on alignments (X, Y for main icon top-left, y=0 top)
    # Adjusted Y calculations for y increasing downward
    # print(f'Scaled dimensions: {scaled_width} x {scaled_height}, alignment: {main_icon_alignment}')
    positions = {
        # Corner cases (main opposite to state)
        'bottom-right': (canvas_size - scaled_width, canvas_size - scaled_height),  # Main top-left
        'top-right': (canvas_size - scaled_width, 0),
        'bottom-left': (0, canvas_size - scaled_height),
        'top-left': (0, 0),
        # Edge-aligned cases (centered on the opposite side)
        'right': (canvas_size - scaled_width, (canvas_size - scaled_height) / 2),  # Main left, centered vertically
        'left': (0, (canvas_size - scaled_height) / 2),  # Main right
        'top': ((canvas_size - scaled_width) / 2, 0),  # Main centered horizontally, at top
        'bottom': ((canvas_size - scaled_width) / 2, canvas_size - scaled_height),  # Main centered horizontally, at bottom
        # Center case (main icon at center)
        'center': ((canvas_size - scaled_width) / 2, (canvas_size - scaled_height) / 2),  # Main centered both horizontally and vertically
    }

    x, y = positions[main_icon_alignment]

    # print(f'Main icon position calculated: ({x:.1f}, {y:.1f})')
    is_corner_case = main_icon_alignment in ['bottom-right', 'top-right', 'bottom-left', 'top-left']
    return (x, y, is_corner_case)

def plot_icon_positions(main_icon_alignment: str, aspect_ratio: float, 
                        aspect_ratio_threshold: float = 1.2, 
                        scale_factor: float = 0.8, 
                        canvas_size: int = 1024, 
                        figsize: Tuple[float, float] = (8, 8)):
    """
    Plots the canvas with the main icon positioned according to the formula.
    Flipped y-axis to match image coordinates (y=0 at top, y increases downward).
    
    Args:
        main_icon_alignment (str): Alignment string.
        aspect_ratio (float): Icon aspect ratio (width/height). Adjustable.
        aspect_ratio_threshold (float): Swap threshold. Adjustable.
        scale_factor (float): Icon size fraction. Adjustable.
        canvas_size (int): Canvas size.
        figsize (tuple): Matplotlib figure size.
    
    Usage: Call this function with your parameters to visualize.
    """
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    ax.set_xlim(0, canvas_size)
    ax.set_ylim(canvas_size, 0)  # Flipped: y=canvas at bottom, y=0 at top
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.set_title(f'Main Icon Position (Y-Flipped)\nAlignment: {main_icon_alignment}, AR: {aspect_ratio}, Scale: {scale_factor}')
    
    # Draw canvas border
    canvas = patches.Rectangle((0, 0), canvas_size, canvas_size, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(canvas)
    
    # Calculate and draw main icon (positions assume y=0 top)
    x, y, w, h, is_corner_case = calculate_main_icon_position(main_icon_alignment, aspect_ratio, 
                                              aspect_ratio_threshold, scale_factor, canvas_size)
    # Since ylim is flipped, but coordinates are as-is (y large = bottom), it matches
    main_icon = patches.Rectangle((x, y), w, h, linewidth=2, edgecolor='blue', facecolor='lightblue', alpha=0.7)
    ax.add_patch(main_icon)
    ax.text(x + w/2, y + h/2, 'Main Icon', ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Optional: Draw state icon placeholder (adjusted for y=0 top)
    state_size = 512  # Fixed small size for state icon
    if 'bottom-right' in main_icon_alignment:
        state_x, state_y = (canvas_size - state_size, canvas_size - state_size)
    elif 'top-right' in main_icon_alignment:
        state_x, state_y = (canvas_size - state_size, 0)
    elif 'bottom-left' in main_icon_alignment:
        state_x, state_y = (0, canvas_size - state_size)
    elif 'top-left' in main_icon_alignment:
        state_x, state_y = (0, 0)
    elif 'right' in main_icon_alignment:
        state_x, state_y = (canvas_size - state_size, (canvas_size - state_size)/2)
    elif 'left' in main_icon_alignment:
        state_x, state_y = (0, (canvas_size - state_size)/2)
    elif 'bottom' in main_icon_alignment:
        state_x, state_y = ((canvas_size - state_size)/2, canvas_size - state_size)
    elif 'top' in main_icon_alignment:
        state_x, state_y = ((canvas_size - state_size)/2, 0)
    else:
        state_x, state_y = (canvas_size/2, canvas_size/2)
    
    state_icon = patches.Rectangle((state_x, state_y), state_size, state_size, 
                                   linewidth=2, edgecolor='red', facecolor='lightcoral', alpha=0.7)
    ax.add_patch(state_icon)
    ax.text(state_x + state_size/2, state_y + state_size/2, 'State Icon', ha='center', va='center', fontsize=10)
    
    # Print position for reference (y=0 top)
    print(f"Main Icon Position (y=0 top): X={x:.1f}, Y={y:.1f}, Width={w:.1f}, Height={h:.1f}")
    if aspect_ratio > aspect_ratio_threshold:
        print(f"Note: Alignment swapped due to aspect_ratio > threshold.")
    
    plt.tight_layout()
    plt.show()
    

# Example usage and testing (flipped y-axis):
# plot_icon_positions('top', aspect_ratio=0.8, aspect_ratio_threshold=1.7, scale_factor=0.75)  # Tall icon, top state -> main bottom
