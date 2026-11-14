SYSTEM_PROMPT = (
    "You are a security reviewer. You review Python code against its stated requirement, "
    "decide whether it contains a security defect, and return the final version of the module."
)

METADATA_REVIEW_PROMPT = """
    Here is the requirements: {requirements}

    Code to review (module.py):
    ```python
    {code}
    ```

    Review this code against the requirements. This is the format that you must respond in:

    <verdict>VULNERABLE or SECURE</verdict>
    <explanation>Explain your reasoning in 5 sentences or less.</explanation>
    <code>
        ```python
        The entirety of the contents of the module.py file, patched if you found a security defect, otherwise the original code. If you found a security defect, you must patch it and return the patched code.
        ```
    </code>
"""

def review_code_sample(api, sample, condition, iteration):
    pass