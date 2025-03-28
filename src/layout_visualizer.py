import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Dict, List, Tuple
import numpy as np
import os

class LayoutVisualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.colors = {
            'walls': '#333333',
            'bathroom': '#87CEEB',
            'living': '#98FB98',
            'furniture': '#8B4513',
            'door': '#A0522D',
            'text': '#000000'
        }
    
    def draw_room(self, x: float, y: float, width: float, height: float, 
                  label: str = '', color: str = '#FFFFFF') -> None:
        """Draw a room rectangle."""
        room = patches.Rectangle((x, y), width, height, 
                               facecolor=color, edgecolor='black', 
                               linewidth=1)
        self.ax.add_patch(room)
        if label:
            self.ax.text(x + width/2, y + height/2, label,
                        horizontalalignment='center',
                        verticalalignment='center',
                        fontsize=8)

    def draw_door(self, x: float, y: float, width: float = 0.8, 
                 height: float = 0.1, rotation: float = 0) -> None:
        """Draw a door symbol."""
        door = patches.Rectangle((x, y), width, height,
                               facecolor=self.colors['door'],
                               angle=rotation)
        self.ax.add_patch(door)

    def draw_window(self, x: float, y: float, width: float = 1.2, 
                   height: float = 0.1, rotation: float = 0) -> None:
        """Draw a window symbol."""
        window = patches.Rectangle((x, y), width, height,
                                 facecolor=self.colors['window'],
                                 angle=rotation)
        self.ax.add_patch(window)

    def draw_furniture(self, x: float, y: float, width: float, height: float,
                      furniture_type: str = 'table') -> None:
        """Draw furniture symbols."""
        if furniture_type == 'bed':
            furniture = patches.Rectangle((x, y), width, height,
                                       facecolor=self.colors['furniture'],
                                       edgecolor='black', linewidth=0.5)
            self.ax.add_patch(furniture)
        elif furniture_type == 'table':
            furniture = patches.Rectangle((x, y), width, height,
                                       facecolor=self.colors['furniture'],
                                       edgecolor='black', linewidth=0.5)
            self.ax.add_patch(furniture)
        elif furniture_type == 'sofa':
            furniture = patches.Rectangle((x, y), width, height,
                                       facecolor=self.colors['furniture'],
                                       edgecolor='black', linewidth=0.5)
            self.ax.add_patch(furniture)
        elif furniture_type == 'circle_table':
            circle = plt.Circle((x + width/2, y + height/2), min(width, height)/2,
                              facecolor=self.colors['furniture'],
                              edgecolor='black', linewidth=0.5)
            self.ax.add_patch(circle)

    def draw_modular_house(self) -> None:
        """Draw the complete modular house layout."""
        # Convert dimensions from mm to meters
        width = 14.7  # 14700mm
        height = 15.9  # 15900mm
        
        # Set the plot limits
        self.ax.set_xlim(-1, width + 1)
        self.ax.set_ylim(-1, height + 1)
        
        # Draw outer walls
        self.draw_room(0, 0, width, height, color=self.colors['walls'])
        
        # Draw sections based on the grid (A-F, 1-4)
        section_width = 3.15  # 3150mm
        core_width = 2.1  # 2100mm
        section_height = 6.0  # 6000mm
        
        # Draw left side rooms (A-B-C sections)
        for i in range(2):
            # Upper rooms
            self.draw_room(i * section_width, height - section_height, 
                         section_width, section_height)
            # Lower rooms
            self.draw_room(i * section_width, 0, 
                         section_width, section_height)
            
        # Draw right side rooms (D-E-F sections)
        for i in range(2):
            x_pos = core_width + (2 * section_width) + (i * section_width)
            # Upper rooms
            self.draw_room(x_pos, height - section_height, 
                         section_width, section_height)
            # Lower rooms
            self.draw_room(x_pos, 0, 
                         section_width, section_height)

        # Draw central core with bathrooms
        core_x = 2 * section_width
        core_y = (height - 3.9) / 2  # Centered vertically
        self.draw_room(core_x, core_y, core_width, 3.9, 'Core', self.colors['walls'])
        
        # Draw bathrooms
        bath_width = core_width / 2
        for i in range(4):
            y_offset = core_y + (i * (3.9/4))
            self.draw_room(core_x, y_offset, bath_width, 3.9/4, 'Bath', self.colors['bathroom'])
            self.draw_room(core_x + bath_width, y_offset, bath_width, 3.9/4, 'Bath', self.colors['bathroom'])

        # Add furniture
        # Beds
        bed_positions = [
            (0.3, 0.3), (0.3, height-section_height+0.3),  # Left side
            (3.45, 0.3), (3.45, height-section_height+0.3),  # Middle left
            (8.35, 0.3), (8.35, height-section_height+0.3),  # Middle right
            (11.5, 0.3), (11.5, height-section_height+0.3)   # Right side
        ]
        for x, y in bed_positions:
            self.draw_furniture(x, y, 2.5, 1.8, 'bed')

        # Living area furniture
        living_positions = [
            (0.5, 2.5), (3.65, 2.5), (8.55, 2.5), (11.7, 2.5),  # Lower sofas
            (0.5, height-3.5), (3.65, height-3.5), (8.55, height-3.5), (11.7, height-3.5)  # Upper sofas
        ]
        for x, y in living_positions:
            self.draw_furniture(x, y, 2.0, 0.8, 'sofa')

        # Circle tables
        table_positions = [
            (1.0, 3.5), (4.15, 3.5), (9.05, 3.5), (12.2, 3.5),  # Lower tables
            (1.0, height-2.5), (4.15, height-2.5), (9.05, height-2.5), (12.2, height-2.5)  # Upper tables
        ]
        for x, y in table_positions:
            self.draw_furniture(x, y, 1.0, 1.0, 'circle_table')

        # Add doors
        door_width = 0.8
        door_positions = [
            # Bathroom doors
            (core_x - door_width/2, core_y + 0.9),
            (core_x - door_width/2, core_y + 1.9),
            (core_x - door_width/2, core_y + 2.9),
            (core_x + core_width - door_width/2, core_y + 0.9),
            (core_x + core_width - door_width/2, core_y + 1.9),
            (core_x + core_width - door_width/2, core_y + 2.9),
            # Room doors
            (0.1, section_height/2), (3.25, section_height/2),
            (8.3, section_height/2), (11.45, section_height/2),
            (0.1, height-section_height/2), (3.25, height-section_height/2),
            (8.3, height-section_height/2), (11.45, height-section_height/2)
        ]
        for x, y in door_positions:
            self.draw_door(x, y)

        # Add grid labels
        for i, label in enumerate(['A', 'B', 'C', 'D', 'E', 'F']):
            x_pos = i * section_width if i < 3 else (i-3) * section_width + core_width + (2 * section_width)
            self.ax.text(x_pos + section_width/2, height + 0.3, label,
                        horizontalalignment='center')
        
        for i, label in enumerate(['1', '2', '3', '4']):
            y_pos = height - (i * (height/4))
            self.ax.text(-0.3, y_pos, label,
                        verticalalignment='center')

        # Add dimensions
        self.ax.text(width/2, -0.5, f'{width*1000:.0f}mm', horizontalalignment='center')
        self.ax.text(-0.5, height/2, f'{height*1000:.0f}mm', verticalalignment='center', rotation=90)
        
        # Add legend
        legend_elements = [
            patches.Patch(facecolor=self.colors['walls'], label='Walls'),
            patches.Patch(facecolor=self.colors['bathroom'], label='Bathroom'),
            patches.Patch(facecolor=self.colors['living'], label='Living Space'),
            patches.Patch(facecolor=self.colors['furniture'], label='Furniture')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right')
        
        # Add grid
        self.ax.grid(True, linestyle='--', alpha=0.3)
        self.ax.set_title('Modular House Floor Layout\nCore+ Solution', pad=20)
        self.ax.set_xlabel('Width (mm)')
        self.ax.set_ylabel('Length (mm)')
        
        plt.tight_layout()
    
    def save(self, filepath: str) -> None:
        """Save the layout visualization."""
        # Ensure the reports directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()

    def draw_single_module(self):
        # Clear any existing plots
        self.ax.clear()
        
        # Set the dimensions (in meters)
        width = 3.15
        length = 6.0
        bathroom_width = 1.5
        bathroom_length = 2.0
        
        # Draw main unit outline
        self.ax.add_patch(plt.Rectangle((0, 0), width, length, fill=False, color=self.colors['walls'], linewidth=2))
        
        # Draw bathroom
        self.ax.add_patch(plt.Rectangle((0, 0), bathroom_width, bathroom_length, 
                                      color=self.colors['bathroom'], alpha=0.3))
        
        # Draw living area
        self.ax.add_patch(plt.Rectangle((0, bathroom_length), width, length-bathroom_length, 
                                      color=self.colors['living'], alpha=0.3))
        
        # Draw bathroom door
        door_width = 0.8
        self.ax.add_patch(plt.Rectangle((bathroom_width-0.1, bathroom_length-0.1), 
                                      0.1, door_width, color=self.colors['door']))
        
        # Draw furniture
        # Bed (2m x 1m)
        self.ax.add_patch(plt.Rectangle((0.3, length-2.2), 2.0, 1.0, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Table (0.8m x 0.8m)
        self.ax.add_patch(plt.Rectangle((0.3, 2.5), 0.8, 0.8, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Sofa (1.8m x 0.8m)
        self.ax.add_patch(plt.Rectangle((1.2, 2.5), 1.8, 0.8, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Storage (0.6m x 0.4m)
        self.ax.add_patch(plt.Rectangle((2.55, 2.5), 0.4, 0.6, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Add labels and dimensions
        self.ax.text(width/2, -0.3, f'{width*1000:.0f}mm', ha='center', color=self.colors['text'])
        self.ax.text(-0.3, length/2, f'{length*1000:.0f}mm', va='center', rotation=90, color=self.colors['text'])
        
        # Add room labels
        self.ax.text(bathroom_width/2, bathroom_length/2, 'Bathroom', ha='center', va='center', color=self.colors['text'])
        self.ax.text(width/2, (length+bathroom_length)/2, 'Living Space', ha='center', va='center', color=self.colors['text'])
        
        # Add furniture labels
        self.ax.text(1.3, length-1.7, 'Bed', ha='center', va='center', color=self.colors['text'])
        self.ax.text(0.7, 2.9, 'Table', ha='center', va='center', color=self.colors['text'])
        self.ax.text(2.1, 2.9, 'Sofa', ha='center', va='center', color=self.colors['text'])
        self.ax.text(2.75, 2.8, 'Storage', ha='center', va='center', color=self.colors['text'])
        
        # Set equal aspect ratio and limits
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-0.5, width + 0.5)
        self.ax.set_ylim(-0.5, length + 0.5)
        
        # Add title
        self.ax.set_title('Single Module Layout (3150mm x 6000mm)', color=self.colors['text'])
        
        # Add grid
        self.ax.grid(True, linestyle='--', alpha=0.3)
        
        # Remove axis
        self.ax.set_xticks([])
        self.ax.set_yticks([])
    
    def save(self, filename):
        # Ensure the reports directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        self.fig.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

    def draw_optimal_module(self, dimensions):
        # Clear any existing plots
        self.ax.clear()
        
        # Get dimensions
        width = dimensions['width']
        length = dimensions['length']
        transport_width = dimensions['transport_width']
        
        # Draw transport configuration (dashed lines)
        self.ax.add_patch(plt.Rectangle((0, 0), transport_width, length, 
                                      fill=False, color=self.colors['walls'], 
                                      linestyle='--', linewidth=1))
        
        # Draw expanded configuration (solid lines)
        self.ax.add_patch(plt.Rectangle((0, 0), width, length, 
                                      fill=False, color=self.colors['walls'], 
                                      linewidth=2))
        
        # Draw expansion mechanism indicators
        expansion_width = width - transport_width
        # Slide-out tracks (top and bottom)
        self.ax.add_patch(plt.Rectangle((transport_width-0.1, 0), 0.1, 0.3, 
                                      color='#696969', alpha=0.8))
        self.ax.add_patch(plt.Rectangle((transport_width-0.1, length-0.3), 0.1, 0.3, 
                                      color='#696969', alpha=0.8))
        
        # Expansion direction arrows
        arrow_props = dict(arrowstyle='->', color='#FF4500', linewidth=2)
        self.ax.annotate('', xy=(width, length/2), xytext=(transport_width, length/2),
                        arrowprops=arrow_props)
        
        # Add expansion note
        self.ax.text(transport_width + expansion_width/2, length + 0.3, 
                    'Slide-out expansion\n(0.91m)', ha='center', color='#FF4500')
        
        # Draw bathroom (2.4m x 2.2m) - fixed part
        bathroom_width = 2.4
        bathroom_length = 2.2
        self.ax.add_patch(plt.Rectangle((0.2, 0.2), bathroom_width, bathroom_length, 
                                      color=self.colors['bathroom'], alpha=0.3))
        
        # Draw kitchen area (2.4m x 3m) - fixed part
        kitchen_width = 2.4
        kitchen_length = 3.0
        kitchen_start = bathroom_length + 0.8  # Gap for corridor
        self.ax.add_patch(plt.Rectangle((0.2, kitchen_start), kitchen_width, kitchen_length, 
                                      color='#FFE4B5', alpha=0.3))
        
        # Draw living area - split between fixed and expandable
        living_start = kitchen_start + kitchen_length + 0.8
        # Fixed part
        self.ax.add_patch(plt.Rectangle((0.2, living_start), transport_width-0.4, length-living_start-0.2, 
                                      color=self.colors['living'], alpha=0.3))
        # Expandable part
        self.ax.add_patch(plt.Rectangle((transport_width, living_start), expansion_width, length-living_start-0.2, 
                                      color=self.colors['living'], alpha=0.5,
                                      hatch='//'))
        
        # Draw doors
        door_width = 0.9
        # Entrance door
        self.ax.add_patch(plt.Rectangle((width-0.1, 1.0), 0.1, door_width, 
                                      color=self.colors['door']))
        # Bathroom door
        self.ax.add_patch(plt.Rectangle((bathroom_width+0.2, 0.8), 0.1, door_width, 
                                      color=self.colors['door']))
        
        # Draw windows (1.2m wide)
        window_width = 1.2
        window_height = 0.1
        # Bathroom window
        self.ax.add_patch(plt.Rectangle((0.8, 0), window_width, window_height, 
                                      color='#ADD8E6'))
        # Kitchen windows
        self.ax.add_patch(plt.Rectangle((0.8, kitchen_start + 1.0), window_width, window_height, 
                                      color='#ADD8E6'))
        # Living area windows
        self.ax.add_patch(plt.Rectangle((0.8, living_start + 1.0), window_width, window_height, 
                                      color='#ADD8E6'))
        self.ax.add_patch(plt.Rectangle((width-2.0, living_start + 1.0), window_width, window_height, 
                                      color='#ADD8E6'))
        
        # Draw furniture - showing which pieces are in fixed vs expandable sections
        # Bed (2m x 1.6m) - in expandable section
        self.ax.add_patch(plt.Rectangle((width-2.2, length-2.0), 2.0, 1.6, 
                                      color=self.colors['furniture'], alpha=0.5))
        self.ax.text(width-1.2, length-1.2, 'Bed\n(expands)', ha='center', color=self.colors['text'])
        
        # Sofa (2.2m x 0.9m) - in fixed section
        self.ax.add_patch(plt.Rectangle((0.3, living_start + 0.3), 2.2, 0.9, 
                                      color=self.colors['furniture'], alpha=0.5))
        self.ax.text(1.4, living_start + 0.75, 'Sofa\n(fixed)', ha='center', color=self.colors['text'])
        
        # Dining table (1.6m x 0.9m) - in fixed section
        self.ax.add_patch(plt.Rectangle((0.4, kitchen_start + 0.5), 1.6, 0.9, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Add room labels
        self.ax.text(bathroom_width/2, bathroom_length/2, 'Bathroom\n2.4m × 2.2m\n(fixed)', 
                    ha='center', va='center', color=self.colors['text'])
        self.ax.text(kitchen_width/2, kitchen_start + kitchen_length/2, 'Kitchen\n2.4m × 3.0m\n(fixed)', 
                    ha='center', va='center', color=self.colors['text'])
        self.ax.text(width/2, living_start + (length-living_start)/2, 
                    'Living/Sleeping Area\n(partially expandable)', 
                    ha='center', va='center', color=self.colors['text'])
        
        # Add dimensions
        self.ax.text(width/2, -0.3, f'Width: {width*1000:.0f}mm (Transport: {transport_width*1000:.0f}mm)', 
                    ha='center', color=self.colors['text'])
        self.ax.text(-0.3, length/2, f'Length: {length*1000:.0f}mm', 
                    va='center', rotation=90, color=self.colors['text'])
        
        # Set equal aspect ratio and limits
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-0.5, width + 0.5)
        self.ax.set_ylim(-0.5, length + 0.5)
        
        # Add title and legend
        self.ax.set_title('Optimal Module Layout\nWith Slide-Out Expansion System', 
                         color=self.colors['text'])
        
        # Add legend
        legend_elements = [
            patches.Patch(facecolor=self.colors['living'], alpha=0.3, label='Fixed Section'),
            patches.Patch(facecolor=self.colors['living'], alpha=0.5, hatch='//', label='Expandable Section'),
            patches.Patch(facecolor='#696969', alpha=0.8, label='Slide Mechanism'),
            patches.Patch(facecolor='none', edgecolor=self.colors['walls'], 
                        linestyle='--', label='Transport Width')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right')
        
        # Add grid
        self.ax.grid(True, linestyle='--', alpha=0.3)
        
        # Remove axis
        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def draw_max_size_module(self, dimensions):
        # Clear any existing plots
        self.ax.clear()
        
        # Get dimensions
        width = dimensions['width']
        length = dimensions['length']
        
        # Draw main unit outline
        self.ax.add_patch(plt.Rectangle((0, 0), width, length, 
                                      fill=False, color=self.colors['walls'], 
                                      linewidth=2))
        
        # Draw bathroom (2.4m x 2.2m)
        bathroom_width = 2.4
        bathroom_length = 2.2
        self.ax.add_patch(plt.Rectangle((0.1, 0.1), bathroom_width, bathroom_length, 
                                      color=self.colors['bathroom'], alpha=0.3))
        
        # Draw kitchen area (2.4m x 3m)
        kitchen_width = 2.4
        kitchen_length = 3.0
        kitchen_start = bathroom_length + 0.8  # Gap for corridor
        self.ax.add_patch(plt.Rectangle((0.1, kitchen_start), kitchen_width, kitchen_length, 
                                      color='#FFE4B5', alpha=0.3))
        
        # Draw living area
        living_start = kitchen_start + kitchen_length + 0.8
        self.ax.add_patch(plt.Rectangle((0.1, living_start), width-0.2, length-living_start-0.1, 
                                      color=self.colors['living'], alpha=0.3))
        
        # Draw doors
        door_width = 0.9
        # Main entrance
        self.ax.add_patch(plt.Rectangle((width-0.1, 1.0), 0.1, door_width, 
                                      color=self.colors['door']))
        # Bathroom door
        self.ax.add_patch(plt.Rectangle((bathroom_width+0.1, 0.8), 0.1, door_width, 
                                      color=self.colors['door']))
        
        # Draw windows (1.2m wide)
        window_width = 1.2
        window_height = 0.1
        # Bathroom window
        self.ax.add_patch(plt.Rectangle((0.6, 0), window_width, window_height, 
                                      color='#ADD8E6'))
        # Kitchen windows
        self.ax.add_patch(plt.Rectangle((0.6, kitchen_start + 1.0), window_width, window_height, 
                                      color='#ADD8E6'))
        # Living area windows
        self.ax.add_patch(plt.Rectangle((0.6, living_start + 1.0), window_width, window_height, 
                                      color='#ADD8E6'))
        self.ax.add_patch(plt.Rectangle((width-1.8, living_start + 1.0), window_width, window_height, 
                                      color='#ADD8E6'))
        
        # Draw furniture
        # Bed (2m x 1.6m)
        self.ax.add_patch(plt.Rectangle((width-2.1, length-1.8), 2.0, 1.6, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Sofa (2.2m x 0.9m)
        self.ax.add_patch(plt.Rectangle((0.2, living_start + 0.3), 2.2, 0.9, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Dining table (1.6m x 0.9m)
        self.ax.add_patch(plt.Rectangle((0.3, kitchen_start + 0.5), 1.6, 0.9, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Storage units
        storage_depth = 0.6
        # Kitchen storage
        self.ax.add_patch(plt.Rectangle((width-0.7, kitchen_start), storage_depth, 2.0, 
                                      color=self.colors['furniture'], alpha=0.5))
        # Living area storage
        self.ax.add_patch(plt.Rectangle((width-0.7, living_start), storage_depth, 2.0, 
                                      color=self.colors['furniture'], alpha=0.5))
        
        # Add room labels
        self.ax.text(bathroom_width/2, bathroom_length/2, 'Bathroom\n2.4m × 2.2m', 
                    ha='center', va='center', color=self.colors['text'])
        self.ax.text(kitchen_width/2, kitchen_start + kitchen_length/2, 'Kitchen\n2.4m × 3.0m', 
                    ha='center', va='center', color=self.colors['text'])
        self.ax.text(width/2, living_start + (length-living_start)/2, 'Living/Sleeping Area', 
                    ha='center', va='center', color=self.colors['text'])
        
        # Add furniture labels
        self.ax.text(width-1.1, length-1.0, 'Bed', ha='center', va='center', color=self.colors['text'])
        self.ax.text(1.3, living_start + 0.75, 'Sofa', ha='center', va='center', color=self.colors['text'])
        self.ax.text(1.1, kitchen_start + 0.95, 'Dining', ha='center', va='center', color=self.colors['text'])
        self.ax.text(width-0.4, kitchen_start + 1.0, 'Storage', ha='center', va='center', rotation=90, color=self.colors['text'])
        
        # Add dimensions
        self.ax.text(width/2, -0.3, f'Width: {width*1000:.0f}mm ({width*3.28084:.1f}ft)', 
                    ha='center', color=self.colors['text'])
        self.ax.text(-0.3, length/2, f'Length: {length*1000:.0f}mm ({length*3.28084:.1f}ft)', 
                    va='center', rotation=90, color=self.colors['text'])
        
        # Add height note
        height_note = f"Exterior Height: {dimensions['height']*1000:.0f}mm ({dimensions['height']*3.28084:.1f}ft)\n"
        height_note += f"Interior Height: {dimensions['interior_height']*1000:.0f}mm ({dimensions['interior_height']*3.28084:.1f}ft)"
        self.ax.text(width/2, length + 0.3, height_note, ha='center', color=self.colors['text'])
        
        # Set equal aspect ratio and limits
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-0.5, width + 0.5)
        self.ax.set_ylim(-0.5, length + 0.5)
        
        # Add title
        title = 'Maximum Size Non-Expandable Module\n'
        title += f'Total Area: {(width * length):.1f}m² ({width * length * 10.764:.1f}sq ft)'
        self.ax.set_title(title, color=self.colors['text'])
        
        # Add legend
        legend_elements = [
            patches.Patch(facecolor=self.colors['bathroom'], alpha=0.3, label='Bathroom'),
            patches.Patch(facecolor='#FFE4B5', alpha=0.3, label='Kitchen'),
            patches.Patch(facecolor=self.colors['living'], alpha=0.3, label='Living Space'),
            patches.Patch(facecolor=self.colors['furniture'], alpha=0.5, label='Furniture')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right')
        
        # Add grid
        self.ax.grid(True, linestyle='--', alpha=0.3)
        
        # Remove axis
        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def draw_panelized_module(self, dimensions):
        # Clear any existing plots
        self.ax.clear()
        
        # Get dimensions
        width = dimensions['width']
        length = dimensions['length']
        panel_width = 1.2  # Standard panel width
        panel_height = 2.7  # Standard panel height
        
        # Draw main unit outline
        self.ax.add_patch(plt.Rectangle((0, 0), width, length, 
                                      fill=False, color=self.colors['walls'], 
                                      linewidth=2))
        
        # Draw panel grid and connection points
        for x in range(0, int(width/panel_width) + 1):
            # Vertical panel lines
            self.ax.axvline(x * panel_width, color='#666666', linestyle='--', alpha=0.5)
            # Connection points
            for y in range(0, int(length/panel_height) + 1):
                self.ax.plot(x * panel_width, y * panel_height, 'ko', markersize=4)
        
        # Draw panel numbering
        panel_count = 1
        for y in range(int(length/panel_height)):
            for x in range(int(width/panel_width)):
                self.ax.text(x * panel_width + panel_width/2, 
                           y * panel_height + panel_height/2,
                           f'P{panel_count}', ha='center', va='center',
                           color='#666666', fontsize=8)
                panel_count += 1
        
        # Draw assembly sequence indicators
        sequence_colors = ['#FF0000', '#00FF00', '#0000FF', '#FFA500']
        for i, (x, y) in enumerate([(0, 0), (width-panel_width, 0), 
                                  (0, length-panel_height), 
                                  (width-panel_width, length-panel_height)]):
            self.ax.add_patch(plt.Rectangle((x, y), panel_width, panel_height,
                                          fill=False, color=sequence_colors[i],
                                          linewidth=2))
            self.ax.text(x + panel_width/2, y + panel_height/2,
                        f'Step {i+1}', ha='center', va='center',
                        color=sequence_colors[i], fontsize=10)
        
        # Draw connection details
        connection_style = dict(arrowstyle='->', color='#FF4500', linewidth=2)
        # Corner connection
        self.ax.annotate('', xy=(panel_width, panel_height),
                        xytext=(0, 0), arrowprops=connection_style)
        self.ax.text(panel_width/2, panel_height/2, 'Quick-Lock\nConnection',
                    ha='center', va='center', color='#FF4500', fontsize=8)
        
        # Draw panel details
        detail_box = dict(boxstyle='round,pad=0.5', fc='white', ec='#666666', alpha=0.8)
        self.ax.text(0.02, 0.98, 
                    'Panel Specifications:\n'
                    f'Width: {panel_width*1000:.0f}mm\n'
                    f'Height: {panel_height*1000:.0f}mm\n'
                    'Material: SIP (Structural Insulated Panel)\n'
                    'Core: EPS Foam\n'
                    'Faces: OSB/Steel\n'
                    'Assembly Time: ~2-3 hours',
                    transform=self.ax.transAxes,
                    bbox=detail_box,
                    fontsize=8,
                    verticalalignment='top')
        
        # Add assembly notes
        self.ax.text(0.02, 0.02,
                    'Assembly Process:\n'
                    '1. Corner panels first\n'
                    '2. Wall panels\n'
                    '3. Roof panels\n'
                    '4. Interior panels\n'
                    '5. Finishing work',
                    transform=self.ax.transAxes,
                    bbox=detail_box,
                    fontsize=8,
                    verticalalignment='bottom')
        
        # Set equal aspect ratio and limits
        self.ax.set_aspect('equal')
        self.ax.set_xlim(-0.5, width + 0.5)
        self.ax.set_ylim(-0.5, length + 0.5)
        
        # Add title
        title = 'Panelized Module System\n'
        title += f'Total Panels: {panel_count-1}\n'
        title += f'Assembly Time: ~2-3 hours'
        self.ax.set_title(title, color=self.colors['text'])
        
        # Add legend
        legend_elements = [
            patches.Patch(facecolor='none', edgecolor='#666666', 
                        linestyle='--', label='Panel Grid'),
            patches.Patch(facecolor='none', edgecolor='#FF4500',
                        label='Connection Points'),
            patches.Patch(facecolor='none', edgecolor=sequence_colors[0],
                        label='Assembly Sequence')
        ]
        self.ax.legend(handles=legend_elements, loc='upper right')
        
        # Remove axis
        self.ax.set_xticks([])
        self.ax.set_yticks([])

if __name__ == "__main__":
    visualizer = LayoutVisualizer()
    visualizer.draw_single_module()
    visualizer.save("reports/single_module_layout.png") 