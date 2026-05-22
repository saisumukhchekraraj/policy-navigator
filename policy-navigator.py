import os# Required functions and classes


def replace_line_in_file(filename, line_number_to_replace, new_content):  #Function to replace any line in a file
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        index_to_replace = line_number_to_replace - 1
        if 0 <= index_to_replace < len(lines):
            if not new_content.endswith('\n') and lines[index_to_replace].endswith('\n'):
                new_content += '\n'
            lines[index_to_replace] = new_content
        else:
            print(f"Error: Line number {line_number_to_replace} is out of range.")
            return

        with open(filename, 'w') as file:
            file.writelines(lines)
        print(f"Line {line_number_to_replace} replaced successfully in {filename}.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


class Policy:# A basic policy class
    def __init__(self, policy_id, title, description):
        self.policy_id = policy_id
        self.title = title
        self.description = description

    def __str__(self):
        return f"{self.policy_id}. {self.title} - {self.description}"


class PolicyManager:# a class policy manager to have all functions used for managing policies
    def __init__(self):
        self.education = []
        self.health = []
        self.agriculture = []
        self.safety = []
        self.load_existing_policies()

    def load_existing_policies(self):
        """Scan current folder for existing .txt files and classify them"""
        self.education.clear()
        for file in os.listdir():
            if file.endswith(".txt"):
                try:
                    with open(file, "r") as f:
                        content = f.read()
                        if "Education" in content:
                            self.education.append(file)
                        elif "Health" in content:
                            self.health.append(file)
                        elif "Safety" in content:
                            self.safety.append(file)
                        elif "Agriculture" in content:
                            self.agriculture.append(file)
                except:
                    pass

    def add_policy(self, category): #adding policies using files
        policy_id = input("Enter policy ID: ")
        filename = f"{policy_id}.txt"

        title1 = input("What is the title of policy...? ")
        des1 = input("Enter the policy description: ")
        wef = input("When is the policy effective from...? ")
        eligibility = input("What is the eligibility for the policy...? ")

        categories = {
            1: "📔 Education",
            2: "🏥 Health",
            3: "🛡 Safety",
            4: "🌾 Agriculture"
        }

        category_name = categories.get(category, "Unknown")

        with open(filename, "w") as file:
            file.write(f"Policy Category: {category_name}\n")
            file.write(f"Title: {title1}\n")
            file.write(f"Description: {des1}\n")
            file.write(f"The eligibility is: {eligibility}\n")
            file.write(f"With effective from: {wef}\n")

        print(f"✅ Policy added successfully under {category_name}!")
        self.load_existing_policies()
        if category == 1:
            self.education.append(filename)
        elif category == 2:
            self.health.append(filename)
        elif category == 3:
            self.safety.append(filename)
        elif category == 4:
            self.agriculture.append(filename)
        else:
            print("Invalid type")

    def view_policy(self): #viewing policy using policy id
        policy_id = input("Enter policy ID to view: ")
        filename = f"{policy_id}.txt"
        try:
            with open(filename, "r") as file:
                policy_data = file.read()
            print("\n📄 POLICY DETAILS 📄\n" + policy_data)
        except FileNotFoundError:
            print(f"❌ Policy with ID {policy_id} not found.")

    def remove_policy(self):#removing policy using policy id
        policy_id = input("Enter policy ID to remove: ")
        filename = f"{policy_id}.txt"
        if os.path.exists(filename):
            os.remove(filename)
            print("🗑️ Policy removed successfully.")
            for lst in [self.education, self.health, self.safety, self.agriculture]:
                if filename in lst:
                    lst.remove(filename)
        else:
            print("❌ The file does not exist.")

    def edit_policy(self):#editing any info in any existing policy
        policy_id = input("Enter policy ID to edit: ")
        edit_item = int(input("What do you want to edit?\n1. Title\n2. Description\n3. Eligibility\n4. WEF\nEnter choice: "))
        new_content = input("Enter the new content: ")
        policy_edit = f"{policy_id}.txt"

        if edit_item == 1:
            replace_line_in_file(policy_edit, 2, f"Title: {new_content}")
        elif edit_item == 2:
            replace_line_in_file(policy_edit, 3, f"Description: {new_content}")
        elif edit_item == 3:
            replace_line_in_file(policy_edit, 4, f"The eligibility is: {new_content}")
        elif edit_item == 4:
            replace_line_in_file(policy_edit, 5, f"With effective from: {new_content}")
        else:
            print("Invalid choice to edit.")
        self.load_existing_policies
    def view_all_policies(self):#viewing all policies without taking any id by user
        self.load_existing_policies
        all_files = self.education + self.health + self.safety + self.agriculture
        if not all_files:
            print("No policies available.")
            return
        print("All policies:")
        for filename in all_files:
          info=open(filename,"r")
          print(info.read())
          info.close()


    def view_policies_in_category(self, category):#viewing all policies in any category required
        category_lists = {
            1: self.education,
            2: self.health,
            3: self.safety,
            4: self.agriculture,
        }
        policies = category_lists.get(category, [])
        if not policies:
            print("No policies found in this category.")
            return
        print(f"\nPolicies in category {category}:")
        for filename in policies:
            try:
                with open(filename, "r") as file1:
                    data = file1.read()
                    print(data)

                    print("-" * 40)
            except FileNotFoundError:
                print(f"Policy file {filename} not found.")
    def take_suggestions(self):
      s=input("Any suggestions that you would like to give: ")
      with open("suggestions.txt","a") as file2:
        file2.write(f"* {s}\n {'-'*20}\n")
    def see_suggestions(self):
       print("SUGGESTIONS:\n")
       with open("suggestions.txt","r") as file2:
          suggestion=file2.read()
          print(suggestion)
                #Creating basic user interface

print("नमस्ते 🙏")
TYPE = int(input("1. PUBLIC \n2. AUTHORITY \nEnter choice: "))
new = PolicyManager()
#Authority interface
if TYPE == 2:
#a password verifying authority
    password = 1234
    PASSWORD = int(input("Enter the password: "))
    if PASSWORD == password:
        print("🙏 Welcome 🙏")

        while True:
            task = int(input(
                "What do you want to do today?\n1. VIEW POLICIES\n2. ADD NEW POLICY\n3. EDIT A POLICY\n4. REMOVE A POLICY\n5.VIEW SUGGESTIONS\n6. QUIT\nEnter choice: "
            ))
      #closing the output instance
            if task == 6:
                print("👋 Exiting... Have a great day!")
                break
   #performing required task
            if task in [1, 2, 3, 4]:
                category = int(input(
                    "Category of the policy:\n1.📔 EDUCATION\n2.🏥 HEALTH\n3.🛡 SAFETY\n4.🌾 AGRICULTURE\n"
                ))

                if task == 1:
                    new.view_policy()
                elif task == 2:
                    new.add_policy(category)
                elif task == 3:
                    new.edit_policy()
                elif task == 4:
                    new.remove_policy()
            if task==5:
                    new.see_suggestions()
            print("\nWould you like to continue or quit?")
    else:
        print("❌ Wrong password.")

#Public user interface
elif TYPE == 1:
    print("welcome! What do you want to view today...?")
    while True:
        choice = int(input("1. View policies by category\n2. View all policies in a category\n3. View all policies\n4.Quit\nEnter choice: "))
        if choice==4:
          new.take_suggestions()
          break
        if choice in [1,2,3]:
          if choice == 1:#Viewing specific policy
              category = int(input("Please enter your Category:\n1.📔  EDUCATION\n2.🏥 HEALTH\n3.🛡 SAFETY\n4.🌾 AGRICULTURE\n"))
              if category == 1:
                  print("\n📔 Education Policies:")
                  print(*new.education, sep="\n")

                  new.view_policy()
              elif category == 2:
                  print("\n🏥 Health Policies:")
                  print(*new.health, sep="\n")
                  new.view_policy()
              elif category == 3:
                  print("\n🛡 Safety Policies:")
                  print(*new.safety, sep="\n")
                  new.view_policy()
              elif category == 4:
                  print("\n🌾 Agriculture Policies:")
                  print(*new.agriculture, sep="\n")
                  new.view_policy()
              else:
                  print("Invalid category!")

          elif choice == 2: #viewing all policies in a category
              category = int(input("Please enter your Category:\n1.📔  EDUCATION\n2.🏥 HEALTH\n3.🛡 SAFETY\n4.🌾 AGRICULTURE\n"))
              new.view_policies_in_category(category)

          elif choice == 3: #Viewing all policy
              new.view_all_policies()

    else:
        print("Invalid choice!")

print("Thankyou!\nSee you again...")
