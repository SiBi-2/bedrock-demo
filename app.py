import os
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
    prompt = "Write a paragraph about Steve Jobs success and failures, and the impact of his work on the world."
    image_prompt = "A beautiful sunset over the ocean, with a sailboat in the distance."
    response = ""
    try:
        #Meta LLAMA2 Model
        # parms_meta = bedrock.create_parms_meta(prompt)
        # response = bedrock.execute(enums.BedrockModels.LLAMA2_CHAT_13B.value, parms_meta)
        # completion = response["generation"]
        # print_pretty(enums.BedrockModels.LLAMA2_CHAT_13B.value, completion)

        # #AI21 J2 Model
        # parms_ai21 = bedrock.create_parms_ai21(prompt)
        # response = bedrock.execute(enums.BedrockModels.J2_MID.value, parms_ai21)
        # completion = response["completions"][0]["data"]["text"]
        # print_pretty(enums.BedrockModels.J2_MID.value, completion)

        # #Anthropic CLAUDE2 Model
        # parms_claude = bedrock.create_parms_claude(prompt)
        # response = bedrock.execute(enums.BedrockModels.CLAUDE2.value, parms_claude)
        # completion = response["completion"]
        # print_pretty(enums.BedrockModels.CLAUDE2.value, completion)

        # #Amazon TITAN EMBEDDING Model
        # parms_titan_emb = bedrock.create_parms_titan_embedding(prompt, enums.BedrockModels.TITAN_EMBEDDING.value)
        # response = bedrock.execute_embeddings(parms_titan_emb)
        # embeddings = response.get('embedding')
        # print_pretty(enums.BedrockModels.TITAN_EMBEDDING.value, embeddings)

        # #Stable Diffusion XL Model
        parms_stability = bedrock.create_parms_stability_ai(image_prompt, enums.StylePreset.CINEMATIC.value)
        response = bedrock.execute(enums.BedrockModels.STABILITY_XL_1.value, parms_stability)
        base64_image_data = response["artifacts"][0]["base64"]
        image_path = bedrock.save_image(base64_image_data)
        print(f"The generated image has been saved to {image_path}")


    except Exception as e:
        log.error(f"Error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()