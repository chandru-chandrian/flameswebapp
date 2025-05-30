from django.shortcuts import render

# Create your views here.

def flames_result(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    count = len(name1 + name2)

    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index+1:] + flames[:split_index]
        else:
            flames = flames[:len(flames)-1]
    return flames[0]

def flames_view(request):
    result = ""
    if request.method == "POST":
        name1 = request.POST.get("name1")
        name2 = request.POST.get("name2")
        result = flames_result(name1, name2)
    return render(request, "flames.html", {"result": result})
