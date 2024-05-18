import requests

def get_matching_percentage(keywords):
    endpoint = 'http://localhost:5000/match'
    response = requests.post(endpoint, json={'keywords': keywords})
    return response.json()

def main():
    while True:
        user_input = input("Enter keywords separated by commas (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        keywords = [keyword.strip() for keyword in user_input.split(',')]  # Ensure spaces are removed
        result = get_matching_percentage(keywords)
        print(f"You are {result['percentage']}% matching to the {result['job_position']}.")

if __name__ == "__main__":
    main()
