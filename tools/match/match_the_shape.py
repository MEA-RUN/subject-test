import js
from collections import defaultdict
import sys
import io
import random

WIDTH = 600 
HEIGHT = WIDTH
SIDE = (WIDTH // 6)

# Window dimensions
CANVAS_WIDTH = WIDTH
CANVAS_HEIGHT = HEIGHT
INTERPRETER_WIDTH = 400
WINDOW_WIDTH = CANVAS_WIDTH + INTERPRETER_WIDTH
WINDOW_HEIGHT = HEIGHT + 100

shape_entities = []

# Shape namespace class to hold shape constructors
class ShapeNamespace:
    """Namespace for shape constructors"""
    def __init__(self):
        self.Square = None
        self.Circle = None
        self.Triangle = None

# Create shape namespace instance
shape = ShapeNamespace()

# Persistent namespace for REPL execution
repl_namespace = {
    'shape': shape,
    'shape_entities': shape_entities,
    '__builtins__': __builtins__,
}

# Color conversion helper
def get_color_rgb(color_name):
    """Convert color name or hex to RGB tuple"""
    try:
        if color_name.startswith('#'):
            r = int(color_name[1:3], 16)
            g = int(color_name[3:5], 16)
            b = int(color_name[5:7], 16)
            return (r, g, b)
        else:
            # Map common color names to RGB
            color_map = {
                'red': (255, 0, 0),
                'green': (0, 255, 0),
                'blue': (0, 0, 255),
                'yellow': (255, 255, 0),
                'cyan': (0, 255, 255),
                'magenta': (255, 0, 255),
                'white': (255, 255, 255),
                'black': (0, 0, 0),
                'gray': (128, 128, 128),
                'grey': (128, 128, 128),
                'orange': (255, 165, 0),
                'purple': (128, 0, 128),
                'pink': (255, 192, 203),
                'brown': (165, 42, 42),
                'navy': (0, 0, 128),
                'darkblue': (0, 0, 139),
                'darkgreen': (0, 100, 0),
                'maroon': (128, 0, 0),
                'darkred': (139, 0, 0),
                'lightgray': (211, 211, 211),
            }
            return color_map.get(color_name.lower(), (0, 0, 0))
    except:
        return (0, 0, 0)  # Default to black

def get_arrow_color_rgb(base_color_name):
    """Get contrasting arrow color as RGB"""
    try:
        if base_color_name.startswith('#'):
            rgb_sum = sum(int(base_color_name[i:i+2], 16) for i in (1, 3, 5))
            return (255, 255, 255) if rgb_sum < 384 else (0, 0, 0)
        else:
            dark_colors = ['black', 'navy', 'darkblue', 'darkgreen', 'maroon', 'purple', 'darkred']
            return (255, 255, 255) if base_color_name.lower() in dark_colors else (0, 0, 0)
    except:
        return (0, 0, 0)

class CanvasInterface:
    """Abstract interface for canvas drawing operations"""
    def clear(self, canvas_id, r, g, b):
        """Clear the canvas with the given RGB color"""
        raise NotImplementedError
    
    def fill_rect(self, canvas_id, x, y, w, h, r, g, b, a=1.0):
        """Fill a rectangle with the given RGB color and alpha"""
        raise NotImplementedError
    
    def stroke_rect(self, canvas_id, x, y, w, h, r, g, b, width):
        """Stroke a rectangle with the given RGB color and line width"""
        raise NotImplementedError
    
    def fill_circle(self, canvas_id, x, y, radius, r, g, b, a=1.0):
        """Fill a circle with the given RGB color and alpha"""
        raise NotImplementedError
    
    def stroke_circle(self, canvas_id, x, y, radius, r, g, b, width):
        """Stroke a circle with the given RGB color and line width"""
        raise NotImplementedError
    
    def draw_line(self, canvas_id, x1, y1, x2, y2, r, g, b, width):
        """Draw a line with the given RGB color and line width"""
        raise NotImplementedError
    
    def fill_polygon(self, canvas_id, coords, r, g, b, a=1.0):
        """Fill a polygon with the given RGB color and alpha. coords is a list of [x1, y1, x2, y2, ...]"""
        raise NotImplementedError
    
    def stroke_polygon(self, canvas_id, coords, r, g, b, width):
        """Stroke a polygon with the given RGB color and line width. coords is a list of [x1, y1, x2, y2, ...]"""
        raise NotImplementedError
    
    def draw_text(self, canvas_id, text, x, y, fontSize, r, g, b):
        """Draw text with the given RGB color and font size"""
        raise NotImplementedError

class JSCanvasInterface(CanvasInterface):
    """Canvas interface implementation using js.canvas_* functions"""
    def clear(self, canvas_id, r, g, b):
        js.canvas_clear(canvas_id, r, g, b)
    
    def fill_rect(self, canvas_id, x, y, w, h, r, g, b, a=1.0):
        js.canvas_fill_rect(canvas_id, x, y, w, h, r, g, b, a)
    
    def stroke_rect(self, canvas_id, x, y, w, h, r, g, b, width):
        js.canvas_stroke_rect(canvas_id, x, y, w, h, r, g, b, width)
    
    def fill_circle(self, canvas_id, x, y, radius, r, g, b, a=1.0):
        js.canvas_fill_circle(canvas_id, x, y, radius, r, g, b, a)
    
    def stroke_circle(self, canvas_id, x, y, radius, r, g, b, width):
        js.canvas_stroke_circle(canvas_id, x, y, radius, r, g, b, width)
    
    def draw_line(self, canvas_id, x1, y1, x2, y2, r, g, b, width):
        js.canvas_draw_line(canvas_id, x1, y1, x2, y2, r, g, b, width)
    
    def fill_polygon(self, canvas_id, coords, r, g, b, a=1.0):
        js.canvas_fill_polygon(canvas_id, coords, r, g, b, a)
    
    def stroke_polygon(self, canvas_id, coords, r, g, b, width):
        js.canvas_stroke_polygon(canvas_id, coords, r, g, b, width)
    
    def draw_text(self, canvas_id, text, x, y, fontSize, r, g, b):
        js.canvas_draw_text(canvas_id, text, x, y, fontSize, r, g, b)

# Global canvas interface - will be initialized in main()
canvas_interface = None

class Shape:
    def __init__(self, color, direction):
        # Check for duplicate shapes (same color + same type)
        shape_type = type(self).__name__
        for existing_shape in shape_entities:
            if existing_shape.color == color and type(existing_shape).__name__ == shape_type:
                raise ValueError(f"A {shape_type} with color '{color}' already exists. Cannot create duplicate shapes.")
        
        # Hard limit of 4 shapes
        if len(shape_entities) >= 4:
            raise ValueError("Maximum of 4 shapes allowed")
        self.color = color
        self.x = -1
        self.y = -1
        # Destination cell (set when position is set)
        self.dest_x = -1
        self.dest_y = -1
        # Direction as a vector (dx, dy)
        # (1, 0) = right, (0, 1) = down, (-1, 0) = left, (0, -1) = up
        self.direction = direction
        # Animation state
        self.animating = False
        self.start_x = -1
        self.start_y = -1
        self.target_x = -1
        self.target_y = -1
        self.animation_progress = 0.0
        shape_entities.append(self)

    def set_position(self, x, y):
        self.x = x
        self.y = y
        # Calculate destination based on number of shapes
        self._calculate_destination()
        return self
    
    def _calculate_destination(self):
        """Calculate a random destination cell. The more shapes, the further the destination.
        Always generates a NEW destination different from the previous one to prevent cheating."""
        num_shapes = len(shape_entities)
        grid_width = WIDTH // SIDE
        grid_height = HEIGHT // SIDE
        
        # Get all cells currently occupied by shapes
        occupied_cells = set()
        for shape in shape_entities:
            if shape.x >= 0 and shape.y >= 0:
                occupied_cells.add((shape.x, shape.y))
        
        # Get all cells currently used as destinations by other shapes
        # (exclude this shape's own previous destination)
        destination_cells = set()
        for shape in shape_entities:
            if shape is not self and shape.dest_x >= 0 and shape.dest_y >= 0:
                destination_cells.add((shape.dest_x, shape.dest_y))
        
        # Store previous destination to ensure we get a different one
        previous_dest = (self.dest_x, self.dest_y) if self.dest_x >= 0 and self.dest_y >= 0 else None
        
        # Calculate distance constraints based on number of shapes
        # 1 shape: must be on same line/col as shape (based on direction), can be further apart
        # 2 shapes: max 2 cells apart (distance <= 2)
        # 3 or 4 shapes: at least 3 cells apart (distance >= 3)
        if num_shapes == 1:
            # Special case: destination must be on same line or column based on direction
            max_distance = None  # No maximum distance
            min_distance = 0
            # Get direction to determine line/column constraint
            dx, dy = self.direction
            same_line_col_required = True
        elif num_shapes == 2:
            max_distance = 2
            min_distance = 0
            same_line_col_required = False
        else:  # 3 or 4 shapes
            max_distance = None  # No maximum
            min_distance = 3
            same_line_col_required = False
        
        # Try to find a valid destination
        max_attempts = 500
        candidates = []
        
        for attempt in range(max_attempts):
            # For 1 shape with line/col constraint, generate appropriate candidates
            if num_shapes == 1 and same_line_col_required and self.x >= 0 and self.y >= 0:
                # Generate destination on same line (if facing left/right) or same column (if facing up/down)
                if dx != 0:  # Facing left or right - same row (same y)
                    dest_x = random.randint(0, grid_width - 1)
                    dest_y = self.y  # Same row
                elif dy != 0:  # Facing up or down - same column (same x)
                    dest_x = self.x  # Same column
                    dest_y = random.randint(0, grid_height - 1)
                else:
                    # Fallback: random cell
                    dest_x = random.randint(0, grid_width - 1)
                    dest_y = random.randint(0, grid_height - 1)
            else:
                # Random cell
                dest_x = random.randint(0, grid_width - 1)
                dest_y = random.randint(0, grid_height - 1)
            
            # Skip if destination is occupied by a shape
            if (dest_x, dest_y) in occupied_cells:
                continue
            
            # Skip if destination is already used by another shape
            if (dest_x, dest_y) in destination_cells:
                continue
            
            # Skip if it's the same as previous destination (prevent cheating)
            if previous_dest and (dest_x, dest_y) == previous_dest:
                continue
            
            # Skip if it's the same as current position
            if self.x >= 0 and self.y >= 0 and dest_x == self.x and dest_y == self.y:
                continue
            
            # Calculate distance from current position
            if self.x >= 0 and self.y >= 0:
                distance = abs(dest_x - self.x) + abs(dest_y - self.y)
                # Check if distance meets the constraints
                if distance >= min_distance and (max_distance is None or distance <= max_distance):
                    # For 1 shape, verify it's on the same line/col
                    if same_line_col_required:
                        dx, dy = self.direction
                        if dx != 0:  # Facing left/right - must be same row
                            if dest_y == self.y:
                                candidates.append((dest_x, dest_y, distance))
                        elif dy != 0:  # Facing up/down - must be same column
                            if dest_x == self.x:
                                candidates.append((dest_x, dest_y, distance))
                    else:
                        candidates.append((dest_x, dest_y, distance))
            else:
                # If no position set yet, accept any valid cell (but still different from previous)
                self.dest_x = dest_x
                self.dest_y = dest_y
                return
        
        # If we found candidates, pick one randomly (or furthest if 3-4 shapes)
        if candidates:
            if num_shapes >= 3:
                # For 3-4 shapes, prefer furthest distance
                candidates.sort(key=lambda x: x[2], reverse=True)
                self.dest_x, self.dest_y, _ = candidates[0]
            else:
                # For 1-2 shapes, pick randomly from valid candidates
                self.dest_x, self.dest_y, _ = random.choice(candidates)
            return
        
        # Fallback: if we couldn't find a valid cell, try with relaxed constraints
        # First, try with distance constraints but allow occupied cells (except current shape's position)
        if self.x >= 0 and self.y >= 0:
            available_cells = []
            for x in range(grid_width):
                for y in range(grid_height):
                    if (x, y) == previous_dest:
                        continue
                    if x == self.x and y == self.y:
                        continue
                    # Skip if already used as destination by another shape
                    if (x, y) in destination_cells:
                        continue
                    distance = abs(x - self.x) + abs(y - self.y)
                    if distance >= min_distance and (max_distance is None or distance <= max_distance):
                        # For 1 shape, verify it's on the same line/col
                        if same_line_col_required:
                            dx, dy = self.direction
                            if dx != 0:  # Facing left/right - must be same row
                                if y == self.y:
                                    available_cells.append((x, y))
                            elif dy != 0:  # Facing up/down - must be same column
                                if x == self.x:
                                    available_cells.append((x, y))
                        else:
                            available_cells.append((x, y))
            
            if available_cells:
                self.dest_x, self.dest_y = random.choice(available_cells)
                return
        
        # Last resort: use any cell except the previous one, occupied cells, and destination cells
        available_cells = [(x, y) for x in range(grid_width) for y in range(grid_height) 
                         if (x, y) not in occupied_cells 
                         and (x, y) not in destination_cells
                         and (x, y) != previous_dest]
        if available_cells:
            self.dest_x, self.dest_y = random.choice(available_cells)
        else:
            # Absolute fallback: any cell except previous destination and other destinations
            all_cells = [(x, y) for x in range(grid_width) for y in range(grid_height)
                        if (x, y) not in destination_cells]
            if previous_dest:
                all_cells = [cell for cell in all_cells if cell != previous_dest]
            if all_cells:
                self.dest_x, self.dest_y = random.choice(all_cells)
            else:
                # Absolute fallback (shouldn't happen)
                self.dest_x = 0
                self.dest_y = 0

    def get_position(self):
        return self.x, self.y

    def forward(self, steps=1):
        # Move along the direction vector with animation
        dx, dy = self.direction
        self.start_x = self.x
        self.start_y = self.y
        self.target_x = self.x + dx * steps
        self.target_y = self.y + dy * steps
        # Clamp to grid boundaries
        grid_width = WIDTH // SIDE
        grid_height = HEIGHT // SIDE
        self.target_x = max(0, min(self.target_x, grid_width - 1))
        self.target_y = max(0, min(self.target_y, grid_height - 1))
        # Update position immediately so __repr__ shows correct position
        self.x = self.target_x
        self.y = self.target_y
        self.animation_progress = 0.0
        self.animating = True
        return self

    def backward(self, steps=1):
        # Move opposite to the direction vector with animation
        dx, dy = self.direction
        self.start_x = self.x
        self.start_y = self.y
        self.target_x = self.x - dx * steps
        self.target_y = self.y - dy * steps
        # Clamp to grid boundaries
        grid_width = WIDTH // SIDE
        grid_height = HEIGHT // SIDE
        self.target_x = max(0, min(self.target_x, grid_width - 1))
        self.target_y = max(0, min(self.target_y, grid_height - 1))
        # Update position immediately so __repr__ shows correct position
        self.x = self.target_x
        self.y = self.target_y
        self.animation_progress = 0.0
        self.animating = True
        return self

    def left(self):
        # Rotate vector counterclockwise: (dx, dy) -> (dy, -dx)
        dx, dy = self.direction
        self.direction = (dy, -dx)
        return self

    def right(self):
        # Rotate vector clockwise: (dx, dy) -> (-dy, dx)
        dx, dy = self.direction
        self.direction = (-dy, dx)
        return self

    def _get_direction_name(self):
        """Get human-readable direction name"""
        direction_names = {
            (1, 0): "right",
            (0, 1): "down",
            (-1, 0): "left",
            (0, -1): "up"
        }
        return direction_names.get(self.direction, f"{self.direction[0]} {self.direction[1]}")

    def _draw_arrow(self, canvas_id, center_x, center_y, arrow_size):
        """Draw arrow indicating direction - shared by both Square and Circle"""
        # Get direction vector components
        dx, dy = self.direction
        
        # Calculate arrow tip position (scaled by arrow_size)
        tip_x = center_x + dx * arrow_size
        tip_y = center_y + dy * arrow_size
        
        # Calculate perpendicular vector for arrow base (rotate 90 degrees)
        perp_dx = -dy
        perp_dy = dx
        
        # Arrow base points (perpendicular to direction)
        base_width = arrow_size * 0.5
        base1_x = center_x + perp_dx * base_width
        base1_y = center_y + perp_dy * base_width
        base2_x = center_x - perp_dx * base_width
        base2_y = center_y - perp_dy * base_width
        
        # Middle point (slightly back from tip)
        mid_x = center_x + dx * arrow_size * 0.3
        mid_y = center_y + dy * arrow_size * 0.3
        
        # Create arrow polygon points
        arrow_points = [tip_x, tip_y, base1_x, base1_y, mid_x, mid_y, base2_x, base2_y]
        
        # Draw arrow in contrasting color
        arrow_color_rgb = get_arrow_color_rgb(self.color)
        canvas_interface.fill_polygon(canvas_id, arrow_points, arrow_color_rgb[0], arrow_color_rgb[1], arrow_color_rgb[2])
        canvas_interface.stroke_polygon(canvas_id, arrow_points, 0, 0, 0, 1)

    def _draw_destination(self, canvas_id):
        """Draw destination as an outline shape"""
        if self.dest_x < 0 or self.dest_y < 0:
            return
        
        if self.dest_x >= WIDTH // SIDE or self.dest_y >= HEIGHT // SIDE:
            return
        
        # Calculate base cell position
        base_x1 = self.dest_x * SIDE
        base_y1 = self.dest_y * SIDE
        
        # Shape size is 1/4 of the cell (half the side length)
        shape_size = SIDE / 2
        
        # Destination is always drawn centered (single shape position)
        center_x = base_x1 + SIDE / 2
        center_y = base_y1 + SIDE / 2
        
        # Draw as outline only (no fill)
        color_rgb = get_color_rgb(self.color)
        
        # This will be overridden by Square and Circle
        pass
    
    def __str__(self):
        """Human-readable representation"""
        return f"<{self.__repr__()}>"

class Square(Shape):
    def __init__(self, color, direction=(1, 0)):
        super().__init__(color, direction)
        self.side = SIDE

    def __repr__(self):
        """Unambiguous representation for debugging"""
        dir_name = self._get_direction_name()
        return f"{self.color} Square at {self.x}, {self.y} facing {dir_name}"

    def _draw(self, canvas_id, subcell_index=0, total_in_cell=1):
        # Use interpolated position during animation
        if self.animating:
            current_x = self.start_x + (self.target_x - self.start_x) * self.animation_progress
            current_y = self.start_y + (self.target_y - self.start_y) * self.animation_progress
        else:
            current_x = self.x
            current_y = self.y
        
        if current_x < 0 or current_x >= WIDTH // SIDE or current_y < 0 or current_y >= HEIGHT // SIDE:
            return
        
        # Calculate base cell position using interpolated coordinates
        base_x1 = current_x * self.side
        base_y1 = current_y * self.side
        
        # Destination size is 1/4 of the cell (half the side length)
        # Shape size is 85% of destination size (slightly smaller)
        dest_size = self.side / 2
        shape_size = dest_size * 0.85
        
        # Position the shape based on number of shapes in cell
        if total_in_cell == 1:
            # Single entity: centered
            x1 = base_x1 + self.side / 2 - shape_size / 2
            y1 = base_y1 + self.side / 2 - shape_size / 2
        elif total_in_cell == 2:
            # Two shapes: diagonal (top-left and bottom-right)
            if subcell_index == 0:
                # First entity: top-left
                x1 = base_x1 + (dest_size - shape_size) / 2
                y1 = base_y1 + (dest_size - shape_size) / 2
            else:  # subcell_index == 1
                # Second entity: bottom-right
                x1 = base_x1 + self.side - dest_size + (dest_size - shape_size) / 2
                y1 = base_y1 + self.side - dest_size + (dest_size - shape_size) / 2
        else:
            # 3 or 4 shapes: 2x2 grid (left to right, then top to bottom)
            # Positions: 0=top-left, 1=top-right, 2=bottom-left, 3=bottom-right
            grid_x = subcell_index % 2
            grid_y = subcell_index // 2
            # Calculate position with some padding to center shapes in their grid cells
            cell_padding = (self.side - dest_size * 2) / 3
            x1 = base_x1 + cell_padding + grid_x * (dest_size + cell_padding) + (dest_size - shape_size) / 2
            y1 = base_y1 + cell_padding + grid_y * (dest_size + cell_padding) + (dest_size - shape_size) / 2
        
        x2 = x1 + shape_size
        y2 = y1 + shape_size
        
        # Draw the square with 60% opacity (40% transparent)
        color_rgb = get_color_rgb(self.color)
        canvas_interface.fill_rect(canvas_id, x1, y1, x2 - x1, y2 - y1, color_rgb[0], color_rgb[1], color_rgb[2], 0.6)
        canvas_interface.stroke_rect(canvas_id, x1, y1, x2 - x1, y2 - y1, 0, 0, 0, 1)
        
        # Draw arrow indicating direction from vector
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        arrow_size = min(x2 - x1, y2 - y1) * 0.3
        self._draw_arrow(canvas_id, center_x, center_y, arrow_size)
    
    def _draw_destination(self, canvas_id):
        """Draw destination as an outline square"""
        if self.dest_x < 0 or self.dest_y < 0:
            return
        
        if self.dest_x >= WIDTH // SIDE or self.dest_y >= HEIGHT // SIDE:
            return
        
        # Calculate base cell position
        base_x1 = self.dest_x * self.side
        base_y1 = self.dest_y * self.side
        
        # Shape size is 1/4 of the cell (half the side length)
        shape_size = self.side / 2
        
        # Destination is always drawn centered (single shape position)
        x1 = base_x1 + self.side / 2 - shape_size / 2
        y1 = base_y1 + self.side / 2 - shape_size / 2
        x2 = x1 + shape_size
        y2 = y1 + shape_size
        
        # Draw as outline only (no fill)
        color_rgb = get_color_rgb(self.color)
        canvas_interface.stroke_rect(canvas_id, x1, y1, x2 - x1, y2 - y1, color_rgb[0], color_rgb[1], color_rgb[2], 2)

class Circle(Shape):
    def __init__(self, color, direction=(-1, 0)):
        super().__init__(color, direction)
        self.diameter = SIDE
        self.radius = SIDE / 2

    def __repr__(self):
        """Unambiguous representation for debugging"""
        dir_name = self._get_direction_name()
        return f"{self.color} Circle at {self.x}, {self.y} facing {dir_name}"

    def _draw(self, canvas_id, subcell_index=0, total_in_cell=1):
        # Use interpolated position during animation
        if self.animating:
            current_x = self.start_x + (self.target_x - self.start_x) * self.animation_progress
            current_y = self.start_y + (self.target_y - self.start_y) * self.animation_progress
        else:
            current_x = self.x
            current_y = self.y
        
        if current_x < 0 or current_x >= WIDTH // SIDE or current_y < 0 or current_y >= HEIGHT // SIDE:
            return
        
        # Calculate base cell position using interpolated coordinates
        base_x1 = current_x * SIDE
        base_y1 = current_y * SIDE
        
        # Destination size is 1/4 of the cell (half the side length)
        # Shape size is 85% of destination size (slightly smaller)
        dest_size = SIDE / 2
        shape_size = dest_size * 0.85
        radius = shape_size / 2
        dest_radius = dest_size / 2
        
        # Position the shape based on number of shapes in cell
        if total_in_cell == 1:
            # Single entity: centered
            center_x = base_x1 + SIDE / 2
            center_y = base_y1 + SIDE / 2
        elif total_in_cell == 2:
            # Two shapes: diagonal (top-left and bottom-right)
            if subcell_index == 0:
                # First entity: top-left
                center_x = base_x1 + dest_radius
                center_y = base_y1 + dest_radius
            else:  # subcell_index == 1
                # Second entity: bottom-right
                center_x = base_x1 + SIDE - dest_radius
                center_y = base_y1 + SIDE - dest_radius
        else:
            # 3 or 4 shapes: 2x2 grid (left to right, then top to bottom)
            # Positions: 0=top-left, 1=top-right, 2=bottom-left, 3=bottom-right
            grid_x = subcell_index % 2
            grid_y = subcell_index // 2
            # Calculate position with some padding to center shapes in their grid cells
            cell_padding = (SIDE - dest_size * 2) / 3
            center_x = base_x1 + cell_padding + grid_x * (dest_size + cell_padding) + dest_radius
            center_y = base_y1 + cell_padding + grid_y * (dest_size + cell_padding) + dest_radius
        
        # Draw the circle with 60% opacity (40% transparent)
        color_rgb = get_color_rgb(self.color)
        canvas_interface.fill_circle(canvas_id, center_x, center_y, radius, color_rgb[0], color_rgb[1], color_rgb[2], 0.6)
        canvas_interface.stroke_circle(canvas_id, center_x, center_y, radius, 0, 0, 0, 1)
        
        # Draw arrow indicating direction from vector
        arrow_size = radius * 0.6
        self._draw_arrow(canvas_id, center_x, center_y, arrow_size)
    
    def _draw_destination(self, canvas_id):
        """Draw destination as an outline circle"""
        if self.dest_x < 0 or self.dest_y < 0:
            return
        
        if self.dest_x >= WIDTH // SIDE or self.dest_y >= HEIGHT // SIDE:
            return
        
        # Calculate base cell position
        base_x1 = self.dest_x * SIDE
        base_y1 = self.dest_y * SIDE
        
        # Shape size is 1/4 of the cell (half the side length)
        # Radius is half of that
        shape_size = SIDE / 2
        radius = shape_size / 2
        
        # Destination is always drawn centered (single shape position)
        center_x = base_x1 + SIDE / 2
        center_y = base_y1 + SIDE / 2
        
        # Draw as outline only (no fill)
        color_rgb = get_color_rgb(self.color)
        canvas_interface.stroke_circle(canvas_id, center_x, center_y, radius, color_rgb[0], color_rgb[1], color_rgb[2], 2)

class Triangle(Shape):
    def __init__(self, color, direction=(0, -1)):
        super().__init__(color, direction)
        self.side = SIDE

    def __repr__(self):
        """Unambiguous representation for debugging"""
        dir_name = self._get_direction_name()
        return f"{self.color} Triangle at {self.x}, {self.y} facing {dir_name}"

    def _draw(self, canvas_id, subcell_index=0, total_in_cell=1):
        # Use interpolated position during animation
        if self.animating:
            current_x = self.start_x + (self.target_x - self.start_x) * self.animation_progress
            current_y = self.start_y + (self.target_y - self.start_y) * self.animation_progress
        else:
            current_x = self.x
            current_y = self.y
        
        if current_x < 0 or current_x >= WIDTH // SIDE or current_y < 0 or current_y >= HEIGHT // SIDE:
            return
        
        # Calculate base cell position using interpolated coordinates
        base_x1 = current_x * self.side
        base_y1 = current_y * self.side
        
        # Destination size is 1/4 of the cell (half the side length)
        # Shape size is 85% of destination size (slightly smaller)
        dest_size = self.side / 2
        shape_size = dest_size * 0.85
        
        # Position the shape based on number of shapes in cell
        if total_in_cell == 1:
            # Single entity: centered
            center_x = base_x1 + self.side / 2
            center_y = base_y1 + self.side / 2
        elif total_in_cell == 2:
            # Two shapes: diagonal (top-left and bottom-right)
            if subcell_index == 0:
                # First entity: top-left
                center_x = base_x1 + dest_size / 2
                center_y = base_y1 + dest_size / 2
            else:  # subcell_index == 1
                # Second entity: bottom-right
                center_x = base_x1 + self.side - dest_size / 2
                center_y = base_y1 + self.side - dest_size / 2
        else:
            # 3 or 4 shapes: 2x2 grid (left to right, then top to bottom)
            # Positions: 0=top-left, 1=top-right, 2=bottom-left, 3=bottom-right
            grid_x = subcell_index % 2
            grid_y = subcell_index // 2
            # Calculate position with some padding to center shapes in their grid cells
            cell_padding = (self.side - dest_size * 2) / 3
            center_x = base_x1 + cell_padding + grid_x * (dest_size + cell_padding) + dest_size / 2
            center_y = base_y1 + cell_padding + grid_y * (dest_size + cell_padding) + dest_size / 2
        
        # Calculate triangle vertices (equilateral triangle pointing in the direction)
        # Base size is shape_size
        height = shape_size * 0.866  # sqrt(3)/2 for equilateral triangle
        
        # Get direction vector to determine triangle orientation
        dx, dy = self.direction
        
        # Calculate triangle points based on direction
        # Default: pointing up (0, -1)
        if dx == 0 and dy == -1:  # Up
            p1_x, p1_y = center_x, center_y - height * 2/3  # Top vertex
            p2_x, p2_y = center_x - shape_size / 2, center_y + height / 3  # Bottom left
            p3_x, p3_y = center_x + shape_size / 2, center_y + height / 3  # Bottom right
        elif dx == 0 and dy == 1:  # Down
            p1_x, p1_y = center_x, center_y + height * 2/3  # Bottom vertex
            p2_x, p2_y = center_x + shape_size / 2, center_y - height / 3  # Top right
            p3_x, p3_y = center_x - shape_size / 2, center_y - height / 3  # Top left
        elif dx == 1 and dy == 0:  # Right
            p1_x, p1_y = center_x + height * 2/3, center_y  # Right vertex
            p2_x, p2_y = center_x - height / 3, center_y - shape_size / 2  # Top left
            p3_x, p3_y = center_x - height / 3, center_y + shape_size / 2  # Bottom left
        elif dx == -1 and dy == 0:  # Left
            p1_x, p1_y = center_x - height * 2/3, center_y  # Left vertex
            p2_x, p2_y = center_x + height / 3, center_y + shape_size / 2  # Bottom right
            p3_x, p3_y = center_x + height / 3, center_y - shape_size / 2  # Top right
        else:
            # Default to up
            p1_x, p1_y = center_x, center_y - height * 2/3
            p2_x, p2_y = center_x - shape_size / 2, center_y + height / 3
            p3_x, p3_y = center_x + shape_size / 2, center_y + height / 3
        
        # Draw the triangle with 60% opacity (40% transparent)
        color_rgb = get_color_rgb(self.color)
        triangle_points = [p1_x, p1_y, p2_x, p2_y, p3_x, p3_y]
        canvas_interface.fill_polygon(canvas_id, triangle_points, color_rgb[0], color_rgb[1], color_rgb[2], 0.6)
        canvas_interface.stroke_polygon(canvas_id, triangle_points, 0, 0, 0, 1)
        
        # Draw arrow indicating direction from vector
        arrow_size = shape_size * 0.3
        self._draw_arrow(canvas_id, center_x, center_y, arrow_size)
    
    def _draw_destination(self, canvas_id):
        """Draw destination as an outline triangle"""
        if self.dest_x < 0 or self.dest_y < 0:
            return
        
        if self.dest_x >= WIDTH // SIDE or self.dest_y >= HEIGHT // SIDE:
            return
        
        # Calculate base cell position
        base_x1 = self.dest_x * self.side
        base_y1 = self.dest_y * self.side
        
        # Shape size is 1/4 of the cell (half the side length)
        shape_size = self.side / 2
        
        # Destination is always drawn centered (single shape position)
        center_x = base_x1 + self.side / 2
        center_y = base_y1 + self.side / 2
        
        # Calculate triangle vertices (equilateral triangle pointing in the direction)
        height = shape_size * 0.866  # sqrt(3)/2 for equilateral triangle
        
        # Get direction vector to determine triangle orientation
        dx, dy = self.direction
        
        # Calculate triangle points based on direction
        if dx == 0 and dy == -1:  # Up
            p1_x, p1_y = center_x, center_y - height * 2/3
            p2_x, p2_y = center_x - shape_size / 2, center_y + height / 3
            p3_x, p3_y = center_x + shape_size / 2, center_y + height / 3
        elif dx == 0 and dy == 1:  # Down
            p1_x, p1_y = center_x, center_y + height * 2/3
            p2_x, p2_y = center_x + shape_size / 2, center_y - height / 3
            p3_x, p3_y = center_x - shape_size / 2, center_y - height / 3
        elif dx == 1 and dy == 0:  # Right
            p1_x, p1_y = center_x + height * 2/3, center_y
            p2_x, p2_y = center_x - height / 3, center_y - shape_size / 2
            p3_x, p3_y = center_x - height / 3, center_y + shape_size / 2
        elif dx == -1 and dy == 0:  # Left
            p1_x, p1_y = center_x - height * 2/3, center_y
            p2_x, p2_y = center_x + height / 3, center_y + shape_size / 2
            p3_x, p3_y = center_x + height / 3, center_y - shape_size / 2
        else:
            # Default to up
            p1_x, p1_y = center_x, center_y - height * 2/3
            p2_x, p2_y = center_x - shape_size / 2, center_y + height / 3
            p3_x, p3_y = center_x + shape_size / 2, center_y + height / 3
        
        # Draw as outline only (no fill)
        color_rgb = get_color_rgb(self.color)
        triangle_points = [p1_x, p1_y, p2_x, p2_y, p3_x, p3_y]
        canvas_interface.stroke_polygon(canvas_id, triangle_points, color_rgb[0], color_rgb[1], color_rgb[2], 2)

def draw_grid(canvas_id):
    for x in range(0, WIDTH, SIDE):
        canvas_interface.draw_line(canvas_id, x, 0, x, HEIGHT, 0, 0, 0, 1)
    for y in range(0, HEIGHT, SIDE):
        canvas_interface.draw_line(canvas_id, 0, y, WIDTH, y, 0, 0, 0, 1)

def update_animations():
    """Update animation progress for all shapes"""
    animation_speed = 0.03  # How fast animation progresses per frame (slower movement)
    any_animating = False
    
    for entity in shape_entities:
        if entity.animating:
            any_animating = True
            entity.animation_progress += animation_speed
            if entity.animation_progress >= 1.0:
                # Animation complete
                entity.animation_progress = 1.0
                entity.x = entity.target_x
                entity.y = entity.target_y
                entity.animating = False
    
    return any_animating

class StreamingStdout:
    """Custom stdout that streams to JavaScript in real-time while also capturing"""
    def __init__(self, original_stdout, capture_buffer):
        self.original_stdout = original_stdout
        self.capture_buffer = capture_buffer
        try:
            import repl_output
            self.repl_output = repl_output
        except ImportError:
            self.repl_output = None
    
    def write(self, text):
        # Write to capture buffer
        self.capture_buffer.write(text)
        # Stream to JavaScript in real-time
        if self.repl_output:
            try:
                self.repl_output.write(text)
            except:
                pass
    
    def flush(self):
        self.capture_buffer.flush()
        if self.repl_output:
            try:
                self.repl_output.flush()
            except:
                pass

def execute_code(code, repl_namespace):
    """Execute Python code in a persistent namespace"""
    # Update the shape namespace with current shape classes
    repl_namespace['shape'].Square = Square
    repl_namespace['shape'].Circle = Circle
    repl_namespace['shape'].Triangle = Triangle
    repl_namespace['shape_entities'] = shape_entities
    
    # Capture stdout with streaming
    old_stdout = sys.stdout
    sys.stderr = old_stderr = sys.stderr  # Keep stderr as is for now
    captured_output = io.StringIO()
    sys.stdout = StreamingStdout(old_stdout, captured_output)
    
    result = None
    output = ""
    error = None
    
    try:
        # Try to compile as an expression first (like a real REPL)
        try:
            # Check if it's a simple expression
            compiled = compile(code, '<string>', 'eval')
            # It's an expression, evaluate it and show the result
            result = eval(code, repl_namespace)
            output = captured_output.getvalue()
        except SyntaxError:
            # Not an expression, execute as a statement
            exec(code, repl_namespace)
            output = captured_output.getvalue()
    except Exception as e:
        error = str(e)
        # Also capture any output before the error
        output = captured_output.getvalue()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
    
    # Ensure output is a string
    if output is None:
        output = ""
    
    return result, output, error

# Global variables
canvas_surface_id = 'canvas'

def main():
    # Initialize canvas interface
    global canvas_interface
    canvas_interface = JSCanvasInterface()
    
    # Initialize canvas
    canvas_interface.clear(canvas_surface_id, 255, 255, 255)
    
    # Start the render loop (will be called from JavaScript)
    render_frame()

def check_win_condition():
    """Check if all 4 shapes are on their destination cells"""
    if len(shape_entities) != 4:
        return False
    
    # Check if all shapes are on their destinations (and not animating)
    for entity in shape_entities:
        if entity.animating:
            return False
        if entity.x < 0 or entity.y < 0:
            return False
        if entity.dest_x < 0 or entity.dest_y < 0:
            return False
        if entity.x != entity.dest_x or entity.y != entity.dest_y:
            return False
    
    return True

def draw_win_message(canvas_id):
    """Draw the victory message in big colored letters"""
    message = "Congratulation !!!"
    font_size = 48
    
    # Calculate text position (centered)
    # Approximate text width - using a more accurate estimate
    char_width = font_size * 0.55
    total_width = len(message) * char_width
    start_x = (WIDTH - total_width) / 2
    text_y = HEIGHT / 2 + font_size / 3  # Center vertically (accounting for baseline)
    
    # Draw text with rainbow colors (cycling through colors for each letter)
    colors = [
        (255, 0, 0),      # Red
        (255, 127, 0),    # Orange
        (255, 255, 0),    # Yellow
        (0, 255, 0),      # Green
        (0, 0, 255),      # Blue
        (75, 0, 130),     # Indigo
        (148, 0, 211),    # Violet
    ]
    
    text_x = start_x
    for i, char in enumerate(message):
        if char == ' ':
            text_x += char_width
            continue
        color_index = i % len(colors)
        r, g, b = colors[color_index]
        # Draw shadow/outline for better visibility (black outline)
        for offset_x in [-2, -1, 1, 2]:
            for offset_y in [-2, -1, 1, 2]:
                canvas_interface.draw_text(canvas_id, char, text_x + offset_x, text_y + offset_y, font_size, 0, 0, 0)
        # Draw the colored text on top
        canvas_interface.draw_text(canvas_id, char, text_x, text_y, font_size, r, g, b)
        text_x += char_width

def render_frame():
    """Render a single frame - called from JavaScript animation loop"""
    # Update animations
    update_animations()
    
    # Clear and draw canvas
    canvas_interface.clear(canvas_surface_id, 255, 255, 255)
    draw_grid(canvas_surface_id)
    
    # Draw destinations first (so they appear behind shapes)
    for entity in shape_entities:
        if not entity.animating:  # Only draw destination for non-animating shapes
            entity._draw_destination(canvas_surface_id)
    
    # Group entities by cell position
    entities_by_cell = defaultdict(list)
    animating_entities = []
    
    for entity in shape_entities:
        if entity.animating:
            animating_entities.append(entity)
        else:
            if entity.x >= 0 and entity.x < WIDTH // SIDE and entity.y >= 0 and entity.y < HEIGHT // SIDE:
                cell_key = (entity.x, entity.y)
                entities_by_cell[cell_key].append(entity)
    
    # Draw non-animating entities
    for cell_key, cell_entities in entities_by_cell.items():
        total_in_cell = len(cell_entities)
        if total_in_cell > 4:
            total_in_cell = 4
        
        for i, entity in enumerate(cell_entities[:4]):
            entity._draw(canvas_surface_id, subcell_index=i, total_in_cell=total_in_cell)
    
    # Draw animating entities
    for entity in animating_entities:
        entity._draw(canvas_surface_id, subcell_index=0, total_in_cell=1)
    
    # Check win condition and display message
    if check_win_condition():
        draw_win_message(canvas_surface_id)

def execute_python_code(code):
    """Execute Python code and return result - called from JavaScript"""
    return execute_code(code, repl_namespace)

# Note: main() will be called from JavaScript after setup
