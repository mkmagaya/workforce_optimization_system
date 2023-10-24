def calculate_number_of_workers(productivity_data, target_productivity):
    total_productivity = sum(productivity_data)
    average_productivity = total_productivity / len(productivity_data)
    required_workers = (target_productivity * len(productivity_data)) / average_productivity
    return round(required_workers)

# Example usage
productivity_data = [80, 90, 95, 85, 75]  # List of individual productivity values
target_productivity = 100  # Desired target productivity

number_of_workers = calculate_number_of_workers(productivity_data, target_productivity)
print(f"Number of workers to employ: {number_of_workers}")