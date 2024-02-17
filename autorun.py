import os
import sys
import base64  
import webbrowser
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


def select_model():
    os.system('cls' if os.name == 'nt' else 'clear')
    model_names = {
        '0': "exit",
        '1': "amazon.titan",
        '2': "meta.llama2",
        '3': "ai21.j2",
        '4': "cohere.command",
        '5': "anthropic.claude2",
        '6': "stability.stable-diffusion (IMAGE)",
    }
    while True:
        print("Select a model:")
        for number, name in model_names.items():
            print(f"{number}. {name}")
        model_choice = input("Enter the number of the model you want to use: ")
        if model_choice in model_names:
            if model_choice == '0':
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.exit(0)
            model_name = model_names[model_choice]
            print("-" * 67)
            print(f"Model {model_name} selected.")
            print("-" * 67)
            return model_choice, model_name  # Return both choice and full name
        else:
            print("Invalid selection. Please enter a valid number.")


def main():
    message = "Starting bedrock.py"
    log.info(message)
    print(message)


    bedrock = br.bedrock()
    model_choice, model_name = select_model()
    input_prompt = "(or type 'exit' to quit, 'model' to switch models):\n"
    while True:
        if model_choice == '6':
            question =input(f"Create an Image: {input_prompt}")
        else:
            question = input(f"Ask your question: {input_prompt}")
        if question.lower() == 'exit':
            print("Exiting...")
            break
        elif question.lower() == 'model':
            model_choice, model_name = select_model()
        else:
            try:
                prompt = question
                # Titan Text Model
                if model_choice == '1':
                    model_titan = enums.BedrockModels.TITAN_TEXT_G1_LITE.value
                    log.info(f"Model: {model_titan}")
                    parms_titan = bedrock.create_parms_titan_text(prompt, model_titan)
                    response = bedrock.execute_titan(model_titan, parms_titan)
                    print_pretty(model_titan, response)

                #Meta LLAMA2 Model
                elif model_choice == '2':    
                    model_meta = enums.BedrockModels.LLAMA2_CHAT_13B.value
                    log.info(f"Model: {model_meta}")
                    parms_meta = bedrock.create_parms_meta(prompt)
                    response = bedrock.execute(model_meta, parms_meta)
                    print_pretty(model_meta, response)
                

                #AI21 J2 Model
                elif model_choice == '3': 
                    model_j2 = enums.BedrockModels.J2_MID.value
                    log.info(f"Model: {model_j2}")
                    parms_j2 = bedrock.create_parms_ai21(prompt)
                    response = bedrock.execute(model_j2, parms_j2)
                    print_pretty(model_j2, response)

                #Cohere Model
                elif model_choice == '4':
                    model_cohere = enums.BedrockModels.COHERE_COMMAND_LIGHT_TEXT_14.value
                    log.info(f"Model: {model_cohere}")
                    parms_cohere = bedrock.create_parms_cohere(prompt)
                    response = bedrock.execute(model_cohere, parms_cohere)
                    print_pretty(model_cohere, response)

                #Anthropic CLAUDE2 Model
                elif model_choice == '5':
                    model_claude = enums.BedrockModels.CLAUDE2.value
                    log.info(f"Model: {model_claude}")
                    parms_claude = bedrock.create_parms_claude(prompt)
                    response = bedrock.execute(model_claude, parms_claude)
                    print_pretty(model_claude, response)

                #Stable Diffusion XL Model
                elif model_choice == '6':
                    image_prompt = question
                    model_stability = enums.BedrockModels.STABILITY_XL_1.value
                    log.info(f"Model: {model_stability}")
                    parms_stability = bedrock.create_parms_stability_ai(image_prompt, enums.StylePreset.CINEMATIC.value)
                    response = bedrock.execute(model_stability, parms_stability)
                    image_path = bedrock.save_image(response)
                    model_stability = enums.BedrockModels.STABILITY_XL_1.value
                    print_pretty(model_stability, f"The generated image has been saved to {image_path}")

                    # Open the image in the default browser
                    webbrowser.open('file://' + os.path.realpath(image_path))

                else:
                    print("Invalid model choice.")
                
            except Exception as e:
                log.error(f"Error: {e}")
                print(f"Error: {e}")

if __name__ == "__main__":
    main()