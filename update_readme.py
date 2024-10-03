import openai
import os


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)


client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)


def get_openai_response(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4o-mini",
    )

    return chat_completion.choices[0].message.content


def update_readme():
    code_file_path = 'triangle.py'
    readme_file_path = 'README.md'

    code_content = read_file(code_file_path)
    readme_content = read_file(readme_file_path)

    # Updated prompt to ensure correct formatting
    prompt = f"""
    Based on the following Python code, please update the README documentation accordingly.
    Make sure to use proper Markdown syntax with sections, code blocks, and clear formatting.
    If a function is removed, please also remove it when you are updating the README.

    **Example Format**:
    # Title
    Description of the code.

    ## Usage
    Instructions on how to use the code.

    ## Functions
    ### `function_name()`
    Description of the function.

    Code:
    ```python
    {code_content}
    ```

    Existing README:
    {readme_content}

    Please return the updated README documentation with correct Markdown syntax.
    """

    updated_readme_content = get_openai_response(prompt)

    print(updated_readme_content)

    # Write the new README content back to README.md
    write_file(readme_file_path, updated_readme_content)


if __name__ == '__main__':
    update_readme()
