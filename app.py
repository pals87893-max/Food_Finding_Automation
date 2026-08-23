from flask import Flask,render_template,request,jsonify
from automation_function import recipie,Recipe
from urllib.parse import quote

def add_youtube_link(recipe: Recipe) -> dict:
    data = recipe.model_dump()
    query = quote(f"{recipe.recipe_name} recipe")
    data["youtube_search_url"] = f"https://www.youtube.com/results?search_query={query}"
    return data

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        prompt=request.form['ingredients']
        if not prompt:
            return jsonify({"reply": "Please enter some ingredients"}), 400
        try:
            result=recipie(prompt)
            result_with_link= add_youtube_link(result)
            return jsonify({
                "status":"ok",
                "recipe": result_with_link
                })
        except:
            return jsonify({"reply": "recipe not found"}), 400
    
    return render_template('index.html')

from urllib.parse import quote




if __name__=="__main__":
    app.run(debug= True)