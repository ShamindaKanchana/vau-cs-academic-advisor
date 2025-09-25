import os 
from flask import Flask, request, jsonify
from flask_cors import CORS

os.environ['GRPC_ENABLE_FORK_SUPPORT'] = '0'
os.environ['GRPC_VERBOSITY'] = 'NONE'

from langgraph.constants import START, END
from dotenv import load_dotenv
from states import *
from prompts import *

# to create state graph related 
from langgraph.graph import StateGraph

load_dotenv() 

from agents import user_input_handler, subject_content_based, subject_information_retrieval, result_based_infor_extraction, results_info_retrieval, academic_advice_ready, general_information_provider, final_user_response

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Build the graph
graph = StateGraph(dict)
graph.add_node("user_input_handler", user_input_handler)

#I want to add a node after the existing node but the existing node need to create three edges based on the type of user input and let them go with the related node 


graph.add_node("subject_content_based", subject_content_based)
graph.add_node("subject_information_retrieval", subject_information_retrieval)
graph.add_node("result_based_infor_extraction", result_based_infor_extraction)
graph.add_node("results_info_retrieval", results_info_retrieval)
graph.add_node("academic_advice_ready", academic_advice_ready)
graph.add_node("general_information_provider", general_information_provider)
graph.add_node("final_user_response", final_user_response)

graph.add_edge("subject_content_based", END)

graph.add_conditional_edges(
    "user_input_handler",
    lambda x: ("subject_content_based" 
              if x["user_input_handler"].type == "Subject_content_based" 
              else "result_based_infor_extraction" 
              if x["user_input_handler"].type == "result_based"
              else "academic_advice_ready"
              if x["user_input_handler"].type == "academic_advice"
              else "general_information_provider"
              if x["user_input_handler"].type == "general_information"
              else END)
)
graph.add_edge("subject_content_based", "subject_information_retrieval")


graph.add_edge("result_based_infor_extraction", "results_info_retrieval")


graph.add_edge("subject_information_retrieval", "final_user_response")
graph.add_edge("results_info_retrieval", "final_user_response")
graph.add_edge("academic_advice_ready", "final_user_response")
graph.add_edge("general_information_provider", "final_user_response")

graph.add_edge("final_user_response", END)

# Set the entry point for the graph
graph.set_entry_point("user_input_handler")


@app.route('/')
def home():
    return """
    <h1>VAU-CS Academic Advisor API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li>POST /api/chat - Process chat messages</li>
        <li>GET /api/health - Health check endpoint</li>
    </ul>
    """
    
# Compile the graph to an app
langgraph_app = graph.compile()



# #Extract clear response 
# def extract_clean_response(langchain_result):
#     # Get the main content from subject_information_retrieval
#     subject_info = langchain_result.get('subject_information_retrieval', {})
    
#     if subject_info.get('success'):
#         # This is the clean text response you want to send to frontend
#         clean_response = subject_info.get('result', 'No content found.')
        
#         # Optional: You can clean up the formatting if needed
#         # Remove markdown formatting if you want plain text
#         clean_response = clean_response.replace('**', '').replace('*', '')
        
#         return clean_response
#     else:
#         return "Sorry, I couldn't retrieve the information you requested."

# Define the chat endpoint
@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({'status': 'success'})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
        
    try:
        data = request.get_json()
        print(f"Received data: {data}")
        if not data or 'message' not in data:
            return jsonify({
                'status': 'error',
                'message': 'No message provided'
            }), 400

        user_message = data['message'].strip()
        if not user_message:
            return jsonify({
                'status': 'error',
                'message': 'Message cannot be empty'
            }), 400

        print(f"Processing message: {user_message}")

        # Process the message using the LangGraph app
        result = langgraph_app.invoke(
            {"user_input": user_message}, 
            {"recursion_limit": 20}
        )
        
        
        print(f"LangGraph result: {result}")
        print(f"Data type of that : {type(result)}")
    
        #Here now need to send that result in to the frontend 
        
     
        
        response = jsonify({
            'status': 'success',
            'response': result
        })
        
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error in /api/chat: {error_details}")
        response = jsonify({
            'status': 'error',
            'message': str(e),
            'details': 'Check server logs for more details'
        })
        response.status_code = 500
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


