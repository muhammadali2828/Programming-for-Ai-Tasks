from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

university_data = {
    "admission": {
        "keywords": ["admission", "how to apply", "apply", "enroll", "admission process", "application"],
        "response": "To apply for admission, visit our admission portal and fill out the online application form. You'll need scanned documents and transcripts."
    },
    "programs": {
        "keywords": ["programs", "courses", "degrees", "majors", "subjects", "fields of study", "what do you offer"],
        "response": "We offer undergraduate and postgraduate programs in Computer Science, Business, Engineering, and Social Sciences."
    },
    "deadlines": {
        "keywords": ["deadline", "last date", "application deadline", "apply by", "submission date"],
        "response": "The application deadline for Fall 2025 is July 31, 2025."
    },
    "fees": {
        "keywords": ["fee", "tuition", "cost", "price", "charges", "how much"],
        "response": "The tuition fee for undergraduate programs is Rs 155,000/- per semester. Scholarships are available based on merit."
    },
    "contact": {
        "keywords": ["contact", "email", "phone", "reach", "get in touch", "admissions office"],
        "response": "You can reach the admissions office at  info@superior.edu.pk or call us at (042) 38102223. Inquiry Timings: (Mon- Fri) 08 AM to 4 PM"
    },
    "superior": {
        "keywords": ["superior", "why", "why not superior"],
        "response": "Superior University is among Pakistan’s top private universities, known for its award-winning incubator, global links, and the 3U1M program — 3 years study, 1 year industry mentorship"
    },
    "scholarships": {
        "keywords": ["scholarship", "financial aid", "merit", "grant", "funding"],
        "response": "We offer merit-based scholarships, need-based grants, and financial aid packages. Check our scholarships page for eligibility and deadlines."
    },
    "hostel": {
        "keywords": ["hostel", "accommodation", "dorm", "living", "stay", "housing"],
        "response": "We provide on-campus housing with single and shared rooms. Hostel facilities include Wi-Fi, laundry, and mess services."
    },
    "transport": {
        "keywords": ["bus", "transport", "shuttle", "commute", "travel"],
        "response": "We offer shuttle services across major city routes for students and staff. Monthly passes are available."
    },
    "campus": {
        "keywords": ["campus", "location", "facilities", "infrastructure", "library", "labs"],
        "response": "Our campus features modern labs, a large library, sports facilities, cafes, and student lounges. It's located in the heart of the city."
    },
    "internships": {
        "keywords": ["internship", "intern", "job", "placement", "career", "recruitment"],
        "response": "Our Career Services Office helps students secure internships and jobs through industry partnerships and career fairs."
    },
    "duration": {
        "keywords": ["duration", "how long", "length of program", "years", "semester"],
        "response": "Most undergraduate programs are 4 years long, while master's programs typically take 2 years."
    },
    "documents": {
        "keywords": ["documents", "required documents", "needed documents", "transcripts", "requirements"],
        "response": "You will need your academic transcripts, national ID, passport-size photos, and any standardized test scores for your application."
    },
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "what’s up", "yo", "sup"],
        "response": "Hello! How can I assist you today? You can ask about admissions, programs, fees, deadlines, or anything else!"
    }
}


def get_response(user_input):
    user_input = user_input.lower()
    response = "Sorry, I couldn't understand that. Can you please rephrase?"

    for category, info in university_data.items():
        for keyword in info["keywords"]:
            if keyword in user_input:
                response = info["response"]
                return response
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
