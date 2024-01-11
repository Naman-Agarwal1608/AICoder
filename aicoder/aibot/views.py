from django.shortcuts import render
from django.views import View
from django.contrib import messages
# Create your views here.


class Home(View):
    languages = ["markup", "css", "clike", "javascript", "arduino", "c", "csharp", "cpp", "dart", "django", "git", "go", "gradle", "haskell", "http", "java", "julia", "kotlin", "latex",
                 "markup-templating", "matlab", "mongodb", "perl", "php", "plsql", "powershell", "python", "r", "jsx", "ruby", "rust", "solidity", "sql", "swift", "typescript", "visual-basic", "yaml"]

    def get(self, request):
        return render(request, 'home.html', {'languages': sorted(self.languages)})

    def post(self, request):
        code = request.POST['code']
        lang = request.POST['lang']

        if lang == "Select Language":
            messages.warning(
                request, "You forgot to select your programming language...")

        return render(request, 'home.html', {'languages': self.languages, 'code': code, 'lang': lang})
