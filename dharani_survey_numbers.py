import requests
import json

def get_survey_numbers(district_id, mandal_id, village_id):
    url = "https://dharani.telangana.gov.in/knowLandStatus/getVillageWiseSurveyNumbersByMandalID"
    payload = {
        "districtId": district_id,
        "mandalId": mandal_id,
        "villageId": village_id
    }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    data = response.json()

    if "surveyNumbers" in data:
        survey_numbers = data["surveyNumbers"]
    else:
        survey_numbers = []

    return survey_numbers

def main():
    # Example usage
    district_id = "3"  # Hyderabad
    mandal_id = "2"     # Secunderabad
    village_id = "23"   # Yapral

    survey_numbers = get_survey_numbers(district_id, mandal_id, village_id)
    print(f"Survey numbers for District: {district_id}, Mandal: {mandal_id}, Village: {village_id}:")
    for survey_number in survey_numbers:
        print(survey_number)

if __name__ == "__main__":
    main()
