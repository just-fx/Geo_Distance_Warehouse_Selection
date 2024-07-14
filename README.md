# Warehouse Distance Calculator
This Python script calculates the average distance between a given warehouse and a list of customer locations. The user inputs the warehouse name, its coordinates, and a CSV file containing the customer locations. The script processes this data and computes the average distance of all customers to the specified warehouse.

# Requirements
- Python 3.x
- Pandas
- Geopy

# Installation
1. Clone the repository:
```sh
git clone https://github.com/yourusername/warehouse-distance-calculator.git
```
3. Navigate to the project directory:
```sh
cd warehouse-distance-calculator
```
5. Install the required Python packages:
```sh
pip install -r requirements.txt
```

# Usage
1. Prepare your CSV file with customer locations. You may also use the csv file provided in thsi repo, which was extracted from Looker Ecommerce sample data. The file should have the following columns:
- `user_country`
- `user_latitude`
- `user_longitude`
2. Run the script:
```sh
python calculate_distance.py
```
3. Follow the prompts to input the warehouse name and its coordinates.
4. The script will read the CSV file, compute the average distance of all customers to the warehouse, and display the result.
