import os
import sys
import base64  
import time
import utils.bedrock_helper as br
from utils.parms import ModelParams as parms
### ENUMS ###
import utils.enums as enums

### Logging ###
import logging as log
from utils.logger_config import LoggerConfig
logger_config = LoggerConfig()
logger_config.setup_logging()

def print_pretty(model_name, completion):
    print("-" * 67)
    print("Model: ", model_name)
    print("-" * 67)
    print(completion)
    print("-" * 67)

def print_by_words(model_name, completion):
    print("-" * 67)
    print("Model: ", model_name)
    print("-" * 67)
    print_words_by_speed(completion, 0.06)
    print("-" * 67)

def print_words_by_speed(text, speed):
    words = text.split()
    word_count = 0
    for word in words:
        sys.stdout.write(word + ' ')
        sys.stdout.flush() 
        time.sleep(speed)  # Wait for the specified speed - lower is faster
        word_count += 1
        
        # Example condition to add a break/newline
        if word.endswith('.') or word.endswith("\n") or word.endswith(":"): # or word_count % 10 == 0
            print()  # Move to the next line
            word_count = 0  # Reset the word count for the next line


def main():
    message = "Starting bedrock.py"
    log.info(message)
    print(message)

    bedrock = br.bedrock()
    prompt = "Write a paragraph about Steve Jobs and his impact on the world."
    image_prompt = "A beautiful sunset over the ocean, with a sailboat in the distance."
    try:
        # Titan Text Model
        model_titan = enums.BedrockModels.TITAN_TEXT_G1_LITE.value
        parms_titan = bedrock.create_parms_titan_text(prompt, model_titan)
        response = bedrock.execute_titan(model_titan, parms_titan)
        print_by_words(model_titan, response)

        # #Meta LLAMA2 Model
        # model_meta = enums.BedrockModels.LLAMA2_CHAT_13B.value
        # parms_meta = bedrock.create_parms_meta(prompt)
        # response = bedrock.execute(model_meta, parms_meta)
        # print_by_words(model_meta, response)

        # #AI21 J2 Model
        # model_j2 = enums.BedrockModels.J2_MID.value
        # parms_j2 = bedrock.create_parms_ai21(prompt)
        # response = bedrock.execute(model_j2, parms_j2)
        # print_by_words(model_j2, response)

        # #Cohere Model
        # model_cohere = enums.BedrockModels.COHERE_COMMAND_LIGHT_TEXT_14.value
        # parms_cohere = bedrock.create_parms_cohere(prompt)
        # response = bedrock.execute(model_cohere, parms_cohere)
        # print_by_words(model_cohere, response)

        # #Anthropic CLAUDE2 Model
        # model_claude = enums.BedrockModels.CLAUDE2.value
        # parms_claude = bedrock.create_parms_claude(prompt)
        # response = bedrock.execute(model_claude, parms_claude)
        # print_by_words(model_claude, response)

        # #Stable Diffusion XL Model
        # model_stability = enums.BedrockModels.STABILITY_XL_1.value
        # parms_stability = bedrock.create_parms_stability_ai(image_prompt, enums.StylePreset.CINEMATIC.value)
        # response = bedrock.execute(model_stability, parms_stability)
        # image_path = bedrock.save_image(response)
        # print(f"The generated image has been saved to {image_path}")
        
        # #Amazon TITAN EMBEDDING Model - <<needed for vector embeddings>>
        # model_titan_embedding = enums.BedrockModels.TITAN_EMBEDDING.value
        # parms_titan_embedding = bedrock.create_parms_titan_embedding(prompt, model_titan_embedding)
        # response = bedrock.execute_titan(model_titan_embedding, parms_titan_embedding)
        # print_pretty(model_titan_embedding, response)

        
    except Exception as e:
        log.error(f"Error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()