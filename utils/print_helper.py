import os
import sys
import time
import re
from rich.markdown import Markdown
from rich.console import Console

### Logging ###
import logging as log


class PrintHelper:
    def __init__(self):
        log.info(f"CLASS:PrintHelper initialized")


    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def print_and_log(self, message):
        log.info(message)
        print(message)


    def print_markdown(self, text):
        console = Console()
        markdown = Markdown(text)
        console.print(markdown)


    def print_pretty(self, model_name, text, prompt, clear_screen=False, isEmbedding=False):
        if clear_screen:
            self.clear_screen()

        print("-" * 67)
        print("Model: ", model_name)
        print("-" * 67)
        print("Question: ", prompt)
        print("-" * 67)
        md = self.contains_markdown(text, 1)
        if md==True:
            log.info(f"Displaying response from {model_name} in markdown format.")
            self.print_markdown(text)
        elif isEmbedding:
            log.info(f"Displaying response from {model_name} in streaming text format.")
            print(text)
        else:
            log.info(f"Displaying response from {model_name} in streaming text format.")
            self.print_words_by_speed(text, 0.05) # lower number is faster

        print("\n")    
        print("-" * 67)


    def print_words_by_speed(self,text, speed):
        words = text.split()

        for word in words:
            sys.stdout.write(word + ' ')
            sys.stdout.flush()
            time.sleep(speed)
            
            if word.endswith('.') or word.endswith("\n") or word.endswith(":"):
                print("\n")


    def contains_markdown(self, text, threshold=2):
        patterns = [
            r"\#[^#]",  # Headers
            r"\[.*?\]\(.*?\)",  # Links
            r"\*\w+?\*|_\w+?_",  # Emphasis
            r"(\-\s|\*\s|\+\s|\d\.\s)",  # Lists
            r"```.*?```|`.*?`",  # Code blocks and inline code
            r"\>.*",  # Blockquotes
            r"!\[.*?\]\(.*?\)"  # Images
        ]

        elements_found = sum(bool(re.search(pattern, text)) for pattern in patterns)

        if elements_found >= threshold:
            return True
        else:
            return False