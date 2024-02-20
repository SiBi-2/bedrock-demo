from utils.bedrock_helper import Bedrock
from utils.print_helper import PrintHelper
### ENUMS ###
import utils.enums as enums

### Logging ###
import logging as log
from utils.logger_config import LoggerConfig
logger_config = LoggerConfig()
logger_config.setup_logging()


def main():
    message = "Starting bedrock.py"
    pt = PrintHelper()
    pt.clear_screen()
    pt.print_and_log(message)

    bedrock = Bedrock()
    prompt = "Write a paragraph about Steve Jobs and his impact on the world."
    image_prompt = "A beautiful sunset over the ocean, with a sailboat in the distance."

    try:
        # Titan Text Model
        model_titan = enums.BedrockModels.TITAN_TEXT_G1_LITE.value
        parms_titan = bedrock.create_parms_titan_text(prompt, model_titan)
        response = bedrock.execute_titan(model_titan, parms_titan)
        pt.print_pretty(model_titan, response, prompt)

        # #Meta LLAMA2 Model
        # model_meta = enums.BedrockModels.LLAMA2_CHAT_13B.value
        # parms_meta = bedrock.create_parms_meta(prompt)
        # response = bedrock.execute(model_meta, parms_meta)
        # pt.print_pretty(model_meta, response, prompt)

        # #AI21 J2 Model
        # model_j2 = enums.BedrockModels.J2_MID.value
        # parms_j2 = bedrock.create_parms_ai21(prompt)
        # response = bedrock.execute(model_j2, parms_j2)
        # pt.print_pretty(model_j2, response, prompt)

        # #Cohere Model
        # model_cohere = enums.BedrockModels.COHERE_COMMAND_LIGHT_TEXT_14.value
        # parms_cohere = bedrock.create_parms_cohere(prompt)
        # response = bedrock.execute(model_cohere, parms_cohere)
        # pt.print_pretty(model_cohere, response, prompt)

        # #Anthropic CLAUDE2 Model
        # model_claude = enums.BedrockModels.CLAUDE2.value
        # parms_claude = bedrock.create_parms_claude(prompt)
        # response = bedrock.execute(model_claude, parms_claude)
        # pt.print_pretty(model_claude, response, prompt)

        # #Stable Diffusion XL Model
        # model_stability = enums.BedrockModels.STABILITY_XL_1.value
        # parms_stability = bedrock.create_parms_stability_ai(image_prompt, enums.StylePreset.CINEMATIC.value)
        # response = bedrock.execute(model_stability, parms_stability)
        # image_path = bedrock.save_image(response)
        # pt.print_pretty(model_stability, f"The generated image has been saved to {image_path}", image_prompt)
        
        # #Amazon TITAN EMBEDDING Model - <<needed for vector embeddings>>
        # model_titan_embedding = enums.BedrockModels.TITAN_EMBEDDING.value
        # parms_titan_embedding = bedrock.create_parms_titan_embedding(prompt, model_titan_embedding)
        # response = bedrock.execute_titan(model_titan_embedding, parms_titan_embedding)
        # pt.print_pretty(model_titan_embedding, str(response), prompt, False, True)

        
    except Exception as e:
        log.error(f"Error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()