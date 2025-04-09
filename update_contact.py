import showcontactinfo

def UpdateData(contacts):
    name = input("수정할 이름을 입력하세요: ").strip()
    matches = [i for i, contact in enumerate(contacts) if contact["name"].lower() == name.lower()]
    #잘못입력한(없는) 경우
    if not matches:
        print(f"'{name}'의 정보를 찾을 수 없습니다.")
        return contacts

    #일치하는 연락처 목록 출력
    print("\n일치하는 연락처:")
    for idx, match in enumerate(matches):
        print(f"{idx + 1}. 이름: {contacts[match]['name']}, 전화번호: {contacts[match]['number']}")

    #수정할 연락처 선택 후 수정
    while True:
        try:
            choice = int(input("수정할 연락처 번호를 선택하세요 (예: 1): ")) - 1
            if 0 <= choice < len(matches):
                break
            else:
                print("잘못된 선택입니다. 다시 시도하세요.")
        except ValueError:
            print("숫자를 입력하세요.")

    selected_contact = contacts[matches[choice]]

    #새로운 전화번호 입력
    new_number = input(f"새로운 전화번호를 입력하세요 (현재: {selected_contact['number']}): ").strip()
    if not new_number:
        print("전화번호가 변경되지 않았습니다.")
        return contacts

    #수정
    selected_contact["number"] = new_number
    print(f"'{selected_contact['name']}'님의 전화번호가 '{new_number}'로 변경되었습니다.")

    return contacts