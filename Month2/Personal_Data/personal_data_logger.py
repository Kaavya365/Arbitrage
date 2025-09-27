def main():
    data_file_path = "data.csv"
    user_data = user_details()
    save_details_to_file(user_data, data_file_path)

def user_details():
    while True:
        print("Kindly Provide the following details:")
        user_name = input("Name: ").strip()
        user_age = input("Age: ").strip()
        user_date_of_birth = input("Date of Birth: ").strip()
        user_gender = input("Gender: ").strip()
        user_edu_qual = input("Educational Qualification: ").strip()
        user_profession = input("Profession: ").strip()
        user_phone_no = input("Phone Number: ").strip()
        user_email = input("Email ID: ").strip()

        return{
            'name': user_name,
            'age': user_age,
            'date_of_birth': user_date_of_birth,
            'gender': user_gender,
            'education': user_edu_qual,
            'profession': user_profession,
            'phone_no': user_phone_no,
            'email': user_email
        }


def save_details_to_file(user_data, data_file_path):
    with open(data_file_path, "a") as f:
        f.write(f"{user_data['name']},{user_data['age']},{user_data['date_of_birth']},{user_data['gender']},{user_data['education']},{user_data['profession']},{user_data['phone_no']},{user_data['email']}\n")
    print("Data Successfully Saved!")

if __name__ == '__main__':
    main()
