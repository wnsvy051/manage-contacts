def InputData(contacts):
    name = input("이름 입력: ")
    number = input("전화번호 입력: ")
    
    #입력된 정보의 이름과 번호가 이미 입력된 경우 검사 및 원래 화면으로 돌아가기
    for contact in contacts:
        if contact["name"] == name and contact["number"] == number:            
            print("이미 입력된 정보입니다.")
            return contacts
    
    #입력된 정보 확인
    contacts.append({"name": name, "number": number})
    print("\n연락처가 추가되었습니다.\n")
    print(f"이름: {name}\n전화번호: {number}\n")
    #print(contacts)
    return contacts