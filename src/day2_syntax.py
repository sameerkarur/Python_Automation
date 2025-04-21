from typing import List, Dict, Optional
import json
from pathlib import Path

class DataProcessor:
    """Example class demonstrating Python syntax concepts."""
    
    def __init__(self, data_file: Optional[str] = None):
        self.data: List[Dict] = []
        self.data_file = data_file

    def load_data(self) -> None:
        """
        Demonstrates file handling and exception handling.
        Loads data from a JSON file if provided, otherwise uses empty list.
        """
        try:
            if self.data_file and Path(self.data_file).exists():
                with open(self.data_file, 'r') as f:
                    self.data = json.load(f)
            else:
                print("No data file provided or file doesn't exist. Using empty list.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

    def process_items(self, minimum_value: float = 0) -> Dict[str, List]:
        """
        Demonstrates loops, list comprehension, and dictionary manipulation.
        
        Args:
            minimum_value: Minimum value for filtering items
            
        Returns:
            Dictionary with processed and filtered items
        """
        # Dictionary comprehension example
        categories = {item['category'] for item in self.data if 'category' in item}
        
        # Initialize results
        results = {
            'processed': [],
            'filtered_out': []
        }
        
        # For loop with exception handling
        for item in self.data:
            try:
                # Demonstrate multiple conditions
                if ('value' in item and 
                    isinstance(item['value'], (int, float)) and 
                    item['value'] >= minimum_value):
                    
                    # List manipulation
                    processed_item = {
                        **item,  # Dictionary unpacking
                        'status': 'processed',
                        'value_doubled': item['value'] * 2
                    }
                    results['processed'].append(processed_item)
                else:
                    results['filtered_out'].append(item)
                    
            except (KeyError, TypeError) as e:
                print(f"Error processing item {item}: {e}")
                continue
            
        return results

    def demonstrate_loops(self) -> None:
        """Demonstrates different types of loops and iterations."""
        # Range-based for loop
        print("\nRange-based loop:")
        for i in range(3):
            print(f"Index: {i}")
        
        # Enumerate example
        print("\nEnumerate example:")
        sample_list = ['a', 'b', 'c']
        for index, value in enumerate(sample_list):
            print(f"Index {index}: {value}")
        
        # While loop example
        print("\nWhile loop example:")
        counter = 0
        while counter < 3:
            print(f"Counter: {counter}")
            counter += 1
            
        # List comprehension
        squares = [x**2 for x in range(5)]
        print(f"\nList comprehension result: {squares}")

def main():
    # Create sample data
    sample_data = [
        {"category": "A", "value": 100},
        {"category": "B", "value": 50},
        {"category": "A", "value": 75},
        {"category": "C", "value": -10},
        {"category": "B"},  # Missing value
        {"category": "D", "value": "invalid"}  # Invalid value type
    ]
    
    # Save sample data to file
    with open('sample_data.json', 'w') as f:
        json.dump(sample_data, f, indent=2)
    
    # Create processor instance
    processor = DataProcessor('sample_data.json')
    
    try:
        # Load and process data
        processor.load_data()
        results = processor.process_items(minimum_value=60)
        
        print("\nProcessed items:")
        for item in results['processed']:
            print(f"  {item}")
            
        print("\nFiltered out items:")
        for item in results['filtered_out']:
            print(f"  {item}")
            
        # Demonstrate various loops
        processor.demonstrate_loops()
        
    except Exception as e:
        print(f"Error in main: {e}")
    finally:
        # Cleanup
        Path('sample_data.json').unlink(missing_ok=True)

if __name__ == "__main__":
    main()
