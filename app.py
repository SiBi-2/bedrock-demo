import os
import sys
import base64  
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

def main():
    message = "Starting bedrock.py"
    log.info(message)
    print(message)

    bedrock = br.bedrock()
    prompt = "Write a paragraph about Steve Jobs and his impact on the world."
    image_prompt = "A beautiful sunset over the ocean, with a sailboat in the distance."
    response = ""
    try:
        # #Meta LLAMA2 Model
        # model_meta = enums.BedrockModels.LLAMA2_CHAT_13B.value
        # parms_meta = bedrock.create_parms_meta(prompt)
        # response = bedrock.execute(model_meta, parms_meta)
        # print_pretty(model_meta, response)

        # Titan Text Lite Model
        model_titan = enums.BedrockModels.TITAN_TEXT_G1_LITE.value
        parms_titan = bedrock.create_parms_titan_text(prompt, model_titan)
        response = bedrock.execute_titan(parms_titan)
        print_pretty(model_titan, response)

        # #AI21 J2 Model
        # model_j2 = enums.BedrockModels.J2_MID.value
        # parms_j2 = bedrock.create_parms_ai21(prompt)
        # response = bedrock.execute(model_j2, parms_j2)
        # print_pretty(model_j2, response)

        # #Anthropic CLAUDE2 Model
        # model_claude = enums.BedrockModels.CLAUDE2.value
        # parms_claude = bedrock.create_parms_claude(prompt)
        # response = bedrock.execute(model_claude, parms_claude)
        # print_pretty(model_claude, response)

        # #Stable Diffusion XL Model
        # model_stability = enums.BedrockModels.STABILITY_XL_1.value
        # parms_stability = bedrock.create_parms_stability_ai(image_prompt, enums.StylePreset.CINEMATIC.value)
        # response = bedrock.execute(model_stability, parms_stability)
        # image_path = bedrock.save_image(response)
        # print(f"The generated image has been saved to {image_path}")
        
        # #Amazon TITAN EMBEDDING Model - <<needed for vector embeddings>>
        # model_titan_embedding = enums.BedrockModels.TITAN_EMBEDDING.value
        # parms_titan_embedding = bedrock.create_parms_titan_embedding(prompt, model_titan_embedding)
        # response = bedrock.execute_titan(parms_titan_embedding)
        # print_pretty(model_titan_embedding, response)

        
    except Exception as e:
        log.error(f"Error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()