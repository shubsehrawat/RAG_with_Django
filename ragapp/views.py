from django.shortcuts import render, redirect
from collections import deque
from .rag_pipeline import get_rag_response

# In-memory chat history (last 5 only)
chat_history = deque(maxlen=5)

def chat_view(request):
    global chat_history

    if request.method == "POST":

        # Clear chat
        if request.POST.get("clear") == "true":
            chat_history.clear()
            return redirect("/")

        # Normal question
        user_input = request.POST.get("query")
        if user_input:
            result = get_rag_response(user_input)

            chat_history.append({
                "question": user_input,
                "answer": result["answer"],
                "sources": result["sources"]
            })

        # Post-Redirect-Get
        return redirect("/")

    return render(request, "ragapp/chat.html", {
        "chat_history": list(chat_history)
    })
