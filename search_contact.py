import showcontactinfo

def SearchData(contacts):
    search = input("검색할 이름 또는 전화번호를 입력하세요: ").strip().lower()
    #리스트 컴프리헨션 기능 이용, .lower()로 대소문자 구분 X
    results = [contact for contact in contacts if search in contact["name"].lower() or search in contact["number"]]

    #결과 출력
    if results:
        print("\n검색 결과:")
        for idx, contact in enumerate(results, start=1):
            print(f"{idx}. 이름: {contact['name']}, 전화번호: {contact['number']}")
    else:
        print("검색 결과가 없습니다.")

    return contacts
