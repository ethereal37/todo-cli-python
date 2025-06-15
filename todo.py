# 设置文件名
FILENAME = "todo.txt"

# 初始化任务列表 
task=[]

# 从文件加载任务
def load_task():
    try:
        with open(FILENAME, "r",encoding="utf-8") as file:
            for line in file:
                task.append(line.strip())
        print("喵(●'◡'●)，加载任务成功！😺")
    except FileNotFoundError:
        print("喵(┬┬﹏┬┬)，没有找到任务文件，开始新的任务列表！😿")

# 将任务保存到文件
def save_task():
    with open(FILENAME, "w",encoding="utf-8") as file:
        for t1 in task:
            file.write(t1 + "\n")
    print("喵(●'◡'●)，任务已经保存喵！😺")

def show_meum():
    print("\n 喵ヾ(≧▽≦*)o请选择操作:")
    print("1.添加任务")
    print("2.删除任务")
    print("3.查看任务")
    print("4.退出程序")

def add_task():
    task_name = input("请输入任务名称:")
    task.append(task_name)
    print("喵(●'◡'●)，添加任务成功！😺")

def delete_task():
    if not task:
        print("喵(┬┬﹏┬┬)，当前没有任务，无法删除！😿")
    else:
        task_del = input("请输入要删除的任务:")
        for i, t in enumerate(task, 1):
            if i <= int(task_del) <= len(task):
                del task[int(task_del)-1]
                print("喵(●'◡'●)，删除任务成功！😺")

def view_task():
    if not task:
        print("喵(┬┬﹏┬┬)，当前没有任务！😿")
    else:
        print("喵(●'◡'●)，当前任务列表:")
        for i, t in enumerate(task,1):
            print(f"{i}. {t}")


load_task()

while True:
    show_meum()
    choice = input("输入你的选择:")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
        delete_task()
    elif choice == "3":
        view_task()
    elif choice == "4":
        save_task()
        print("喵(┬┬﹏┬┬)，俺走了！再见喵！😸")
        break
    else:
        print("没有这个选项，请重新输入喵！😾")