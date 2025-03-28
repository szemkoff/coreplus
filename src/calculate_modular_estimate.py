import matplotlib.pyplot as plt
from layout_visualizer import LayoutVisualizer
import pandas as pd
import yaml
import os

# Create reports directory if it doesn't exist
os.makedirs('reports', exist_ok=True)

# Load cost rates
with open('data/cost_rates.yaml', 'r') as f:
    cost_rates = yaml.safe_load(f)

# Maximum size module dimensions
dimensions = {
    'width': 2.55,  # meters (8'4")
    'length': 12.0,  # meters (39'4")
    'height': 2.9,  # meters (9'6")
    'interior_height': 2.7  # meters (8'10")
}

# Panel specifications
panel_width = 1.2  # meters
panel_height = 2.7  # meters
panels_per_wall = int(dimensions['width'] / panel_width)
panels_per_length = int(dimensions['length'] / panel_height)

# Calculate areas
total_area = dimensions['width'] * dimensions['length']
bathroom_area = 2.4 * 2.2  # 2.4m x 2.2m
kitchen_area = 2.4 * 3.0   # 2.4m x 3.0m
living_area = total_area - (bathroom_area + kitchen_area)

# Calculate panel counts
wall_panels = (2 * (dimensions['width'] + dimensions['length']) * dimensions['height']) / (panel_width * panel_height)
roof_panels = total_area / (panel_width * panel_width)
total_panels = wall_panels + roof_panels

# Calculate costs
costs = {
    'Foundation': total_area * cost_rates['foundation_per_sqm'],
    'Panel Manufacturing': total_panels * cost_rates['panel_rates']['wall_panel_1000x200'],
    'Connection Kits': (total_panels * 4) * cost_rates['panel_rates']['connection_kit'],
    'Bathroom Fixtures': bathroom_area * cost_rates['bathroom_fixtures_per_sqm'],
    'Kitchen Fixtures': kitchen_area * cost_rates['kitchen_fixtures_per_sqm'],
    'Interior Finishes': total_area * cost_rates['interior_finishes_per_sqm'],
    'Electrical': total_area * cost_rates['electrical_per_sqm'],
    'Plumbing': total_area * cost_rates['plumbing_per_sqm'],
    'HVAC': total_area * cost_rates['hvac_per_sqm'],
    'Windows and Doors': (2 * (dimensions['width'] + dimensions['length'])) * cost_rates['windows_doors_per_m'],
    'Assembly Labor': 3 * cost_rates['labor_rates']['specialized_installation'] * 8,  # 3 workers, 8 hours
    'Equipment Rental': 2 * cost_rates['equipment_rates']['tools_and_equipment'],  # 2 days
    'Transportation': cost_rates['equipment_rates']['container_transport'] * 2  # 2 containers
}

# Calculate total cost
total_cost = sum(costs.values())

# Create detailed Excel report
writer = pd.ExcelWriter('panelized_module_estimate.xlsx', engine='xlsxwriter')

# Cost breakdown sheet
cost_df = pd.DataFrame(list(costs.items()), columns=['Component', 'Cost'])
cost_df.to_excel(writer, sheet_name='Cost Breakdown', index=False)

# Dimensions sheet
dim_data = {
    'Dimension': ['Width', 'Length', 'Height', 'Interior Height', 'Total Area'],
    'Metric': [
        f"{dimensions['width']:.2f}m",
        f"{dimensions['length']:.2f}m",
        f"{dimensions['height']:.2f}m",
        f"{dimensions['interior_height']:.2f}m",
        f"{total_area:.2f}m²"
    ],
    'Imperial': [
        f"{dimensions['width']*3.28084:.2f}ft",
        f"{dimensions['length']*3.28084:.2f}ft",
        f"{dimensions['height']*3.28084:.2f}ft",
        f"{dimensions['interior_height']*3.28084:.2f}ft",
        f"{total_area*10.764:.2f}sq ft"
    ]
}
dim_df = pd.DataFrame(dim_data)
dim_df.to_excel(writer, sheet_name='Dimensions', index=False)

# Panel specifications sheet
panel_data = {
    'Specification': ['Panel Width', 'Panel Height', 'Total Panels', 'Wall Panels', 'Roof Panels', 'Connection Points'],
    'Value': [
        f"{panel_width*1000:.0f}mm",
        f"{panel_height*1000:.0f}mm",
        f"{total_panels:.0f}",
        f"{wall_panels:.0f}",
        f"{roof_panels:.0f}",
        f"{total_panels * 4:.0f}"
    ]
}
panel_df = pd.DataFrame(panel_data)
panel_df.to_excel(writer, sheet_name='Panel Specifications', index=False)

# Assembly timeline sheet
timeline_data = {
    'Phase': ['Site Preparation', 'Foundation', 'Panel Assembly', 'Interior Work', 'Finishing'],
    'Duration (hours)': [4, 8, 8, 8, 4],
    'Workers': [2, 3, 3, 2, 2],
    'Equipment': ['Excavator', 'Concrete Mixer', 'Crane', 'Scaffolding', 'None']
}
timeline_df = pd.DataFrame(timeline_data)
timeline_df.to_excel(writer, sheet_name='Assembly Timeline', index=False)

writer.close()

# Create layout visualization
visualizer = LayoutVisualizer()
visualizer.draw_panelized_module(dimensions)
plt.savefig('reports/panelized_module_layout.png', dpi=300, bbox_inches='tight')
plt.close()

print(f"\nTotal estimated cost: ${total_cost:,.2f}")
print(f"Assembly time: ~32 hours (4 days with 3 workers)")
print(f"Total panels: {total_panels:.0f}")
print(f"Detailed report saved to panelized_module_estimate.xlsx")
print(f"Layout visualization saved to reports/panelized_module_layout.png") 