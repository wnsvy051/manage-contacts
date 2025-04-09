import showcontactinfo

def DeleteData(contacts):
    name = input("삭제할 이름을 입력하세요: ").strip()
    matches = [i for i, number in enumerate(contacts) if number["name"] == name]
    #삭제할 이름이 없는 경우
    if not matches:
        print("삭제할 이름이 없습니다.")
        return contacts
    #삭제할 이름이 1개뿐인 경우
    elif len(matches) == 1:
        del contacts[matches[0]]
        print("삭제가 완료되었습니다.")
        return contacts
    #삭제할 이름이 여러 개(중복)인 경우
    else :
        print("삭제할 이름을 선택하세요.")
        for idx, match in enumerate(matches):
            print(f"{idx + 1}. ")
            showcontactinfo.PrintContactInfo(contacts[match]) #중복된 이름들 데이터 출력

        while True:
            try:
                choice = int(input("번호 입력: ")) - 1
                if 0 <= choice < len(matches):
                    break
                else:
                    print("잘못된 선택입니다. 다시 시도하세요.")
            except ValueError:
                print("숫자를 입력하세요.")
        #데이터 삭제
        
        del contacts[matches[choice]]
        print("삭제가 완료되었습니다.")
        
    return contacts