import sys
import datetime
### Local Imports ###
from utils.parms import ModelParams as parms
from utils.bedrock_helper import Bedrock
from utils.print_helper import PrintHelper
### ENUMS ###
import utils.enums as enums
### Logging ###
import logging as log
from utils.logger_config import LoggerConfig
logger_config = LoggerConfig()
logger_config.setup_logging()

bedrock = Bedrock()
pr = PrintHelper()

def select_model():
    pr.clear_screen()
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
                pr.clear_screen()
                sys.exit(0)
            model_name = model_names[model_choice]
            print("-" * 67)
            pr.print_and_log(f"Model {model_name} selected.")
            print("-" * 67)
            return model_choice, model_name
        else:
            pr.print_and_log("Invalid selection. Please enter a valid number.")

def process_model_choice(model_name, prompt):
    log.info(f"Model: {model_name}")
    model_parms = None

    if model_name == enums.BedrockModels.LLAMA2_CHAT_13B.value:
        model_parms = bedrock.create_parms_meta(prompt)
    elif model_name == enums.BedrockModels.J2_MID.value:
        model_parms = bedrock.create_parms_ai21(prompt)
    elif model_name == enums.BedrockModels.CLAUDE2.value:
        model_parms = bedrock.create_parms_claude(prompt)
    elif model_name == enums.BedrockModels.COHERE_COMMAND_LIGHT_TEXT_14.value:
        model_parms = bedrock.create_parms_cohere(prompt)
    else:
        pr.print_and_log("Invalid model choice.")
        return
    response = bedrock.execute(model_name, model_parms)
    pr.print_pretty(model_name, response, prompt, True)

def main():
    current_time = datetime.datetime.now()
    pr.print_and_log(f"Starting MAIN: {current_time}")

    model_choice, model_name = select_model()
    input_prompt = "(or type 'exit' to quit, 'model' to switch models):\n"

    while True:
        if model_choice == '6':
            question =input(f"Create an Image: {input_prompt}")
        else:
            question = input(f"Ask your question: {input_prompt}")

        if question.lower() == 'exit':
            pr.print_and_log("Exiting...")
            break
        elif question.lower() == 'model' or question.lower() == 'models' or question.lower() == 'clear':
            model_choice, model_name = select_model()
        else:
            try:
                prompt = question

                # Titan Text Model
                if model_choice == '1':
                    model_titan = enums.BedrockModels.TITAN_TEXT_G1_LITE.value
                    parms_titan = bedrock.create_parms_titan_text(prompt, model_titan)
                    response = bedrock.execute_titan(model_titan, parms_titan)
                    pr.clear_screen()
                    pr.print_pretty(model_titan, response, prompt, True)

                #Meta LLAMA2 Model
                elif model_choice == '2':    
                    process_model_choice(enums.BedrockModels.LLAMA2_CHAT_13B.value, prompt)
                
                #AI21 J2 Model
                elif model_choice == '3': 
                    process_model_choice(enums.BedrockModels.J2_MID.value, prompt)

                #Cohere Model
                elif model_choice == '4':
                    process_model_choice(enums.BedrockModels.COHERE_COMMAND_LIGHT_TEXT_14.value, prompt)

                #Anthropic CLAUDE2 Model
                elif model_choice == '5':
                    process_model_choice(enums.BedrockModels.CLAUDE2.value, prompt)

                #Stable Diffusion XL Model
                elif model_choice == '6':
                    model_stability = enums.BedrockModels.STABILITY_XL_1.value
                    parms_stability = bedrock.create_parms_stability_ai(prompt, enums.StylePreset.CINEMATIC.value)
                    response = bedrock.execute(model_stability, parms_stability)
                    image_path = bedrock.save_image(response)
                    pr.clear_screen()
                    pr.print_pretty(model_stability, f"The generated image has been saved to {image_path}", prompt, True)

                else:
                    print("Invalid model choice.")
                
            except Exception as e:
                log.error(f"Error: {e}")
                print(f"Error: {e}")

if __name__ == "__main__":
    main()