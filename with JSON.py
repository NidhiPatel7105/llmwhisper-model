import os
import time
import json
from dotenv import load_dotenv
from unstract.llmwhisperer import LLMWhispererClientV2

# Load environment variables
load_dotenv()

# Initialize client
client = LLMWhispererClientV2(
    base_url="https://llmwhisperer-api.us-central.unstract.com/api/v2",
    api_key=os.getenv("UNSTRACT_API_KEY")
)

# Step 1: Send file to Whisperer
result = client.whisper(file_path=r"C:\Users\nidhi\OneDrive\Desktop\llm\RAWDDIVB.pdf")

# Step 2: Wait until processing is complete
while True:
    status = client.whisper_status(whisper_hash=result["whisper_hash"])
    if status["status"] == "processed":
        resultx = client.whisper_retrieve(whisper_hash=result["whisper_hash"])
        break
    time.sleep(5)

# Step 3: Get extracted text
extracted_text = resultx["extraction"]["result_text"]

# Step 4: Wrap in JSON and print
output_json = {
    "file_name": "healthcare-example.pdf",
    "whisper_hash": result["whisper_hash"],
    "extracted_text": extracted_text
}

# Pretty print the JSON result
print(json.dumps(output_json, indent=2))

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output_json, f, indent=2, ensure_ascii=False)
