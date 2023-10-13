import openai
openai.api_key = "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"

model_name = "text-davinci-002"
prompt = "Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent.\n\nNotes when classifying:\n+ Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides.\n+ Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it.\n+ Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided.\n\nNote: always gives me the result (0 or 1) in the form below:\nIncomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)\n\nBelow is information for 2 parts:\n1. Data Safety - Share section: No data shared with third parties;\n2. Privacy Policy - Share section: The sharing information section from the given content is:\nWho we share your data with\nSuggested text: If you request a password reset, your IP address will be included in the reset email."

completion = openai.Completion.create(
    model=model_name,
    prompt=prompt,
    n=1,
    stop=None,
    temperature=1.0,
    max_tokens=150
)

generated_text = completion.choices[0].text
print(generated_text)
