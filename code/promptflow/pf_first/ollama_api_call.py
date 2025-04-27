
from promptflow import tool
from ollama import chat
from ollama import ChatResponse

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(input1: str) -> str:
    response: ChatResponse = chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': input1,
    },
    ])
    # print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
    return response.message.content
