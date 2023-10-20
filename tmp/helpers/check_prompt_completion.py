# import json

# json_file_path = '/Users/nghiempt/Corporation/scientific_research/paper_policy/14_09_2023/bard/bard_generate/input1.3.json'


# with open(json_file_path, 'r') as file:
#     data = json.load(file)

# for index, item in enumerate(data):
#     print("========================== " +
#           str(index) + " times ==========================")
#     print(item['prompt'])

print("Let's compare and analyze the information between Data Safety and Privacy Policy to clarify 3 issues: which information is incorrect, which information is incomplete and which information is inconsistent.\nNotes when classifying:\n+ Incomplete: Data Safety provides information but is not as complete as the Privacy Policy provides.\n+ Incorrect: Data Safety does not provide that information, but the Privacy Policy mentions it.\n+ Inconsistency: Data Safety is provided but its description is inconsistent with the Privacy Policy information provided.\nNote: always gives me the result (0 or 1) in the form below:\nIncomplete: 0 or 1 (1 is yes, 0 is no)\nIncorrect: 0 or 1 (1 is yes, 0 is no)\nInconsistency: 0 or 1 (1 is yes, 0 is no)\nBelow is information for 2 parts:\nData Safety - Share section: Location(Approximate location), App activity(App interactions), App info and performance(Diagnostics), Device or other IDs(Device or other IDs);\nPrivacy Policy - Share section: The sharing information section of the content is as follows:\nThird-party disclosure\nWe do not sell, trade, or otherwise transfer to outside parties your Personally Identifiable Information unless we provide users with advance notice. This does not include website hosting partners and other parties who assist us in operating our website, conducting our business, or serving our users, so long as those parties agree to keep this information confidential. We may also release information when it's release is appropriate to comply with the law, enforce our site policies, or protect ours or others' rights, property or safety.\nThird-party links\nOccasionally, at our discretion, we may include or offer third-party products or services on our website. These third-party sites have separate and independent privacy policies. We therefore have no responsibility or liability for the content and activities of these linked sites. Nonetheless, we seek to protect the integrity of our site and welcome any feedback about these sites.")