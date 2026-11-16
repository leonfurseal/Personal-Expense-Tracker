
def add_expense(expenses):
    print("\n===== 新增消費 =====")

    date = input("日期（例如 2026-11-16）：")
    category = input("消費分類：")
    item = input("消費項目：")

    try:
        amount = float(input("消費金額："))
        if amount <= 0:
            print("金額必須大於 0！")
            return
    except ValueError:
        print("請輸入有效的數字！")
        return

    expense = {
        "date": date,
        "category": category,
        "item": item,
        "amount": amount
    }

    expenses.append(expense)
    print("新增成功！")


def show_expenses(expenses):
    print("\n===== 所有消費紀錄 =====")

    if not expenses:
        print("目前沒有消費紀錄。")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['date']} | "
            f"{expense['category']} | "
            f"{expense['item']} | "
            f"${expense['amount']:.2f}"
        )


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\n總消費金額：${total:.2f}")


def show_category_report(expenses):
    print("\n===== 分類統計 =====")

    if not expenses:
        print("目前沒有消費紀錄。")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    for category, total in category_totals.items():
        print(f"{category}：${total:.2f}")


def search_expense(expenses):
    keyword = input("請輸入要搜尋的項目或分類：")

    found = False

    for i, expense in enumerate(expenses, start=1):
        if (keyword in expense["item"]
                or keyword in expense["category"]):
            print(
                f"{i}. {expense['date']} | "
                f"{expense['category']} | "
                f"{expense['item']} | "
                f"${expense['amount']:.2f}"
            )
            found = True

    if not found:
        print("找不到符合的紀錄。")


def update_expense(expenses):
    show_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("請輸入要修改的紀錄編號："))

        if number < 1 or number > len(expenses):
            print("編號不存在！")
            return

        expense = expenses[number - 1]

        expense["date"] = input("新的日期：")
        expense["category"] = input("新的分類：")
        expense["item"] = input("新的項目：")

        amount = float(input("新的金額："))

        if amount <= 0:
            print("金額必須大於 0！")
            return

        expense["amount"] = amount

        print("修改成功！")

    except ValueError:
        print("輸入格式錯誤！")


def delete_expense(expenses):
    show_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("請輸入要刪除的紀錄編號："))

        if number < 1 or number > len(expenses):
            print("編號不存在！")
            return

        deleted = expenses.pop(number - 1)
        print(f"已刪除：{deleted['item']}")

    except ValueError:
        print("請輸入有效的編號！")


def main():
    expenses = []

    while True:
        print("\n========== 個人記帳系統 ==========")
        print("1. 新增消費紀錄")
        print("2. 查看所有消費紀錄")
        print("3. 查看總消費金額")
        print("4. 查看分類統計")
        print("5. 搜尋消費紀錄")
        print("6. 修改消費紀錄")
        print("7. 刪除消費紀錄")
        print("8. 離開系統")

        choice = input("請選擇功能：")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            show_category_report(expenses)
        elif choice == "5":
            search_expense(expenses)
        elif choice == "6":
            update_expense(expenses)
        elif choice == "7":
            delete_expense(expenses)
        elif choice == "8":
            print("感謝使用個人記帳系統！")
            break
        else:
            print("請輸入 1～8 之間的選項！")


if __name__ == "__main__":
    main()
