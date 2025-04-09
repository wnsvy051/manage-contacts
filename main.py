import create_contact
import delete_contact
import search_contact
import update_contact

def main():
    contacts = []
    choice = 0

    while choice!=5:
        print("---------------------------------------------------------------\n")
        print("1. 연락처 추가    2. 연락처 삭제    3. 연락처 검색    4. 연락처 수정    5. 종료\n")
        print("---------------------------------------------------------------\n")
        choice = input("선택 : ")
        if choice == "1":
            contacts = create_contact.InputData(contacts)
        elif choice == "2":
            contacts = delete_contact.DeleteData(contacts)
        elif choice == "3":
            contacts = search_contact.SearchData(contacts)
        elif choice == "4":
            contacts = update_contact.UpdateData(contacts)
        elif choice == "5":
            break
        else : print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()