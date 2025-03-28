import pandas as pd
import yaml
from pathlib import Path
from typing import Dict, List, Optional
import matplotlib.pyplot as plt
import seaborn as sns

class ModularConstructionEstimator:
    def __init__(self, config_path: str = "data/cost_rates.yaml"):
        self.config = self._load_config(config_path)
        self.components = {
            'cores': [],
            'panels': {'wall': [], 'floor': [], 'roof': []},
            'modules': []
        }
        self.bom = []  # Bill of Materials
        self.specifications = []  # Technical specifications
        self.total_estimate = 0.0
        
    def _load_config(self, config_path: str) -> dict:
        """Load cost rates from YAML configuration file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def add_core_module(self, quantity: int = 1) -> None:
        """Add Core+ engineering module with detailed components."""
        core_cost = self.config['core_module_rates']['engineering_core'] * quantity
        installation_cost = self.config['equipment_rates']['core_installation'] * quantity
        
        # Technical specifications for Core+ module
        core_specs = {
            'Dimensions': {
                'Length': '2400mm',
                'Width': '3900mm',
                'Height': '2300mm',
                'Total Volume': '21.528 m³'
            },
            'Plumbing System': {
                'Water Supply': 'Integrated 3/4" main line with pressure regulator',
                'Drainage': 'PVC 110mm main line with venting',
                'Hot Water': '50L electric water heater',
                'Fixtures': {
                    'Toilet': 'Wall-mounted with concealed cistern',
                    'Sink': 'Ceramic wall-mounted with mixer',
                    'Shower': 'Thermostatic mixer with rainfall head'
                }
            },
            'Electrical System': {
                'Main Supply': '230V/400V, 50Hz, 3-phase',
                'Distribution': '24-circuit consumer unit',
                'Lighting': 'LED recessed spots, IP44 rated',
                'Outlets': 'IP44 rated GFCI protected',
                'Cable Rating': 'Fire-resistant to E150 standard'
            },
            'HVAC System': {
                'Ventilation': 'Mechanical with heat recovery',
                'Air Changes': '30m³/h per person',
                'Temperature Range': '18-26°C',
                'Controls': 'Digital thermostat with humidity sensor'
            },
            'Structure': {
                'Frame': 'Galvanized steel frame, E150 fire-rated',
                'Insulation': {
                    'Walls': 'Mineral wool, 100mm, R-value: 2.9 m²K/W',
                    'Floor': 'XPS foam, 150mm, R-value: 4.4 m²K/W',
                    'Ceiling': 'Mineral wool, 200mm, R-value: 5.8 m²K/W'
                },
                'Interior Finish': {
                    'Walls': 'Moisture-resistant gypsum board',
                    'Floor': 'Anti-slip ceramic tiles',
                    'Ceiling': 'Washable PVC panels'
                }
            },
            'Certifications': {
                'Fire Rating': 'E150',
                'Thermal Performance': 'U-value < 0.25 W/m²K',
                'Acoustic Rating': 'Rw = 45dB',
                'Water Resistance': 'IP44'
            }
        }
        
        self.specifications.append({
            'Module': 'Core+',
            'Specifications': core_specs
        })
        
        # Add core components to BOM with detailed specifications
        core_components = {
            'Plumbing System': {
                'toilet': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Wall-mounted with concealed cistern, dual flush 3/6L'},
                'sink': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Ceramic wall-mounted, 600mm width with mixer tap'},
                'shower': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Thermostatic mixer with rainfall head, 200mm diameter'},
                'water_heater': {'qty': 1 * quantity, 'unit': 'unit', 'spec': '50L electric, 2kW heating element'},
                'pipes_and_fittings': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'PEX piping with brass fittings'}
            },
            'Electrical System': {
                'main_panel': {'qty': 1 * quantity, 'unit': 'unit', 'spec': '24-circuit, 100A main breaker'},
                'outlets': {'qty': 8 * quantity, 'unit': 'pcs', 'spec': 'IP44 GFCI protected, 16A'},
                'switches': {'qty': 4 * quantity, 'unit': 'pcs', 'spec': 'IP44 rated with LED indicator'},
                'lighting': {'qty': 4 * quantity, 'unit': 'pcs', 'spec': 'LED recessed, 12W, 3000K'},
                'wiring': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Fire-resistant cables to E150 standard'}
            },
            'HVAC System': {
                'ventilation_unit': {'qty': 1 * quantity, 'unit': 'unit', 'spec': 'Heat recovery, 90% efficiency'},
                'ductwork': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Insulated aluminum, 125mm diameter'},
                'controls': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Digital thermostat with WiFi connectivity'}
            },
            'Core Structure': {
                'frame': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Galvanized steel, 3mm thickness'},
                'insulation': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Mineral wool + XPS composite'},
                'interior_finish': {'qty': 1 * quantity, 'unit': 'set', 'spec': 'Moisture-resistant panels'}
            }
        }
        
        for system, components in core_components.items():
            for component, details in components.items():
                self.bom.append({
                    'System': system,
                    'Component': component,
                    'Quantity': details['qty'],
                    'Unit': details['unit'],
                    'Module': 'Core+',
                    'Specifications': details['spec']
                })
        
        self.components['cores'].append({
            'type': 'Core+ Module',
            'quantity': quantity,
            'base_cost': core_cost,
            'installation_cost': installation_cost,
            'total': core_cost + installation_cost,
            'components': core_components
        })
    
    def add_panels(self, wall_panels: Dict[str, int], floor_panels: int, roof_panels: int) -> None:
        """Add wall, floor and roof panels with specifications."""
        # Wall panels
        wall_cost = sum(
            self.config['panel_rates'][f'wall_panel_1000x{thickness}'] * quantity
            for thickness, quantity in wall_panels.items()
        )
        
        # Add wall panels to BOM
        for thickness, quantity in wall_panels.items():
            self.bom.append({
                'System': 'Wall System',
                'Component': f'Wall Panel {thickness}mm',
                'Quantity': quantity,
                'Unit': 'panels',
                'Specifications': f'1000x{thickness}x2700mm, Weight: {60 + int(thickness)/10}kg'
            })
            # Add fasteners and sealants
            self.bom.append({
                'System': 'Wall System',
                'Component': 'Panel Fasteners',
                'Quantity': quantity * 8,  # 8 fasteners per panel
                'Unit': 'pcs',
                'Specifications': 'Heavy-duty steel fasteners'
            })
            self.bom.append({
                'System': 'Wall System',
                'Component': 'Sealant',
                'Quantity': quantity * 2,  # 2 tubes per panel
                'Unit': 'tubes',
                'Specifications': 'Weather-resistant sealant'
            })
        
        # Floor panels
        floor_cost = self.config['panel_rates']['floor_panel'] * floor_panels
        self.bom.append({
            'System': 'Floor System',
            'Component': 'Floor Panel',
            'Quantity': floor_panels,
            'Unit': 'panels',
            'Specifications': '1000x150x1000mm, Load-bearing'
        })
        
        # Roof panels
        roof_cost = self.config['panel_rates']['roof_panel'] * roof_panels
        self.bom.append({
            'System': 'Roof System',
            'Component': 'Roof Panel',
            'Quantity': roof_panels,
            'Unit': 'panels',
            'Specifications': '1000x200x1000mm, Insulated'
        })
        
        # Add connection components
        self.bom.append({
            'System': 'Assembly Components',
            'Component': 'Panel Connectors',
            'Quantity': (sum(wall_panels.values()) + floor_panels + roof_panels) * 4,
            'Unit': 'sets',
            'Specifications': 'Steel connection sets'
        })
        
        self.components['panels']['wall'].append({
            'type': 'Wall Panels',
            'quantities': wall_panels,
            'total': wall_cost
        })
        
        self.components['panels']['floor'].append({
            'type': 'Floor Panels',
            'quantity': floor_panels,
            'total': floor_cost
        })
        
        self.components['panels']['roof'].append({
            'type': 'Roof Panels',
            'quantity': roof_panels,
            'total': roof_cost
        })
    
    def add_labor_costs(self, specialized_hours: float, assembly_hours: float) -> None:
        """Add labor costs for installation and assembly."""
        specialized_cost = specialized_hours * self.config['labor_rates']['specialized_installation']
        assembly_cost = assembly_hours * self.config['labor_rates']['general_assembly']
        
        self.components['modules'].append({
            'type': 'Labor',
            'specialized_hours': specialized_hours,
            'assembly_hours': assembly_hours,
            'specialized_cost': specialized_cost,
            'assembly_cost': assembly_cost,
            'total': specialized_cost + assembly_cost
        })
    
    def calculate_total_estimate(self) -> float:
        """Calculate total estimate including all components, labor, and markups."""
        # Sum all component costs
        core_costs = sum(core['total'] for core in self.components['cores'])
        panel_costs = (
            sum(panel['total'] for panel in self.components['panels']['wall']) +
            sum(panel['total'] for panel in self.components['panels']['floor']) +
            sum(panel['total'] for panel in self.components['panels']['roof'])
        )
        labor_costs = sum(module['total'] for module in self.components['modules'])
        
        # Add transportation costs
        transport_costs = self.config['equipment_rates']['container_transport'] * 2  # Two containers
        
        # Add certification costs
        certification_costs = (
            self.config['certification_rates']['fire_resistance_testing'] +
            self.config['certification_rates']['quality_control']
        )
        
        subtotal = core_costs + panel_costs + labor_costs + transport_costs + certification_costs
        
        # Apply markup rates
        contractor_fee = subtotal * self.config['markup_rates']['contractor_fee']
        contingency = subtotal * self.config['markup_rates']['contingency']
        
        self.total_estimate = subtotal + contractor_fee + contingency
        return self.total_estimate
    
    def generate_report(self) -> pd.DataFrame:
        """Generate a detailed cost report."""
        report_data = []
        
        # Core modules
        for core in self.components['cores']:
            report_data.append({
                'Component': core['type'],
                'Quantity': core['quantity'],
                'Base Cost': core['base_cost'],
                'Installation Cost': core['installation_cost'],
                'Total Cost': core['total']
            })
        
        # Panels
        for panel_type, panels in self.components['panels'].items():
            for panel in panels:
                if panel_type == 'wall':
                    for thickness, quantity in panel['quantities'].items():
                        report_data.append({
                            'Component': f'Wall Panel {thickness}mm',
                            'Quantity': quantity,
                            'Base Cost': self.config['panel_rates'][f'wall_panel_1000x{thickness}'] * quantity,
                            'Installation Cost': 0,
                            'Total Cost': self.config['panel_rates'][f'wall_panel_1000x{thickness}'] * quantity
                        })
                else:
                    report_data.append({
                        'Component': panel['type'],
                        'Quantity': panel['quantity'],
                        'Base Cost': panel['total'],
                        'Installation Cost': 0,
                        'Total Cost': panel['total']
                    })
        
        # Labor
        for module in self.components['modules']:
            report_data.append({
                'Component': 'Specialized Labor',
                'Quantity': module['specialized_hours'],
                'Base Cost': module['specialized_cost'],
                'Installation Cost': 0,
                'Total Cost': module['specialized_cost']
            })
            report_data.append({
                'Component': 'Assembly Labor',
                'Quantity': module['assembly_hours'],
                'Base Cost': module['assembly_cost'],
                'Installation Cost': 0,
                'Total Cost': module['assembly_cost']
            })
        
        return pd.DataFrame(report_data)
    
    def generate_bom_report(self) -> pd.DataFrame:
        """Generate a detailed bill of materials report."""
        return pd.DataFrame(self.bom)
    
    def generate_visualizations(self, output_dir: str = "reports") -> None:
        """Generate visualization charts for the cost breakdown."""
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Prepare data for visualization
        report = self.generate_report()
        
        # 1. Cost Breakdown Pie Chart
        plt.figure(figsize=(12, 8))
        costs = report.groupby('Component')['Total Cost'].sum()
        plt.pie(costs, labels=costs.index, autopct='%1.1f%%')
        plt.title('Cost Distribution by Component')
        plt.savefig(f"{output_dir}/cost_distribution_pie.png")
        plt.close()
        
        # 2. Component Costs Bar Chart
        plt.figure(figsize=(15, 8))
        sns.barplot(data=report, x='Component', y='Total Cost')
        plt.xticks(rotation=45, ha='right')
        plt.title('Component Costs Breakdown')
        plt.tight_layout()
        plt.savefig(f"{output_dir}/component_costs_bar.png")
        plt.close()
        
        # 3. Installation vs Base Cost Comparison
        plt.figure(figsize=(15, 8))
        report_melt = report.melt(id_vars=['Component'], 
                                value_vars=['Base Cost', 'Installation Cost'],
                                var_name='Cost Type', value_name='Cost')
        sns.barplot(data=report_melt, x='Component', y='Cost', hue='Cost Type')
        plt.xticks(rotation=45, ha='right')
        plt.title('Base Cost vs Installation Cost by Component')
        plt.tight_layout()
        plt.savefig(f"{output_dir}/cost_comparison_bar.png")
        plt.close()

    def export_to_excel(self, filepath: str) -> None:
        """Export the estimation report, BOM, and specifications to Excel."""
        report = self.generate_report()
        bom_report = self.generate_bom_report()
        
        # Create specifications DataFrame
        specs_data = []
        for spec in self.specifications:
            for category, details in spec['Specifications'].items():
                if isinstance(details, dict):
                    for subcategory, value in details.items():
                        if isinstance(value, dict):
                            for subsubcategory, subvalue in value.items():
                                specs_data.append({
                                    'Module': spec['Module'],
                                    'Category': category,
                                    'Subcategory': f"{subcategory} - {subsubcategory}",
                                    'Specification': subvalue
                                })
                        else:
                            specs_data.append({
                                'Module': spec['Module'],
                                'Category': category,
                                'Subcategory': subcategory,
                                'Specification': value
                            })
                else:
                    specs_data.append({
                        'Module': spec['Module'],
                        'Category': category,
                        'Subcategory': '',
                        'Specification': details
                    })
        
        specs_df = pd.DataFrame(specs_data)
        
        # Calculate summary data
        summary_data = self._calculate_summary_data(report)
        
        # Export to Excel
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            report.to_excel(writer, sheet_name='Detailed Estimate', index=False)
            bom_report.to_excel(writer, sheet_name='Bill of Materials', index=False)
            specs_df.to_excel(writer, sheet_name='Technical Specifications', index=False)
            pd.DataFrame([summary_data]).to_excel(writer, sheet_name='Summary', index=False)
        
        # Generate visualizations
        self.generate_visualizations()

    def _calculate_summary_data(self, report: pd.DataFrame) -> Dict:
        """Calculate summary data for the report."""
        subtotal = report['Total Cost'].sum()
        transport_costs = self.config['equipment_rates']['container_transport'] * 2
        certification_costs = (
            self.config['certification_rates']['fire_resistance_testing'] +
            self.config['certification_rates']['quality_control']
        )
        contractor_fee = subtotal * self.config['markup_rates']['contractor_fee']
        contingency = subtotal * self.config['markup_rates']['contingency']
        
        return {
            'Subtotal': subtotal,
            'Transport Costs': transport_costs,
            'Certification Costs': certification_costs,
            'Contractor Fee': contractor_fee,
            'Contingency': contingency,
            'Total Estimate': self.total_estimate
        } 