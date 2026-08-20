def process_iris_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    total_records = 0
    # Venn Diagram concept
    flower_types = set() 
    
    # Extract and Process the data
    for line in lines:
        line = line.strip() 
    
        if line: 
            total_records += 1
            pieces = line.split(',')
            
            # flower species
            species_name = pieces[-1] 
            flower_types.add(species_name)
            
    # results
    print(f"Total number of records: {total_records}")
    print(f"Total number of different flowers available: {len(flower_types)}")
    print(f"Names of all different flowers: {', '.join(flower_types)}")

# Run
if __name__ == '__main__':
    process_iris_data("iris.data")