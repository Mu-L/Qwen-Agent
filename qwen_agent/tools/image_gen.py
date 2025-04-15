import json
import urllib.parse
from typing import Union

from qwen_agent.tools.base import BaseTool, register_tool


@register_tool('image_gen')
class ImageGen(BaseTool):
    description = 'An image generation service that takes text descriptions as input and returns a URL of the image. (The generated image URL should be described in markdown format in the reply to display the image: ![](URL_of_the_image))'
    parameters = [{
        'name':
            'prompt',
        'type':
            'string',
        'description':
            'Detailed description of the desired content of the generated image, such as details of characters, environment, actions, etc., in English.',
        'required':
            True
    }]

    def call(self, params: Union[str, dict], **kwargs) -> str:
        params = self._verify_json_format_args(params)

        prompt = params['prompt']
        prompt = urllib.parse.quote(prompt)
        return json.dumps({'image_url': f'https://image.pollinations.ai/prompt/{prompt}'}, ensure_ascii=False)
