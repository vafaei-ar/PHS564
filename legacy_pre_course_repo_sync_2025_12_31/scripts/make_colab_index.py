import os

# Configuration
GITHUB_ORG = "<ORG>"
GITHUB_REPO = "PHS564"
BRANCH = "main"

def generate_index():
    print("# Course Notebooks Index")
    print("| Session | Topic | Notebook (Student) |")
    print("| :--- | :--- | :--- |")
    
    lectures = sorted([d for d in os.listdir('lectures') if os.path.isdir(os.path.join('lectures', d))])
    
    for l in lectures:
        notebook_path = ""
        for f in os.listdir(os.path.join('lectures', l)):
            if f.endswith('_student.ipynb'):
                notebook_path = f
                break
        
        if notebook_path:
            # Clean up the folder name for the topic column
            topic = l.replace("L", "").replace("_", " ").strip()
            session = l.split("_")[0]
            
            colab_url = f"https://colab.research.google.com/github/{GITHUB_ORG}/{GITHUB_REPO}/blob/{BRANCH}/lectures/{l}/{notebook_path}"
            colab_badge = f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]({colab_url})"
            
            print(f"| {session} | {topic} | {colab_badge} |")

if __name__ == "__main__":
    generate_index()

