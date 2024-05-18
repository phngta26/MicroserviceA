from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to map keywords to matching percentages
matching_scores = {
    "radiology": 70, "x-ray": 50, "rad tech": 60, "radiology technologist": 80,
    "pharm": 30, "pharmacy": 60, "pharm tech": 55, "pharmacy technician": 75, "pharmacist": 90,
    "program coordinator": 80, "project coordinator": 89, "supply chain": 92
}

# Map keywords to job positions
job_positions = {
    "radiology": "Radiology Technologist (full-time, day shift)",
    "x-ray": "Radiology Technologist (full-time, day shift)",
    "rad tech": "Radiology Technologist (full-time, day shift)",
    "radiology technologist": "Radiology Technologist (full-time, day shift)",
    "pharm": "Pharmacist 1 (full-time, day shift)",
    "pharmacy": "Pharmacist 1 (full-time, day shift)",
    "pharm tech": "Pharmacist 1 (full-time, day shift)",
    "pharmacy technician": "Pharmacist 1 (full-time, day shift)",
    "pharmacist": "Pharmacist 1 (full-time, day shift)",
    "program coordinator": "Implant Coordinator (full-time, night shift)",
    "project coordinator": "Implant Coordinator (full-time, night shift)",
    "supply chain": "Implant Coordinator (full-time, night shift)"
}

@app.route('/match', methods=['POST'])
def match():
    data = request.json
    keywords = data.get('keywords', [])
    max_score = 0
    best_match = ""

    # Calculate the highest matching percentage based on keywords
    for keyword in keywords:
        keyword = keyword.strip().lower()
        score = matching_scores.get(keyword, 0)
        if score > max_score:
            max_score = score
            best_match = keyword

    response = {
        "percentage": max_score,
        "job_position": job_positions.get(best_match, "No suitable position found.")
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
