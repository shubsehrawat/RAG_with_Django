from django.shortcuts import render
from .rag_pipeline import get_rag_response

def chat_view(request):
    response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.POST.get("query")
        response = get_rag_response(user_input)

    return render(request, "ragapp/chat.html", {
        "user_input": user_input,
        "response": response
    })
