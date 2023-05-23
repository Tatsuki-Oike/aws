import argparse

from torchvision.io import read_image
from torchvision.models import resnet50, ResNet50_Weights

def image_recognition(input_image_path):
    img = read_image(input_image_path)

    # Step 1: Initialize model with the best available weights
    weights = ResNet50_Weights.DEFAULT
    model = resnet50(weights=weights)
    model.eval()

    # Step 2: Initialize the inference transforms
    preprocess = weights.transforms()

    # Step 3: Apply inference preprocessing transforms
    batch = preprocess(img).unsqueeze(0)

    # Step 4: Use the model and print the predicted category
    prediction = model(batch).squeeze(0).softmax(0)
    class_id = prediction.argmax().item()
    score = prediction[class_id].item()
    category_name = weights.meta["categories"][class_id]

    return category_name, score

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--img', type=str, required=True)
    args = parser.parse_args()

    category_name, score = image_recognition(args.img)
    print(f"{category_name}: {100 * score:.1f}%")

if __name__ == "__main__":
    main()