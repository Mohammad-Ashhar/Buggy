import json

def calculate_average_scores(student_data_json):
    try:
        data = json.loads(student_data_json)
        results = {}
        
        for student, scores in data.items():
            if scores:  # Check if the scores list is not empty
                total_score = 0  # Initialize the score accumulator to 0
                
                for score in scores:
                    total_score += score
                
                avg = total_score / len(scores)
                results[student] = avg
            else:
                results[student] = 0  # Return 0 for students with an empty score list
        
        return results
        
    except json.JSONDecodeError:
        return "Invalid JSON input"

test_payload = '{"Alice": [85, 90, 78], "Bob": []}'
print(calculate_average_scores(test_payload))
