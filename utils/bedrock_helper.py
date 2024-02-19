import json
import boto3
from botocore.exceptions import ClientError
import logging as log
import sys
import random 
from pathlib import Path
import base64
import os
from utils.parms import ModelParams as parms
import webbrowser

class Bedrock:
    def __init__(self):
        log.info(f"CLASS:Bedrock Initialized")
        #######  credentials and config are handled by boto3 files in ~/.aws  #######
        try: 
            self.bedrock_client = boto3.client(service_name="bedrock-runtime")
        except Exception as e:
            log.error(f"Error in create_bedrock_client: {e}")
            print(e)
            sys.exit(1)


    def execute(self, model_name, parms_obj):
        log.info(f"Invoking model: {model_name} with parameters: {parms_obj}")
        try:
            body = { **parms_obj.get_params() }
            
            response = self.bedrock_client.invoke_model(
                modelId=model_name, body=json.dumps(body)
            )
            response_body = json.loads(response["body"].read())
            log.info(f"Received response from model: {model_name}")
            return self.get_response(model_name, response_body)

        except ClientError:
            raise


    def execute_titan(self, model_name, parms_obj):
        log.info(f"Invoking titan with parameters: {parms_obj}")
        try:
            response = self.bedrock_client.invoke_model(
                **parms_obj.get_params()
            )

            response_body = json.loads(response["body"].read())
            log.info(f"Received response from Embedding")
            return self.get_response(model_name, response_body)

        except ClientError:
            raise


    def create_parms_meta(self, prompt, temperature=0.5, top_p=0.9, max_gen_len=500):
        log.info(f"Creating parameters for Meta model")
        parms_obj = parms(prompt)
        parms_obj.upsert_param('temperature', temperature)
        parms_obj.upsert_param('top_p', top_p)
        parms_obj.upsert_param('max_gen_len', max_gen_len) 
        return parms_obj
    
    def create_parms_ai21(self, prompt, temperature=0.5, maxTokens=500):
        log.info(f"Creating parameters for AI21 model")
        parms_obj = parms(prompt)
        parms_obj.upsert_param('temperature', temperature)
        parms_obj.upsert_param('maxTokens', maxTokens)
        return parms_obj
    
    def create_parms_claude(self, prompt, temperature=0.5, max_tokens_to_sample=500):
        log.info(f"Creating parameters for Claude model")
        enclosed_prompt = "Human: " + prompt + "\n\nAssistant:"
        parms_obj = parms(enclosed_prompt)
        parms_obj.upsert_param('temperature', temperature)
        parms_obj.upsert_param('max_tokens_to_sample', max_tokens_to_sample)
        parms_obj.upsert_param('stop_sequences', ["\n\nHuman:"])
        return parms_obj
    
    def create_parms_cohere(self, prompt, temperature=0.5, max_tokens=500):
        log.info(f"Creating parameters for Cohere model")
        parms_obj = parms(prompt)
        parms_obj.upsert_param('temperature', temperature)
        parms_obj.upsert_param('max_tokens', max_tokens)
        return parms_obj

    def create_parms_titan_embedding(self, prompt, model):
        log.info(f"Creating parameters for Titan Embedding model")
        parms_obj = parms(prompt)
        parms_obj.remove_param('prompt')  # Embedding doesn't require a prompt
        parms_obj.upsert_param('modelId', model)
        parms_obj.upsert_param('body', json.dumps({"inputText": prompt}))
        parms_obj.upsert_param('accept', 'application/json')
        parms_obj.upsert_param('contentType', 'application/json')
        return parms_obj
    
    def create_parms_titan_text(self, prompt, model, temperature=0.5, maxTokenCount=500):
        log.info(f"Creating parameters for Titan Text model")
        parms_obj = parms(prompt)
        parms_obj.remove_param('prompt')  # Embedding doesn't require a prompt
        parms_obj.upsert_param('modelId', model)
        parms_obj.upsert_param('accept', 'application/json')
        parms_obj.upsert_param('contentType', 'application/json')

        body = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": maxTokenCount,
                "stopSequences": [],
                "temperature": temperature,
                "topP": 1
            }
        }

        body_json = json.dumps(body)
        parms_obj.upsert_param('body', body_json)
        return parms_obj

    
    def create_parms_stability_ai(self, prompt, style):
        log.info(f"Creating parameters for Stability AI model")
        parms_obj = parms(prompt)
        parms_obj.remove_param('prompt')  # Embedding doesn't require a prompt
        parms_obj.upsert_param('text_prompts', [{"text": prompt}])
        parms_obj.upsert_param('seed', random.randint(0, 4294967295))
        parms_obj.upsert_param('cfg_scale', 10)
        parms_obj.upsert_param('steps', 30)
        parms_obj.upsert_param('style_preset', style)
        return parms_obj

    def get_response(self, model, response):
        log.info(f"Getting response for model: {model}")
        if model == "meta.llama2-13b-chat-v1" or model == "meta.llama2-70b-chat-v1":
            return response["generation"]
        elif model == "ai21.j2-mid-v1" or model == "ai21.j2-ultra-v1":
            return response["completions"][0]["data"]["text"]
        elif model == "anthropic.claude-v2":
            return response["completion"]
        elif model == "amazon.titan-embed-text-v1":
            return response.get('embedding')
        elif model == "amazon.titan-text-lite-v1" or model == "amazon.titan-text-express-v1":
            return response['results'][0]['outputText']
        elif model == "stability.stable-diffusion-xl-v1":
            return response["artifacts"][0]["base64"]
        elif model == "cohere.command-text-v14" or model == "cohere.command-light-text-v14":
            return response["generations"][0]["text"]
        else:
            return response


    def save_image(self, base64_image_data):
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)

        i = 1
        while (output_dir / f"image_{i}.png").exists():
            i += 1

        image_data = base64.b64decode(base64_image_data)
        file_path = output_dir / f"image_{i}.png"
        
        with open(file_path, "wb") as file:
            file.write(image_data)

        webbrowser.open('file://' + os.path.realpath(file_path))
        return str(file_path)
