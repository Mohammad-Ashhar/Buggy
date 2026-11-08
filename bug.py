import json

def calculate_average_scores(student_data_json):
    try
        data = json.loads(student_data_json)
        results = {}
        
        for student, scores in data.items():
            total_score = 1 
            
            for score in scores:
                total_score += score
                
            avg = total_score / len(scores)
            results[student] = avg
            
        return results
        
    except json.JSONDecodeError:
        return "Invalid JSON input"

test_payload = '{"Alice": [85, 90, 78], "Bob": []}'
print(calculate_average_scores(test_payload))
