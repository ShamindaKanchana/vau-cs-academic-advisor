import os 

os.environ['GRPC_ENABLE_FORK_SUPPORT'] = '0'
os.environ['GRPC_VERBOSITY'] = 'NONE'

from langgraph.constants import START, END
from dotenv import load_dotenv
from states import *
from prompts import *

# to create state graph related 
from langgraph.graph import StateGraph

load_dotenv() 

from agents import user_input_handler,subject_content_based,subject_information_retrieval,result_based_infor_extraction


# Build the graph
graph = StateGraph(dict)
graph.add_node("user_input_handler", user_input_handler)

#I want to add a node after the existing node but the existing node need to create three edges based on the type of user input and let them go with the related node 


graph.add_node("subject_content_based", subject_content_based)
graph.add_node("subject_information_retrieval", subject_information_retrieval)
graph.add_node("result_based_infor_extraction", result_based_infor_extraction)

graph.add_edge("subject_content_based", END)

graph.add_conditional_edges(
    "user_input_handler",
    lambda x: ("subject_content_based" 
              if x["user_input_handler"].type == "Subject_content_based" 
              else "result_based_infor_extraction" 
              if x["user_input_handler"].type == "result_based"
              else END)
)
graph.add_edge("subject_content_based", "subject_information_retrieval")

graph.add_edge("subject_information_retrieval", END)
graph.add_edge("result_based_infor_extraction", END)

graph.set_entry_point("user_input_handler")

# Compile the graph to an app
app = graph.compile()

if __name__ == "__main__":
	test_set=["I have C pass for differential equations and B pass for Computer Science then how my results affect to industry "]



	for i in range(len(test_set)):
		result = app.invoke({"user_input": test_set[i] }, {"recursion_limit": 20})
		print(result)


