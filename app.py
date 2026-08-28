from flask import Flask,render_template,request,jsonify,url_for
from automation_function import recipie,Recipe
from urllib.parse import quote

from image_generation import recipe_image

def add_youtube_link(recipe: Recipe) -> dict:
    data = recipe.model_dump()
    query = quote(f"{recipe.recipe_name} recipe")
    data["youtube_search_url"] = f"https://www.youtube.com/results?search_query={query}"
    return data

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        prompt=request.form['ingredients']
        model=request.form['model']
        if not prompt:
            return jsonify({"reply": "Please enter some ingredients"}), 400
        try:
            result=recipie(prompt,model)
            result_with_link= add_youtube_link(result)
            recipe_image(prompt)
            image_url = url_for('static', filename='recipe_here.png')
            return jsonify({
                "status":"ok",
                "recipe": result_with_link,
                "img":image_url
                })
        except:
            return jsonify({"reply": "recipe not found"}), 400
    
    return render_template('index.html')




if __name__=="__main__":
    app.run(debug= True)
