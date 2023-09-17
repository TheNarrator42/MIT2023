import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjA4ZmU0MDgtMGMyYS00MWYxLTk4NzMtNGIzZjUxYTM3MGUwIiwidHlwZSI6ImFwaV90b2tlbiJ9.SW7Capkzw8nByzrUAz5dWntZ_MUJLK3WpbIHHGVBG40"}

url ="https://api.edenai.run/v2/text/keyword_extraction"
payload={"show_original_response": False,"fallback_providers": "","providers": "amazon,microsoft", "language": "en", "text": "Pythagorean theorem. The equation for the Pythagorean theorem is a^2 + b^2 = c^2 where a and b are the lengths of the two legs of the triangle, and c is the length of the hypotenuse."}

response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
print(result['amazon']['items'])  #chose Amazon's API in this case, can chooose any