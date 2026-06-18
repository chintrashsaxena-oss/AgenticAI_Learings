from transformers import pipeline

pipe = pipeline("image-text-to-text", model= "google/gemma-3-4b-it")

message = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/leejet/deogram-4-GGUF"}
            {
                "type": "text", "text": "What animal is on the candy"
            }
        ]
    }
]

pipe(text=message)