from estimator import ConstructionEstimator
from plan_processor import PlanProcessor
import os

def main():
    # Initialize the plan processor
    processor = PlanProcessor()
    
    # Load room data from the architectural plan
    rooms_data = [
        ("ENTRY", 84.29),
        ("LAUNDRY", 42.83),
        ("OFFICE", 110.44),
        ("PANTRY", 26.04),
        ("LIVING ROOM", 451.41),
        ("BALCONY", 37.48),
        ("CLOSET", 41.15),
        ("BATHROOM", 42.83),
        ("PRIMARY BEDROOM", 190.47),
        ("PRIMARY BATHROOM", 55.11),
        ("FAMILY ROOM", 365.11),
        ("WIC", 43.29),
        ("BATHROOM 2", 42.83),
        ("BEDROOM 1", 178.29),
        ("BEDROOM 2", 166.64),
        ("BATHROOM 3", 65.68)
    ]
    
    for name, area in rooms_data:
        processor.add_room_data(name, area)
    
    # Get processed room data
    rooms = processor.get_rooms_data()
    
    # Initialize the estimator
    estimator = ConstructionEstimator()
    
    # Add rooms to the estimator
    for room_name, room_data in rooms.items():
        estimator.add_room(room_name, room_data['area'], room_data['type'])
    
    # Calculate total estimate
    total = estimator.calculate_total_estimate()
    
    # Generate and export report
    output_file = "construction_estimate_new.xlsx"
    estimator.export_to_excel(output_file)
    
    print(f"\nEstimation complete!")
    print(f"Total estimated cost: ${total:,.2f}")
    print(f"Detailed report has been saved to: {output_file}")

if __name__ == "__main__":
    main() 