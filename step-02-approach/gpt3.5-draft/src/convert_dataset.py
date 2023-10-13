import json

# Đọc file JSON ban đầu
with open('/Users/nghiempt/Corporation/scientific_research/paper_policy/step-02-approach/gpt3.5-draft/assets/resources/dataset_manual_200.json', 'r') as input_file:
    data = json.load(input_file)

# Tạo một danh sách mới để lưu trữ các dữ liệu được chuyển đổi
new_data = []

# Lặp qua mỗi cặp pair trong data ban đầu
for pair in data:
    prompt = pair["prompt"]
    completion = pair["completion"]

    # Tạo một dict mới theo định dạng mong muốn
    new_entry = {
        "messages": [
            {
                "role": "system",
                "content": "Boss system"
            },
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": completion
            }
        ]
    }

    # Thêm new_entry vào danh sách mới
    new_data.append(new_entry)

# Ghi danh sách mới vào file JSON mới
with open('output.json', 'w') as output_file:
    json.dump(new_data, output_file, indent=4)

print("File JSON mới đã được tạo.")
