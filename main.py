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

from agents import user_input_handler,subject_content_based,subject_information_retrieval,result_based_infor_extraction,results_info_retrieval,academic_advice_ready,general_information_provider


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

graph.add_edge("subject_information_retrieval", END)
graph.add_edge("result_based_infor_extraction", "results_info_retrieval")
graph.add_edge("results_info_retrieval", END)
graph.add_edge("academic_advice_ready", END)
graph.add_edge("general_information_provider", END)

graph.set_entry_point("user_input_handler")

# Compile the graph to an app
app = graph.compile()

if __name__ == "__main__":
	test_set=["First semester each of subjects credits i need to know "]


#"I have C pass for differential equations and B pass for Computer Science then how my results affect to industry ? Also need to know for that results how for the next semesters can affect"
	for i in range(len(test_set)):
		result = app.invoke({"user_input": test_set[i] }, {"recursion_limit": 20})
		print("\n\n\n***********Finally after finishing all the sates the final result be like :************\n\n",result,"\n\n\n*********************************")


