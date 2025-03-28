from typing import Dict, List, Tuple
import pandas as pd

class PlanProcessor:
    def __init__(self):
        self.rooms = {}
        
    def add_room_data(self, name: str, area: float, room_type: str = None) -> None:
        """Add room data from the architectural plan."""
        if room_type is None:
            room_type = self._determine_room_type(name)
            
        self.rooms[name] = {
            'area': area,
            'type': room_type
        }
    
    def _determine_room_type(self, room_name: str) -> str:
        """Determine room type based on room name."""
        room_name = room_name.lower()
        if 'bath' in room_name:
            return 'bathroom'
        elif 'bed' in room_name:
            return 'bedroom'
        elif 'kitchen' in room_name:
            return 'kitchen'
        elif 'living' in room_name:
            return 'living_room'
        elif 'family' in room_name:
            return 'living_room'
        elif 'dining' in room_name:
            return 'dining_room'
        else:
            return 'other'
    
    def load_from_excel(self, filepath: str, sheet_name: str = None) -> None:
        """Load room data from Excel file."""
        df = pd.read_excel(filepath, sheet_name=sheet_name)
        
        # Assuming Excel has columns: NAME, AREA
        for _, row in df.iterrows():
            self.add_room_data(row['NAME'], row['AREA'])
    
    def get_rooms_data(self) -> Dict:
        """Get processed room data."""
        return self.rooms

# Example usage based on the architectural plan
if __name__ == "__main__":
    processor = PlanProcessor()
    
    # Adding rooms from the architectural plan
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
    
    # Get processed data
    processed_rooms = processor.get_rooms_data() 