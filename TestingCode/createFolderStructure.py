import os

def create_folder_and_readme(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")
    
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write(f"# {os.path.basename(path)}\n\nThis folder contains information about {os.path.basename(path)} in the context of Generative AI.")
        print(f"Created README.md in: {path}")
    else:
        print(f"README.md already exists in: {path}")

def create_genai_folder_structure():
    structure = {
        "Text Generation": [
            "Language Models", "Transformers", "GPT Architecture", 
            "BERT and Variants", "Text-to-Text Models"
        ],
        "Image Generation": [
            "GANs", "VAEs", "Diffusion Models", 
            "StyleGAN", "DALL-E", "Stable Diffusion"
        ],
        "Audio Generation": [
            "WaveNet", "Tacotron", "Jukebox",
            "Text-to-Speech", "Music Generation"
        ],
        "Video Generation": [
            "Video Prediction", "Text-to-Video Models",
            "Motion Transfer", "Video Inpainting"
        ],
        "Multimodal Generation": {
            "Text-to-Image": ["DALL-E", "Midjourney", "Stable Diffusion"],
            "Text-to-Audio": ["AudioLM", "MusicLM"],
            "Text-to-Video": ["Make-A-Video", "Phenaki"]
        },
        "Generative AI Ethics": [
            "Bias and Fairness", "Privacy Concerns",
            "Copyright Issues", "Deepfakes and Misinformation"
        ]
    }

    for category, items in structure.items():
        create_folder_and_readme(category)
        
        if isinstance(items, list):
            for item in items:
                create_folder_and_readme(os.path.join(category, item))
        elif isinstance(items, dict):
            for subcategory, subitems in items.items():
                subcategory_path = os.path.join(category, subcategory)
                create_folder_and_readme(subcategory_path)
                for subitem in subitems:
                    create_folder_and_readme(os.path.join(subcategory_path, subitem))

    print("Generative AI folder structure creation and README.md file addition completed!")

if __name__ == "__main__":
    create_genai_folder_structure()