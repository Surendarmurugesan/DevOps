import subprocess

@app.route("/run_script", methods=["POST"])
def run_script():
    subprocess.run(["python", "your_script.py"])
    return "Script ran successfully!"
