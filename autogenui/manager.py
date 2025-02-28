# a manager class that can
# load an autogen flow run an autogen flow and return the response to the client


from typing import Dict
import autogen
from .utils import parse_token_usage
import os,time

api_keys = [os.environ.get("OPENAI_API_KEY")]
base_urls = [os.environ.get("OPENAI_API_BASE") or None] # You can specify API base URLs if needed. eg: localhost:8000
api_type = "openai"  # Type of API, e.g., "openai" or "aoai".
api_version = ""  # Specify API version if needed.


config_list = autogen.get_config_list(
    api_keys,
    api_bases=base_urls,
    api_type=api_type,
    api_version=api_version
)


class Manager(object):
    def __init__(self) -> None:

        pass

    def run_flow(self, prompt: str, flow: str = "default") -> None:
        autogen.ChatCompletion.start_logging(compact=False)

        #config_list = autogen.config_list_openai_aoai()

        llm_config = {
            "timeout": 180,
            "seed": 42,  # seed for caching and reproducibility
            "config_list": config_list,  # a list of OpenAI API configurations
            "temperature": 0,  # temperature for sampling
            "use_cache": True,  # whether to use cache
        }

        assistant = autogen.AssistantAgent(
            name="assistant",
            max_consecutive_auto_reply=3, llm_config=llm_config,)

        # create a UserProxyAgent instance named "user_proxy"
        user_proxy = autogen.UserProxyAgent(
            name="user_proxy",
            human_input_mode="NEVER",
            llm_config=llm_config,
            max_consecutive_auto_reply=3,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                "work_dir": "scratch/coding",
                #"use_docker": False
                "use_docker":"ubuntu-python-runtime:3.10"  # python:3.10
            },
        )
        start_time = time.time()
        user_proxy.initiate_chat(
            assistant,
            message=prompt,
        )

        messages = user_proxy.chat_messages[assistant]
        logged_history = autogen.ChatCompletion.logged_history
        autogen.ChatCompletion.stop_logging()
        response = {
            "messages": messages[1:],
            "usage": parse_token_usage(logged_history),
            "duration": time.time() - start_time,
        }
        return response
