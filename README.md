📄 README.md
markdown
Copy
Edit
# 🧠 LLMWhisperer Text Extraction & JSON Output

This project uses the **Unstract LLM Whisperer API** to extract text from an image or document file (like a `.jpg`, `.png`, or `.pdf`) and outputs the result in clean, structured JSON format.

---

## 📌 Features

- ✅ Extract text from scanned images or PDFs using LLM Whisperer
- ✅ Polls for asynchronous job completion
- ✅ Outputs extracted content in JSON format
- ✅ Optionally saves the output as a `.json` file

---

## 🛠️ Requirements

- Python 3.8+
- An API key from [Unstract](https://unstract.com/)
- Internet connection

---

## 📦 Installation

1. Clone this repo or download the script:

```bash
git clone https://github.com/your-username/unstract-json-extractor.git
cd unstract-json-extractor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file and add your Unstract API key:

ini
Copy
Edit
UNSTRACT_API_KEY=your_api_key_here
📁 File Structure
bash
Copy
Edit
.
├── with_JSON.py          # Main script to extract and print JSON
├── .env                  # Environment file (you create this)
├── output.json           # Output file (generated after run)
└── README.md             # You're reading it now
▶️ Usage
Edit the file path inside with_JSON.py and run:

bash
Copy
Edit
python with_JSON.py
If successful, the script will:

Extract the text from your file

Print the output in JSON format

Save it to output.json (optional)

📝 Sample Output
json
Copy
Edit
{
  "file_name": "tata-steel-ir-2022-23.jpg",
  "whisper_hash": "abc123xyz",
  "extracted_text": "Tata Steel Integrated Report 2022-23..."
}
❓ FAQ
Q: What kind of files can I upload?
A: JPG, PNG, PDF, or any file supported by LLM Whisperer.

Q: Is this offline?
A: No. This uses a cloud-based API by Unstract, so internet access is required.

Q: Can I query the extracted data?
A: Yes, with Unstract's collections API. This version just extracts and formats the text.

📌 To-Do
 Add document search using Unstract hybrid query

 Add CLI interface

 Add support for batch processing

💡 Credits
Built using the Unstract LLM Whisperer API.

📜 License
MIT License

yaml
Copy
Edit

---

Let me know if you want me to generate a `requirements.txt` as well or include collection querying in a future version.







