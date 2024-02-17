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


class bedrock:
    def __init__(self):
        log.info(f"CLASS:Bedrock Initialized")
        # credentials and config are handled by boto3 files in ~/.aws
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
            return response_body

        except ClientError:
            raise


    def execute_embeddings(self, parms_obj):
        log.info(f"Invoking Embedding with parameters: {parms_obj}")
        try:
            response = self.bedrock_client.invoke_model(
                **parms_obj.get_params()
            )

            response_body = json.loads(response["body"].read())
            log.info(f"Received response from Embedding")
            return response_body

        except ClientError:
            raise


    def create_parms_meta(self, prompt, temperature=0.5, top_p=0.9, max_gen_len=512):
        log.info(f"Creating parameters for Meta model")
        parms_obj = parms(prompt)
        parms_obj.upsert_param('temperature', temperature)
        parms_obj.upsert_param('top_p', top_p)
        parms_obj.upsert_param('max_gen_len', max_gen_len) 
        return parms_obj
    
    def create_parms_ai21(self, prompt, temperature=0.5, maxTokens=512):
        log.info(f"Creating parameters for AI21 model")
        parms_obj = parms(prompt)
        parms_obj.upsert_param('temperature', temperature)
        parms_obj.upsert_param('maxTokens', maxTokens)
        return parms_obj
    
    def create_parms_claude(self, prompt, temperature=0.5, max_tokens_to_sample=512):
        log.info(f"Creating parameters for Claude model")
        enclosed_prompt = "Human: " + prompt + "\n\nAssistant:"
        parms_obj = parms(enclosed_prompt)
        parms_obj.upsert_param('temperature', temperature)
        parms_obj.upsert_param('max_tokens_to_sample', max_tokens_to_sample)
        parms_obj.upsert_param('stop_sequences', ["\n\nHuman:"])
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

        return str(file_path)
