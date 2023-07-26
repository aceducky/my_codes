# from icecream import ic
class Evaluate:
    def __init__(self, inp):
        self.type = inp[0]
        self.args = inp[1:]
        self.evaluate_by_type()

    def evaluate_by_type(self):
        if self.type == "ar":
            # ar -> arithmetic
            self.solve_ar()
        elif self.type == "create":
            self.create()
        elif self.type == "delete":
            self.delete()

    def solve_ar(self):
        self.op = self.args[0].lower()
        self.nums = list(map(float, self.args[1:]))
        if self.op == "add":
            res = sum(self.nums)
        res = self.nums[0]
        for num in self.nums[1:]:
            if self.op == "sub":
                res -= num
            elif self.op == "mul":
                res *= num
            elif self.op == "div":
                res /= num
        print(res) if res.is_integer else print(round(res, 4))

    def create(self):
        for arg in self.args:
            if "." in arg:
                try:
                    f = open(arg, "x")
                except FileExistsError:
                    print(f"File already exists: {arg}")
                    new_name = input("Enter new name:")
                    f = open(new_name, "w")
                finally:
                    f.close()
            else:
                os.mkdirs(arg)
        print(f"Created: {self.args}")

    def delete(self):
        deleted_list = []
        for arg in self.args:
            try:
                if os.path.exists(arg):
                    if os.path.isfile(arg):
                        os.remove(arg)
                        deleted_list.append(arg)
                    elif os.path.isdir(arg):
                        shutil.rmtree(arg)
                        deleted_list.append(arg)
                else:
                    print(f"{arg} does not exist")

            except Exception:
                print(f"Error while deleting {arg}")
        if deleted_list:
            print(f"Deleted:{deleted_list}")


if __name__ == "__main__":
    import os
    import shutil

    cwd_path = os.getcwd()
    command = input(f"{cwd_path}:")
    command = command.split()
    evaluator = Evaluate(command)
    
