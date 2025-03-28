import pandas as pd
import yaml
from pathlib import Path
from typing import Dict, List, Optional

class ConstructionEstimator:
    def __init__(self, config_path: str = "data/cost_rates.yaml"):
        self.config = self._load_config(config_path)
        self.rooms_data = {}
        self.total_estimate = 0.0
        
    def _load_config(self, config_path: str) -> dict:
        """Load cost rates from YAML configuration file."""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def add_room(self, name: str, area: float, room_type: str) -> None:
        """Add a room to the estimation."""
        base_cost = sum(self.config['base_rates'].values()) * area
        
        # Add room-specific costs
        additional_cost = 0
        if room_type.lower() in self.config['room_specific_rates']:
            additional_cost = self.config['room_specific_rates'][room_type.lower()]['additional_cost'] * area
            
        room_total = base_cost + additional_cost
        
        self.rooms_data[name] = {
            'area': area,
            'type': room_type,
            'base_cost': base_cost,
            'additional_cost': additional_cost,
            'total': room_total
        }
    
    def calculate_total_estimate(self) -> float:
        """Calculate the total estimate including markup rates."""
        subtotal = sum(room['total'] for room in self.rooms_data.values())
        
        # Apply markup rates
        contractor_fee = subtotal * self.config['markup_rates']['contractor_fee']
        contingency = subtotal * self.config['markup_rates']['contingency']
        
        self.total_estimate = subtotal + contractor_fee + contingency
        return self.total_estimate
    
    def generate_report(self) -> pd.DataFrame:
        """Generate a detailed cost report."""
        report_data = []
        for room_name, room_data in self.rooms_data.items():
            report_data.append({
                'Room': room_name,
                'Type': room_data['type'],
                'Area (sq ft)': room_data['area'],
                'Base Cost': room_data['base_cost'],
                'Additional Cost': room_data['additional_cost'],
                'Total Cost': room_data['total']
            })
        
        df = pd.DataFrame(report_data)
        return df
    
    def export_to_excel(self, filepath: str) -> None:
        """Export the estimation report to Excel."""
        report = self.generate_report()
        
        # Add summary information
        summary_data = {
            'Subtotal': sum(room['total'] for room in self.rooms_data.values()),
            'Contractor Fee': self.total_estimate * self.config['markup_rates']['contractor_fee'],
            'Contingency': self.total_estimate * self.config['markup_rates']['contingency'],
            'Total Estimate': self.total_estimate
        }
        
        with pd.ExcelWriter(filepath, engine='openpyxl') as writer:
            report.to_excel(writer, sheet_name='Detailed Estimate', index=False)
            pd.DataFrame([summary_data]).to_excel(writer, sheet_name='Summary', index=False)

if __name__ == "__main__":
    # Example usage
    estimator = ConstructionEstimator()
    
    # Add rooms from the architectural plan
    estimator.add_room("Living Room", 451.41, "living_room")
    estimator.add_room("Kitchen", 176.44, "kitchen")
    estimator.add_room("Primary Bedroom", 190.47, "bedroom")
    estimator.add_room("Bathroom 1", 42.83, "bathroom")
    estimator.add_room("Bathroom 2", 65.68, "bathroom")
    
    # Calculate total estimate
    total = estimator.calculate_total_estimate()
    
    # Generate and export report
    estimator.export_to_excel("construction_estimate.xlsx") 